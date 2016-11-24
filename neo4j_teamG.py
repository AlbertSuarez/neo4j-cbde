from neo4j.v1 import GraphDatabase, basic_auth
import datetime
import time


def inserts(db):
    print('Inserts: START')
    session = db.session()

    date = datetime.datetime(2016,11,24)
    date2 = datetime.datetime(2016,11,25)
    timestamp = time.mktime(date.timetuple())
    timestamp2 = time.mktime(date2.timetuple())

    session.run("MATCH (n) DETACH DELETE n")
    # 4 port 2 supplier 6 lineitem 2 orders
    session.run("CREATE (p1:Part {partkey:'1', mfgr:'aaaa', type: 'A', size: 10})")
    session.run("CREATE (p2:Part {partkey:'2', mfgr:'bbbb', type: 'B', size: 15})")
    session.run("CREATE (p3:Part {partkey:'3', mfgr:'aaaa', type: 'A', size: 5})")
    session.run("CREATE (p4:Part {partkey:'4', mfgr:'cccc', type: 'C', size: 2})")
    session.run("CREATE (s1:Supplier {suppkey: 's1', name: 'supp1', accbal: 1.00, adress: 'Main Street', phone: '111111111', comment: 'nothing', n_name: 'Spain', r_name: 'Barcelona'})")
    session.run("CREATE (s2:Supplier {suppkey: 's2', name: 'supp2', accbal: 2.00, adress: 'Main Street2', phone: '222222222', comment: 'nothing2', n_name: 'Spain', r_name: 'Barcelona'})")
    session.run("CREATE (o1:Order {orderkey: 'o1', orderdate: {date}, shippriority:'1', c_marketsegment: 'MKT1', n_name: 'Spain'})", {"date" : timestamp })
    session.run("CREATE (o2:Order {orderkey: 'o2',orderdate: {date}, shippriority:'2', c_marketsegment: 'MKT1', n_name: 'Spain'})", {"date" : timestamp })
    session.run("CREATE (l1:LineItem {orderkey: 'o1', suppkey: 's1', returnflag: 'a', quantity: 10, extendedPrice: 10.0, discount: 0.1, tax: 2.0, shipdate: {date2}, linestatus: 'a'})", {"date2" : timestamp2})
    session.run("CREATE (l2:LineItem {orderkey: 'o1', suppkey: 's1', returnflag: 'a', quantity: 5, extendedPrice: 18.0, discount: 0.5, tax: 3.0, shipdate: {date2}, linestatus: 'a'})", {"date2" : timestamp2})
    session.run("CREATE (l3:LineItem {orderkey: 'o1', suppkey: 's1', returnflag: 'a', quantity: 5, extendedPrice: 5.0, discount: 0.05, tax: 1.0, shipdate: {date2}, linestatus: 'a'})", {"date2" : timestamp2})
    session.run("CREATE (l4:LineItem {orderkey: 'o2', suppkey: 's2', returnflag: 'b', quantity: 10, extendedPrice: 20.0, discount: 0.3, tax: 3.0, shipdate: {date2}, linestatus: 'b'})", {"date2" : timestamp2})
    session.run("CREATE (l5:LineItem {orderkey: 'o2', suppkey: 's2', returnflag: 'b', quantity: 20, extendedPrice: 40.0, discount: 0.5, tax: 1.0, shipdate: {date2}, linestatus: 'b'})", {"date2" : timestamp2})
    session.run("CREATE (l6:LineItem {orderkey: 'o2', suppkey: 's2', returnflag: 'b', quantity: 5, extendedPrice: 10.0, discount: 0.2, tax: 2.0, shipdate: {date2}, linestatus: 'b'})", {"date2" : timestamp2})
    
    #ARESTES
    session.run("MATCH (s1:Supplier {suppkey: 's1'}), (p1:Part {partkey: '1'}) CREATE (s1)-[:ps {supplycost: ['10']}]->(p1)")
    session.run("MATCH (s1:Supplier {suppkey: 's1'}), (p2:Part {partkey: '2'}) CREATE (s1)-[:ps {supplycost: ['20']}]->(p2)")
    session.run("MATCH (s1:Supplier {suppkey: 's1'}), (p3:Part {partkey: '3'}) CREATE (s1)-[:ps {supplycost: ['30']}]->(p3)")
    session.run("MATCH (s1:Supplier {suppkey: 's1'}), (p4:Part {partkey: '4'}) CREATE (s1)-[:ps {supplycost: ['40']}]->(p4)")
    session.run("MATCH (s2:Supplier {suppkey: 's2'}), (p1:Part {partkey: '1'}) CREATE (s2)-[:ps {supplycost: ['5']}]->(p1)")
    session.run("MATCH (s2:Supplier {suppkey: 's2'}), (p2:Part {partkey: '2'}) CREATE (s2)-[:ps {supplycost: ['10']}]->(p2)")
    session.run("MATCH (s2:Supplier {suppkey: 's2'}), (p3:Part {partkey: '3'}) CREATE (s2)-[:ps {supplycost: ['15']}]->(p3)")
    session.run("MATCH (s2:Supplier {suppkey: 's2'}), (p4:Part {partkey: '4'}) CREATE (s2)-[:ps {supplycost: ['20']}]->(p4)")

    session.run("MATCH (o1:Order {orderkey: 'o1'}), (l1:LineItem {orderkey: 'o1'}) CREATE (o1)-[:has]->(l1)")
    session.run("MATCH (o2:Order {orderkey: 'o2'}), (l4:LineItem {orderkey: 'o2'}) CREATE (o2)-[:has]->(l4)")

    session.run("MATCH (l1:LineItem {suppkey: 's1'}), (s1:Supplier {suppkey: 's1'}) CREATE (l1)-[:isFrom]->(s1)")
    session.run("MATCH (l2:LineItem {suppkey: 's2'}), (s2:Supplier {suppkey: 's2'}) CREATE (l2)-[:isFrom]->(s2)")

   

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
