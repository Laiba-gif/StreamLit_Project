# save this file as yourname.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes

# ------------------------------
# Title & Description
# ------------------------------
st.set_page_config(page_title="Digital Wellness & Screen Time Manager", layout="centered")
st.title("📱 Digital Wellness & Screen Time Manager")
st.write("Track your screen time, socializing, and mindfulness to manage stress better!")

# ------------------------------
# Load a Dataset from sklearn
# ------------------------------
data = load_diabetes(as_frame=True)
df = data.frame


# ------------------------------
# User Inputs (Widgets)
# ------------------------------
st.subheader("✨ Enter Your Daily Habits")

screen_time = st.slider("📱 Screen Time (hours per day)", 0, 15, 5)
social_time = st.slider("🫂 Socializing Time (minutes per day)", 0, 300, 60)
mindfulness = st.slider("🧘 Mindfulness / Meditation (minutes per day)", 0, 120, 10)

# Extra Widgets
caffeine = st.number_input("☕ Caffeine intake (mg per day)", min_value=0, max_value=1000, value=200)
sleep_quality = st.radio("😴 How was your sleep?", ["Poor", "Average", "Good"])

# ------------------------------
# Simple Stress Estimation
# ------------------------------
stress_score = screen_time * 2 - (social_time / 60) - (mindfulness / 10)

if caffeine > 300:
    stress_score += 10
if sleep_quality == "Poor":
    stress_score += 15

stress_level = "😌 Low"
if stress_score > 20:
    stress_level = "😟 Medium"
if stress_score > 40:
    stress_level = "🔥 High"

# ------------------------------
# Display Results
# ------------------------------
st.subheader("📋 Your Stress Analysis")
st.metric(label="Estimated Stress Score", value=int(stress_score))
st.success(f"Your Stress Level: {stress_level}")

# ------------------------------
# Recommendations
# ------------------------------
st.subheader("💡 Recommendations")
if stress_level == "😌 Low":
    st.write("✅ You're doing well! Keep maintaining balance.")
elif stress_level == "😟 Medium":
    st.write("⚠️ Try reducing screen time or adding 15 mins of mindfulness.")
else:
    st.write("🔥 High stress detected! Reduce caffeine, sleep better, and meditate.")

# ------------------------------
# Visualization
# ------------------------------
st.subheader("📈 Wellness Breakdown")
chart_data = pd.DataFrame({
    "Activity": ["Screen Time", "Socializing", "Mindfulness"],
    "Minutes": [screen_time*60 , social_time, mindfulness]
})
st.bar_chart(chart_data.set_index("Activity"))

