#this is an example for test case writing

def validate_user(username, password):
    "Validates user credentials based on simple rules"

    if not username or not password:
        return "Username or password cannot be empty"
    
    if len(password) <6:
        return "Password too short"
    
    if username == "admin" and password == "admin123":
        return"Login successful"
    
    return "Invalid credentials"