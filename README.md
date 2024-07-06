# NBA Player Database Analysis System

This project contains a set of Python scripts for analyzing NBA player data, with a focus on dietary preferences and image retrieval. Part of Databases course from UConn.

Toy model of a Python app connecting cloud hosted MySQL, MongoDB, and Milvus (a vector DB) databases to query articles with text embeddings from a sentence transformer about whether NBA players are vegetarian, and other fun stats. 

Yes this is an invitation to talk to me about basketball*. 

- Note, won't run because IP addresses and passwords were removed/redacted 
- Also note, the documentation isn't documentation, but rather associated documents that show some outputs of the project

*Editors note, Robin knows nothing about basketball

## Files

1. `embeddedsql.py`: queries MySQL database to check if a specific player is vegetarian.
2. `hypothesis.py`: calculates fraction of vegetarian players in the backcourt and frontcourt of team T5 (ie, does being a frontcourt vs backcourt player make you more or less likely to be a vegetarian).
3. `mongo.py`: retrieves and displays images of vegetarian athletes from a MongoDB database.
4. `vdbquery.py`: performs vector similarity search on player data using Milvus.

## Setup

### Prerequisites

- Python 3+
- MySQL
- MongoDB
- Milvus vector database

Install the required packages using:
`pip install mysql-connector-python pymongo InstructorEmbedding pymilvus`


### Database Configuration

1. Set up a MySQL database named 'nba' with a 'players' table.
2. Configure MongoDB with a 'myDatabase' database and 'cse4701_ext' collection.
3. Set up a Milvus vector database with a 'cse4701_ext' collection.

## Usage

1. `embeddedsql.py`: Run to check if a specific player (default: Luka Doncic) is vegetarian.
2. `hypothesis.py`: Execute to compare vegetarian ratios between backcourt and frontcourt players.
3. `mongo.py`: Run to retrieve and display images of vegetarian athletes.
4. `vdbquery.py`: Use to perform vector similarity searches on player data with natural language.

## Note

Ensure you replace the placeholder credentials and connection strings with your actual database credentials and connection information.


