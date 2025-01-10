from flask import Flask, json , render_template , jsonify
from dataabas import engine
from sqlalchemy import text

app = Flask(__name__)
# simuating database here we can pass this data in our html file
# JOBS=[{
#   'id':1,
#   'title':'Data Analyst',
#   'location':'Bangluru,India',
#   'salary':'10,00,000'
# },
# {
#   'id':2,
#   'title':'Data Analyst',
#   'location':'Delhi,India',
#   'salary':'1,00,000'
# },
#  {
#   'id':3,
#   'title':'Front end Engineer',
#   'location':'Remote',
#   # 'salary':'7,00,000'
#  },
# {
#   'id':4,
#   'title':'Back End Engineer',
#   'location':'San Francisco,USA',
#   'salary':'$10000'
# }      
#      ]

def load_jobs_from_db():
  with engine.connect() as connection:
    print("Connected to the database!")
    result = connection.execute(text("SELECT * FROM jobs"))
    result_dict = [dict(row._mapping) for row in result]
    print(result_dict)


@app.route("/")
def hello_world():
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs)  

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True) 