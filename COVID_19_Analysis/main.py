from flask import Flask, render_template, request
from db.connection import get_db_connection
from db.db_manager import fetch_records_with_conditions
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    analytics = {}
    records = []
    chart_path = None

    if request.method == 'POST':
        # قراءة المدخلات من المستخدم
        country = request.form.get('country')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        if country and start_date and end_date:
            # جلب البيانات من قاعدة البيانات
            records = fetch_records_with_conditions(country, start_date, end_date)
            
            # إجراء التحليلات
            analytics = calculate_analytics(records)
            
            # إنشاء الرسم البياني
            chart_path = create_charts(records, country, start_date, end_date)
            
    return render_template('index.html', records=records, analytics=analytics, chart_path=chart_path)

def calculate_analytics(data):
    """تحليل بيانات COVID-19"""
    if not data:
        return {}

    total_cases = sum(row['total_cases'] for row in data)
    total_deaths = sum(row['total_deaths'] for row in data)
    cfr = (total_deaths / total_cases * 100) if total_cases > 0 else 0

    max_cases_day = max(data, key=lambda x: x['total_cases'])
    max_deaths_day = max(data, key=lambda x: x['total_deaths'])

    return {
        'total_cases': total_cases,
        'total_deaths': total_deaths,
        'cfr': round(cfr, 2),
        'max_cases_day': {
            'date': max_cases_day['date'],
            'cases': max_cases_day['total_cases']
        },
        'max_deaths_day': {
            'date': max_deaths_day['date'],
            'deaths': max_deaths_day['total_deaths']
        }
    }

def create_charts(data, country, start_date, end_date):
    """إنشاء الرسومات البيانية"""
    dates = [row['date'] for row in data]
    cases = [row['total_cases'] for row in data]
    deaths = [row['total_deaths'] for row in data]

    plt.figure(figsize=(5, 3))
    plt.plot(dates, cases, label='Total Cases', marker='o')
    plt.plot(dates, deaths, label='Total Deaths', marker='x', color='red')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title(f'COVID-19 Trend in {country} ({start_date} to {end_date})')
    plt.legend()
    plt.xticks(rotation=45)
  
    # حفظ الرسم البياني
  
    plt.tight_layout()
    plt.savefig('static/plot.png')
    plt.close()
    return 'static/plot.png'
if __name__ == '__main__':
    app.run(debug=True)