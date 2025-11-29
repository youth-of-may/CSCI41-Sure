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
    Retrieve all stations. Can be filtered to get stations part of local/intertown routes.
    """
    if local_only is None:
        # Return all stations
        return db.dictfetchall("""
            SELECT stationID, stationName 
            FROM station 
            ORDER BY stationID
        """)
    
    # Return stations serving specific route type (with DISTINCT to avoid duplicates)
    sql = """
        SELECT DISTINCT s.stationID, s.stationName
        FROM station s
        JOIN route r ON s.stationID IN (r.originStationID, r.destinationStationID)
        WHERE r.isLocalRoute = %s
        ORDER BY s.stationID
    """
    return db.execute(sql, [1 if local_only else 0])
   


def get_station_name(stationID=None):
    """Get a specific station name"""
    result = db.execute('SELECT stationName FROM station WHERE stationID=%s', [stationID])
    return result[0] if result else None

def create_station(stationName):
    """
    Function used to create a new station
    """
    sql = '''
    INSERT INTO station(stationName)
    VALUES (%s);
    '''
    return db.execute_return_lastrowid(sql, [stationName])