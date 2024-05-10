import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="nba"
)

cursor = my_db.cursor()

player_name = "Luka Doncic"

query = f"SELECT vegetarian FROM players WHERE name = '{player_name}' AND team_id = 'T5'"
cursor.execute(query)
result = cursor.fetchone()

if result:
    if result[0] == 'Yes':
        print(f"Is {player_name} a vegetarian? Yes")
    else:
        print(f"Is {player_name} a vegetarian? No")
else:
    print(f"{player_name} not found in team T5")

# Close cursor and connection
cursor.close()
my_db.close()