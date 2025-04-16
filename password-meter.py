
import streamlit as st
import re
import random

# Blacklist of weak passwords
blacklist = ["abc123" "password", "123456", "password123", "qwerty", "admin", "letmein"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common. Choose something more unique.")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong random password
def generate_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choices(chars, k=length))

# Streamlit UI
st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider strengthening it.")
        else:
            st.error("❌ Weak Password - Improve it using the tips below.")

        for item in feedback:
            st.write(item)
    else:
        st.warning("⚠️ Please enter a password.")

if st.button("Suggest Strong Password"):
    strong_pass = generate_password()
    st.info(f"💡 Try this strong password: `{strong_pass}`")