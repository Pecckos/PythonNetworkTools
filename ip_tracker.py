import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='8.8.8.8'):
    try: 
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)

        data = {
            '[Status]': response.get('status'),
            '[IP]': response.get('query'),
            'Internet Provider': response.get('isp'),
            'Organisation': response.get('org'),
            'Country': response.get('country'),
            'Region': response.get('regionName'),
            'City': response.get('city'),
            'Zip Code': response.get('zip'),
            'TimeZone': response.get('timezone'),
            'Latitude': response.get('lat'),
            'Longitude': response.get('lon'),
        }

        for key, value in data.items():
            print(f'{key} : {value}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        folium.Marker(
            location=[response.get('lat'), response.get('lon')],
            popup=f'{response.get('query')} - {response.get('city')}, {response.get('country')}',
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(area)

        city = response.get('city') or 'Unknown'
        filename = f'{response.get('query')} {city}.html'

        area.save(filename)
            
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection')

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('Pecckos IP Tracker'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip='')


if __name__ == "__main__":
    main()
