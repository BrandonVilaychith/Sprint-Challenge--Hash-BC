#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index in range(0, length):
        # Grab the weight and check if in hashtable
        # If not add it
        hash_item = hash_table_retrieve(ht, (limit - weights[index]))
        if hash_item is None:
            # Insert weight value and key and index as value
            hash_table_insert(ht, weights[index], index)
        elif hash_item is not None:
            # if hash item is not none then we have 2 index's that add to the limit
            return (index, hash_item)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
