from sqlalchemy import create_engine

host = "bxz0uj9mhdeyduwfoglg-mysql.services.clever-cloud.com"
port = 3306
user = "uyuwka7azei6q1q2"
password = "bQnZeRvaBMAEYGnhhxtp"
database = "bxz0uj9mhdeyduwfoglg"

db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        print("Connected to the database!")
        result = connection.execute(text("SELECT * FROM jobs"))
        result_dict = [dict(row._mapping) for row in result]
        print(result_dict)

except Exception as e:
    print("Error while connecting to the database:", e)

