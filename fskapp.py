from flask import Flask, request, jsonify
import sqlite3
from pymongo import MongoClient


app = Flask(__name__)

@app.route('/companies', methods = ['GET'])
def read_companies():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM companies LIMIT 20')
    companies = []
    for com in cursor.fetchall():
        kompanii = {
            'id': com[0],
            'name': com[1],
            'country iso': com[2],
            'city': com[3],
            'nace': com[4],
            'website': com[5]
        }
        companies.append(kompanii)
    connection.close()

    return jsonify({'companies': companies})


@app.route('/cleanedCompanies', methods = ['POST'])
def add_data():
    connection = MongoClient('mongodb://localhost:27017')
    mydb = connection['mydata']
    mycollection = mydb['cleanedData']
    data = request.get_json()
    mycollection.insert_one(data)
    return 'Data added'


if __name__ == "__main__":
     app.run(debug=True)

