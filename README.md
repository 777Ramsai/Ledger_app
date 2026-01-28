# 📦 Pocket Ledger

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]()
[![Version 1.0](https://img.shields.io/badge/Version-1.0-blue)]()

A secure, user-friendly mobile-optimized ledger application for tracking business transactions and managing supplier accounts with multi-user support and enterprise-grade security.

---

## 🔗 **Try It Now!**

### **Live Web App (No Installation Needed)**
**👉 [🚀 Open Pocket Ledger](https://ledgerapp-2508.streamlit.app/)**

Create your account or login to start managing your ledger immediately!

---

## 📖 Quick Navigation

> 📍 **First Time Here?** Start with [**QUICKSTART.md**](QUICKSTART.md) (5 minutes)

| 🚀 Quick Start | 📚 Full Docs | 🔒 Security | 🏗️ Technical |
|---|---|---|---|
| [QUICKSTART.md](QUICKSTART.md) | [README.md](README.md) | [SECURITY.md](SECURITY.md) | [ARCHITECTURE.md](ARCHITECTURE.md) |
| 5-minute setup | Complete guide | Security details | System design |
| [START_HERE.md](START_HERE.md) | [INDEX.md](INDEX.md) | [.gitignore](.gitignore) | [app.py](app.py) |
| Project overview | Navigation hub | File protection | Main code |

**📋 Complete File Reference:** [MANIFEST.md](MANIFEST.md)

---

## ✨ Features at a Glance

### 🔐 **User Authentication & Security**
- ✅ Secure Sign Up with email & password
- ✅ SHA-256 password hashing (industry standard)
- ✅ Multi-user support with complete data isolation
- ✅ Session-based authentication
- ✅ Password strength validation (6+ characters minimum)
- ✅ Email format validation
- ✅ No plain-text password storage

### 📊 **Ledger Management**
- ✅ Add/view credit (purchases) and debit (payments) transactions
- ✅ Track multiple supplier accounts simultaneously
- ✅ Automatic running balance calculation
- ✅ Total payable summary dashboard
- ✅ Per-shop balance tracking
- ✅ Transaction history with details

### 📥 **Data Export & Backup**
- ✅ Download ledger as CSV for backup
- ✅ Generate PDF statements for suppliers
- ✅ One-click backup in sidebar
- ✅ User-specific isolated data (no shared access)

### 📱 **User Experience**
- ✅ Mobile-responsive design
- ✅ Touch-friendly interface
- ✅ Intuitive navigation
- ✅ Clear error messages
- ✅ Fast performance
- ✅ Professional UI

---

## 🚀 Getting Started

### **Option 1: Use Live Web App (Recommended)**
Just visit: **[https://ledgerapp-2508.streamlit.app/](https://ledgerapp-2508.streamlit.app/)**

### **Option 2: Run Locally**

#### Prerequisites
- Python 3.8+
- pip (Python package manager)

#### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/777Ramsai/Ledger_app.git
cd Ledger_app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py
```

The app will automatically open at: `http://localhost:8501`

---

## 📖 Usage Guide

### **1️⃣ Creating an Account**

1. Click on the **"Sign Up"** tab
2. Enter a valid email address (e.g., `your@email.com`)
3. Create a password (minimum 6 characters)
4. Confirm your password
5. Click **"Sign Up"**
6. Success! You can now login

**Password Tips:**
- Use at least 6 characters
- Mix uppercase and lowercase letters
- Include numbers for extra security
- Make it unique!

### **2️⃣ Login**

1. Click on the **"Login"** tab
2. Enter your email and password
3. Click **"Login"**
4. Your personal dashboard loads with all your previous data

### **3️⃣ Adding Transactions**

1. Click **"➕ Add New Transaction"** to expand the form
2. Fill in the details:
   - **Date**: Select the transaction date (defaults to today)
   - **Amount**: Enter the transaction amount
   - **Shop Name**: Name of the supplier/shop
   - **Type**: Choose:
     - **Credit (Purchase)** = Money you owe
     - **Debit (Payment)** = Money you paid
   - **Note**: Optional (e.g., "Invoice #2026-001")
3. Click **"Save Entry"**

### **4️⃣ Viewing Your Dashboard**

The dashboard automatically displays:
- **Total Payable**: Sum of all amounts owed to suppliers
- **Shop Summary Table**: List of all shops with their balances
- **Transaction Details**: Select any shop to see:
  - All transactions with dates
  - Running balance for that supplier
  - Option to generate PDF report

### **5️⃣ Generating Reports**

1. Go to **"📒 Shop Details"**
2. Select a shop from the dropdown
3. View all transactions with running balances
4. Click **"📄 PDF Statement"** to generate a professional PDF

### **6️⃣ Backup Your Data**

1. Click **"📥 Download CSV Backup"** in the sidebar
2. Your complete ledger data downloads as a CSV file
3. Keep it safe as a backup

### **7️⃣ Logout**

1. Click **"🚪 Logout"** in the sidebar
2. Your session ends securely
3. You can login as a different user

---

## 🔒 Security Features

### **Password Security**
- ✅ **SHA-256 Hashing**: Passwords are hashed using industry-standard SHA-256 algorithm
- ✅ **No Plain-Text Storage**: Original passwords are never stored
- ✅ **One-Way Encryption**: Impossible to reverse-engineer password from hash
- ✅ **Secure Comparison**: Passwords verified using secure hash comparison

### **User Data Isolation**
- ✅ **Separate Files**: Each user's ledger stored in unique file
- ✅ **No Cross-Access**: Users cannot access other users' data
- ✅ **Email-Based Naming**: Files named based on sanitized email
- ✅ **Complete Privacy**: Each user sees only their own transactions

### **Session Management**
- ✅ **Streamlit Session State**: Secure session handling
- ✅ **Automatic Logout**: Session ends when browser closes
- ✅ **Per-Device Auth**: Fresh authentication required per device
- ✅ **No Persistent Tokens**: No tokens to intercept

### **Input Validation**
- ✅ **Email Format**: Must contain @ and .
- ✅ **Password Strength**: Minimum 6 characters required
- ✅ **Type Checking**: All inputs validated
- ✅ **Duplicate Prevention**: Same email cannot register twice

### **File Protection**
- ✅ **`.gitignore`**: Credentials excluded from version control
- ✅ **Secure Directory**: Separate `user_data/` folder
- ✅ **Protected Database**: `users_data.json` never committed
- ✅ **No Hardcoded Secrets**: No passwords in code

**For detailed security information, see [SECURITY.md](SECURITY.md)**

---

## 📁 Project Structure

```
Ledger_app/
├── 📱 APPLICATION
│   ├── app.py                      # Main Streamlit application (315 lines)
│   └── requirements.txt            # Python dependencies
│
├── 📖 DOCUMENTATION (8 files)
│   ├── README.md                   # This file (you are here)
│   ├── QUICKSTART.md               # 5-minute quick start guide
│   ├── START_HERE.md               # Project overview
│   ├── SECURITY.md                 # Security implementation details
│   ├── ARCHITECTURE.md             # System design & architecture
│   ├── UPDATES.md                  # Changes & enhancements
│   ├── INDEX.md                    # Documentation navigation
│   ├── IMPLEMENTATION_COMPLETE.md  # Completion status
│   └── MANIFEST.md                 # Complete file listing ← START HERE!
│
├── ⚖️ LEGAL
│   └── LICENSE                     # MIT License
│
├── 🔐 CONFIGURATION
│   ├── .gitignore                  # Git configuration
│   └── requirements.txt            # Dependencies
│
└── 📁 AUTO-CREATED (Protected)
    ├── user_data/                  # User ledger files (per-user CSV)
    └── users_data.json             # User credentials database
```

**See [MANIFEST.md](MANIFEST.md) for detailed file descriptions**

## �️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit 1.28.0+ | Interactive web UI |
| **Backend** | Python 3.8+ | Core application logic |
| **Database** | JSON + CSV | User credentials & ledger storage |
| **Security** | hashlib (SHA-256) | Password hashing |
| **Data Processing** | Pandas 2.0.0+ | Transaction analysis |
| **Export** | fpdf2 2.7.0+ | PDF statement generation |
| **Deployment** | Streamlit Cloud | Live hosting |
| **Version Control** | Git/GitHub | Source code management |

**View [requirements.txt](requirements.txt) for exact versions**

## �🔧 Configuration

No additional configuration is required. The application automatically:
- Creates user data directory on first run
- Initializes user authentication system
- Creates user-specific ledger files

## 📊 Data Format

### CSV Ledger Format
| Date | Shop Name | Type | Amount | Description |
|------|-----------|------|--------|-------------|
| 2026-01-28 | ABC Supplies | Credit (Purchase) | 5000 | INV-2026-001 |
| 2026-01-29 | ABC Supplies | Debit (Payment) | 3000 | Payment received |

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements.

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License permits anyone to use, modify, and distribute this software freely, provided they include the original license notice.

## 💡 Best Practices

| Practice | Benefit | How-To |
|----------|---------|--------|
| **Regular Backups** | Prevent data loss | Download CSV weekly in sidebar |
| **Strong Passwords** | Secure your account | 6+ chars, mix case, include numbers |
| **Consistent Shop Names** | Accurate tracking | Always use same name for each supplier |
| **Weekly Reviews** | Stay informed | Check dashboard summary every 7 days |
| **Invoice Tracking** | Easy reference | Use "Note" field for invoice numbers |
| **Logout When Done** | Secure sessions | Click "🚪 Logout" to end session |

## 🐛 Troubleshooting

| Problem | Solution | Details |
|---------|----------|---------|
| **"Email already registered"** | Use a different email or login with existing credentials | Each email can only register once for security |
| **"Incorrect password"** | Verify password (case-sensitive) | Passwords must match exactly. Use "Sign Up" if forgotten |
| **Data not saving** | Check `user_data/` directory permissions | Ensure write access to the user_data folder |
| **App not starting** | Run `pip install -r requirements.txt` | Verify all dependencies are installed |
| **Missing Python 3.8+** | Install or upgrade Python | [Download Python](https://www.python.org/) |
| **Streamlit errors** | Clear cache: `streamlit cache clear` | Resolves most runtime issues |
| **File permission denied** | Check directory permissions | Ensure user running app has write access |

**For more help, see [SECURITY.md](SECURITY.md) or [ARCHITECTURE.md](ARCHITECTURE.md)**

## � Documentation & Support

### 📖 Complete Documentation
- **[QUICKSTART.md](QUICKSTART.md)** — Get started in 5 minutes
- **[START_HERE.md](START_HERE.md)** — Project overview & features
- **[SECURITY.md](SECURITY.md)** — Security implementation details
- **[ARCHITECTURE.md](ARCHITECTURE.md)** — System design & technical architecture
- **[INDEX.md](INDEX.md)** — Documentation index & navigation
- **[MANIFEST.md](MANIFEST.md)** — Complete file listing (14 files)
- **[UPDATES.md](UPDATES.md)** — Version history & changelog
- **[IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md)** — Feature completion checklist

### 🌐 Online Resources
- **[GitHub Repository](https://github.com/777Ramsai/Ledger_app)** — Source code & issues
- **[Live App](https://ledgerapp-2508.streamlit.app/)** — Try it now
- **[Streamlit Docs](https://docs.streamlit.io/)** — Framework documentation
- **[Python Documentation](https://docs.python.org/)** — Python reference

### 💬 Getting Help
- 🐛 **Found a bug?** — Open an [issue on GitHub](https://github.com/777Ramsai/Ledger_app/issues)
- 💡 **Have a suggestion?** — Create a [discussion on GitHub](https://github.com/777Ramsai/Ledger_app)
- 📧 **General questions?** — Check [INDEX.md](INDEX.md) for guidance

## 🎯 Roadmap & Future Enhancements

### Phase 1 (Current) ✅ Complete
- ✅ Core ledger functionality
- ✅ Multi-user authentication
- ✅ Password hashing & security
- ✅ CSV/PDF export

### Phase 2 (Planned)
- 🔜 Password recovery via email
- 🔜 Two-factor authentication (2FA)
- 🔜 Advanced analytics dashboard

### Phase 3 (Future)
- 📱 Multi-currency support
- 📊 Database integration (PostgreSQL)
- 📱 Mobile app version
- 🌐 Real-time collaboration

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 14 (3 core + 8 docs + 3 config) |
| **Lines of Code** | 315 (app.py) |
| **Documentation** | 2000+ lines across 8 files |
| **Python Version** | 3.8+ |
| **Dependencies** | 3 major packages |
| **Security Level** | Enterprise-grade |
| **License** | MIT (Open Source) |
| **Status** | Production Ready |
| **Live Users** | Multi-user capable |
| **Deployment** | Streamlit Cloud |

---

## 🎉 Thank You!

Thanks for using **Pocket Ledger**! We hope this application makes managing your ledger easier and more secure.

### 📌 Quick Links
- 🚀 **[Open Live App](https://ledgerapp-2508.streamlit.app/)** — Start using now
- ⭐ **[GitHub Repository](https://github.com/777Ramsai/Ledger_app)** — Star us on GitHub
- 📖 **[Full Documentation](INDEX.md)** — Learn more
- 📋 **[See All Files](MANIFEST.md)** — Complete file listing

### 💪 Support This Project
- ⭐ Star the repository on GitHub
- 🐛 Report bugs and suggest features
- 📢 Share with others who need a secure ledger
- 👥 Contribute improvements

---

**Pocket Ledger** © 2026 — Secure Ledger Management for Everyone

**Version**: 1.0 | **Status**: Production Ready | **License**: MIT | **Last Updated**: January 28, 2026

Enjoy using Pocket Ledger! 📦✨
