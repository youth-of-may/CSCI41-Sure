import trainapp._db as db

"""
ROUTE:
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

"""
def get_destination_routes(destID):
    """
    Retrieve all the routes leading to a destination station using destID
    """
    sql = """SELECT r.routeID, s1.stationName AS origin, s2.stationName AS destination, 
    IF(r.isLocalRoute = 1, 'Local', 'Intertown') AS routeType, estimatedDuration 
    FROM route r 
    JOIN station s1 
    ON s1.stationID = r.originStationID
    JOIN station s2 
    ON s2.stationID = r.destinationStationID
    WHERE r.destinationStationID=%s
    ;"""
    return db.execute(sql, [destID])
