<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
    crossorigin="anonymous" />

  <title></title>
</head>

<body>
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


<div class="container my-5">




  {% if category %}
    <h1 class="text-center mb-5">{{ category }}</h1>
{% endif %}

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
            <small class="text-muted">{{ product.Price }} Kč</small>
          </div>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

</body>

</html>