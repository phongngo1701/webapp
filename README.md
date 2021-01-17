# webapp

# Lê Mai Tú
# Ngô Quốc Phong
# Nguyễn Huy Hoàng


# Entity
## Customer
* CustomerID: int
* CustomerName: string
* ContactName: string
* Address: string
* City: string
* PostalCode: string
* Country: string


# API
## Customer
### Get all customer
* Request
    * Method: GET
    * Endpoint: /customer/all
    * Params: None
    * Body: None
* Response: [Customer]
### Add a customer
* Request
    * Method: POST
    * Endpoint: /customer
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /customer/:customer_id
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /customer/:customer_id
* Response: message