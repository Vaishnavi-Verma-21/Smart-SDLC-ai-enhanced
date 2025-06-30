from security import hash_password, verify_password

# In-memory user "database"
users_db = {}

def register_user(username: str, password: str):
    if username in users_db:
        return False
    users_db[username] = {
        "username": username,
        "hashed_password": hash_password(password)
    }
    return True

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if user and verify_password(password, user["hashed_password"]):
        return user
    return None
