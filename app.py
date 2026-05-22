import streamlit as st

st.set_page_config(page_title="Mankhin Digital Hub 2026", page_icon="💎", layout="wide")

# সাদা থিম এবং আধুনিক সিএসএস (Light Theme Design)
st.markdown("""
<style>
/* মূল ব্যাকগ্রাউন্ড এবং স্ট্রীমলিটের ডিফল্ট গ্যাপ ফিক্স */
.stApp { background-color: #FFFFFF !important; color: #1E293B !important; }
.block-container { padding-bottom: 2rem !important; }

/* Welcome Page / Hero Banner Style (Light Version) */
.welcome-container { background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%); padding: 50px 20px; border-radius: 20px; border: 2px solid #D4AF37; text-align: center; margin-bottom: 40px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }
.main-title { font-size: 48px; font-weight: 900; color: #1E293B; margin-bottom: 15px; font-family: 'Helvetica Neue', sans-serif; letter-spacing: 1px; }
.welcome-desc { font-size: 19px; color: #475569; max-width: 800px; margin: 0 auto; line-height: 1.7; font-weight: 400; }

/* প্রোডাক্ট কার্ডের আধুনিক সাদা স্টাইল */
.product-card { background-color: #F8FAFC; padding: 30px; border-radius: 15px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.03); margin-bottom: 25px; transition: 0.3s; position: relative; }
.product-card:hover { border-color: #D4AF37; transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.08); }

/* ক্যাটাগরি লেবেল ব্যাজ */
.badge-book { background-color: #A020F0; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }
.badge-soft { background-color: #00A3FF; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }
.badge-gift { background-color: #FF007F; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; text-transform: uppercase; }

/* হাই-কনভার্সন ডার্ক গোল্ড বাটন */
.buy-btn { display: inline-block; background-color: #1E293B; color: #FFFFFF !important; padding: 12px 28px; text-align: center; font-weight: bold; border-radius: 6px; text-decoration: none; margin-top: 20px; font-size: 15px; width: 100%; transition: 0.3s; border: 1px solid #1E293B; }
.buy-btn:hover { background-color: #D4AF37; color: #000000 !important; border-color: #D4AF37; text-decoration: none; }

h3 { color: #1E293B !important; font-size: 22px !important; margin-top: 5px !important; margin-bottom: 12px !important; font-weight: 700 !important; }
p { color: #475569 !important; font-size: 14px; line-height: 1.6; }

/* ফুটার সেকশন ডিজাইন */
.footer-bar { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; padding: 20px 0px; margin-top: 60px; width: 100%; }
.footer-social { display: flex; gap: 20px; }
.footer-social a { color: #475569 !important; font-size: 20px; text-decoration: none !important; }
.footer-social a:hover { color: #D4AF37 !important; }
.footer-links { display: flex; gap: 25px; }
.footer-links a { color: #2563EB !important; font-size: 15px; text-decoration: none !important; font-weight: 500; }
.footer-links a:hover { text-decoration: underline !important; color: #1D4ED8 !important; }
.copyright-section { text-align: center; color: #64748B; font-size: 14px; margin-top: 25px; padding-bottom: 20px; font-family: sans-serif; }
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

# ৩টি কলাম একসাথে জেনারেট করা (লাইট লেআউট)
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
        <h3>Microsoft Office 2026</h3>
        <p>100% Genuine Pro Plus Lifetime Activation Key. Upgrade your personal computer or business laptop securely with instant digital delivery.</p>
        <a href="YOUR_SOFTWARE_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get Genuine License</a>
    </div>
    <!-- 🎁 কলাম ৩: গিফট কার্ড -->
    <div class="product-card" style="flex: 1;">
        <span class="badge-gift">🎁  Gift Card</span>
        <h3>Amazon Gift Card</h3>
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
