from db.connection import get_db_connection

def insert_record(table, data):
    """إضافة سجل إلى الجدول المحدد"""
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    values = tuple(data.values())

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            connection.commit()
    finally:
        connection.close()

def update_record(table, data, where_clause):
    """تحديث سجل في الجدول المحدد"""
    set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    values = tuple(data.values())

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            connection.commit()
    finally:
        connection.close()

def delete_record(table, where_clause):
    """حذف سجل من الجدول المحدد"""
    sql = f"DELETE FROM {table} WHERE {where_clause}"

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

def fetch_records(table, where_clause=None):
    """استرجاع سجلات من الجدول المحدد"""
    sql = f"SELECT * FROM {table}"
    if where_clause:
        sql += f" WHERE {where_clause}"

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

def search_records(table, where_clause=None):
    
    """
    البحث عن سجلات في جدول معين بناءً على شروط محددة.
    :param table: اسم الجدول.
    :param where_clause: جملة شرطية لتحديد النتائج (اختياري).
    :return: قائمة من السجلات.
    """
    sql = f"SELECT * FROM {table}"
    if where_clause:
        sql += f" WHERE {where_clause}"

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
        return results
    finally:
        connection.close()