# app.py
# Arts & Advanced Big Data - Week 10
# Open API Project (with API Key): Healing Project by Seyeon
# Author: Kim Seyeon

import streamlit as st
import requests
import random

# -------------------------------
# 🌈 Page Config
# -------------------------------
st.set_page_config(page_title="Healing Project by Seyeon", page_icon="🌿", layout="centered")

st.markdown("""
<style>
body {background-color: #fffaf7; font-family: 'Helvetica'; color: #333;}
h1 {font-family: 'Didot'; font-size: 40px; text-align:center;}
hr {border: none; border-top: 2px solid #f5d0c5;}
.image-card {background-color: #fdeee6; border-radius: 20px; padding: 25px; text-align:center; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🖼️ Title Section
# -------------------------------
st.title("🌿 Healing Project by Seyeon")
st.markdown("### Take a breath, see something beautiful, and heal. 💕")

st.divider()

# -------------------------------
# 🌍 User Selection
# -------------------------------
choice = st.radio("Choose your healing theme:", ["🐾 Animals", "🌸 Nature"], horizontal=True)

# -------------------------------
# 🔑 API Key (Required)
# -------------------------------
PEXELS_KEY = st.secrets.get("PEXELS_KEY", None)

if not PEXELS_KEY:
    st.error("❌ Missing API Key! Please set your PEXELS_KEY in Streamlit Secrets.")
    st.stop()

# -------------------------------
# 🎨 Fetch Image
# -------------------------------
if st.button("✨ Show me something healing!"):
    query = "cute animals" if "Animals" in choice else "nature landscape"
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=50"
    headers = {"Authorization": PEXELS_KEY}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            st.error("⚠️ Failed to fetch from API. Check your API Key or rate limit.")
        else:
            data = res.json()
            photos = data.get("photos", [])
            if not photos:
                st.warning("No images found. Try again.")
            else:
                img = random.choice(photos)
                img_url = img["src"]["large"]
                photographer = img["photographer"]

                colors = ["#FFF0F5", "#F0FFF0", "#F0F8FF", "#FFF8DC", "#E6E6FA", "#FAF0E6"]
                bg = random.choice(colors)

                phrases = [
                    "“Take a deep breath and smile.”",
                    "“You deserve a gentle day.”",
                    "“Be kind to yourself today.”",
                    "“Stay pawsitive!”",
                    "“Little moments matter most.”",
                    "“Breathe in calm, breathe out love.”"
                ]

                st.markdown(
                    f"""
                    <div class="image-card" style="background-color:{bg}">
                        <img src="{img_url}" width="400">
                        <h3>{random.choice(phrases)}</h3>
                        <p style='font-size:13px; color:#555;'>📸 Photo by {photographer} (via Pexels)</p>
                    </div>
                    """, unsafe_allow_html=True
                )
    except Exception as e:
        st.error("⚠️ Something went wrong. Please try again later.")
