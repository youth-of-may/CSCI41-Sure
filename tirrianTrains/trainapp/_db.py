from django.db import connection

#thsi file contains helper functions making use of cursor, allowing us to execute sql queries

def dictfetchall(cursor):
    """Convert cursor results to list of dictionaries"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def execute(sql, params=None):
    """Execute SQL and return results as dictionaries"""
    with connection.cursor() as cur:
        cur.execute(sql, params or [])
        try:
            return dictfetchall(cur)
        except Exception:
            return None

def executemany(sql, param_list):
    """Execute SQL with multiple parameter sets"""
    with connection.cursor() as cur:
        cur.executemany(sql, param_list)

def execute_return_lastrowid(sql, params=None):
    """Execute SQL and return the last inserted row ID"""
    with connection.cursor() as cur:
        cur.execute(sql, params or [])
        return cur.lastrowid