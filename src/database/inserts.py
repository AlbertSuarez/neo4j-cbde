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
