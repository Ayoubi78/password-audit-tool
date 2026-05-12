import re

def check_password(password):
    score = 0
    feedback = []

    # Rule 1: length
    if len(password) >= 12:
        score += 25
    else:
        feedback.append("Use at least 12 characters.")

    # Rule 2: uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add at least one uppercase letter.")

    # Rule 3: lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 4: number
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one number.")

    # Rule 5: special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one special character.")

    # Rule 6: common weak passwords
    weak_list = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in weak_list:
        score = max(score - 30, 0)
        feedback.append("This is a very common password. Avoid it.")
    else:
        score += 15

    # Decide strength
    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback


if __name__ == "__main__":
    user_password = input("Enter a password to audit: ")
    score, strength, feedback = check_password(user_password)

    print(f"\nScore: {score}/100")
    print(f"Strength: {strength}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great password! No suggestions.")