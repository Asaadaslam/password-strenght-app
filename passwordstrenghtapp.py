import re
import streamlit as st
import random
import string

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

    return score, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        score, _ = check_password_strength(password)
        if score == 4:
            return password

# Streamlit App
st.title("🔐 Password Strength Meter")

password_input = st.text_input("Enter your password", type="password")

if password_input:
    score, feedback = check_password_strength(password_input)
    st.subheader("🔍 Evaluation Result:")

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below:")
        for item in feedback:
            st.write(item)

st.markdown("---")
if st.button("💡 Generate Strong Password"):
    new_password = generate_strong_password()
    st.code(new_password, language="text")
