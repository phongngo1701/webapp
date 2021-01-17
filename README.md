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

## Employee
### Get all Employee
* Request:
    * Method: GET
    * Endpoint: /employee/all
    * Params: None
    * Body: None
* Response: [Employee]
### Add a Employee
* Request:
    * Method: POST
    * Endpoint: /employee/insert
    * Body:
       * LastName: string
       * FirstName: string
       * Birthdate: date
       * Photo: string
       * Notes: string
* Response: Message
### Update a Employee
* Request:
    * Method: PUT
    * Endpoint: /employee/:employee_id
    * Body:
       * LastName: string
       * FirstName: string
       * Birthdate: date
       * Photo: string
       * Notes: string
*Response: Message
### Delete a Employee
* Request:
    * Method: DELETE
    * Endpoint: /employee/:employee_id
* Response: message
## Supplier
### Get all supplier
* Request:
    * Method: GET
    * Endpoint: /supplier/all
    * Params: None
    * Body: None
* Response: [Supplier]
### Add a supplier
* Request:
    * Method: POST
    * Endpoint: /supplier/insert
    * Body:
        * SupplierName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
        * Phone: string
* Response: Message
### Update a supplier
* Request:
    * Method: PUT
    * Endpoint: /supplier/update/:supplier_id
    * Body:
        * SupplierName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
        * Phone: string
* Response: Message
### Delete a supplier
* Request:
    * Method: DELETE
    * Endpoint: /supplier/delete/:supplier_id
    * Response: message
## category
### Get all category
* Request:
    * Method: GET
    * Endpoint: /category/all
    * Params: None
    * Body: None Response: [category]
### Add a category
* Request:
    * Method: POST
    * Endpoint: category/insert
    * Body:
       * CategoryName: string
       * Description: string
       * Response: Message
### Update a category
* Request:
    * Method: PUT
    * Endpoint: /category/update/:category_id
    * Body:
       * CategoryName: string
       * Description: string
* Response: Message
### Delete a category
* Request:
    * Method: DELETE
    * Endpoint: /category/delete/:category_id
* Response: message
## order
### Get all order
* Request:
    * Method: GET
    * Endpoint: /order/all
    * Params: None
    * Body: None
* Response: [order]
### Add a order
* Request:
    * Method: POST
    * Endpoint: /order/insert
    * Body:
        * CustomerID: string
        * EmployeeID: string
        * OrderDate: date
        * ShipperID: string
* Response: Message
### Update a order
* Request:
    * Method: PUT
    * Endpoint: /order/update/:od_id
    * Body:
       * CustomerID: string
       * EmployeeID: string
       * OrderDate: date
       * ShipperID: string
* Response: Message
### Delete a order
* Request:
    * Method: DELETE
    * Endpoint: /order/delete/:od_id
    * Response: message
## orther detail
### Get all orther detail
* Request:
   * Method: GET
   * Endpoint: /order_detail/all
   * Params: None
   * Body: None
* Response: [order_detail]
### Add a orther detail
* Request:
    * Method: POST
    * Endpoint: /order_detail/insert
    * Body:
       * OrderID: string
       * ProductID: string
       * Quantity: string
* Response: Message
### Update a orther detail
* Request:
    * Method: PUT
    * Endpoint: /order_detail/update/:odd_id
    * Body:
        * OrderID: string
        * ProductID: string
        * Quantity: string
* Response: Message
### Delete a orther detail
* Request:
    * Method: DELETE
    * Endpoint: /order_detail/delete/:odd_id
* Response: message
## Product
### Get all Product
* Request:
    * Method: GET
    * Endpoint: /product/all
    * Params: None
    * Body: None
* Response: [Product]
### Add a Product
* Request:
   * Method: POST
   * Endpoint: /product/insert
   * Body:
      * ProductName: string
      * SupplierID: string
      * CategoryID: string
      * Unit: string
      * Price: string
* Response: Message
### Update a Product
* Request:
    * Method: PUT
    * Endpoint: /product/update/:product_id
    * Body:
       * ProductName: string
       * SupplierID: string
       * CategoryID: string
       * Unit: string
       * Price: string
* Response: Message
### Delete a Product
* Request:
    * Method: DELETE
    * Endpoint: /product/delete/:product_id
    * Response: message
## Shipper
### Get all Shipper
* Request:
    * Method: GET
    * Endpoint: /shipper/all
    * Params: None
    * Body: None
    * Response: [Shipper]
### Add a Shipper
* Request:
    * Method: POST
    * Endpoint: /shipper/insert
    * Body:
        * ShipperName: string
        * Phone: string
        * Response: Message
### Update a Shipper
* Request:
    * Method: PUT
    * Endpoint: /shipper/update/:shipper_id
    * Body:
       * ShipperName: string
       * Phone: string
       * Response: Message
### Delete a Shipper
* Request:
    * Method: DELETE
    * Endpoint: /shipper/delete/:shipper_id
* Response: message