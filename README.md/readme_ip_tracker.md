
Ett stilrent och kraftfullt Python-verktyg som spårar IP-adresser och visualiserar deras geografiska plats på en interaktiv karta.  
Perfekt för OSINT-övningar, nätverksprojekt eller bara ren nyfikenhet.

OBS!! --> Detta projekt använder det publika API:t från [ip-api.com](http://ip-api.com) enligt deras fria användarlicens (max 45 requests/minut).  
För högre gränser eller kommersiell användning, se deras [premiumplaner](https://members.ip-api.com/).

Bygger på [Folium](https://python-visualization.github.io/folium/), [ip-api.com](http://ip-api.com), och lite terminalmagi från `pyfiglet`.

---

## Funktioner

- Snyggt terminalgränssnitt med ASCII-banner  
- Hämta detaljerad IP-information (stad, region, land, ISP, m.m.)  
- Generera interaktiva kartor med en pin-marker på IP-positionen  
- Spara varje spårning som en `.html`-fil du kan öppna i webbläsaren  
- CLI-kompatibelt – kör via terminal med argument eller input  
