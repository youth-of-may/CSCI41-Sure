import trainapp._db as db

"""
table schema guide:

CREATE TABLE station (
    stationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationName VARCHAR(50) NOT NULL UNIQUE,
    isLocalStation BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE route (
    routeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    originStationID INT NOT NULL,
    destinationStationID INT NOT NULL,
    baseCost INT NOT NULL,
    isLocalRoute BOOLEAN NOT NULL DEFAULT 1,
    estimatedDuration INT NOT NULL,
    FOREIGN KEY (originStationID) REFERENCES station(stationID),
    FOREIGN KEY (destinationStationID) REFERENCES station(stationID),
    CHECK (originStationID != destinationStationID),
    UNIQUE (originStationID, destinationStationID)
);

CREATE TABLE scheduledTrip (
    tripScheduleID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    routeID INT NOT NULL,
    trainID INT NOT NULL,
    tripDate DATE NOT NULL,
    departureTime TIME NOT NULL,
    arrivalTime TIME NOT NULL,
    actualDuration INT,
    FOREIGN KEY (routeID) REFERENCES route(routeID),
    FOREIGN KEY (trainID) REFERENCES train(trainID)
);
"""

def list_local_trips():
    """
    Returns all local_trips in the database
    """
    
    sql = '''
    SELECT 
        s.tripDate, so.stationName AS originStation, sd.stationName AS destinationStation,
        s.departureTime, s.arrivalTime, r.baseCost FROM scheduledTrip AS s
    JOIN route AS r 
        ON s.routeID = r.routeID
    JOIN station AS so 
        ON r.originStationID = so.stationID
    JOIN station AS sd 
        ON r.destinationStationID = sd.stationID
    WHERE 
        so.isLocalStation = 1
        AND sd.isLocalStation = 1
    ORDER BY s.tripDate;
    '''
    
    return db.execute(sql)

def list_intertown_trips():
    """
    Returns all inter-town trips in the database
    (i.e., at least one station is not a local station)
    """
    sql = '''
    SELECT 
        s.tripDate, so.stationName AS originStation, sd.stationName AS destinationStation,
        s.departureTime, s.arrivalTime, r.baseCost
    FROM scheduledTrip AS s
    JOIN route AS r 
        ON s.routeID = r.routeID
    JOIN station AS so 
        ON r.originStationID = so.stationID
    JOIN station AS sd 
        ON r.destinationStationID = sd.stationID
    WHERE 
        so.isLocalStation = 0
        OR sd.isLocalStation = 0
    ORDER BY s.tripDate;
    '''

    return db.execute(sql)