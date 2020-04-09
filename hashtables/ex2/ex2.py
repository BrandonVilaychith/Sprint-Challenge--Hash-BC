#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """
    # Insert the tickets as starting as key and destination as value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # Since source is the key we want the ticket where source is 'None' to start
    destination = hash_table_retrieve(hashtable, 'NONE')
    while destination is not 'NONE':
        route.append(destination)
        destination = hash_table_retrieve(hashtable, destination)

    return route