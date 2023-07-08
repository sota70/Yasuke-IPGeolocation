import requests
import re
import sys


def build_request_url(ip: str) -> str:
    if not re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip):
        return "Invalid IP Address"
    return f"https://api.iplocation.net/?ip={ip}"

if __name__ == "__main__":
    ip: str = ""
    url: str = ""
    ip_geolocation_info: dict[str, str] = {}
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [ip_address]")
        exit(1)
    ip = sys.argv[1]
    url = build_request_url(ip)
    if url == "Invalid IP Address":
        print(url)
        exit(1)
    ip_geolocation_info = requests.get(url).json()
    if ip_geolocation_info.get("isp") is None:
        print("Lack of information")
        exit(1)
    if ip_geolocation_info["isp"].startswith("Private IP Address"):
        print("That's a private IP")
        exit(1)
    print("+=======================================================+")
    print(f"IP: {ip_geolocation_info.get('ip')}")
    print(f"Country: {ip_geolocation_info.get('country_name')}")
    print(f"ISP: {ip_geolocation_info.get('isp')}")
    print("More info: https://www.iplocation.net")
    print("+=======================================================+")
