#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Union, Callable, Optional
import sys

unionTypes = Union[str, bytes, int, float]


class Cache:
    """A representation of Memory cache"""
    def __init__(self):
        """Stores a instance of Redis client
        as a private variable '_redis'
        it also flushes the instance using flushdb
        """
        self._redis = redis.Redis()
        # flush the instance
        self._redis.flushdb()

    def store(self, data: unionTypes) -> str:
        """Method that stores the input data in Redis
        using the random key and return the key
        Args:
            data (unionTypes): The data to be stored
        Returns:
            Key(Str): The key generated
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, Key: str, fn: Optional[Callable] = None) \
            -> unionTypes:
        """
        convert the data back
        to the desired format
        Args:
            key (str): key to retive value
            fn (Callable): function to convert bytes to string
        Returns:
            data (unionTypes): data associated to the key
        """
        if fn:
            return fn(self._redis.get(Key))
        return self._redis.get(Key)
    
    def get_int(self: bytes) -> int:
        """get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """Get string"""
        return self.decode('utf-8')
