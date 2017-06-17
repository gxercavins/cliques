# dummy input data to test the Bron-Kerbosch algorithm, given in the adjacency list format. 'graph' is a dictionary
# that ssociates each vertex in the graph (keys) with the collection of its neighboring vertices or edges (values).

graph = {
    'John': ['Ed','Arya','Sansa','Robb'],
    'Ed': ['John','Arya','Sansa','Robb'],
    'Arya': ['John','Ed','Sansa','Robb'],
    'Sansa': ['John','Ed','Arya','Robb'],
    'Robb': ['John','Ed','Arya','Sansa'],
    'Tyrion': ['Cersei','Jaime'],
    'Cersei': ['Tyrion','Jaime'],
    'Jaime': ['Tyrion','Cersei'],
    'Hodor': []
}