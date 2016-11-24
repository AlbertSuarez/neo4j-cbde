from neo4j.v1 import GraphDatabase, basic_auth


def inserts(db):
    print('Inserts: START')
    session = db.session()
    session.run("CREATE ('Part' {partkey : '1', mfgr : 'aaaa', type: 'A', size: 10 })")
    #part = db.labels.create('Part' {partkey : "1", mfgr : "aaaa", type: 'A', size: 10 })
    
    '''
    supplier = db.labels.create('Supplier')
    line_item = db.labels.create('LineItem')
    order = db.labels.create('Order')
    '''

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
