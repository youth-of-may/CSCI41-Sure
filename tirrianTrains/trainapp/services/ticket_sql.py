import trainapp._db as db

"""
CREATE TABLE ticket (
    ticketID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customerID INT NOT NULL,
    ticketDate DATE NOT NULL,
    totalCost INT NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);

CREATE TABLE ticketTrip (
    ticketID INT NOT NULL,
    tripScheduleID INT NOT NULL,
    tripCost INT NOT NULL,
    PRIMARY KEY (ticketID, tripScheduleID),
    FOREIGN KEY (ticketID) REFERENCES ticket(ticketID),
    FOREIGN KEY (tripScheduleID) REFERENCES scheduledTrip(tripScheduleID)
);
CREATE TABLE customer (
    customerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    givenName VARCHAR(50) NOT NULL,
    middleInitial VARCHAR(1),
    birthDate DATE NOT NULL,
    gender VARCHAR(10)
);

"""
def total_sales_given_date(ticket_date=None):
    """
    Retrieves total sales for a given date
    Returns only one value: total cost
    """
    return db.execute('SELECT SUM(totalCost) AS total_cost FROM ticket WHERE ticketDate=%s', [ticket_date])

def list_sales_per_date(ticket_date=None):
    """
    Retrieves sales given a date
    Returns: ticket #, Customer Name, Total Cost
    """
    sql = """SELECT ticket.ticketID, CONCAT(c.givenName, ' ', COALESCE(CONCAT(c.middleInitial, '. '), ''), ' ', c.lastName) AS Customer, SUM(tp.tripCost) AS totalCost
    FROM ticket
    JOIN customer c 
    ON ticket.customerID = c.customerID
    JOIN tickettrip tp
    ON tp.ticketID = ticket.ticketID
    WHERE ticket.ticketDate = %s
    GROUP BY ticket.ticketID, Customer
    ;"""
    return db.execute(sql, [ticket_date])

def ticketDetails(ticket_id=None):
    """
    Retrieves trip itinerary
    Returns: Train #, Origin, Destination, Departure, Arrival, Duration, Cost
    """
    sql = """
    SELECT 
        tr.trainID AS train_number,
        origin.stationName AS origin,
        dest.stationName AS destination,
        st.departureTime AS departure,
        st.arrivalTime AS arrival,
        COALESCE(r.estimatedDuration,TIMESTAMPDIFF(MINUTE, st.departureTime, st.arrivalTime)) AS duration,
        tt.tripCost AS cost,
        t.ticketDate AS date,
        (SELECT SUM(tripCost) FROM ticketTrip WHERE ticketID = t.ticketID) AS totalCost
    FROM ticketTrip tt
    JOIN scheduledTrip st ON tt.tripScheduleID = st.tripScheduleID
    JOIN ticket t ON t.ticketID = tt.ticketID
    JOIN route r ON st.routeID = r.routeID
    JOIN station origin ON r.originStationID = origin.stationID
    JOIN station dest ON r.destinationStationID = dest.stationID
    JOIN train tr ON st.trainID = tr.trainID
    WHERE tt.ticketID = %s
    ORDER BY st.tripDate, st.departureTime;
    """
    return db.execute(sql, [ticket_id])

def list_ticket_dates():
    """
    Generates all the dates with tickets
    Used in admin dashboard
    """
    
    sql = "SELECT DISTINCT ticketDate FROM ticket ORDER BY ticketDate;"
    return db.execute(sql)


def ticketCustDetails(ticket_id=None):
    """
    Generate customer details associated to a ticket
    """
    sql = """SELECT c.customerID, c.lastName, c.givenName, 
    c.middleInitial, c.birthDate, c.gender
    FROM customer c 
    JOIN ticket t
    ON c.customerID = t.customerID
    WHERE t.ticketID = %s;
    """
    results = db.execute(sql, [ticket_id])
    return results[0]

def db_create_ticket(customerID, ticketDate, totalCost):
    sql = """
        INSERT INTO ticket (customerID, ticketDate, totalCost)
        VALUES (%s, %s, %s)
    """

    return db.execute_return_lastrowid(sql, [customerID, ticketDate, totalCost])

def create_ticket_trip(ticketID, tripID, tripCost):
    sql = """
        INSERT INTO ticketTrip (ticketID, tripScheduleID, tripCost)
        VALUES (%s, %s, %s)
    """
    return db.execute(sql, [ticketID, tripID, tripCost])