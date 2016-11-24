from neo4jrestclient.client import GraphDatabase


def inserts(db: GraphDatabase):
    print('Inserts: START')

    part = db.labels.create('Part' {partkey : "1", mfgr : "aaaa", type: 'A', size: 10 })
    supplier = db.labels.create('Supplier')
    line_item = db.labels.create('LineItem')
    order = db.labels.create('Order')

    # TODO Create nodes and add into the labels
    # TODO Create relationships between nodes



    return db
