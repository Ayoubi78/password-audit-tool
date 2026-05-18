import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def check_password(password):
    score = 0
    feedback = []

    # Rule 1: Length check
    if len(password) >= 12:
        score += 25
    else:
        feedback.append("Use at least 12 characters.")

    # Rule 2: Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add at least one uppercase letter.")

    # Rule 3: Lowercase letter
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 4: Number
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one number.")

    # Rule 5: Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one special character.")

    # Rule 6: Common weak passwords
    weak_list = ["password", "123456", "qwerty", "admin", "letmein"]

    if password.lower() in weak_list:
        score = max(score - 30, 0)
        feedback.append("This is a very common password. Avoid it.")
    else:
        score += 15

    # Password strength classification
    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback


# Main Program
if __name__ == "__main__":

    print(Fore.CYAN + "\n🔒 Secure Password Audit Tool 🔒\n")

    # User input
    user_password = input("Enter a password to audit: ")

    # Run password audit
    score, strength, feedback = check_password(user_password)

    # Display results
    print("\n========== PASSWORD AUDIT RESULT ==========\n")

    # Weak Password
    if strength == "Weak":
        print(Fore.RED + "❌ Weak Password")
        print(Fore.RED + f"Security Score: {score}/100")

    # Medium Password
    elif strength == "Medium":
        print(Fore.YELLOW + "⚠️ Medium Password")
        print(Fore.YELLOW + f"Security Score: {score}/100")

    # Strong Password
    else:
        print(Fore.GREEN + "✅ Strong Password")
        print(Fore.GREEN + f"Security Score: {score}/100")

        print(Fore.GREEN + "\n✔ Password meets strong security requirements.")
        print(Fore.CYAN + "🔔 Security Reminder:")
        print(Fore.CYAN + "For better account protection, update your password every 30 days.")

    print(Style.RESET_ALL)

    # Recommendations
    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print(Fore.GREEN + "\nExcellent password security.")