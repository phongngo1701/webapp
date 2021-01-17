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
    * Endpoint: /user/all
    * Params: None
    * Body: None
* Response: [Customer]
### Add a customer
* Request
    * Method: POST
    * Endpoint: /user/insert
    * Body:
        * CustomerName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /user/update/:customer_id
    * Body:
        * CustomerName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /user/delete/:customer_id
* Response: message