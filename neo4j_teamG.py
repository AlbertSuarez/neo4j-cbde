from neo4j.v1 import GraphDatabase, basic_auth


def inserts(db):
    print('Inserts: START')
    session = db.session()
    # 4 port 2 supplier 6 lineitem 2 orders
    session.run("CREATE (a:Part {partkey:'1', mfgr:'aaaa', type: 'A', size: 10})")
    session.run("CREATE (b:Part {partkey:'2', mfgr:'bbbb', type: 'B', size: 15})")
    session.run("CREATE (c:Part {partkey:'3', mfgr:'aaaa', type: 'A', size: 5})")
    session.run("CREATE (d:Part {partkey:'4', mfgr:'cccc', type: 'C', size: 2})")

    session.close()
    

def create():
    print('Creation: START')

    db = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
    return inserts(db)


def query1(db):
    print('Query 1')


def query2(db):
    print('Query 2')


def query3(db):
    print('Query 3')


def query4(db):
    print('Query 4')


def run():
    print('Neo4J Laboratory\n')
    db = create()
    query1(db)
    query2(db)
    query3(db)
    query4(db)


if __name__ == '__main__':
    run()
