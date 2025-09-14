import streamlit as st
from utils.feature_extractor import extract_features_dict
from utils.url_checker import rule_based_check

st.set_page_config( page_title="PhishGuard", page_icon="JGKlogo1.png", layout="wide",)
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />""", unsafe_allow_html=True)


st.title("Phishing Website Detection Tool (Streamlit)")
st.markdown("Paste a URL and the tool will run lightweight rule-based checks to estimate if the site is suspicious.")

def interpret_score(score: int) -> str:
    if score <= 20:
        return "✅ Likely Safe (Very low risk)"
    elif score <= 40:
        return "🟡 Low Risk (Some suspicious factors)"
    elif score <= 60:
        return "🟠 Moderate Risk (Caution advised)"
    elif score <= 80:
        return "🔴 High Risk (Likely phishing)"
    else:
        return "🚨 Critical Risk (Almost certainly phishing)"


url_input = st.text_input("Enter URL (including http/https):", value="https://example.com")
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Check URL"):
    if not url_input.strip():
        st.error("Please enter a URL.")
    else:
        features = extract_features_dict(url_input)
        result, score, reasons = rule_based_check(url_input, features)
        risk_text = interpret_score(score)

        col1, col2 = st.columns([1,2])
        with col1:
            if result == "phishing":
                st.metric("Result", "Phishing ⚠️", delta=f"Score: {score}")
            else:
                st.metric("Result", "Likely Safe ✅", delta=f"Score: {score}")
            st.write("**Risk Level:**")
            st.success(risk_text if "Safe" in risk_text else risk_text)
        with col2:
            st.subheader("Analysis")
            st.write("**Extracted features:**")
            st.json(features)
        st.write("**Reasons / Flags:**")
        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("No obvious rule-based flags detected.")
        st.markdown("---")
        st.info("This tool is a demonstration using simple heuristics. For production use, combine rule-based checks with reputation APIs and ML models.")

#Copyright Mark
st.markdown(f"""
    <div class="footer">
        <a href="mailto:jakkakrishna2003@gmail.com"  class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-regular fa-envelope IconsStyle"></i></div>
            <div class="footer_text">Email</div>
        </a>
        <a href="https://www.linkedin.com/in/gopala-krishna-jakka-294a3b2a6/" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-brands fa-linkedin IconsStyle"></i></div>
            <div class="footer_text">Linked In</div>
        </a>
        <a href="https://github.com/JakkaGopalaKrishna" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-brands fa-github IconsStyle"></i></div>
            <div class="footer_text">Git Hub</div>
        </a>
        <a href="https://jgopalakrishna-portfolio.netlify.app/" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-regular fa-folder-open IconsStyle"></i></div>
            <div class="footer_text">Portfolio</div>
        </a>
        <div class='copy_div'>© Copyright 2025 J.Gopala Krishna, All rights reserved | Designed with care and crafted with 🩵 using Streamlit.</div>
    </div>
""", unsafe_allow_html=True)