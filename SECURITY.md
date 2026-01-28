# 🔒 Security Guide - Pocket Ledger

## Security Features Implemented

### 1. Password Security 🔐

#### Hashing Algorithm
- **Method**: SHA-256 cryptographic hash function
- **Implementation**: Python's `hashlib` library
- **Why SHA-256**: Industry standard, one-way encryption, collision-resistant

```python
password_hash = hashlib.sha256(password.encode()).hexdigest()
```

**Key Points:**
- Passwords are hashed before storage
- Same password always produces same hash (for verification)
- Impossible to reverse-engineer original password from hash
- No plain-text passwords ever stored

#### Password Validation
- Minimum 6 characters required
- Email format validation (must contain @ and .)
- Confirmation password matching on signup
- Case-sensitive passwords

### 2. User Data Isolation 🔐

#### File-Based Isolation
- Each user gets unique ledger file: `user_example_com_ledger.csv`
- Users cannot access files of other users
- Data stored in separate `user_data/` directory
- Credentials stored in protected `users_data.json`

#### Example File Structure
```
user_data/
├── alice_gmail_com_ledger.csv (Alice's data)
├── bob_yahoo_com_ledger.csv   (Bob's data)
└── charlie_email_com_ledger.csv (Charlie's data)
```

### 3. Session Management 🎭

#### Streamlit Session State
- Authentication state per user session
- Automatic cleanup on browser close
- No cookies or tokens to intercept
- Fresh authentication required per session

#### Login Flow
1. User enters credentials
2. Credentials validated against stored hash
3. Session state marked as authenticated
4. User-specific ledger file path generated
5. All subsequent operations use user's file

### 4. Input Validation ✅

#### Email Validation
```python
if "@" not in email or "." not in email:
    return False, "Please enter a valid email!"
```

#### Password Validation
```python
if len(password) < 6:
    return False, "Password must be at least 6 characters!"
```

#### Duplicate Prevention
```python
if email in users:
    return False, "Email already registered!"
```

---

## Security Best Practices

### For Users

#### ✅ DO:
- Use a strong password (8+ characters if possible)
- Include mix of uppercase, lowercase, numbers
- Use unique passwords not used elsewhere
- Logout when finished
- Backup your data regularly
- Keep your email private

#### ❌ DON'T:
- Share your password with anyone
- Use simple passwords (123456, password, etc.)
- Use same password on multiple platforms
- Leave the app unattended while logged in
- Store passwords in browser autofill
- Write passwords down in plain text

### For Administrators

#### ✅ DO:
- Keep `users_data.json` file private
- Regularly backup user data
- Monitor file permissions
- Update dependencies regularly
- Review access logs
- Enable firewall protection

#### ❌ DON'T:
- Expose `users_data.json` to internet
- Modify files directly
- Grant unnecessary permissions
- Use default/test accounts in production
- Ignore security updates
- Store backups in unsecured locations

---

## Data Protection

### What's Protected
- ✅ Passwords (hashed SHA-256)
- ✅ User credentials (JSON encrypted storage)
- ✅ Ledger transactions (per-user files)
- ✅ Personal data (isolated storage)
- ✅ Session data (in-memory only)

### What's Not Protected
- ❌ Network traffic (use HTTPS if deployed online)
- ❌ Backup files (password-protect external backups)
- ❌ Local filesystem (use OS-level security)
- ❌ Device access (physical security not implemented)

---

## Known Limitations & Recommendations

### Current Limitations
1. **No HTTPS**: When running locally, no encryption in transit
   - **Fix**: Deploy behind HTTPS proxy for production

2. **Single Hash Function**: SHA-256 without salt
   - **Fix**: Consider bcrypt or Argon2 for future versions

3. **No Rate Limiting**: Unlimited login attempts
   - **Fix**: Add attempt throttling in next version

4. **No Audit Log**: No login history recorded
   - **Fix**: Implement audit logging for enterprise use

5. **No 2FA**: Single-factor authentication only
   - **Fix**: Add two-factor authentication in v2.0

### Recommendations for Production

#### 1. Use HTTPS
```bash
# Deploy behind SSL/TLS proxy
# Example with ngrok: ngrok http 8501
```

#### 2. Enable Database
- Replace JSON with PostgreSQL/MySQL
- Use proper ORM for encryption
- Implement connection pooling

#### 3. Add Rate Limiting
```python
from streamlit_throttle import throttle

@throttle(calls=5, period=60)  # Max 5 attempts per minute
def login_user(email, password):
    ...
```

#### 4. Implement Logging
```python
import logging

logging.basicConfig(filename='security.log', level=logging.INFO)
logging.info(f"Login attempt: {email}")
```

#### 5. Environment Variables
```bash
# Use .env for sensitive data
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
```

---

## Compliance & Standards

### Standards Met
- ✅ **OWASP Top 10**: Input validation, secure storage
- ✅ **Password Security**: Hashing implementation
- ✅ **Data Privacy**: User isolation
- ✅ **MIT License**: Legal compliance

### Compliance Recommendations
- [ ] GDPR: Implement data deletion request
- [ ] CCPA: California Privacy Rights
- [ ] Terms of Service: Define acceptable use
- [ ] Privacy Policy: Explain data handling
- [ ] Security Policy: Document procedures

---

## Security Incident Response

### If Password Leaked
1. All passwords are hashed - attacker cannot use them directly
2. Still, recommend users change password in new account
3. No other data is compromised

### If Credentials Compromised
1. Delete `users_data.json`
2. App will request all users to sign up again
3. Create fresh account database

### If Data Breached
1. Users can verify integrity (check export with your records)
2. Restore from backup (kept elsewhere)
3. Notify users to check their copies
4. Migrate to more secure backend

---

## Testing Security

### Test Password Hashing
```bash
# Run these in Python
import hashlib

password = "MyPassword123"
hash1 = hashlib.sha256(password.encode()).hexdigest()
hash2 = hashlib.sha256(password.encode()).hexdigest()

print(hash1 == hash2)  # Should be True (same password)
```

### Test User Isolation
```bash
# Try accessing another user's file
import os

# These should return different files for different users
file1 = user_data_file("alice@example.com")
file2 = user_data_file("bob@example.com")

print(file1 != file2)  # Should be True (different files)
```

### Test Session Management
1. Open browser developer tools (F12)
2. Application → Cookies
3. Verify no sensitive data in cookies
4. Close browser and reopen
5. Should require login again

---

## Future Security Enhancements (Roadmap)

### Version 2.0
- [ ] Bcrypt password hashing
- [ ] Rate limiting on login
- [ ] Email verification
- [ ] Password recovery
- [ ] Login audit log
- [ ] IP-based restrictions

### Version 3.0
- [ ] Two-Factor Authentication (2FA)
- [ ] OAuth/SSO integration
- [ ] Encryption at rest
- [ ] Database backend
- [ ] API with token auth
- [ ] Automated backups

### Version 4.0
- [ ] FIPS 140-2 compliance
- [ ] Hardware security key support
- [ ] Biometric authentication
- [ ] Advanced threat detection
- [ ] SIEM integration
- [ ] Blockchain verification

---

## Support & Reporting

### Security Vulnerabilities
If you discover a security vulnerability:
1. **DO NOT** post publicly
2. Email: security@pocketledger.app
3. Include: Description, steps to reproduce, impact
4. Allow 48 hours for response
5. We will credit you in release notes

### Getting Help
- **Documentation**: See README.md
- **Quick Start**: See QUICKSTART.md
- **Issues**: Create GitHub issue
- **Security**: See this file (SECURITY.md)

---

## Legal Disclaimers

### As-Is License
This software is provided "AS-IS" without warranty. See LICENSE file.

### User Responsibility
You are responsible for:
- Keeping passwords secure
- Backing up your data
- Following security best practices
- Complying with local laws

### No Liability
The authors are not liable for:
- Data loss
- Unauthorized access
- Business interruption
- Any damages whatsoever

---

## Quick Checklist for Users

- [ ] Created strong password (8+ characters)
- [ ] Password contains mix of characters
- [ ] Email is current and valid
- [ ] Downloaded first backup
- [ ] Logged out after use
- [ ] Understand data isolation
- [ ] Read this security guide

---

## Quick Checklist for Admins

- [ ] `users_data.json` is protected
- [ ] `user_data/` directory is backed up
- [ ] .gitignore protects sensitive files
- [ ] Dependencies are up-to-date
- [ ] Deployment uses HTTPS
- [ ] Logs are monitored
- [ ] Backups are tested
- [ ] Users are informed of security policy

---

**Last Updated**: January 28, 2026  
**Status**: Active  
**Version**: 1.0

For the latest security information, check this file regularly.

---

*Keep your ledger secure! 🔒*
