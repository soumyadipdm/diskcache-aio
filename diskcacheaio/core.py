"""Core component of the library"""

import asyncio

import aioodbc


class CachedDictionary:
    """A SQLite based dictionary"""

    def __init__(self, db_path: str):
        """
        :param db_path: path to the database file
        """
        self._dsn = "Driver=SQLite;Database={}".format(db_path)
        self._connection = aioodbc.connect(
            dsn=self._dsn, loop=asyncio.get_event_loop())
