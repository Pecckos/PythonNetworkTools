
Denna portscanner skannar igenom vanliga portar och visar vilka som är öppna.  
Perfekt för övningar inom red teaming, penetrationstester eller nätverksanalys.

Bygger på SuperFastPython av Jason Brownlee (https://superfastpython.com/threadpoolexecutor-port-scanner/)

---

## Funktioner 
- Skannar flera portar parallellt med `ThreadPoolExecutor`
- Automatiskt urval av vanliga portar (t.ex. 22, 80, 443, 3306)
- Snabb och effektiv tack vare multitrådning
- Enkel CLI-användning via meny i `main.py`
- Felhantering om IP är nere eller port är stängd

OBS !! --> För djupare analys rekommenderas nmap, det kommer att implemeteras i detta projekt senare. 