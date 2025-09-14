import re
from urllib.parse import urlparse
import tldextract

def has_ip_address(domain: str) -> bool:
    # crude IP detection
    return bool(re.match(r'^\d{1,3}(?:\.\d{1,3}){3}$', domain))

def extract_features_dict(url: str) -> dict:
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path  # handle inputs like 'example.com'
    path = parsed.path or ""
    ext = tldextract.extract(domain)
    root_domain = f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain

    features = {}
    features['has_https'] = (parsed.scheme == 'https')
    features['domain_length'] = len(domain)
    features['path_length'] = len(path)
    features['count_at'] = url.count('@')
    features['count_dashes'] = domain.count('-')
    features['count_dots'] = domain.count('.')
    features['count_digits'] = sum(c.isdigit() for c in url)
    features['has_ip'] = has_ip_address(domain)
    features['tld'] = ext.suffix
    features['root_domain'] = root_domain
    features['suspicious_words_in_url'] = any(word in url.lower() for word in ['login', 'secure', 'account', 'update', 'verify', 'bank', 'confirm', 'wp-admin'])
    return features
