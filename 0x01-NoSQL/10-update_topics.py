#!/usr/bin/env python3
"""Change school topics."""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of school documents based on the name.
    Args:
        mongo_collection (MongoCollection): Mongo collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set.
    Returns:
        Update result (dict): Contains information about the update operation.
    """
    mongo_collection.update_many(
        { "name": name },
        { '$set': { "topics": topics } }
    )
