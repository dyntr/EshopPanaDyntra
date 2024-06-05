# Dokumentace projektu "E-shopu Pana Dyntra"

## Obsah

1. [Popis projektu](#popis-projektu)
2. [Struktura projektu](#struktura-projektu)
3. [Funkce](#funkce)
4. [Instalace a spuštění](#instalace-a-spuštění)
5. [Použití](#použití)
6. [Výjimky](#výjimky)
7. [Závěr](#závěr)

## Popis projektu

Projekt **My E-shop** je školní projekt vyvinutý pro správu dat elektronického obchodu. Systém umožňuje přidávat a získávat data o zákaznících, produktech, objednávkách, položkách objednávek a transakcích. Program využívá několik tříd, z nichž každá představuje jiný typ dat v obchodě.

- **Customer**: Reprezentuje zákazníka obchodu a má vlastnosti jako jméno, adresa, město a kreditní body.
- **Product**: Reprezentuje produkt obchodu a má vlastnosti jako jméno, typ a cena.
- **Order**: Reprezentuje objednávku zadanou zákazníkem a má vlastnosti jako ID zákazníka, datum objednávky a ID objednávky.
- **OrderItem**: Reprezentuje jednu položku v objednávce a má vlastnosti jako ID objednávky, ID produktu a množství.
- **Transaction**: Reprezentuje transakci mezi obchodem a zákazníkem a má vlastnosti jako ID transakce, ID objednávky a částka.

## Struktura projektu

Projekt je rozdělen do několika hlavních komponent:

### Struktura souborů

```
config
├── config.ini
└── requirements.txt

sql
└── script.sql

src
├── db_connect.py
├── db_factory.py
├── main.py
├── sc_factory.py
├── sc_test.py
├── test_conn.py
├── test_db.py
└── ui.py

website
├── static
│   ├── script.js
│   └── styles.css
├── templates
│   ├── account.php
│   ├── auth.php
│   ├── base.php
│   ├── cart.php
│   ├── favicon.ico
│   ├── order_history.php
│   ├── products.php
│   └── search.php
├── __init__.py
├── auth.py
├── main.py
├── test_auth.py
├── test_views.py
└── views.py
```

### Soubory projektu

- **config/config.ini**: Konfigurační soubor pro nastavení databáze.
- **config/sql/script.sql**: SQL skript pro vytvoření databáze a tabulek.

- **src/db_connect.py**: Soubor obsahující třídu pro připojení k databázi.
- **src/db_factory.py**: Soubor obsahující tovární třídy pro správu dat (zákazníci, produkty, objednávky, položky objednávek, transakce).
- **src/main.py**: Hlavní soubor aplikace, který inicializuje a spouští aplikaci.
- **src/sc_factory.py**: Soubor obsahující třídy pro vytváření objednávek.
- **src/sc_test.py**: Soubor obsahující testy pro objednávky.
- **src/test_conn.py**: Soubor pro testování připojení k databázi.
- **src/test_db.py**: Soubor pro testování databázových operací.
- **src/ui.py**: Soubor obsahující uživatelské rozhraní pro příkazovou řádku.

- **website/static/script.js**: JavaScript soubor pro interaktivitu webové aplikace.
- **website/static/styles.css**: CSS soubor pro stylování aplikace.

- **website/templates/account.php**: Šablona pro stránku účtu uživatele.
- **website/templates/auth.php**: Šablona pro přihlašování a registraci.
- **website/templates/base.php**: Základní šablona pro celou webovou aplikaci.
- **website/templates/cart.php**: Šablona pro stránku nákupního košíku.
- **website/templates/favicon.ico**: Ikona webu.
- **website/templates/order_history.php**: Šablona pro historii objednávek.
- **website/templates/products.php**: Šablona pro stránku produktů.
- **website/templates/search.php**: Šablona pro stránku vyhledávání.

- **website/__init__.py**: Inicializační soubor pro webovou aplikaci.
- **website/auth.py**: Soubor obsahující autentizační logiku aplikace (přihlášení, registrace, odhlášení).
- **website/main.py**: Hlavní soubor webové aplikace.
- **website/test_auth.py**: Testy pro autentizační funkce.
- **website/test_views.py**: Testy pro hlavní pohledy aplikace.
- **website/views.py**: Soubor obsahující hlavní pohledy a logiku aplikace.

## Funkce

Projekt nabízí následující hlavní funkce:

### Třídy

#### CustomerFactory
- **create_customer**: Vytvoří nového zákazníka a vloží ho do tabulky "Customer".
- **read_customer**: Získá konkrétního zákazníka podle ID z tabulky "Customer".
- **update_customer**: Aktualizuje informace o stávajícím zákazníkovi v tabulce "Customer".
- **delete_customer**: Smaže zákazníka z tabulky "Customer".

#### ProductFactory
- **add_product**: Přidá nový produkt a vloží ho do tabulky "Product".
- **get_product**: Získá konkrétní produkt podle ID z tabulky "Product".
- **update_product**: Aktualizuje informace o stávajícím produktu v tabulce "Product".
- **delete_product**: Smaže produkt z tabulky "Product".

#### OrdersFactory
- **create_order**: Vytvoří novou objednávku a vloží ji do tabulky "Orders".
- **read_order**: Získá konkrétní objednávku podle ID z tabulky "Orders".
- **update_order**: Aktualizuje informace o stávající objednávce v tabulce "Orders".
- **delete_order**: Smaže objednávku z tabulky "Orders".

#### OrderItemFactory
- **create_order_item**: Vytvoří novou položku objednávky a vloží ji do tabulky "OrderItem".
- **read_order_item**: Získá konkrétní položku objednávky podle ID z tabulky "OrderItem".
- **update_order_item**: Aktualizuje informace o stávající položce objednávky v tabulce "OrderItem".
- **delete_order_item**: Smaže položku objednávky z tabulky "OrderItem".

#### TransactionFactory
- **create_transaction**: Vytvoří novou transakci a vloží ji do tabulky "Transaction".
- **read_transaction**: Získá konkrétní transakci podle ID z tabulky "Transaction".
- **update_transaction**: Aktualizuje informace o stávající transakci v tabulce "Transaction".
- **delete_transaction**: Smaže transakci z tabulky "Transaction".

#### GenerateReportFactory
- **generate_report**: Generuje report, který shrnuje data v databázi.

### Další funkce

- **menu function**: Zobrazuje hlavní menu programu a poskytuje možnosti pro přístup k různým částem programu.
- **customer_menu function**: Správa zákazníků (přidávání, úpravy, získávání informací).
- **product_menu function**: Správa produktů (přidávání, úpravy, získávání informací).
- **order_menu function**: Správa objednávek (přidávání, úpravy, získávání informací).
- **order_item_menu function**: Správa položek objednávek (přidávání, úpravy, získávání informací).
- **transaction_menu function**: Správa transakcí (přidávání, úpravy, získávání informací).
- **import_data function**: Import dat do programu z CSV souboru.

## Instalace a spuštění

### Předpoklady

- Nainstalovaný MySQL server.
- Nainstalovaný Python 3.
- Nainstalovaný PhpStorm / Visual Studio Code.

## Instalace a spuštění

### Předpoklady
- Nainstalovaný MySQL server.
- Nainstalovaný Python 3.
- Nainstalovaný Visual Studio Code.

### Instalace závislostí
V terminálu spusťte následující příkaz pro instalaci všech závislostí najednou:

```bash
pip install -r config/requirements.txt
```

### Nastavení databáze

1. Stáhněte a nainstalujte MySQL server.
2. Vytvořte připojení k localhost s následujícími parametry:
   - Hostname: 127.0.0.1
   - Port: 3306
   - Username: SA
   - Password: student
3. V MySQL vytvořte nový dotaz a zkopírujte obsah souboru `script.sql` do dotazu.
4. Nejprve vytvořte a použijte databázi a poté vytvořte tabulky. Poté můžete vložit nějaká data a spustit příkazy pro vytvoření pohledů.

### Spuštění webové aplikace

1. Otevřete terminál a změňte adresář na `website`:
   ```bash
   cd Database_app/website
   ```
2. Spusťte webovou aplikaci:
   ```bash
   python3 -m website.main 5001
   ```
3. Webová aplikace bude dostupná na `http://127.0.0.1:5000`.

### Spuštění terminálové aplikace

1. Otevřete terminál a změňte adresář na `src`:
   ```bash
   cd Database_app/src
   ```
2. Spusťte terminálovou aplikaci:
   ```bash
   python3 main.py 
   ```

## Použití

### Webová aplikace

Webová aplikace je určena pro uživatele a nabízí následující funkce:
- Prohlížení produktů.
- Přidávání produktů do nákupního košíku.
- Nákup produktů
- Správa účtu (zobrazení a úprava informací o účtu).
- Přihlášení a registrace.

### Terminálová aplikace

Terminálová aplikace je určena pro administrátory a nabízí následující funkce:
- Správa zákazníků (přidávání, úpravy, získávání informací).
- Správa produktů (přidávání, úpravy, získávání informací).
- Správa objednávek (přidávání, úpravy, získávání informací).
- Správa položek objednávek (přidávání, úpravy, získávání informací).
- Správa transakcí (přidávání, úpravy, získávání informací).
- Generování reportů.
- Import dat z CSV souborů.

## Výjimky

Při používání aplikace se mohou vyskytnout následující výjimky:

- **mysql.connector.errors.IntegrityError**: Při pokusu o smazání zákazníka, který má přidružené objednávky.
- **AttributeError**: Při pokusu o přístup k neexistujícímu atributu objektu.
- **TypeError**: Při předání nesprávného typu argumentu funkci.
- **IndexError**: Při pokusu o přístup k neexistujícímu indexu v seznamu nebo n-tici.
- **ProgrammingError**: Při pokusu o provedení neplatného SQL příkazu.

## Závěr

Tento projekt poskytuje kompletní řešení pro správu dat e-shopu, včetně správy zákazníků, produktů, objednávek, položek objednávek a transakcí. Systém je navržen tak, aby byl snadno rozšiřitelný a přizpůsobitelný pro různé potřeby. Pokud najdete nějaké chyby nebo máte návrhy na zlepšení, neváhejte mě kontaktovat na mém emailu. Děkuji za použití a přeji vám příjemné používání aplikace!

---

** Autor: Patrick Dyntr**  
Třída: C3b  
Telefon: +420607111006  
Email: dyntr@spsejecna.cz  
Škola: SPŠE Ječná 
Popis: Závěrečná práce 3. ročníku.
