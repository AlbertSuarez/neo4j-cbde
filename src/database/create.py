from neo4jrestclient.client import GraphDatabase
from src.database.inserts import inserts


def create():
    print('Creation: START')

    db = GraphDatabase("http://localhost:7474",
                       username="neo4j",
                       password="neo4j")

    return inserts(db)
