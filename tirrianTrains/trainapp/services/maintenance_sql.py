import trainapp._db as db

"""
CREATE TABLE train (
    trainID INT NOT NULL PRIMARY KEY,
    model VARCHAR(20) NOT NULL, 
    seriesType ENUM('S-Series', 'A-Series') NOT NULL DEFAULT 'S-Series',
    maxSpeed INT NOT NULL,
    numSeats INT NOT NULL,
    numToilets INT NOT NULL,
    recliningSeats BOOLEAN NOT NULL DEFAULT 1,
    foldingTables BOOLEAN NOT NULL DEFAULT 1,
    disabilityAccess BOOLEAN NOT NULL DEFAULT 1,
    luggageStorage BOOLEAN NOT NULL DEFAULT 0,
    vendingMachine BOOLEAN NOT NULL DEFAULT 0,
    foodService BOOLEAN NOT NULL DEFAULT 0,
    CHECK (model REGEXP '^[sSaA]-[0-9]+$')
);
MAINTENANCE
CREATE TABLE maintenance (
    maintenanceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    trainID INT NOT NULL,
    maintenanceDate DATE NOT NULL,
    crewInCharge VARCHAR(50),
    tasks VARCHAR(255),
    condition ENUM('Excellent', 'Very Good', 'Satisfactory', 'Poor') NOT NULL,
    FOREIGN KEY (trainID) REFERENCES train(trainID),
);
"""
def list_trains():
    """
    Retrieves all trains
    Returns trainID, model, and seriesType
    """
    sql = """
    SELECT trainID, model, seriesType FROM train 
    ORDER BY trainID ASC;
    """
    return db.execute(sql, [])

#this is the logic for the train maintenance history view
def get_train_details(train_id = None):
    """
    Retrieves train details given train_id
    Returns all columns of train
    """
    sql = """
    SELECT * FROM train 
    WHERE trainID = %s;
    """
    return db.execute(sql, [train_id])

def get_train_maintenance(train_id = None, ):
    """
    Retrieves maintenance history of a train given its id
    """
    sql = """
    SELECT maintenanceID, maintenanceDate, crewInCharge, tasks, 'condition' FROM maintenance
    WHERE trainID = %s;
    """
    return db.execute(sql, [train_id])
"""
maintenanceDate DATE NOT NULL,
    crewInCharge VARCHAR(50),
    tasks VARCHAR(255),
    condition ENUM('Excellent', 'Very Good', 'Satisfactory', 'Poor') NOT NULL,"""
def add_maintenance(trainID, maintenanceDate, crew, task, condition):
    """
    Function used to create a new maintenance task
    """
    sql = '''
    INSERT INTO maintenance(trainID, maintenanceDate, crewInCharge, tasks, train_condition)
    VALUES (%s, %s, %s, %s, %s);
    '''
    return db.execute_return_lastrowid(sql, [trainID, maintenanceDate, crew, task, condition])
