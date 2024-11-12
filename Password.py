import re

# Function to calculate password strength
def check_password_strength(password: str) -> str:
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Lowercase + Uppercase letters
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength += 1

    # Numbers check
    if re.search(r'\d', password):
        strength += 1

    # Special characters check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    # Length check for longer passwords (12+ characters)
    if len(password) >= 12:
        strength += 1

    # Final password strength evaluation
    if strength == 0:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    elif strength >= 4:
        return "Very Strong"

# Main program to prompt user input
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
