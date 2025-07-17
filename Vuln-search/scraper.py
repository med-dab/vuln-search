import requests

def search_surface_web(equipment):
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={equipment}&resultsPerPage=5'
    res = requests.get(url, timeout=10)
    items = []
    if res.status_code == 200:
        data = res.json()
        for vuln in data.get('vulnerabilities', []):
            cve_id = vuln['cve']['id']
            desc = vuln['cve']['descriptions'][0]['value']
            items.append({'title': cve_id, 'description': desc, 'source': 'NVD'})
    return items

def search_dark_web(equipment):
    # Needs Tor running on port 9050
    proxies = {'http': 'socks5h://tor:9050', 'https': 'socks5h://tor:9050'}
    dark_results = []
    try:
        url = f'http://exampledarkwebforum.onion/search?q={equipment}'
        r = requests.get(url, proxies=proxies, timeout=15)
        if r.status_code == 200:
            # Dummy parse
            dark_results.append({'title': f"Found on dark web: {equipment}", 'description': "Details hidden", 'source': url})
    except Exception as e:
        print(f"[!] Dark web error: {e}")
    return dark_results
