import requests
import folium
import logging
import ipaddress 

#Function to get geolocation info by using IP address
#Fetches data from ip-api.com see the json result and trasnform it to an python directory and generates an HTML map with the location
def get_info_by_ip(ip):
    try:
        #validate IP address
        ipaddress.ip_address(ip)
    except ValueError:
        print("[!] Invalid IP address format.")
        logging.error(f"Invalid IP address format: {ip}")
        return
    
    try: 
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

        if response.get("status") != "success":
            print(f"[!] Could not retrieve information for IP: {ip}")
            logging.error(f"Failed to retrieve IP information for {ip}: {response}")
            return

        data = {
            "[Status]": response.get("status"),
            "[IP]": response.get("query"),
            "Internet Provider": response.get("isp"),
            "Organisation": response.get("org"),
            "Country": response.get("country"),
            "Region": response.get("regionName"),
            "City": response.get("city"),
            "Zip Code": response.get("zip"),
            "TimeZone": response.get("timezone"),
            "Latitude": response.get("lat"),
            "Longitude": response.get("lon"),
        }
        

        for key, value in data.items():
            print(f"{key} : {value}")

        area = folium.Map(location=[response.get("lat"), response.get("lon")])
        folium.Marker(
            location=[response.get("lat"), response.get("lon")],
            popup=f"{response.get('query')} - {response.get('city')}, {response.get('country')}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(area)

        city = response.get("city") or "Unknown"
        filename = f"{response.get('query')} {city}.html"

        area.save(filename)
        logging.info(f"Map saved as {filename}")
            
    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection")
        logging.error("Connection error while trying to fetch IP information.")

