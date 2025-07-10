import re
def check_password_strength (password):
    if len(password)<8:
        return "weak : passord must contain at least 8 character"
    if not any (char .isdigit() for char in password):
        return "weak : password must contain at least one numerical value"
    if not any (char .isupper() for char in password):
        return "weak : password must contain at least one upper character"
    if not any (char .islower() for char in password):
        return "weak : password must contain at least one lower character"
    if not re.search(r"[!@#$%^&*()_-+={}'':;><?/]",password):
        return "medium : password must contain at least one special character"
    return "strong : password is saved"
def password_checker():
    while True:
        password =input("enter your password (or type exit to quit) : ")
        if password == "exit":
            print("thank you")
            break
        result = check_password_strength(password)
        print (result)
password_checker()

