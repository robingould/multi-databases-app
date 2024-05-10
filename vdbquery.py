import mysql.connector
from InstructorEmbedding import INSTRUCTOR
from pymilvus import Collection, connections

# Indicate which embedding model you plan to use.
model = INSTRUCTOR("hkunlp/instructor-xl")
# Connect to a Milvus DB
conn = connections.connect(
 alias="default",
 uri="uri",
 user='user',
 password='pass',
)

# Select a vector DB collection as your search choice.
collection = Collection("cse4701_ext")
# Set search parameters.
search_params = {
 "metric_type": "L2",
 "offset": 0,
 "ignore_growing": False,
 "params": {"nprobe": 10}
}

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="nba"
)

cursor = my_db.cursor()

cursor.execute(cursor.execute("SELECT name FROM players"))
result = cursor.fetchall()



# You can replace it with different questions.
for i in result:
    Queryquestion = f"Is {i} a vegetarian?"
    # You embed our query question using the model you decided.
    Embeddings = model.encode([Queryquestion],show_progress_bar=True)

    # Perform the query
    results = collection.search(
        data=[Embeddings[0]],
        anns_field="vector",
        param=search_params,
        limit=10,
        expr=None,
        output_fields=["text","filename","chunk_index"]
        )
        # Print out query results
    for hit in results[0]:
        print("Vector distance:", hit.distance)
        print("Text: ",hit.entity.get('text'))
        print("Filename: ",hit.entity.get('filename'))
        print("Chunk index: ",hit.entity.get('chunk_index'))

# Close cursor and connection
cursor.close()
my_db.close()