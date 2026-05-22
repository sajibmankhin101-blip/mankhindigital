import streamlit as st

st.set_page_config(page_title="Welcome | AI Masterclass Hub", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #071B33;
    }
    .page-header {
        padding: 40px 20px 10px;
        text-align: center;
        color: #FFFFFF;
    }
    .main-title {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: -0.02em;
    }
    .sub-title {
        font-size: 20px;
        color: #B8C7E0;
        margin-bottom: 32px;
        max-width: 820px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    .book-card {
        background: linear-gradient(170deg, rgba(6,18,40,0.95), rgba(5,15,30,0.85));
        padding: 28px;
        border-radius: 18px;
        border: 1px solid rgba(0, 240, 255, 0.18);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.30);
        margin-bottom: 24px;
        text-align: center;
    }
    .book-card h3 {
        color: #FFFFFF;
    }
    .book-card p {
        color: #D0D8F4;
    }
    .buy-btn {
        display: inline-block;
        background-color: #5E4BFF;
        color: white;
        padding: 14px 26px;
        font-weight: 700;
        border-radius: 999px;
        text-decoration: none;
        margin-top: 18px;
        transition: transform 0.2s ease, background-color 0.2s ease;
    }
    .buy-btn:hover {
        background-color: #7D63FF;
        transform: translateY(-2px);
    }
    .feature-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 18px;
        margin-top: 30px;
    }
    .feature-pill {
        background-color: rgba(255, 255, 255, 0.08);
        color: #E4EEFF;
        padding: 12px 18px;
        border-radius: 999px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        font-size: 14px;
    }
    .footer-note {
        color: #A3B1D2;
        text-align: center;
        margin-top: 36px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-header">', unsafe_allow_html=True)
st.markdown('<div class="main-title">Welcome to the AI Masterclass Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Discover easy-to-follow AI guides designed to help beginners, seniors, and professionals build confidence with ChatGPT, Claude, Gemini, and the latest AI tools for work, life, and business.</div>', unsafe_allow_html=True)

st.markdown('<div class="feature-list">', unsafe_allow_html=True)
st.markdown('<span class="feature-pill">No coding experience needed</span>', unsafe_allow_html=True)
st.markdown('<span class="feature-pill">Practical automation workflows</span>', unsafe_allow_html=True)
st.markdown('<span class="feature-pill">Step-by-step learning</span>', unsafe_allow_html=True)
st.markdown('<span class="feature-pill">Current for 2026 AI tools</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.subheader("🤖 ChatGPT & AI for Seniors")
    st.write("A warm, friendly introduction to AI for seniors and beginners. Learn how to use ChatGPT, Claude, and Gemini to stay connected, productive, and confident.")
    st.markdown('<a href="YOUR_SENIOR_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">Explore this Guide</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.subheader("🚀 AI for Beginners Guide 2026")
    st.write("A practical roadmap to mastering AI without technical barriers. Learn real-world prompts, tools, and workflows for home, career, and small business.")
    st.markdown('<a href="YOUR_BEGINNER_BOOK_AFFILIATE_LINK" target="_blank" class="buy-btn">Start Learning Today</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='footer-note'>© 2026 AI Masterclass Hub | Affiliate Disclosure: As an Amazon Associate I earn from qualifying purchases.</div>", unsafe_allow_html=True)
