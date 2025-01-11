from flask import Flask, json, render_template, jsonify
from dataabase import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
    with engine.connect() as connection:
        print("Connected to the database!")
        result = connection.execute(text("SELECT * FROM jobs"))
        result_dict = [dict(row._mapping) for row in result]
        print(result_dict)
        return result_dict  # Add this line to return the fetched jobs

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()  # Now it will have the data
    return render_template('home    .html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Now it will have the data
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
