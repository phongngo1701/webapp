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
## categories
* CategoryID: int
* CategoryName:string
* Description:string
## shippers 
    ShipperID:int
    ShipperName :string
    Phone:string

## suppliers 
    SupplierID:int
    SupplierName:string
    ContactName:string
    Address:string
    City:string
    PostalCode:string
    Country :string
    Phone :string


## employees 
    EmployeeID:int
    LastName:string
    FirstName:string
    Birthdate:string
    Photo:string
    Notes:string

## products 
    ProductID:int
    ProductName:string
    Unit:string
    Price :string
    SupplierID :int
    CategoryID: int
);

## orders (
    OrderID :int
    CustomerID: int
    EmployeeID: int,
    OrderDate:string
    ShipperID :int


## orderdetails 
    OrderDetailID :int
    OrderID :int
    ProductID: int
    Quantity :string
);
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