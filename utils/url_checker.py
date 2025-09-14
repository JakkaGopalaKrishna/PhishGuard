import re
from urllib.parse import urlparse
from .feature_extractor import extract_features_dict

def rule_based_check(url: str, features: dict = None):
    """Returns (result, score, reasons)
    result: 'phishing' or 'safe'
    score: 0-100 (higher means more suspicious)
    reasons: list of strings explaining flags
    """
    if features is None:
        features = extract_features_dict(url)

    score = 0
    reasons = []

    # HTTPS check
    if not features.get('has_https'):
        score += 20
        reasons.append("No HTTPS scheme detected.")

    # IP address in domain
    if features.get('has_ip'):
        score += 30
        reasons.append("Domain appears to be an IP address.")

    # '@' symbol
    if features.get('count_at', 0) > 0:
        score += 25
        reasons.append("'@' symbol present in URL (often used to obscure destination).")

    # long domain or path
    if features.get('domain_length', 0) > 30:
        score += 10
        reasons.append("Unusually long domain name.")
    if features.get('path_length', 0) > 100:
        score += 10
        reasons.append("Very long URL path.")

    # many dashes or digits
    if features.get('count_dashes', 0) >= 2:
        score += 5
        reasons.append("Multiple '-' characters in domain (possible obfuscation).")
    if features.get('count_digits', 0) > 5:
        score += 5
        reasons.append("Many numeric characters in URL.")

    # suspicious words
    if features.get('suspicious_words_in_url'):
        score += 15
        reasons.append("Contains suspicious keywords like 'login', 'verify', 'secure', etc.")

    # too many dots (subdomain obfuscation)
    if features.get('count_dots', 0) > 3:
        score += 10
        reasons.append("Many subdomains / dots in domain (possible obfuscation).")

    # final decision threshold
    if score >= 40:
        return 'phishing', score, reasons
    else:
        return 'safe', score, reasons
