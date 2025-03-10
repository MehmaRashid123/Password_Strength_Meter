import re
import streamlit as st
import random


def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check (8+ characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Extra Strength Length Check (12+ characters)
    if len(password) >= 12:
        score += 1  # Extra point for longer passwords

    # Contain uppercase & lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase & lowercase letters.")

    # Include at least one digit (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one digit (0-9).")

    # Have one special character (!@#$%&*+-=)
    if re.search(r"[!@#$%&*+-=]", password):
        score += 1
    else:
        feedback.append("❌ Password should have at least one special character (!@#$%&*+-=).")

    # Blacklist password check
    common_passwords = {"password", "123456", "password123", "name123", "abc123"}
    if password.lower() in common_passwords:
        feedback.append("❌ This password is too common and easy to guess.")
        score = min(score, 1)  # If it's common, force it to be weak.

    return score, feedback

#random pass
def generate_strong_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*+-="
    return "".join(random.choice(characters) for _ in range(length))



# UI
st.title(":lock: Password Strength Meter")

password = st.text_input("Enter Your Password", type="password")

if password:
    score, feedback = check_password_strength(password)

    # Display Score
    st.subheader(f"Password Score: {score}/5")

    if score == 5:
        st.success("✔ **Very Strong Password!** Your password meets all security criteria.")
        st.balloons()
    elif score == 4:
        st.success("✅ **Strong Password!** Good, but could be longer.")
    elif score == 3:
        st.warning("⚠ **Moderate Password.** Good, but missing some security features.")
    else:
        st.error("❎ **Weak Password!** Your password is missing key security elements.")

    # Display feedback
    if feedback:
        st.write("### 🔍 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")

    if score < 4:
        st.write("🔹 **Suggested Strong Password:**")
        st.code(generate_strong_password(), language="bash")