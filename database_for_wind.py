import sqlite3
import pandas as pd
from avg_wind_speed_direction import avg

def csv_to_db(csv_filename, db_filename, table_name):
    # Read CSV data using pandas
    csv_data = pd.read_csv(csv_filename)

    # Create or connect to the SQLite database
    conn = sqlite3.connect(db_filename)

    # Write CSV data to the SQLite database
    csv_data.to_sql(table_name, conn, index=False, if_exists='replace')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Usage example
csv_filename = 'data.csv'  # Replace with your CSV file's name
db_filename = 'data.db'    # Replace with the desired SQLite database file name
table_name = 'data_table'  # Replace with the desired table name

csv_to_db(csv_filename, db_filename, table_name)


connection = sqlite3.connect("data.db")
connection.row_factory = lambda cursor, row: row[0]
cursor = connection.cursor()

max_sales = 'select WindSpeedMph from data_table union all select WindHeading from data_table'

cursor.execute(max_sales)
x = cursor.fetchall()
y = []
i = 0
while i <= 985:
  y.append(int(x[i]))
  if x[i + 986] == "N":
    y.append(int(0))
  elif x[i + 986] == "NE":
    y.append(int(45))
  elif x[i + 986] == "NW":
    y.append(int(315))
  elif x[i + 986] == "E":
    y.append(int(90))
  elif x[i + 986] == "W":
    y.append(int(270))
  elif x[i + 986] == "SE":
    y.append(int(135))
  elif x[i + 986] == "SW":
    y.append(int(225))
  elif x[i + 986] == "S":
    y.append(int(180))
  i = i + 1

avg(y)
#1-985 = speed, 986-inf = direction
connection.close()
