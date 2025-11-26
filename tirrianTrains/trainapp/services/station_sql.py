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

def get_station_name(stationID=None):
    """Get a specific station name"""
    result = db.execute('SELECT stationName FROM station WHERE stationID=%s', [stationID])
    return result[0] if result else None

def create_station(stationName, isLocal):
    """
    Function used to create a new station
    """
    sql = '''
    INSERT INTO station(stationName, isLocalStation)
    VALUES (%s, %s);
    '''
    return db.execute_return_lastrowid(sql, [stationName, isLocal])