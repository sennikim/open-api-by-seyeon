# app.py
# Arts & Advanced Big Data - Week 10
# Open API Project: Healing Project by Seyeon (Final Version)
# Author: Kim Seyeon

import streamlit as st
import requests
import random

# -------------------------------
# 🌿 Page Config
# -------------------------------
st.set_page_config(page_title="Healing Project by Seyeon", page_icon="🌿", layout="centered")

st.markdown("""
<style>
body {background-color: #fffaf7; font-family: 'Helvetica'; color: #333;}
h1 {font-family: 'Didot'; font-size: 42px; text-align:center; color:#333;}
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
# 🧭 Sidebar Input Section
# -------------------------------
st.sidebar.header("🔑 API Settings")
saved_key = st.secrets.get("PEXELS_KEY", None)
api_key = st.sidebar.text_input("Enter your Pexels API Key (optional):", value=saved_key if saved_key else "", type="password")

theme = st.sidebar.radio("Choose your healing theme:", ["🐾 Animals", "🌸 Nature"])
show_button = st.sidebar.button("✨ Show me something healing!")

# -------------------------------
# 🎨 Random Quotes & Colors
# -------------------------------
phrases = [
    "“Take a deep breath and smile.”",
    "“You deserve a gentle day.”",
    "“Be kind to yourself today.”",
    "“Stay pawsitive!”",
    "“Little moments matter most.”",
    "“Breathe in calm, breathe out love.”"
]

colors = ["#FFF0F5", "#F0FFF0", "#F0F8FF", "#FFF8DC", "#E6E6FA", "#FAF0E6"]

# -------------------------------
# 🐾 Display Image Section
# -------------------------------
if show_button:
    query = "cute animals" if "Animals" in theme else "nature landscape"

    if api_key:
        headers = {"Authorization": api_key}
        url = f"https://api.pexels.com/v1/search?query={query}&per_page=50"
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                photos = data.get("photos", [])
                if photos:
                    img = random.choice(photos)
                    img_url = img["src"]["large"]
                    photographer = img["photographer"]
                    bg = random.choice(colors)

                    st.markdown(
                        f"""
                        <div class="image-card" style="background-color:{bg}">
                            <img src="{img_url}" width="400">
                            <h3>{random.choice(phrases)}</h3>
                            <p style='font-size:13px; color:#555;'>📸 Photo by {photographer} (via Pexels)</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
                else:
                    st.warning("No images found for this theme. Try again.")
            else:
                st.error("⚠️ Failed to fetch from Pexels API. Check your key or rate limit.")
        except Exception as e:
            st.error("⚠️ Something went wrong. Try again later.")
    else:
        st.info("🔍 Demo Mode: No API key provided. Showing sample image.")
        demo_images = {
            "🐾 Animals": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
            "🌸 Nature": "https://images.pexels.com/photos/355241/pexels-photo-355241.jpeg"
        }
        demo_url = demo_images[theme]
        bg = random.choice(colors)
        st.markdown(
            f"""
            <div class="image-card" style="background-color:{bg}">
                <img src="{demo_url}" width="400">
                <h3>{random.choice(phrases)}</h3>
                <p style='font-size:13px; color:#555;'>📸 Demo image (Pexels)</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.info("🩵 Use the sidebar to enter your API Key and click the button!")
