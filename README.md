# 📦 Pocket Ledger

A secure, user-friendly mobile-optimized ledger application for tracking business transactions and managing supplier accounts.

## 🔗 Live App

**Try the app now:** [🚀 Open Pocket Ledger](https://ledgerapp-2508.streamlit.app/)

> **Demo Credentials (Optional):**
> - Email: `demo@example.com`
> - Password: `demo123` (or create your own account)

---

## ✨ Features

### 🔐 User Authentication
- **Secure Sign Up**: Create accounts with email and password validation
- **Login/Logout**: Easy authentication system with password hashing (SHA-256)
- **Account Security**: Each user has isolated, encrypted account data
- **Password Validation**: Minimum 6 characters required for security

### 📊 Ledger Management
- **Quick Transaction Entry**: Add credit (purchases) and debit (payments) transactions
- **Shop Management**: Track multiple supplier accounts
- **Running Balance**: Automatic calculation of balances per shop
- **Summary Dashboard**: View total payable amount and per-shop breakdown

### 📥 Data Export
- **CSV Backup**: Download ledger data as CSV for backup/external use
- **PDF Statements**: Generate detailed PDF statements for individual suppliers
- **User-Specific Data**: Each user's data is completely isolated and private

### 📱 Mobile Friendly
- Responsive design optimized for mobile devices and tablets
- Centered layout for better usability on smaller screens
- Touch-friendly buttons and form inputs

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or extract the repository**
```bash
cd Ledger_app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### Creating an Account
1. Open the app and go to the **"Sign Up"** tab
2. Enter a valid email address
3. Create a password (minimum 6 characters)
4. Confirm your password
5. Click **"Sign Up"**
6. You can now login with your credentials

### Login
1. Go to the **"Login"** tab
2. Enter your email and password
3. Click **"Login"**
4. Your personal ledger will load

### Adding Transactions
1. Click on **"➕ Add New Transaction"** to expand the form
2. Fill in the details:
   - **Date**: Select the transaction date
   - **Amount**: Enter the amount
   - **Shop Name**: Name of the supplier/shop
   - **Type**: Choose between "Credit (Purchase)" or "Debit (Payment)"
   - **Note**: Optional description (e.g., Invoice number)
3. Click **"Save Entry"**

### Viewing Summary
- The dashboard automatically shows:
  - **Total Payable**: Total amount owed to all suppliers
  - **Shop List**: Individual shop balances
  - **Running Balance**: Cumulative balance for each shop

### Generating Reports
1. Select a shop from the dropdown in **"📒 Shop Details"**
2. View detailed transactions with running balances
3. Click **"📄 PDF Statement"** to generate and download a PDF

### Backup Your Data
1. Click **"📥 Download CSV Backup"** in the left sidebar
2. Your ledger data will download as a CSV file

### Logout
1. Click **"🚪 Logout"** in the sidebar
2. You will be returned to the login screen
3. You can now login as a different user

## 🔒 Security Features

- **Password Hashing**: All passwords are hashed using SHA-256 algorithm before storage
- **User Isolation**: Each user's data is stored in separate files
- **Session Management**: Secure session handling with Streamlit
- **Input Validation**: Email and password validation to prevent invalid entries
- **No Plain-Text Storage**: Passwords are never stored in plain text

## 📁 File Structure

```
Ledger_app/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
├── users_data.json       # Encrypted user credentials (auto-generated)
└── user_data/            # Directory containing user-specific ledger files
    ├── user1_email_com_ledger.csv
    ├── user2_email_com_ledger.csv
    └── ...
```

## 🔧 Configuration

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

## 💡 Tips for Users

1. **Data Backup**: Regularly download CSV backups to prevent data loss
2. **Strong Passwords**: Use unique passwords for each account
3. **Shop Naming**: Use consistent shop names for accurate tracking
4. **Regular Review**: Check your summary dashboard weekly to stay updated
5. **Invoice Tracking**: Use the "Note" field to track invoice numbers for reference

## 🐛 Troubleshooting

### Issue: "Email already registered"
- Use a different email address or login with existing credentials

### Issue: "Incorrect password"
- Ensure your password is correct (case-sensitive)
- Use "Sign Up" to create a new account if you forgot your password

### Issue: Data not saving
- Ensure the `user_data/` directory is writable
- Check available disk space

### Issue: App not starting
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python version is 3.8 or higher

## 📧 Support

For issues or suggestions, please open an issue in the repository or contact the development team.

## 🎯 Future Enhancements

- Password recovery functionality
- Two-factor authentication (2FA)
- Multi-currency support
- Advanced reporting and analytics
- Mobile app version
- Database integration for better scalability

---

**Version**: 1.0  
**Last Updated**: January 28, 2026  
**Status**: Active Development

Enjoy using Pocket Ledger! 📦✨
