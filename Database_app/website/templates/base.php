<!DOCTYPE html>
<html>

<head>
    <!--
    Hlavní HTML dokument pro webovou aplikaci e-shopu

    Tento soubor obsahuje základní HTML strukturu pro webovou aplikaci e-shopu.
    Využívá Bootstrap pro responzivní design a Font Awesome pro ikony.
    Zahrnuje navigační lištu, vyhledávací formulář, dynamický obsah na základě přihlášeného uživatele,
    a výpis kategorií a produktů.

    Struktura:
    - Hlavička HTML dokumentu
    - Tělo HTML dokumentu obsahující navigační lištu, kategorie, filtry a výpis produktů
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

    <style>
        .category-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            padding: 0;
        }

        .category-list li {
            flex: 1 1 calc(20% - 10px);
            margin: 5px;
            text-align: center;
        }

        .categories {
            margin-top: 20px;
        }

        .categories h2 {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        }

        .categories ul {
            list-style: none;
            padding-left: 0;
        }

        .categories li {
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
            transition: transform 0.2s;
        }

        .categories li a {
            color: #333;
            display: block;
            padding: 10px;
            text-decoration: none;
        }

        .categories li a:hover {
            background-color: #eee;
        }

        .categories li:hover {
            transform: scale(1.05);
        }

        .list-group-item {
            border-radius: 0;
            border-color: #ccc;
            border-width: 1px 0 0 0;
        }

        .list-group-item:last-child {
            border-bottom-width: 1px;
        }

        /* Improved styling for the filter form */
        .filter-container {
            width: 100%;
            border: none; /* Removing border */
        }

        .filter-container form {
            width: 100%;
        }

        .filter-container form .form-group {
            width: 100%;
            margin-bottom: 15px;
        }

        .filter-container form .form-group label {
            width: 100%;
            font-weight: bold;
        }

        .filter-container form .form-group input,
        .filter-container form .form-group select {
            width: 100%;
        }

        .filter-container form .btn {
            width: 100%;
        }

        @media (max-width: 1200px) {
            .category-list li {
                flex: 1 1 calc(25% - 10px);
            }
        }

        @media (max-width: 992px) {
            .category-list li {
                flex: 1 1 calc(33.33% - 10px);
            }

            .categories h2 {
                font-size: 22px;
            }
        }

        @media (max-width: 768px) {
            .category-list li {
                flex: 1 1 calc(50% - 10px);
            }

            .categories h2 {
                font-size: 20px;
            }
        }

        @media (max-width: 576px) {
            .category-list li {
                flex: 1 1 100%;
            }

            .categories h2 {
                font-size: 18px;
            }

            .categories li a {
                padding: 15px;
            }

            .filter-container {
                padding: 10px;
            }

            .filter-container form .btn {
                margin-top: 10px;
            }
        }

        /* Styling for footer */
        footer {
            background-color: #f8f9fa;
            text-align: center;
            padding: 10px 0;
            margin-top: 20px;
        }
    </style>
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

Tato část obsahuje výpis kategorií produktů a formulář pro filtrování produktů podle ceny a řazení podle ceny.
Produkty se zobrazují v mřížce s tlačítkem pro přidání do košíku.
-->

<div class="container">
    <div class="row">
        <div class="col">
            <div class="categories">
                <h2 class="text-center mt-5 mb-3">Choose Category</h2>
                <ul class="category-list container d-flex justify-content-center">
                    {% for type in types %}
                    <li class="d-inline-block mr-3 list-item">
                        <a href="{{ url_for('views.products_by_type', type=type) }}">{{ type }}</a>
                    </li>
                    {% endfor %}
                </ul>

                <h2 class="text-center">Filter Products</h2>
                <div class="filter-container container d-flex justify-content-center mb-5 mt-2">
                    <button class="btn btn-primary mb-2" type="button" id="toggleFilterButton" data-toggle="collapse" data-target="#filterForm" aria-expanded="false" aria-controls="filterForm">
                        Toggle Filter
                    </button>
                    <div class="collapse" id="filterForm">
                        <form method="POST" action="{{ request.url }}" class="form-inline mt-3">
                            <div class="form-group mr-3 mb-2">
                                <label for="min-price" class="mr-2">Min Price:</label>
                                <input type="number" class="form-control" id="min-price" name="min-price" placeholder="Enter minimum price">
                            </div>
                            <div class="form-group mr-3 mb-2">
                                <label for="max-price" class="mr-2">Max Price:</label>
                                <input type="number" class="form-control" id="max-price" name="max-price" placeholder="Enter maximum price">
                            </div>
                            <div class="form-group mr-3 mb-2">
                                <label for="price" class="mr-2">Sort by price:</label>
                                <select class="form-control" id="price" name="price">
                                    <option value="asc">Lowest</option>
                                    <option value="desc">Highest</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary mb-2">Filter</button>
                        </form>
                    </div>
                </div>

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
                                    <small class="text-muted">{{ "{:,.2f}".format(product.Price).replace(",", " ").replace(".00", "") }} Kč</small>
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>

<!--
Skripty pro zajištění funkčnosti Bootstrap komponent

Tato část obsahuje skripty pro zajištění správného fungování komponent Bootstrap,
včetně jQuery, Popper.js a samotného Bootstrap JS.
-->

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
<script>
    document.getElementById('toggleFilterButton').addEventListener('click', function() {
        this.style.display = 'none';
    });
</script>

<!-- Zápatí -->
<footer>
    ©Patrick Dyntr, C3b 2024
</footer>

</body>

</html>
