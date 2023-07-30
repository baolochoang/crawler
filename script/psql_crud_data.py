"""CRUD DATA"""
from typing import List


class PostgresqlEngine:
    def __int__(self, host, port):
        self.__host = host
        self.__port = port

    def connect_psql(self):
        return

    def create_table(self, commands ):
        """
        :param table_name:
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
