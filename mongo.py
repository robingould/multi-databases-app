from pymongo import MongoClient
import os
from IPython.display import display, Image
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="nba"
)
cursor = my_db.cursor()
query = "SELECT name FROM players WHERE vegetarian = 'Yes'"
cursor.execute(query)
athletes = cursor.fetchall()
client = MongoClient("mongodb://cse4701:cse4701@ip:port/myDatabase")
db = client['myDatabase']
athletes_collection = db['cse4701_ext']
for i in athletes:
    athlete_name = i[0].split()[0]
    document = athletes_collection.find_one({'description.firstname': athlete_name})
    print(document['description'])
    if document:
        image_data = document.get('images')
        # If image data exists, save it to a file
        if image_data:
            image_file_path = 'athlete_image.jpg'
            with open(image_file_path, 'wb') as image_file:
                image_file.write(image_data)
                print(f"Image saved as {image_file_path}")

    # Automatically open the image file with the default application
            os.system(f'open {image_file_path}')
        else:
            print(f"No image found for {athlete_name}")

    else:
        print(f"No document found for athlete with name {athlete_name}")


cursor.close()
my_db.close()
