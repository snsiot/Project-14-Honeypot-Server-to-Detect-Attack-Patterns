import folium
from geopy.geocoders import Nominatim
from log_parser import parse_log
from time import sleep

def get_location(ip):
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut
    geolocator = Nominatim(user_agent="honeypot-map")
    try:
        return geolocator.geocode(ip, timeout=10)
    except GeocoderTimedOut:
        return None

def visualize_ips():
    attacker_ips = parse_log()
    map_ = folium.Map(location=[20, 0], zoom_start=2)

    for ip in attacker_ips:
        print(f"Locating IP: {ip}")
        try:
            import requests
            res = requests.get(f"http://ip-api.com/json/{ip}").json()
            lat, lon = res.get("lat"), res.get("lon")
            if lat and lon:
                folium.Marker([lat, lon], popup=ip, icon=folium.Icon(color="red")).add_to(map_)
                sleep(1)  # Avoid getting rate-limited
        except:
            continue

    map_.save("attack_map.html")
    print("[+] Map saved as attack_map.html")

if __name__ == "__main__":
    visualize_ips()
