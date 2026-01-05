# Python AI Engine – Demo

Dette repository indeholder et simpelt Python-baseret backend-system, der behandler indgående henvendelser.
Systemet klassificerer beskeder, vurderer konfidens, håndterer fejl og beslutter, om der kan gives autosvar
eller om en henvendelse kræver menneskelig behandling.

## Funktionalitet
- Regelbaseret klassificering (pris, åbningstider, booking, andet)
- Konfidens-score og fallback-logik
- Autoresponder-templates
- Robust fejlhåndtering (fx manglende input)
- Genbrugelig “engine”-komponent

## Kør demo
```bash
python day29.py

## Demonstrerer
Dette projekt demonstrerer, hvordan man kan opbygge backend-logik til automatiseret håndtering
af henvendelser før brug af egentlige AI-modeller (LLM’er).

## Struktur
- engine.py – genbrugelig behandlingsmotor
- day27.py – eksempel på brug af engine
- day28.py – simple tests
- day29.py – samlet demo

