import trainapp._db as db

# list all the stations; includes a logic to determine if stations belong to local or intertown routes 

"""
CREATE TABLE station (
    stationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationName VARCHAR(50) NOT NULL UNIQUE,
    isLocalStation BOOLEAN NOT NULL DEFAULT 1
);

"""

def list_stations(local_only=None):
    """
    Retrieve all stations. Can be calibrated to get stations part of local/intertown routes.
    """
    if local_only is None:
        return db.execute('SELECT * FROM station ORDER BY stationID;')
    return db.execute('SELECT * FROM station WHERE isLocalStation=%s', [1 if local_only else 0])