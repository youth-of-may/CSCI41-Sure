import trainapp._db as db

"""
TABLE
CREATE TABLE scheduledTrip (
    tripScheduleID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    routeID INT NOT NULL,
    trainID INT NOT NULL,
    tripDate DATE NOT NULL,
    departureTime TIME NOT NULL,
    arrivalTime TIME NOT NULL,
    actualDuration INT
    FOREIGN KEY (routeID) REFERENCES route(routeID),
    FOREIGN KEY (trainID) REFERENCES train(trainID)
);
CREATE TABLE route (
    routeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    originStationID INT NOT NULL,
    destinationStationID INT NOT NULL,
    baseCost INT NOT NULL,
    isLocalRoute BOOLEAN NOT NULL DEFAULT 1,
    estimatedDuration INT NOT NULL,  -- in minutes
    FOREIGN KEY (originStationID) REFERENCES station(stationID),
    FOREIGN KEY (destinationStationID) REFERENCES station(stationID),
    CHECK (originStationID != destinationStationID),
    UNIQUE (originStationID, destinationStationID)
);
CREATE TABLE station (
    stationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationName VARCHAR(50) NOT NULL UNIQUE,
    isLocalStation BOOLEAN NOT NULL DEFAULT 1
);

"""

#use this for the general trips page (containing the number of available trips sorted per date)
def list_trips_per_date():
    """
    Counts the number of trips per date 
    """
    sql ="SELECT tripDate, COUNT(tripScheduleID) AS tripNumber FROM scheduledTrip GROUP BY tripDate ORDER BY tripDate ASC;"
    return db.execute(sql, None)

def get_raw_date(trip_date=None):
    """
    Get raw date value
    """
    sql ="SELECT tripDate FROM scheduledTrip WHERE tripDate=%s LIMIT 1;"
    return db.execute(sql, [trip_date])

#use this for the date specific trips
def list_local_intertown(isLocal=True, trip_date=None):
    """
    Retrieve all local/intertown trips given a trip_date
    Returns train number, origin station, destination, departure time, arrival time, and the actual duration of the trip
    """
    sql = '''
    SELECT trip.trainID AS 'trainID', s1.stationName AS 'Origin', s2.stationName AS 'Destination', 
    trip.departureTime 'Departure', trip.arrivalTime 'Arrival', COALESCE(r.estimatedDuration,TIMESTAMPDIFF(MINUTE, trip.departureTime, trip.arrivalTime)) AS actualDuration, r.baseCost
    FROM route r 
    JOIN scheduledTrip trip
    ON trip.routeID = r.routeID
    JOIN station s1
    ON r.originStationID = s1.stationID
    JOIN station s2
    ON r.destinationStationID = s2.stationID
    WHERE trip.tripDate=%s AND 
    r.isLocalRoute=%s
    ORDER BY trip.trainID;
    '''
    return db.execute(sql,[trip_date, isLocal])