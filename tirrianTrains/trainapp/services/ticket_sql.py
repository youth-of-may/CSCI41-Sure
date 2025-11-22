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
    sql = """SELECT * ticket.ticketID, CONCAT(c.givenName, ' ', COALESCE(CONCAT(c.middleInitial, '. '), ''), ' ', c.lastName) AS Customer, ticket.totalCost 
    FROM ticket
    JOIN customer c 
    ON ticket.customerID = c.customerID
    WHERE ticket.ticketDate = %s
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
        COALESCE(st.actualDuration, r.estimatedDuration) AS duration,
        tt.tripCost AS cost
    FROM ticketTrip tt
    JOIN scheduledTrip st ON tt.tripScheduleID = st.tripScheduleID
    JOIN route r ON st.routeID = r.routeID
    JOIN station origin ON r.originStationID = origin.stationID
    JOIN station dest ON r.destinationStationID = dest.stationID
    JOIN train tr ON st.trainID = tr.trainID
    WHERE tt.ticketID = %s
    ORDER BY st.tripDate, st.departureTime;
    """
    return db.execute(sql, [ticket_id])