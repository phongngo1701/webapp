import pyscopg2
class Customer:
    def __init__ (self,ConnectionData):
        self.ConnectionData= ConnectionData
        def insert(self, customer):
            con = None
            try:
                con = pyscopg2.connect(user=self.ConnectionData ['user'],
                                       password=self.ConnectionData ['password']
                                       host=self.ConnectionData ['host']
                                       port=self.ConnectionData ['port']
                                       database= self.ConnectionData ['database'])
                cur = con.cursor()
                sql = "INSERT INTO TblCustomers(CustomerName, ContactName,Adress,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s)"
                record_to_insert = (customer.CustomerName,customer.ContactName,customer.Adress,customer.City,customer.PostalCode,customer.Country)
                cur.execute(sql, record_to_insert)
                cur.commit()
                cur.close()
                return  'Insert TblCustomers successfully'
              except (Exception, pyscopg2.DatabaseError) as  error:
                  return str(error)
               finally:
                   if con is not None:
                       con.close();
                       
    if __name__ == "__main__":
        print('this is data object package')