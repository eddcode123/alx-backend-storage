#!/usr/bin/env python3
''' Creating a cache using the Redis module in Python
'''

import redis
import uuid
from typing import Union

UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    ''' Class to handle caching with Redis.
    '''

    def __init__(self):
        ''' Initializes the Cache instance with a Redis connection
        and flushes the database.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        Stores a value in the cache with a randomly generated UUID key.

        Args:
            data (str): The value to be stored in the cache.

        Returns:
            str: The UUID key used to store the value.
        """
        # Generate a new UUID key
        mykey = str(uuid.uuid4())
        # Store the data in Redis using the generated key
        self._redis.set(mykey, data)
        return mykey
