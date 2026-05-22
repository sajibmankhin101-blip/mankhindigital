import streamlit as st

st.set_page_config(page_title="Premium Digital Hub 2026", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0B0C10 !important; }
    
    /* Welcome Page / Hero Banner Style */
    .welcome-container { background: linear-gradient(135deg, #1F2833 0%, #0B0C10 100%); padding: 50px 20px; border-radius: 20px; border: 1px solid #D4AF37; text-align: center; margin-bottom: 50px; box-shadow: 0 15px 30px rgba(0,0,0,0.7); }
    .main-title { font-size: 48px; font-weight: 900; color: #D4AF37; margin-bottom: 15px; font-family: 'Helvetica Neue', sans-serif; letter-spacing: 1px; }
    .welcome-desc { font-size: 19px; color: #E2E8F0; max-width: 800px; margin: 0 auto; line-height: 1.7; font-weight: 400; }
     .product-card { background-color: #1F2833; padding: 30px; border-radius: 15px; border: 2px solid #333; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); margin-bottom: 25px; transition: 0.3s; position: relative; }
    .product-card:hover { border-color: #D4AF37; transform: translateY(-5px); }
    
    .badge-book { background-color: #A020F0; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; }
    .badge-soft { background-color: #00F0FF; color: black; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; }
    .badge-gift { background-color: #FF007F; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; }
    
    .buy-btn { display: inline-block; background-color: #D4AF37; color: #000000; padding: 12px 28px; text-align: center; font-weight: bold; border-radius: 6px; text-decoration: none; margin-top: 20px; font-size: 15px; width: 100%; transition: 0.3s; }
    .buy-btn:hover { background-color: #FFDF00; }
    
    h3 { color: #FFFFFF !important; font-size: 22px !important; margin-top: 5px !important; }
    p { color: #C5C6C7 !important; font-size: 14px; line-height: 1.6; }
    .footer-bar { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #333; border-bottom: 1px solid #333; padding: 15px 10px; margin-top: 50px; }
    .footer-social a { color: #C5C6C7; margin-right: 15px; font-size: 18px; text-decoration: none; }
    .footer-social a:hover { color: #D4AF37; }
    .footer-links a { color: #4F46E5; margin-left: 20px; font-size: 14px; text-decoration: none; font-weight: 500; }
    .footer-links a:hover { text-decoration: underline; color: #6366F1; }
    .copyright-section { text-align: center; color: #C5C6C7; font-size: 14px; margin-top: 20px; font-family: sans-serif; line-height: 1.5; }
    </style><link rel="stylesheet" href="https://cloudflare.com">
""", unsafe_allow_html=True)

# 🌐 Welcome Page Banner
st.markdown("""
    <div class="welcome-container">
        <div class="main-title">💎 Welcome to Premium Digital Hub</div>
        <div class="welcome-desc">
            Explore our handpicked collection of world-class digital essentials. Whether you want to master Artificial Intelligence with our top-rated beginner guides, upgrade your computer using 100% genuine Microsoft Software, or send official Gift Cards to your loved ones—we provide secure links and instant digital delivery for everything you need.
        </div>
    </div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-book">📚 BEST SELLING BOOK</span>', unsafe_allow_html=True)
    st.subheader("AI For Beginners Guide")
    st.write("Learn AI in 3 Days without any coding. Perfect hands-on guide to boost your daily work, home automation, and online business productivity safely.")
    st.markdown('<a href="YOUR_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get It on Amazon</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-soft">💾 GENUINE SOFTWARE</span>', unsafe_allow_html=True)
    st.subheader("Microsoft Office 2021")
    st.write("100% Genuine Pro Plus Lifetime Activation Key. Upgrade your personal computer or business laptop securely with instant digital delivery.")
    st.markdown('<a href="YOUR_SOFTWARE_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get Genuine License</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-gift">🎁 OFFICIAL GIFT CARD</span>', unsafe_allow_html=True)
    st.subheader("Amazon eGift Card")
    st.write("Official Amazon digital gift cards. Perfect for shopping online, gifting to loved ones, or funding your personal account balance instantly.")
    st.markdown('<a href="YOUR_GIFTCARD_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Purchase Gift Card</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="footer-bar">
        <!-- বাম পাশের সোশ্যাল মিডিয়া আইকনসমূহ -->
        <div class="footer-social">
            <a href="#" target="_blank"><i class="fab fa-tumblr"></i></a>
            <a href="mailto:your-email@example.com"><i class="fas fa-envelope"></i></a>
            <a href="#" target="_blank"><i class="fab fa-pinterest"></i></a>
            <a href="#" target="_blank"><i class="fab fa-youtube"></i></a>
            <a href="#" target="_blank"><i class="fab fa-linkedin"></i></a>
        </div><div class="footer-links">
            <a href="#">Privacy</a>
            <a href="#">Affiliate Disclosure</a>
            <a href="#">Terms & Disclaimer</a>
        </div>
    </div> <div class="copyright-section">
        © 2026 Mankhin Digital | All Rights Reserved
    </div>
""", unsafe_allow_html=True)