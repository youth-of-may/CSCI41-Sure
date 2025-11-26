import trainapp._db as db

"""
Table:
CREATE TABLE customer (
    customerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    givenName VARCHAR(50) NOT NULL,
    middleInitial VARCHAR(1),
    birthDate DATE NOT NULL,
    gender VARCHAR(10)
);
CREATE TABLE ticket (
    ticketID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customerID INT NOT NULL,
    ticketDate DATE NOT NULL,
    totalCost INT NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);
"""

#execute a create function for the customer 
def create_customer(lastName, givenName, middleInitial, birthDate, gender):
    """
    Function used to create a new customer
    """
    sql = '''
    INSERT INTO customer(lastName, givenName, middleInitial, birthDate, gender)
    VALUES (%s, %s, %s, %s, %s);
    '''
    return db.execute_return_lastrowid(sql, [lastName, givenName, middleInitial, birthDate, gender])

def get_customer(customerID=1):
    """
    Retrieves a customer given a customerID
    Returns all columns of customer
    """
    result = db.execute("SELECT customerID, CONCAT(givenName, ' ', middleInitial, '. ', lastName) AS name, birthDate, gender FROM customer WHERE customerID=%s;", [customerID])
    return result[0]
def list_customers():
    """
    Retrieves the list of customers
    """
    return db.execute("SELECT customerID, CONCAT(givenName, ' ', middleInitial, '. ', lastName) AS name, birthDate, gender FROM customer ORDER BY customerID;", [])

def generate_travel_history(customerID=1):
    """
    Retrieves travel history of a customer given a customerID
    Returns only one valeu: total cost
    """
    sql = "SELECT ticketID, ticketDate, totalCost FROM ticket WHERE customerID = %s;"
    return db.execute(sql, [customerID])