import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="nba"
)

cursor = my_db.cursor()

backcourt_veg_query = "SELECT COUNT(*) FROM players WHERE team_id = 'T5' AND vegetarian = 'Yes' AND position IN ('PG', 'SG')"
backcourt_total_query = "SELECT COUNT(*) FROM players WHERE team_id  = 'T5' AND position IN ('PG', 'SG')"

frontcourt_veg_query = "SELECT COUNT(*) FROM players WHERE team_id  = 'T5' AND vegetarian = 'Yes' AND position IN ('C', 'PF', 'SF')"
frontcourt_total_query = "SELECT COUNT(*) FROM players WHERE team_id  = 'T5' AND position IN ('C', 'PF', 'SF')"

cursor.execute(backcourt_veg_query)
backcourt_veg = cursor.fetchone()[0]

cursor.execute(backcourt_total_query)
backcourt_total = cursor.fetchone()[0]

cursor.execute(frontcourt_veg_query)
frontcourt_veg = cursor.fetchone()[0]

cursor.execute(frontcourt_total_query)
frontcourt_total = cursor.fetchone()[0]

print("front court ", frontcourt_veg/frontcourt_total)
print("back court fraction", backcourt_veg/backcourt_total)



cursor.close()
my_db.close()

