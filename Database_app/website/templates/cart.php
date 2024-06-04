<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
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
          <td>{{ product['Quantity'] }} </td>
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


</body>

</html>