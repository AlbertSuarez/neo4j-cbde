from neo4jrestclient.client import GraphDatabase


def inserts(db: GraphDatabase):
    print('Inserts: START')

    part = db.labels.create('Part')
    supplier = db.labels.create('Supplier')
    partsupp = db.labels.create('PartSupplier')
    nation = db.labels.create('Nation')
    region = db.labels.create('Region')
    customer = db.labels.create('Customer')
    line_item = db.labels.create('LineItem')
    order = db.labels.create('Order')

    # TODO Create nodes and add into the labels
    # TODO Create relationships between nodes

    return db


def create():
    print('Creation: START')

    db = GraphDatabase("http://localhost:7474",
                       username="neo4j",
                       password="neo4j")

    return inserts(db)


def query1(db: GraphDatabase):
    print('Query 1')


def query2(db: GraphDatabase):
    print('Query 2')


def query3(db: GraphDatabase):
    print('Query 3')


def query4(db: GraphDatabase):
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
