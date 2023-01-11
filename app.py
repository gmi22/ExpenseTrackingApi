from flask import Flask, request,jsonify,json,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from datetime import date,datetime,timedelta
from flask_migrate import Migrate
from dateutil import parser


app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"db.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app,db)



class Income(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    category =db.Column(db.String(50))
    vendor = db.Column(db.String)
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))


    def __init__(self,date,category,vendor,amount,description):
        self.date = date 
        self.category = category
        self.vendor = vendor
        self.amount = amount
        self.description = description



class Expense(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    category =db.Column(db.String(50))
    vendor = db.Column(db.String)
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))


    def __init__(self,date,category,vendor,amount,description):
        self.date = date
        self.category = category
        self.vendor = vendor
        self.amount = amount
        self.description = description




class IncomeSchema(ma.Schema):
    class Meta:
        fields = ('id','date','category','vendor','amount','description')

class ExpenseSchema(ma.Schema):
    class Meta:
        fields = ('id','date','category','vendor','amount','description')


income_schema = IncomeSchema()
expense_schema = ExpenseSchema()

incomes_schema = IncomeSchema(many=True)
expenses_schema = ExpenseSchema(many=True)


@app.route('/income',methods=['POST'])
def add_income():
    date = parser.parse(request.json['date'])
    category = request.json['category']
    vendor = request.json['vendor']
    amount = request.json['amount']
    description = request.json['description']

    new_income = Income(date,category,vendor,amount,description)

    db.session.add(new_income)
    db.session.commit()

    return income_schema.jsonify(new_income)

@app.route('/expense',methods=['POST'])
def add_expense():
    date = parser.parse(request.json['date'])
    category= request.json['category']
    vendor = request.json['vendor']
    amount = request.json['amount']
    description = request.json['description']

    new_expense = Expense(date,category,vendor,amount,description)

    db.session.add(new_expense)
    db.session.commit()

    return expense_schema.jsonify(new_expense)

@app.route('/income',methods=['Get'])
def get_income():
    all_income = Income.query.all()
    return incomes_schema.dump(all_income)


@app.route('/expense',methods=['Get'])
def get_expense():
    all_expense = Expense.query.all()
    return expenses_schema.dump(all_expense)

#Delete Stuff
@app.route('/income/<id>',methods=['DELETE'])
def del_income(id):
    del_income = Income.query.get(id)
    db.session.delete(del_income)
    db.session.commit()
    return income_schema.jsonify(del_income)

@app.route('/expense/<id>',methods=['DELETE'])
def del_expense(id):
    del_expense = Expense.query.get(id)
    db.session.delete(del_expense)
    db.session.commit()
    return expense_schema.jsonify(del_expense)



# viwes
@app.route("/")
def home():
    name = 'George'
    return render_template("index.html",content = name)

    

#query test
@app.route('/incomex',methods=['Get'])
def incomeByYear():
    year_income = Income.query.filter(Income.date > date(2022,4,30))
    return incomes_schema.dump(year_income)




if __name__ == '__main__':
    app.run(debug=True)






