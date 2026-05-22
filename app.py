import streamlit as st

st.set_page_config(page_title="Mankhin Digital Hub 2026", page_icon="💎", layout="wide")

# থিম ডিজাইন এবং সিএসএস (CSS)
st.markdown("""
<style>
.stApp { background-color: #0B0C10 !important; }
.block-container { padding-bottom: 2rem !important; }
.welcome-container { background: linear-gradient(135deg, #1F2833 0%, #0B0C10 100%); padding: 50px 20px; border-radius: 20px; border: 1px solid #D4AF37; text-align: center; margin-bottom: 40px; box-shadow: 0 15px 30px rgba(0,0,0,0.7); }
.main-title { font-size: 48px; font-weight: 900; color: #D4AF37; margin-bottom: 15px; font-family: 'Helvetica Neue', sans-serif; letter-spacing: 1px; }
.welcome-desc { font-size: 19px; color: #E2E8F0; max-width: 800px; margin: 0 auto; line-height: 1.7; font-weight: 400; }
.product-card { background-color: #1F2833; padding: 30px; border-radius: 15px; border: 2px solid #333; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); margin-bottom: 25px; transition: 0.3s; position: relative; }
.product-card:hover { border-color: #D4AF37; transform: translateY(-5px); }
.badge-book { background-color: #A020F0; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }
.badge-soft { background-color: #00F0FF; color: black; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }
.badge-gift { background-color: #FF007F; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }
.buy-btn { display: inline-block; background-color: #D4AF37; color: #000000; padding: 12px 28px; text-align: center; font-weight: bold; border-radius: 6px; text-decoration: none; margin-top: 20px; font-size: 15px; width: 100%; transition: 0.3s; }
.buy-btn:hover { background-color: #FFDF00; color: #000000; text-decoration: none; }
h3 { color: #FFFFFF !important; font-size: 22px !important; margin-top: 5px !important; margin-bottom: 12px !important; }
p { color: #C5C6C7 !important; font-size: 14px; line-height: 1.6; }
.footer-bar { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #333; border-bottom: 1px solid #333; padding: 20px 0px; margin-top: 60px; width: 100%; }
.footer-social { display: flex; gap: 20px; }
.footer-social a { color: #C5C6C7 !important; font-size: 20px; text-decoration: none !important; }
.footer-social a:hover { color: #D4AF37 !important; }
.footer-links { display: flex; gap: 25px; }
.footer-links a { color: #5865F2 !important; font-size: 15px; text-decoration: none !important; font-weight: 500; }
.footer-links a:hover { text-decoration: underline !important; color: #727FFF !important; }
.copyright-section { text-align: center; color: #888; font-size: 14px; margin-top: 25px; padding-bottom: 20px; font-family: sans-serif; }
</style>
<link rel="stylesheet" href="https://cloudflare.com">
""", unsafe_allow_html=True)

# 🌐 Welcome Page Banner
st.markdown("""
<div class="welcome-container">
    <div class="main-title">💎 Welcome to Mankhin Digital Hub</div>
    <div class="welcome-desc">
        Explore our handpicked collection of world-class digital essentials. Whether you want to master Artificial Intelligence with our top-rated beginner guides, upgrade your computer using 100% genuine Microsoft Software, or send official Gift Cards to your loved ones—we provide secure links and instant digital delivery for everything you need.
    </div>
</div>
""", unsafe_allow_html=True)

# ৩টি কলামের জন্য কন্টেন্ট একসাথে জেনারেট করা (স্পেসিং এরর পুরোপুরি ফিক্সড)
st.markdown("""
<div style="display: flex; gap: 20px; width: 100%;">
    <!-- 📚 কলাম ১: বই -->
    <div class="product-card" style="flex: 1;">
        <span class="badge-book">📚 Best Selling Book</span>
        <h3>AI For Beginners Guide</h3>
        <p>Learn AI in 3 Days without any coding. Perfect hands-on guide to boost your daily work, home automation, and online business productivity safely.</p>
        <a href="YOUR_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get It on Amazon</a>
    </div>
    <!-- 💾 কলাম ২: সফটওয়্যার -->
    <div class="product-card" style="flex: 1;">
        <span class="badge-soft">💾 Genuine Software</span>
        <h3>Microsoft Office 2021</h3>
        <p>100% Genuine Pro Plus Lifetime Activation Key. Upgrade your personal computer or business laptop securely with instant digital delivery.</p>
        <a href="YOUR_SOFTWARE_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get Genuine License</a>
    </div>
    <!-- 🎁 কলাম ৩: গিফট কার্ড -->
    <div class="product-card" style="flex: 1;">
        <span class="badge-gift">🎁 Official Gift Card</span>
        <h3>Amazon eGift Card</h3>
        <p>Official Amazon digital gift cards. Perfect for shopping online, gifting to loved ones, or funding your personal account balance instantly.</p>
        <a href="YOUR_GIFTCARD_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Purchase Gift Card</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 📋 ফুটার লেআউট
st.markdown("""
<div class="footer-bar">
    <div class="footer-social">
        <a href="#" target="_blank"><i class="fab fa-tumblr"></i></a>
        <a href="mailto:your-email@example.com"><i class="fas fa-envelope"></i></a>
        <a href="#" target="_blank"><i class="fab fa-pinterest"></i></a>
        <a href="#" target="_blank"><i class="fab fa-youtube"></i></a>
        <a href="#" target="_blank"><i class="fab fa-linkedin"></i></a>
    </div>
    <div class="footer-links">
        <a href="#">Privacy</a>
        <a href="#">Affiliate Disclosure</a>
        <a href="#">Terms & Disclaimer</a>
    </div>
</div>
<div class="copyright-section">
    © 2026 Search AI Finder | All Rights Reserved
</div>
""", unsafe_allow_html=True)
