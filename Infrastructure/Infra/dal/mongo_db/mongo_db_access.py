import json
from typing import TypeVar, List
import pymongo
from pymongo.database import Database

from Infrastructure.Infra.dal.data_reposetory.data_rep import DataRep
from Infrastructure.Infra.dal.json_encoder.json_encoder import CustomEncoder


class MongoDbAccess:
    T = TypeVar('T')

    @staticmethod
    def initialize_mongo_client() -> Database:
        client = pymongo.MongoClient(DataRep.mongo_connection_string)
        database_name = DataRep.mongo_connection_string.split("net")[1].replace("/", "")
        database = client[database_name]
        return database

    @staticmethod
    def select_all_documents_from_table_as_class(table_name: str, T) -> List[T]:
        database = MongoDbAccess.initialize_mongo_client()
        collection = database[table_name]
        all_documents = collection.find()
        table_as_object = []

        for document in all_documents:
            json_str = json.dumps(document, cls=CustomEncoder)
            load = json.loads(json_str)
            instance = T(**load)
            table_as_object.append(instance)
        return table_as_object

