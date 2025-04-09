import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email's stored password hash matches the hash of the password_to_check.
    Returns True if the login is successful, else False.
    """
    if email in stored_logins:
        stored_hash = stored_logins[email]
        return stored_hash == hash_password(password_to_check)
    return False

def main():
    # Updated stored logins
    stored_logins = {
        "pashmeen@site.com": hash_password("hello123"),
        "zain@codehub.com": hash_password("pythonRocks!"),
        "amina@devmail.com": hash_password("letMeIn456"),
    }

    # User input
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Login check
    if login(email, password, stored_logins):
        print("Login successful! ✅ Welcome,", email)
    else:
        print("Login failed! ❌ Email or password incorrect.")

# Start the program
if __name__ == '__main__':
    main()
