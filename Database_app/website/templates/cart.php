<!DOCTYPE html>
<html>

<head>
    <!--
    Hlavní HTML dokument pro webovou aplikaci e-shopu

    Tento soubor obsahuje základní HTML strukturu pro webovou aplikaci e-shopu.
    Využívá Bootstrap pro responzivní design a Font Awesome pro ikony.
    Zahrnuje navigační lištu, vyhledávací formulář, dynamický obsah na základě přihlášeného uživatele,
    a výpis obsahu nákupního košíku.

    Struktura:
    - Hlavička HTML dokumentu
    - Tělo HTML dokumentu obsahující navigační lištu a obsah nákupního košíku
    -->

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
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
        <input class="form-control form-control-sm mr-sm-2 rounded-pill" type="search" placeholder="Search" aria-label="Search" name="q">
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

        <ul class="navbar-nav ml-auto">
            {% if 'username' in session %}
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('views.cart') }}">Cart</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.account') }}">{{ session['username'] }}</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.logout') }}">Logout</a>
            </li>
            {% else %}
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.login') }}">Log in</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('auth.register') }}">Sign-up</a>
            </li>
            {% endif %}
        </ul>
    </div>
</nav>

<!--
Hlavní obsah HTML dokumentu

Tato část obsahuje výpis obsahu nákupního košíku. Pokud jsou v košíku produkty,
zobrazí se v tabulce s následujícími sloupci: název produktu, cena, množství, a tlačítko pro odstranění.
Je zde také zobrazen celkový součet cen všech produktů v košíku a tlačítko pro dokončení nákupu.
-->

<div class="container mt-4 border rounded">
    <h1 class="text-center mb-4">Shopping Cart</h1>
    {% if products %}
    <div class="table-responsive">
        <table class="table table-striped">
            <thead class="thead-dark">
            <tr>
                <th scope="col">Product Name</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
                <th scope="col"></th>
            </tr>
            </thead>
            <tbody>
            {% for product in products %}
            <tr>
                <td>{{ product['Name'] }}</td>
                <td>{{ product['Price'] }} Kč</td>
                <td>{{ product['Quantity'] }}</td>
                <td>
                    <form action="/cart/remove/{{ product.ID|int }}" method="POST">
                        <button type="submit" class="btn btn-outline-danger btn-sm">Remove</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan="3" class="text-right font-weight-bold">Total Price:</td>
                <td>{{ total_price }} Kč</td>
            </tr>
            </tbody>
        </table>
    </div>
    <form action="{{ url_for('views.buy') }}" method="POST">
        <button type="submit" class="btn btn-primary btn-lg">Buy Now</button>
    </form>
    {% else %}
    <div class="alert alert-info text-center" role="alert">
        Your cart is empty.
    </div>
    {% endif %}
</div>

<!--
Skripty pro zajištění funkčnosti Bootstrap komponent

Tato část obsahuje skripty pro zajištění správného fungování komponent Bootstrap,
včetně jQuery, Popper.js a samotného Bootstrap JS.
-->

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkKrr/E9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>
