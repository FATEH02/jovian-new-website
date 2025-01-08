from flask import Flask, json , render_template , jsonify

app = Flask(__name__)
# simuating database here we can pass this data in our html file
JOBS=[{
  'id':1,
  'title':'Data Analyst',
  'location':'Bangluru,India',
  'salary':'10,00,000'
},
{
  'id':2,
  'title':'Data Analyst',
  'location':'Delhi,India',
  'salary':'15,00,000'
},
 {
  'id':3,
  'title':'Front end Engineer',
  'location':'Remote',
  # 'salary':'7,00,000'
 },
{
  'id':4,
  'title':'Back End Engineer',
  'location':'San Francisco,USA',
  'salary':'$120000'
}      
     ]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)  

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True) 