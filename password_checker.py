import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Include lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Include uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include special characters (e.g. !, @, #).")

    if strength <= 2:
        return "Weak", remarks
    elif strength == 3 or strength == 4:
        return "Moderate", remarks
    else:
        return "Strong", remarks

# Function to generate a random password
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Checker & Generator")

# Password Input
password = st.text_input("Enter your password:", type="password")

if password:
    strength, tips = check_password_strength(password)
    st.markdown(f"### Strength: **{strength}**")
    if tips:
        st.write("Suggestions:")
        for tip in tips:
            st.write(f"– {tip}")

st.markdown("---")

# Password Generator
st.subheader("🔧 Need a strong password?")
length = st.slider("Select password length", 8, 32, 12)

if st.button("Generate Password"):
    generated = generate_password(length)
    st.code(generated, language="text")

st.write("------------")
st.write("Build with ♥ by [Shumaila][https://github.com/shumailahassan]")
