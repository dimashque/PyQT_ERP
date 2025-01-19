import pypyodbc as odbc
from PySide6.QtWidgets import QMessageBox



###def sqlSELECT(column, table):

   ## cursor.execute(f"SELECT {column} FROM TeAmoDB.dbo.{table} ;")
   ## data = cursor.fetchall()
   ## return data



def sqlLogin(username, table):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()
    cursor.execute(f"SELECT password FROM TeAmoDB.dbo.{table} WHERE username LIKE '{username}' ")
    for row in cursor:
        print(row)
        print(row[0])
        passSQL = row[0]



    return passSQL




def sqlChangePss(username, password,newPass, table):

    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    old_PassQuery = sqlLogin(username, table)


    try:
        if password == old_PassQuery:
            cursor.execute(
                f"UPDATE TeAmoDB.dbo.[{table}] SET password = '{newPass}'  WHERE username LIKE '{username}' ")
            cnxn.commit()
            cursor.close()
            cnxn.close()

            return True

        else:
            return False

    except Exception as e:
        return False
    # print(f"Error: {e}")


def sqlFillTableView():


    # Establishing a connection to the SQL Server
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    # SQL query to retrieve data
    sql_query = """
        SELECT 
            Orders.OrderNr, 
            Orders.statu, 
            Customer.Name, 
            Customer.Address, 
            Orders.Amount, 
            Products.ProductName, 
            Mandatory.Name, 
            OrderMandatory.Discount,
            Orders.movement,
            Orders.moveDate
        FROM 
            Orders
            INNER JOIN Customer ON Orders.customerNR = Customer.CustomerNR
            INNER JOIN OrderPosition ON Orders.OrderNr = OrderPosition.OrderNr
            INNER JOIN Products ON Products.ProductNr = OrderPosition.ProductNr
            INNER JOIN OrderMandatory ON OrderMandatory.OrderID = Orders.OrderNr
            INNER JOIN Mandatory ON Mandatory.MandatoryID = OrderMandatory.MandatoryID
    """

    # Executing the SQL query
    sqlQuery = cursor.execute(sql_query)
    return sqlQuery



def findMandatory(num):

    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT OrderMandatory.Rate,  OrderMandatory.Declaration, OrderMandatory.ShipKompensation, OrderMandatory.DeliveryDate
                 From OrderMandatory
                 WHERE OrderMandatory.OrderID = {num}"""


    Result = cursor.execute(sql_querry)

    return Result

def findCustomer(num):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT Customer.Phone, Customer.Address 
                 FROM Customer
                 WHERE CustomerNR = (SELECT Orders.customerNR FROM Orders WHERE Orders.OrderNr = {num} ) """

    Result = cursor.execute(sql_querry)

    return Result


def findOrder(num):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT Orders.Date, Orders.movement, Orders.moveDate, Orders.OfficeFees
                 FROM Orders
                WHERE Orders.OrderNr = {num}  """

    Result = cursor.execute(sql_querry)

    return Result

def findSponser(num):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT Sponser.Name FROM Sponser
                WHERE Sponser.SponserID = (SELECT SponserOrder.SponserID FROM SponserOrder WHERE SponserOrder.OrderID = {num} ) """

    Result = cursor.execute(sql_querry)

    return Result


def findSource(num):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT Source.Name FROM Source
                WHERE Source.SourceID = (SELECT SourceOrder.SourceID FROM SourceOrder WHERE SourceOrder.OrderID = {num} ) """

    Result = cursor.execute(sql_querry)

    return Result

def fillInputPrice(num):
    cnxn = odbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-C3L2I48\\SQLEXPRESS; DATABASE=TeAmoDB; Port=1433;')
    cursor = cnxn.cursor()

    sql_querry = f"""SELECT SUM(p.Price * op.quantity)
                 FROM Orders O
                 JOIN
                 OrderPosition op ON op.OrderNr = O.OrderNr
                 JOIN
                 Products p ON op.ProductNr = p.ProductNr
                 WHERE O.OrderNr = {num}  """

    Result = cursor.execute(sql_querry)

    return Result