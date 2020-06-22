from typing import List

class DBConn:
    def __init__(self, hosts: List[str], table_space: str, config):
        self._onError = lambda x: x

    def onError(self):
        self._onError(1)


def DBConnFactory():
    dbconn = DBConn(['serve1', 'server2', 'server2'], 'demo', { "charset": "utf-8" })
    dbconn._onError = lambda x: print("Error " + x)
    return dbconn