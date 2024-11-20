import pymysql
def get_db_connection():
    """الاتصال بقاعدة البيانات"""
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',  # ضع كلمة المرور إذا لزم الأمر
        database='mydatabase',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8'
    )