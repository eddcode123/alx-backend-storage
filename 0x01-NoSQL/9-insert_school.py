#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Args:
        mongo_collection (MongoCollection): Mongo collection object.
        kwargs (Key-value pair): Key-value pairs to insert into the document.
    Returns:
        id: The ID of the inserted document.
    """
    # Insert kwargs in mongo_collection
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
