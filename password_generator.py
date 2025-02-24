import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_special=True):
    # Define character sets
    letters = string.ascii_letters if use_letters else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Combine all allowed characters
    all_chars = letters + digits + special
    
    # Check if at least one character type is selected
    if not all_chars:
        return "Error: At least one character type must be selected."
    
    # Ensure length is positive
    if length <= 0:
        return "Error: Length must be greater than 0."
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    # Evaluate password strength (basic check)
    strength = "Weak"
    if len(password) >= 12 and use_letters and use_digits and use_special:
        strength = "Strong"
    elif len(password) >= 8 and (use_letters and use_digits):
        strength = "Medium"
    
    return f"Password: {password}\nStrength: {strength}"

def main():
    print("Welcome to Password Generator!")
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        result = generate_password(length, use_letters, use_digits, use_special)
        print("\n" + result)
    except ValueError:
        print("Error: Please enter a valid number for length.")

if __name__ == "__main__":
    main()
