import streamlit as st

st.set_page_config(page_title="Exclusive AI Masterclass Guides", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: bold; text-align: center; color: #00F0FF; margin-bottom: 10px; }
    .sub-title { font-size: 20px; text-align: center; color: #AAB9C8; margin-bottom: 40px; }
    .book-card { background-color: #0B0F19; padding: 25px; border-radius: 10px; border: 1px solid #00F0FF; margin-bottom: 20px; text-align: center; }
    .buy-btn { display: inline-block; background-color: #A020F0; color: white; padding: 12px 24px; text-align: center; font-weight: bold; border-radius: 5px; text-decoration: none; margin-top: 15px; }
    .buy-btn:hover { background-color: #b832ff; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 Master the Future: Top AI Guides for 2026</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Learn ChatGPT, Claude, and Gemini to automate your life, career, and business. No technical skills required!</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.subheader("🤖 ChatGPT & AI for Seniors")
    st.write("Your Friendly Guide to Getting Started. Master ChatGPT, Claude, and Gemini step-by-step. Stay connected and learn new skills seamlessly.")
    st.markdown('<a href="YOUR_SENIOR_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get It on Amazon</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.subheader("🚀 AI for Beginners Guide 2026")
    st.write("Learn AI in 3 Days (No Coding Required). A step-by-step, hands-on beginner's guide to AI for Work, Home & Business productivity.")
    st.markdown('<a href="YOUR_BEGINNER_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">🛒 Get It on Amazon</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr><p style='text-align: center; color: gray;'>© 2026 AI Book Hub | Affiliate Disclosure: As an Amazon Associate I earn from qualifying purchases.</p>", unsafe_allow_html=True)
