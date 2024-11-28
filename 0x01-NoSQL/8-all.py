#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """List all documents in a Mongo collection.
    Args:
        mongo_collection (MongoCollection): Mongo collection object.
    Returns:
        list: List of all documents in the collection.
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
