from src.database.create import create
from src.queries.query1 import query1
from src.queries.query2 import query2
from src.queries.query3 import query3
from src.queries.query4 import query4

print('Neo4J Laboratory\n')
db = create()
query1(db)
query2(db)
query3(db)
query4(db)
