import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',  # ضع كلمة المرور هنا
        database='abdul_rzag',
        cursorclass=pymysql.cursors.DictCursor
    )