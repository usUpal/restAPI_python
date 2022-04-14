
# from urllib import request
from flask import Flask, request
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    sologan = db.Column(db.String(120)) 
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.sologan}"

@app.route('/')
def index():
    return "nice try asshole"

@app.route('/company')
def get_company():
    company = Company.query.all()
    output = []
    for i in company:
        com_sol = {"name": i.name, "sologan":i.sologan}
        output.append(com_sol)
    return {"company": output}

@app.route('/company/<id>')
def get_com(id):
    comp = Company.query.get_or_404(id)
    return {"name":comp.name, "sologan":comp.sologan}

@app.route('/company', methods = ['POST'])
def add_company():
    comp = Company(name=request.json['name'],sologan=request.json['sologan'])
    db.session.add(comp)
    db.session.commit()
    return {"id": comp.id}
#delete
@app.route('/company/<id>', methods=['DELETE'])
def delete_comp(id):
    comp = Company.query.get(id)
    if comp is None:
        return {"error":"company name"}
    db.session.delete(comp)
    db.session.commit()
    return {"Successfully":"deleted"}