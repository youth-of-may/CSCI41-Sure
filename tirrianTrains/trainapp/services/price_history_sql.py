import trainapp._db as db
from django.utils import timezone

# Unsure if I'll use this
def full_price_history():
    """
    Shows the all instances of price changes
    """
    
    sql = ''' SELECT * FROM routePriceHistory ORDER BY effectiveFrom;'''
    
    return db.execute(sql)

def generate_price_history(routeID=1):
    """
    Get price history from a specific route
    """
    
    sql = '''SELECT * FROM routePriceHistory WHERE routeID = %s ORDER BY effectiveFrom;'''
    
    return db.execute(sql, [routeID])

def add_initial_price(routeID, price):
    """
    Add the starting price of a route to the records
    """
    
    sql = '''
    INSERT INTO routePriceHistory (routeID, price, effectiveFrom)
    VALUES (%s, %s, %s);
    '''
    
    params = [routeID, price, timezone.now()]
    return db.execute(sql, params)

def update_route_price(routeID, newPrice):
    """
    Close the previous price record and insert a new one
    """
    now = timezone.now().date()

    # Close previous record
    close_sql = '''
        UPDATE routePriceHistory
        SET effectiveTo = %s
        WHERE routeID = %s AND effectiveTo IS NULL;
    '''
    db.execute(close_sql, [now, routeID])

    # Insert new price
    insert_sql = '''
        INSERT INTO routePriceHistory (routeID, price, effectiveFrom)
        VALUES (%s, %s, %s);
    '''
    db.execute(insert_sql, [routeID, newPrice, now])

    return "Price changed"