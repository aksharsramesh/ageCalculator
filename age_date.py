from flask import Flask, request
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask_cors import CORS, cross_origin
from flask import jsonify
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
@cross_origin()
def login():
    birth = request.args.get('yyyy-mm-dd',type = str)
    print(birth)
    print(datetime.strptime(birth, "%Y-%m-%d").date())
    birthDate = datetime.strptime(birth, "%Y-%m-%d").date()
    #month = request.args.get('month',type = int)
    #date = request.args.get('date',type = int)
    #print (birth, month, date) 
    #print(datetime.date.today())
    print(datetime.date(datetime.now()))
    current = datetime.date(datetime.now())
    age = current - birthDate
    print(age)
    rdelta = relativedelta(current, birthDate)
    print ('Age in years - ', rdelta.years)
    print ('Age in months - ', rdelta.months)
    print ('Age in days - ', rdelta.days )
    result =  "you are " + str(rdelta.years) + " years "+ str(rdelta.months) + " months "+ str(rdelta.days) + " days old" 
    return jsonify(age_message=result)
if __name__ == '__main__':
   app.run()