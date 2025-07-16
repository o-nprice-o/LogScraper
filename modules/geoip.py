import requests
import time

def enrich_with_geoip(events, ip_list):
    geo_cache = {}
    for ip in ip_list:
        try:
            response = requests.get(f"https://ip-api.com/json/{ip}?fields=country,regionName,city,query", timeout=5)
            if response.status_code == 200:
                geo_data = response.json()
                geo_cache[ip] = geo_data
            time.sleep(1)  # ip-api rate limit
        except Exception as e:
            geo_cache[ip] = {"error": str(e)}

    for e in events:
        if 'ip' in e and e['ip'] in geo_cache:
            e['geoip'] = geo_cache[e['ip']]
