from neo4j.v1 import GraphDatabase, basic_auth
import datetime


def inserts(db):
    print('Inserts: START')
    session = db.session()

    date = datetime.datetime(2016,11,24)
    
    session.run("MATCH (n) DETACH DELETE n")
    # 4 port 2 supplier 6 lineitem 2 orders
    session.run("CREATE (p1:Part {partkey:'1', mfgr:'aaaa', type: 'A', size: 10})")
    session.run("CREATE (p2:Part {partkey:'2', mfgr:'bbbb', type: 'B', size: 15})")
    session.run("CREATE (p3:Part {partkey:'3', mfgr:'aaaa', type: 'A', size: 5})")
    session.run("CREATE (p4:Part {partkey:'4', mfgr:'cccc', type: 'C', size: 2})")
    session.run("CREATE (s1:Supplier {name: 's1', accbal: 1.00, adress: 'Main Street', phone: '111111111', comment: 'nothing', n_name: 'Spain', r_name: 'Barcelona'})")
    session.run("CREATE (s1:Supplier {name: 's2', accbal: 2.00, adress: 'Main Street2', phone: '222222222', comment: 'nothing2', n_name: 'Spain', r_name: 'Barcelona'})")
    session.run("CREATE (o1:Order {orderdate: date, shippriority:'1', c_marketsegment: 'MKT1', n_name: 'Spain'})")
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
