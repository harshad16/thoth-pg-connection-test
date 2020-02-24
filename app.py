from thoth.storages import GraphDatabase

if __name__ == '__main__':
    print("Testing PostgreSQL connection!")
    graph = GraphDatabase()
    graph.connect()
