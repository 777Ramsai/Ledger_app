import streamlit as st
import pandas as pd
import os
from datetime import date
from fpdf import FPDF
import tempfile

# --- Simple Security ---
def check_password():
    if "password_guessed" not in st.session_state:
        st.session_state["password_guessed"] = False

    if not st.session_state["password_guessed"]:
        password = st.text_input("Enter Password to Access Ledger", type="password")
        if password == "MyBusiness2026": # <--- CHANGE YOUR PASSWORD HERE
            st.session_state["password_guessed"] = True
            st.rerun()
        elif password != "":
            st.error("Wrong password")
        return False
    return True

if not check_password():
    st.stop() # Do not run the rest of the app
    
# --- Configuration ---
FILE_NAME = 'ledger_data.csv'

# --- 1. Data Functions ---
def load_data():
    """Load data from CSV, creating the file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Shop Name", "Type", "Amount", "Description"])
        df.to_csv(FILE_NAME, index=False)
        return df
    return pd.read_csv(FILE_NAME)

def save_transaction(date_val, shop, trans_type, amount, desc):
    """Save a new transaction to the CSV."""
    df = load_data()
    new_data = pd.DataFrame({
        "Date": [date_val],
        "Shop Name": [shop],
        "Type": [trans_type],
        "Amount": [amount],
        "Description": [desc]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

def create_pdf(shop_name, df_shop):
    """Generate PDF Statement."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    
    # Header
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt=f"Statement: {shop_name}", ln=True, align='C')
    pdf.ln(5)

    # Table Headers
    pdf.set_font("Arial", 'B', 9)
    pdf.cell(25, 8, "Date", 1)
    pdf.cell(75, 8, "Desc", 1)
    pdf.cell(25, 8, "Credit", 1)
    pdf.cell(25, 8, "Debit", 1)
    pdf.cell(30, 8, "Balance", 1)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", size=9)
    for _, row in df_shop.iterrows():
        c = f"{row['Amount']:.2f}" if "Credit" in row['Type'] else "-"
        d = f"{row['Amount']:.2f}" if "Debit" in row['Type'] else "-"
        pdf.cell(25, 8, str(row['Date']), 1)
        pdf.cell(75, 8, str(row['Description'])[:40], 1)
        pdf.cell(25, 8, c, 1)
        pdf.cell(25, 8, d, 1)
        pdf.cell(30, 8, f"{row['Running Balance (B/F)']:.2f}", 1)
        pdf.ln()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name

# --- 2. App Layout (Mobile Friendly) ---
st.set_page_config(page_title="Pocket Ledger", layout="centered") 
st.title("📦 Pocket Ledger")

# --- Sidebar: Data Management ---
with st.sidebar:
    st.header("⚙️ Data Options")
    # Backup Feature
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "rb") as f:
            st.download_button("📥 Download Excel Backup", f, "ledger_backup.csv", "text/csv")

# --- Section A: Quick Add (Expander) ---
with st.expander("➕ Add New Transaction", expanded=False):
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            entry_date = st.date_input("Date", date.today())
            amount = st.number_input("Amount", min_value=0.0, step=100.0)
        with col2:
            # Auto-suggest existing shops
            df_load = load_data()
            existing_shops = df_load["Shop Name"].unique().tolist() if not df_load.empty else []
            shop_name = st.text_input("Shop Name", placeholder="Type name...")
            
        trans_type = st.radio("Type", ["Credit (Purchase)", "Debit (Payment)"], horizontal=True)
        description = st.text_input("Note", placeholder="e.g. Invoice #123")
        
        submitted = st.form_submit_button("Save Entry")
        if submitted:
            if shop_name and amount > 0:
                save_transaction(entry_date, shop_name, trans_type, amount, description)
                st.success("Saved!")
                st.rerun() # Refresh data immediately
            else:
                st.error("Missing Name or Amount")

# --- Section B: Dashboard Summary ---
st.markdown("### 📊 Summary")
df = load_data()

if not df.empty:
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    
    # Calculate Balances
    shops = df["Shop Name"].unique()
    summary_data = []
    total_due_all = 0

    for shop in shops:
        shop_df = df[df["Shop Name"] == shop]
        credits = shop_df[shop_df["Type"].str.contains("Credit")]["Amount"].sum()
        debits = shop_df[shop_df["Type"].str.contains("Debit")]["Amount"].sum()
        balance = credits - debits
        total_due_all += balance
        summary_data.append({"Shop": shop, "Due": balance})

    # Total Debt Metric
    st.metric(label="Total Payable to Suppliers", value=f"{total_due_all:,.2f}")

    # Summary Table
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(
        summary_df.style.format({"Due": "{:.2f}"}),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # --- Section C: Individual Details ---
    st.markdown("### 📒 Shop Details")
    selected_shop = st.selectbox("Select Shop", options=shops)

    if selected_shop:
        shop_data = df[df["Shop Name"] == selected_shop].copy().sort_values(by="Date")
        
        # Calculate B/F
        running_balance = 0
        balances = []
        for _, row in shop_data.iterrows():
            if "Credit" in row["Type"]:
                running_balance += row["Amount"]
            else:
                running_balance -= row["Amount"]
            balances.append(running_balance)
        shop_data["Bal"] = balances

        # Display optimized for mobile
        display_cols = ["Date", "Type", "Amount", "Bal"]
        shop_data["Type"] = shop_data["Type"].apply(lambda x: "Buy" if "Credit" in x else "Pay")
        
        st.dataframe(
            shop_data[display_cols].style.format({"Amount": "{:.0f}", "Bal": "{:.0f}"}),
            use_container_width=True,
            hide_index=True
        )

        # PDF Button
        pdf_path = create_pdf(selected_shop, df[df["Shop Name"] == selected_shop].sort_values(by="Date").assign(**{"Running Balance (B/F)": balances}))
        with open(pdf_path, "rb") as f:
            st.download_button("📄 PDF Statement", f, f"{selected_shop}.pdf", "application/pdf")
else:

    st.info("Start by adding a transaction above.")
