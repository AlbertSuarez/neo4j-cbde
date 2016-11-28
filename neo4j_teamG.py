from neo4j.v1 import GraphDatabase, basic_auth
import datetime
import time


# Drop all data
def drop(session):
    session.run("MATCH (n) DETACH DELETE n")


# Print all data
def print_all(session):
    print('The program have inserted the following nodes:')
    for item in session.run('MATCH (n) RETURN n'):
        print(item)


# Create a part node with parameters specified
def create_part(session, identifier, partkey, mfgr, type, size):
    session.run("CREATE (" + identifier + ":Part {partkey:'" + partkey +
                "', mfgr:'" + mfgr + "', type: '" + type + "', size: " + size + "})")


# Create a supplier node with parameters specified
def create_supplier(session, identifier, suppkey, name, accbal, adress, phone, comment, n_name, r_name):
    session.run("CREATE (" + identifier + ":Supplier {suppkey: '" + suppkey +
                "', name: '" + name + "', accbal: " + accbal + ", adress: '" + adress +
                "', phone: '" + phone + "', comment: '" + comment +
                "', n_name: '" + n_name + "', r_name: '" + r_name + "'})")


# Create an order node with parameters specified
def create_order(session, identifier, orderkey, orderdate, shippriority, c_marketsegment, n_name):
    session.run("CREATE (" + identifier + ":Order {orderkey: '" + orderkey + "', orderdate: {date}, shippriority:'" +
                shippriority + "', c_marketsegment: '" + c_marketsegment + "', n_name: '" + n_name + "'})",
                {"date": orderdate})


# Create a line item node with parameters specified
def create_lineitem(session, identifier, orderkey, suppkey, returnflag, quantity,
                    extendedPrice, discount, tax, shipdate, linestatus):
    session.run("CREATE (" + identifier + ":LineItem {orderkey: '" + orderkey +
                "', suppkey: '" + suppkey + "', returnflag: '" + returnflag + "', quantity: " + quantity +
                ", extendedPrice: " + extendedPrice + ", discount: " + discount + ", tax: " + tax +
                ", shipdate: {date2}, linestatus: '" + linestatus + "'})", {"date2": shipdate})


# Create a edge between supplier and part nodes specified in parameters
def create_edge_supplier_part(session, supplier, suppkey, part, partkey, supplycost):
    session.run(
        "MATCH (" + supplier + ":Supplier {suppkey: '" + suppkey + "'}), (" + part + ":Part {partkey: '" + partkey +
        "'}) CREATE (" + supplier + ")-[:ps {supplycost: ['" + supplycost + "']}]->(" + part + ")")


# Create a edge between order and line item nodes specified in parameters
def create_edge_order_lineitem(session, order, orderkey, lineitem):
    session.run("MATCH (" + order + ":Order {orderkey: '" + orderkey + "'}), (" + lineitem +
                ":LineItem {orderkey: '" + orderkey + "'}) CREATE (" + order + ")-[:has]->(" + lineitem + ")")


# Create a edge between line item and supplier nodes specified in parameters
def create_edge_lineitem_supplier(session, lineitem, supplier, suppkey):
    session.run("MATCH (" + lineitem + ":LineItem {suppkey: '" + suppkey + "'}), (" + supplier +
                ":Supplier {suppkey: '" + suppkey + "'}) CREATE (" + lineitem + ")-[:isFrom]->(" + supplier + ")")


# Insert some data in database
def inserts(db):
    print('Starting inserts...')
    session = db.session()

    date = datetime.datetime(2016, 11, 24)
    date2 = datetime.datetime(2016, 11, 25)
    timestamp = time.mktime(date.timetuple())
    timestamp2 = time.mktime(date2.timetuple())

    drop(session)
    create_part(session, 'p1', '1', 'aaaa', 'A', '10')
    create_part(session, 'p2', '2', 'bbbb', 'B', '15')
    create_part(session, 'p3', '3', 'cccc', 'C', '5')
    create_part(session, 'p4', '4', 'dddd', 'D', '2')
    create_supplier(session, 's1', 's1', 'supp1', '1.00', 'Main Street', '111111', 'nothing', 'Spain', 'Barcelona')
    create_supplier(session, 's2', 's2', 'supp2', '2.00', 'Main Street 2', '2222222 ', 'nothing 2', 'Spain',
                    'Barcelona')
    create_order(session, 'o1', 'o1', timestamp, '1', 'MKT1', 'Spain')
    create_order(session, 'o2', 'o2', timestamp, '2', 'MKT1', 'Spain')
    create_lineitem(session, 'l1', 'o1', 's1', 'a', '10', '10.0', '0.1', '2.0', timestamp2, 'a')
    create_lineitem(session, 'l2', 'o1', 's1', 'a', '5', '18.0', '0.5', '3.0', timestamp2, 'a')
    create_lineitem(session, 'l3', 'o1', 's1', 'a', '5', '5.0', '0.05', '1.0', timestamp2, 'a')
    create_lineitem(session, 'l4', 'o2', 's2', 'b', '10', '20.0', '0.3', '3.0', timestamp2, 'b')
    create_lineitem(session, 'l5', 'o2', 's2', 'b', '20', '40.0', '0.5', '1.0', timestamp2, 'b')
    create_lineitem(session, 'l6', 'o2', 's2', 'b', '5', '10.0', '0.2', '2.0', timestamp2, 'b')

    create_edge_supplier_part(session, 's1', 's1', 'p1', '1', '10')
    create_edge_supplier_part(session, 's1', 's1', 'p2', '2', '20')
    create_edge_supplier_part(session, 's1', 's1', 'p3', '3', '30')
    create_edge_supplier_part(session, 's1', 's1', 'p4', '4', '40')
    create_edge_supplier_part(session, 's2', 's2', 'p1', '1', '50')
    create_edge_supplier_part(session, 's2', 's2', 'p2', '2', '10')
    create_edge_supplier_part(session, 's2', 's2', 'p3', '3', '15')
    create_edge_supplier_part(session, 's2', 's2', 'p4', '4', '20')
    create_edge_order_lineitem(session, 'o1', 'o1', 'l1')
    create_edge_order_lineitem(session, 'o2', 'o2', 'l4')
    create_edge_lineitem_supplier(session, 'l1', 's1', 's1')
    create_edge_lineitem_supplier(session, 'l2', 's2', 's2')

    print_all(session)
    print('Finish inserts!\n')
    session.close()
    return db


# Create the neo4j database
def create():
    print('Create and connect with Database')

    db = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
    return inserts(db)


# Query 1 code
def query1(db):
    print('Query 1 starting...')

    print()


# Query 2 code
def query2(db):
    print('Query 2 starting...')

    print()


# Query 3 code
def query3(db):
    print('Query 3 starting...')

    print()


# Query 4 code
def query4(db):
    print('Query 4 starting...')

    print()


# Main function
def run():
    print('Neo4J Laboratory\n')
    db = create()
    query1(db)
    query2(db)
    query3(db)
    query4(db)
    print('THE END')


if __name__ == '__main__':
    run()
