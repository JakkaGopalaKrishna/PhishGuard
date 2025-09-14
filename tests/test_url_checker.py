from utils.url_checker import rule_based_check

def test_simple_safe():
    url = "https://github.com"
    result, score, reasons = rule_based_check(url)
    assert result == 'safe'
    assert score < 40

def test_ip_phishing():
    url = "http://192.168.0.1/login"
    result, score, reasons = rule_based_check(url)
    assert result == 'phishing'
    assert any('IP' in r or 'IP address' in r or 'IP' for r in reasons)

if __name__ == '__main__':
    test_simple_safe()
    test_ip_phishing()
    print('Tests passed')
