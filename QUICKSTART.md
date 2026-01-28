# 🚀 Quick Start Guide - Pocket Ledger

## Installation (First Time)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## First Time User Workflow

### 1️⃣ Create Your Account
- Click on the **"Sign Up"** tab
- Enter your email (e.g., `yourname@example.com`)
- Create a secure password (minimum 6 characters)
- Confirm your password
- Click **"Sign Up"** button
- You'll see a success message

### 2️⃣ Login
- Click on the **"Login"** tab
- Enter your email and password
- Click **"Login"** button
- Your personal dashboard will load

### 3️⃣ Add Your First Transaction
1. Click **"➕ Add New Transaction"** (expands the form)
2. Select today's date
3. Enter an amount (e.g., 5000)
4. Enter shop name (e.g., "ABC Supplies")
5. Choose type:
   - **Credit (Purchase)**: Money you owe
   - **Debit (Payment)**: Money you paid
6. Optional: Add a note (e.g., invoice number)
7. Click **"Save Entry"**

### 4️⃣ View Your Summary
Your dashboard automatically shows:
- **Total Payable**: Total due to all suppliers
- **Shop Table**: Balance for each supplier
- **Transaction Details**: Click any shop to see all transactions

### 5️⃣ Download Your Data
- Click **"📥 Download CSV Backup"** in the sidebar anytime

### 6️⃣ Logout
- Click **"🚪 Logout"** in the sidebar to switch users

---

## 🔑 Default Demo Account (Optional)

You can test the app without creating an account by creating this test account:
- **Email**: `test@example.com`
- **Password**: `test123`

---

## 💡 Security Tips

✓ Use a strong, unique password  
✓ Don't share your email/password  
✓ Regularly backup your data (Download CSV)  
✓ Logout when finished  

---

## ❓ Common Questions

**Q: Can I use the same email on multiple devices?**
A: Yes! Login with your email/password on any device.

**Q: What if I forget my password?**
A: Currently, you'll need to create a new account with a different email. Future versions will include password recovery.

**Q: Is my data safe?**
A: Yes! Passwords are hashed with SHA-256, and each user's data is isolated.

**Q: Can I export my data?**
A: Yes! Download the CSV backup anytime from the sidebar.

**Q: How do I delete a transaction?**
A: Download your CSV, edit it, and re-upload. This feature will be added soon.

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| App won't start | Install dependencies: `pip install -r requirements.txt` |
| "Email already registered" | Use a different email or login instead |
| "Incorrect password" | Check spelling (case-sensitive) and try again |
| Data not saving | Ensure `user_data/` folder exists (auto-created) |
| Forgot password | Create a new account with different email |

---

## 📞 Need Help?

Check the full [README.md](README.md) for detailed documentation.

---

**Enjoy managing your business ledger! 📦✨**
