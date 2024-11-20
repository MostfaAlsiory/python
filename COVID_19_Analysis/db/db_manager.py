from db.connection import get_db_connection

def fetch_records_with_conditions(country, start_date, end_date):
    """جلب بيانات COVID-19 بناءً على الدولة والفترة الزمنية"""
    sql = """
        SELECT date, location, total_cases, total_deaths 
        FROM `table 2` 
        WHERE location = %s AND date BETWEEN %s AND %s
        ORDER BY date ASC
    """
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (country, start_date, end_date))
            return cursor.fetchall()
    finally:
        connection.close()