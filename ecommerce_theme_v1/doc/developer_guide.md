# Developer Guide

## Getting Started

To get started with the development of the `ecommerce_theme_v1`, you need to have Odoo v16 Community Edition installed on your system. You can download it from the official Odoo website.

## Directory Structure

The directory structure of the `ecommerce_theme_v1` is as follows:

```
ecommerce_theme_v1/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── user.py
│   ├── review.py
│   └── cart.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── views/
│   ├── __init__.py
│   ├── product_template.xml
│   ├── user_template.xml
│   ├── review_template.xml
│   ├── cart_template.xml
│   ├── checkout_template.xml
│   └── search_template.xml
├── static/
│   ├── src/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   ├── img/
│   │   └── fonts/
├── data/
│   ├── product_data.xml
│   ├── user_data.xml
│   ├── review_data.xml
│   └── cart_data.xml
├── i18n/
│   └── en.po
└── doc/
    ├── user_guide.md
    ├── developer_guide.md
    └── api_documentation.md
```

## Models

The `models` directory contains the data schemas for `product`, `user`, `review`, and `cart`. Each model has its own Python file.

## Controllers

The `controllers` directory contains the `main.py` file which handles the business logic of the application.

## Views

The `views` directory contains the XML templates for the different parts of the website.

## Static

The `static` directory contains the CSS, JavaScript, images, and fonts used in the website.

## Data

The `data` directory contains the XML data files for `product`, `user`, `review`, and `cart`.

## i18n

The `i18n` directory contains the translation files for the website.

## Documentation

The `doc` directory contains the user guide, developer guide, and API documentation.

## Running the Application

To run the application, navigate to the root directory of the project and execute the following command:

```
odoo -c /etc/odoo.conf -d mydatabase --dev=all --addons-path=addons/,../custom_addons/ecommerce_theme_v1/
```

Replace `/etc/odoo.conf` with the path to your Odoo configuration file and `mydatabase` with the name of your database.

## Contributing

To contribute to the development of the `ecommerce_theme_v1`, please follow the Odoo 16 CE code pattern and file structure. Make sure to test your code thoroughly before submitting a pull request.