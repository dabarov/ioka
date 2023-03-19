# ioka Python Library

## Table of Contents

- [Authentication](#authentication)
- [Core Resources](#core-resources)
    * [Orders](#orders)
        + [List all orders](#list-all-orders)
        + [Retrieve an order](#retrieve-an-order)
        + [Create an order](#create-an-order)
        + [Capture an order](#capture-an-order)
        + [Cancel an order](#cancel-an-order)
        + [List the order's events](#list-the-order-s-events)
        + [List order's refunds](#list-order-s-refunds)
    * [Payments](#payments)
        + [Retrieve a payment related to an order](#retrieve-a-payment-related-to-an-order)
        + [Create payment card for an order](#create-payment-card-for-an-order)
    * [Customers](#customers)
        + [List all customers](#list-all-customers)
        + [Retrieve a customer](#retrieve-a-customer)
        + [List customer's events](#list-customer-s-events)
        + [Create a customer](#create-a-customer)
        + [Delete a customer](#delete-a-customer)
        + [List order's refunds](#list-order-s-refunds-1)

## Authentication

The ioka API uses API keys to authenticate requests.

```python
import ioka_python

ioka_python.api_key = "YOUR_API_KEY"
```

## Core Resources

### Orders

#### List all orders

Returns a list of your orders. The list of available query parameters can be
found [here](https://ioka.kz/docs_v2.html#tag/orders/operation/GetOrders).
These parameters can be passed into `list()` function as keyword arguments.

```python
import ioka_python

ioka_python.api_key = "Hello"

orders = ioka_python.Order().list(limit=2)

print(orders[0].id)
```

#### Retrieve an order

Retrieves an Order object. The list of returned fields are available [here](https://ioka.kz/docs_v2.html#tag/orders/operation/GetOrderByID).

```python
import ioka_python

ioka_python.api_key = "Hello"

order = ioka_python.Order().retrieve("order_123")

print(order.amount)
```

#### Create an order

#### Capture an order

#### Cancel an order

#### List order's events

#### List order's refunds

### Payments

#### Retrieve a payment related to an order

#### Create payment card for an order

### Customers

#### List all customers

#### Retrieve a customer

#### List customer's events

#### Create a customer

#### Delete a customer

#### List order's refunds

