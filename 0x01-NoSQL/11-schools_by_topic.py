#!/usr/bin/env python3
"""Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    Args:
        mongo_collection (MongoCollection): Mongo collection object.
        topic (str): The topic to search for in schools' topics field.
    Returns:
        list: A list of documents representing schools with the specified topic.
    """
    return list(mongo_collection.find({'topics': topic}))
