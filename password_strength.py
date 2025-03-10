import re
import random
import streamlit as st

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Blacklist Common Passwords
    common_passwords = ["password", "123456", "password123", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        feedback.append("❌ This password is too common and easy to guess.")
        score = 1  # Force weak rating for common passwords

    return score, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)

    if score == 4:
        st.success("✅ Strong Password!")
        st.balloons()
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    # Display Feedback
    if feedback:
        st.write("### 🔍 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")

    # Suggest a strong password
    if score < 4:
        st.write("🔹 **Suggested Strong Password:**")
        st.code(generate_strong_password(), language="bash")
