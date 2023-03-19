## Authentication
The ioka API uses API keys to authenticate requests.

```python
import ioka_python

ioka_python.api_key = "YOUR_API_KEY"
```

## Core Resources

### Orders

#### List all orders

Returns a list of your orders. The list of available query parameters can be found [here](https://ioka.kz/docs_v2.html#tag/orders/operation/GetOrders).
These parameters can be passed into `list()` function as keyword arguments.

```python
import ioka_python

ioka_python.api_key = "Hello"

orders = ioka_python.Order().list(limit=2)

print(orders)
```

### Payments

### Customers

### Dashboards
