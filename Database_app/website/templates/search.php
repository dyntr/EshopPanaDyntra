<!DOCTYPE html>
<html>

<head>
    <!--
    Hlavní HTML dokument pro webovou aplikaci e-shopu

    Tento soubor obsahuje základní HTML strukturu pro webovou aplikaci e-shopu.
    Využívá Bootstrap pro responzivní design a Font Awesome pro ikony.
    Zahrnuje navigační lištu, vyhledávací formulář, dynamický obsah na základě přihlášeného uživatele,
    a dynamické načítání výsledků vyhledávání produktů.

    Struktura:
    - Hlavička HTML dokumentu
    - Tělo HTML dokumentu obsahující navigační lištu a výsledky vyhledávání
    - Vložené styly pro zlepšení vzhledu komponent
    -->

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
          crossorigin="anonymous" />

    <title>My E-shop</title>
</head>

<body>
<!--
Navigační lišta pro webovou aplikaci e-shopu

Tato část HTML kódu obsahuje navigační lištu s odkazem na domovskou stránku,
vyhledávacím formulářem, odkazy na různé stránky (produkty, košík, přihlášení, registrace, odhlášení),
a dynamickým zobrazením stavu přihlášení uživatele.
-->

<nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
    <a class="navbar-brand" href="#">My E-shop</a>

    <form class="form-inline my-2 my-lg-0" action="/search" method="GET">
        <input class="form-control form-control-sm mr-sm-2 rounded-pill" type="search" placeholder="Search"
               aria-label="Search" name="q">
        <button class="btn btn-outline-success btn-sm rounded-pill" type="submit">Search</button>
    </form>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('views.home') }}">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('views.products') }}">Products</a>
            </li>
        </ul>

        {% if 'username' in session %}
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('views.cart') }}">Cart</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.account') }}">{{ session['username'] }}</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.logout') }}">Logout</a>
            </li>
        </ul>
        {% else %}
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.login') }}">Log in</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.register') }}">Sign-up</a>
            </li>
        </ul>
        {% endif %}
    </div>
</nav>

<!--
Hlavní obsah HTML dokumentu

Tato část obsahuje výpis výsledků vyhledávání produktů.
Pokud jsou nalezeny produkty, zobrazí se v kartách, kde každá karta obsahuje název produktu,
cenu a tlačítko pro přidání do košíku.
Pokud nejsou nalezeny žádné produkty, zobrazí se zpráva "No products found".
-->

<h1 class="text-center mb-5">Search Results for "{{ search_term.replace('%', '') }}"</h1>

{% if products %}
<div class="container">
    <div class="row justify-content-center">
        {% for product in products %}
        <div class="col-md-4 mb-4">
            <div class="card shadow-sm h-100">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ product.Name }}</h5>
                    <div class="mt-auto d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <form method="POST" action="/add_to_cart">
                                <input type="hidden" name="product_id" value="{{ product.ID }}">
                                <button type="submit" class="btn btn-sm btn-outline-secondary">Add to cart</button>
                            </form>
                        </div>
                        <small class="text-muted">{{ product.Price | format_price }} Kč</small>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% else %}
<p class="text-center">No products found.</p>
{% endif %}

<!--
Skripty pro zajištění funkčnosti Bootstrap komponent

Tato část obsahuje skripty pro zajištění správného fungování komponent Bootstrap,
včetně jQuery, Popper.js a samotného Bootstrap JS.
-->

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/E9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

<!--
Vložené styly pro vylepšení vzhledu komponent

Tato část obsahuje vložené CSS styly pro vylepšení vzhledu komponent,
včetně kategorií, seznamu položek a dalších prvků uživatelského rozhraní.
-->

<style>
    .category-list li {
        width: 10%;
        text-align: center;
    }

    .categories {
        margin-top: 20px;
    }

    .categories h2 {
        font-size: 24px;
        font-weight: bold;
    }

    .categories ul {
        list-style: none;
        padding-left: 0;
    }

    .categories li {
        border: 1px solid #ccc;
        border-radius: 4px;
        margin-bottom: 10px;
    }

    .categories li a {
        color: #333;
        display: block;
        padding: 10px;
    }

    .categories li a:hover {
        background-color: #eee;
    }

    .list-group-item {
        border-radius: 0;
        border-color: #ccc;
        border-width: 1px 0 0 0;
    }

    .list-group-item:last-child {
        border-bottom-width: 1px;
    }
</style>

</html>
