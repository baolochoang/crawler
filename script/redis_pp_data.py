"""CRUD DATA"""
from typing import List


class ElasticsearchEngine:
    def __int__(self, host, port):
        self.__host = host
        self.__port = port

    def connect_es(self):
        return

    def create_index(self, index_db: str, index_mapping: dict):
        """
        :param index_db:
        :param index_mapping:
        :return:
        """
        return

    def insert_data(self, data: List[dict]):
        return

    def update_data(self, data: List[dict]):
        return

    def read_data(self, **kwargs):
        return

    def delete_data(self, **kwargs):
        return

