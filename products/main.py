from flask import Flask, render_template, request, redirect, url_for
from db.db_manager import fetch_records, insert_record, update_record, delete_record

app = Flask(__name__)

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    table_name = 'products'  # يمكن تغييره لجدول آخر
    products = fetch_records(table_name)
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add():
    """إضافة سجل جديد"""
    table_name = 'products'
    data = {
        'name': request.form['name'],
        'price': request.form['price']
    }
    insert_record(table_name, data)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    """تحديث سجل موجود"""
    table_name = 'products'
    product_id = request.form['id']
    data = {
        'name': request.form['name'],
        'price': request.form['price']
    }
    update_record(table_name, data, f"id = {product_id}")
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    """حذف سجل"""
    table_name = 'products'
    product_id = request.form['id']
    delete_record(table_name, f"id = {product_id}")
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    """الصفحة الرئيسية"""
    if request.method == 'POST':
        # البحث بناءً على المدخلات
        search_query = request.form.get('search_query')
        if search_query:
            # البحث عن المنتجات التي تحتوي على النص المدخل
            products = fetch_records('products', f"name LIKE '%{search_query}%'")
        else:
            # استرجاع جميع المنتجات
            products = fetch_records('products')
    else:
        # استرجاع جميع المنتجات
        products = fetch_records('products')
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)