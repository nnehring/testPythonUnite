from flask import Flask, jsonify
from OurClass.DBClass import DBClass
from OurClass.Customer import Customer

import json
import decimal
from flask_cors import CORS
# application = app
app = Flask(__name__)
db = DBClass("localhost", "natnz", "HelioUnitec*", "natnz_SaleDB")
#db = DBClass("localhost", "root", "", "testflask")
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/customers', methods=['GET'])
def getCustomers():
    result = db.selectQuery("customers")
    newresult =[]
    for row in result:
        newRow = []
        for item in row:
            if isinstance(item, decimal.Decimal):
                item = float(item)
            newRow.append(item)
        customer = Customer(newRow)

        newresult.append(customer.__dict__)
    return json.dumps(newresult)


@app.route('/customers/country', methods=['GET'])
def getCustomersCountry():
    result = db.countrySort("customers")
    newresult =[]
    for row in result:
        newRow= []
        for item in row:
            if isinstance(item, decimal.Decimal):
                item= float(item)
            newRow.append(item)
        customer = Customer(newRow)

        newresult.append(customer.__dict__)
    return json.dumps(newresult)
#     print(result)
#     # for x in result:
#     #     print(x)
#     return simplejson.dumps(result)

@app.route('/customers/country/<countryname>', methods=['GET'])
def getCustomersCountrybyName(countryname):
    result = db.countrySort("customers", countryname)
    newresult =[]
    for row in result:
        newRow= []
        for item in row:
            if isinstance(item, decimal.Decimal):
                item= float(item)
            newRow.append(item)
        customer = Customer(newRow)

        newresult.append(customer.__dict__)
    return json.dumps(newresult)

@app.route('/customers/countryList', methods=['GET'])
def listCountries():
    result = db.uniqueColumn("customers","country")
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)