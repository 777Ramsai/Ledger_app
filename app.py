import streamlit as st
import pandas as pd
import os
from datetime import date
from fpdf import FPDF
import tempfile
import json
import hashlib
from pathlib import Path

# --- Authentication and User Management ---
USERS_FILE = 'users_data.json'
DATA_DIR = 'user_data'

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def hash_password(password: str) -> str:
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load all registered users."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users: dict):
    """Save users to file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def register_user(email: str, password: str) -> tuple:
    """Register a new user."""
    users = load_users()
    
    if email in users:
        return False, "Email already registered!"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters!"
    
    if "@" not in email or "." not in email:
        return False, "Please enter a valid email!"
    
    users[email] = {
        "password_hash": hash_password(password),
        "created_at": str(date.today())
    }
    save_users(users)
    return True, "Account created successfully!"

def login_user(email: str, password: str) -> tuple:
    """Verify user credentials."""
    users = load_users()
    
    if email not in users:
        return False, "Email not found!"
    
    if users[email]["password_hash"] != hash_password(password):
        return False, "Incorrect password!"
    
    return True, "Login successful!"

def get_user_data_file(email: str) -> str:
    """Get user-specific ledger file path."""
    return os.path.join(DATA_DIR, f"{email.replace('@', '_').replace('.', '_')}_ledger.csv")

def initialize_auth_session():
    """Initialize authentication session state."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

initialize_auth_session()

def render_auth_page():
    """Render login/signup page."""
    st.set_page_config(page_title="Pocket Ledger - Login", layout="centered")
    st.title("🔐 Pocket Ledger")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("Login to Your Account")
        login_email = st.text_input("Email", key="login_email", placeholder="your@email.com")
        login_password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login", use_container_width=True, type="primary"):
            if login_email and login_password:
                success, message = login_user(login_email, login_password)
                if success:
                    st.session_state.authenticated = True
                    st.session_state.user_email = login_email
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please fill in all fields!")
    
    with tab2:
        st.subheader("Create a New Account")
        signup_email = st.text_input("Email", key="signup_email", placeholder="your@email.com")
        signup_password = st.text_input("Password", type="password", key="signup_password", 
                                        help="At least 6 characters")
        signup_password_confirm = st.text_input("Confirm Password", type="password", 
                                                key="signup_password_confirm")
        
        if st.button("Sign Up", use_container_width=True, type="primary"):
            if not signup_email or not signup_password:
                st.error("Please fill in all fields!")
            elif signup_password != signup_password_confirm:
                st.error("Passwords don't match!")
            else:
                success, message = register_user(signup_email, signup_password)
                if success:
                    st.success(message)
                    st.info("Now you can login with your credentials!")
                else:
                    st.error(message)

# --- Check Authentication ---
if not st.session_state.authenticated:
    render_auth_page()
    st.stop()

# --- Configuration ---
def get_file_name():
    if st.session_state.authenticated:
        return get_user_data_file(st.session_state.user_email)
    return 'ledger_data.csv'

# --- 1. Data Functions ---
def load_data():
    """Load data from CSV, creating the file if it doesn't exist."""
    file_name = get_file_name()
    if not os.path.exists(file_name):
        df = pd.DataFrame(columns=["Date", "Shop Name", "Type", "Amount", "Description"])
        df.to_csv(file_name, index=False)
        return df
    return pd.read_csv(file_name)

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
    df.to_csv(get_file_name(), index=False)

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
st.markdown(f"👤 Logged in as: **{st.session_state.user_email}**")

# --- Sidebar: Data Management & User Options ---
with st.sidebar:
    st.header("⚙️ Options")
    
    st.subheader("User Account")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.user_email = None
        st.success("Logged out successfully!")
        st.rerun()
    
    st.divider()
    st.subheader("📊 Data Management")
    
    # Backup Feature
    file_name = get_file_name()
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            st.download_button("📥 Download CSV Backup", f, "ledger_backup.csv", "text/csv")

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
