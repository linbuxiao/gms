import pymongo


class Engine:
    def __init__(self, host, port, db_name, username, password, collection, key_column):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.username = username
        self.password = password
        self.collection = collection
        self.key_column = key_column

    def get_connection(self):
        params = {
            "host": self.host,
            "port": self.port,
        }
        if self.username and self.password:
            params["username"] = self.username
            params["password"] = self.password
        conn = pymongo.MongoClient(**params)
        return conn

    def get_all_columns(self):
        db = self.get_connection()[self.db_name]
        result = {}
        collection = db[self.collection]
        key_columns = collection.distinct(self.key_column)
        for kc in key_columns:
            record = collection.find_one(
                {
                    self.key_column: kc,
                },
                sort=[("_id", pymongo.DESCENDING)],
            )
            for key, value in record.items():
                if key in result or key == "_id":
                    continue
                result[key] = type(value).__name__
        return result
