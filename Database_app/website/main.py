"""
Hlavní aplikace - main.py

Tento skript inicializuje a spouští Flask webovou aplikaci e-shopu.

Funkce:
- Importuje funkci `create_app` z balíčku `website`.
- Vytváří instanci aplikace voláním `create_app`.
- Spouští aplikaci ve vývojovém režimu, pokud je tento skript spuštěn jako hlavní modul.

Použití:
- Spusťte tento skript příkazem `python main.py` pro spuštění aplikace.

"""

from website import create_app
from flask import session

# Vytvoření instance aplikace voláním create_app
app = create_app()

# Spuštění aplikace ve vývojovém režimu
if __name__ == '__main__':
   app.run(debug=True)
