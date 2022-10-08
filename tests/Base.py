import pymysql
from pymysql import DatabaseError

from common_imports import *
from enum import Enum
import logging
import random
import json
import time
import os
import pytest

logger = logging.getLogger(__name__)
import uuid
import requests
from requests.models import Response


class Base(object):
    class ResponseObject(object):
        def __init__(self, response: Response):
            self.status_code = response.status_code
            self.content = response.content
            self.text = response.text
            try:
                self.json = response.json()
            except Exception as e:
                self.json = None
                logger.warning(e)
            self.header = response.headers
            self.url = response.url

    class RequestMethod(str, Enum):
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        DELETE = "DELETE"
        PATCH = "PATCH"

    def __init__(self) -> None:
        pass

    @staticmethod
    def gen_unique_str():
        id = uuid.uuid4()
        return id

    def send_request(self,
                     method: RequestMethod = RequestMethod.GET,
                     payload=None,
                     chunk_size: int = 0,
                     cookies=None,
                     custom_url: str = None,
                     headers=None,
                     files: list = None
                     ) -> ResponseObject:

        _payload = None

        if files:
            _payload = {}

        if custom_url is None:
            logging.warning("should provide url when sending request")

        if payload is None:
            logging.warning("should provide payload when sending request")
        else:
            _payload = payload

        if headers is None:
            _headers = {"Content-Type": "application/json"}
        else:
            _headers = headers

        # new request session
        res = None
        session_res = requests.session()

        if method is self.RequestMethod.GET:
            res = session_res.get(custom_url, headers=_headers, cookies=cookies, stream=True)
        elif method is self.RequestMethod.POST:
            res = session_res.post(custom_url, headers=_headers, cookies=cookies, stream=True, json=_payload,
                                   files=files)
        elif method is self.RequestMethod.PUT:
            res = session_res.put(custom_url, headers=_headers, cookies=cookies, stream=True, json=_payload,
                                  files=files)
        elif method is self.RequestMethod.DELETE:
            res = session_res.delete(custom_url, headers=_headers, cookies=cookies, stream=True)
        elif method is self.RequestMethod.PATCH:
            res = session_res.patch(custom_url, headers=_headers, cookies=cookies, stream=True, json=_payload,
                                    files=files)
        else:
            res = session_res.put(custom_url, headers=_headers, cookies=cookies, stream=True, data=_payload,
                                  files=files)

        res_obj = self.ResponseObject(res)

        logger.info("\n=============URL=================\n")
        logger.info(res_obj.url)
        logger.info("\n============Payload==============\n")
        logger.info(payload)
        logger.info("\n============Response=============\n")
        if len(res.content) < 10000:
            logger.info(res_obj.text)
        else:
            logger.info("Too large response body, skipped to print.")
        logger.info("\n=================================\n")
        return res_obj


class Database(object):

    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        try:

            self.db = pymysql.connect(host=self.host, user=self.user,
                                      passwd=self.password, database=self.database, port=self.port)
            self.db.set_charset('utf8')
            self.cursor = self.db.cursor()
            logger.info("Constructor Executed Successfully !!!")
        except DatabaseError as e:
            logger.info(f"Failed to connect to Database ==> {self.database} ")

    def update_data_in_db(self, query, append):  # make sure hostname and database name is passed from ride
        query = str(query) + str(append)
        print("this is the query: {}".format(query))
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print(data)
            self.db.commit()
            time.sleep(5)
        except:
            print('Invalid Query' + query)
            raise

    def get_data_from_db(self, query, append):  # make sure hostname and database name is passed from ride
        query = str(query) + str(append)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except:
            print('Invalid Query' + query)
            raise

    def get_data_from_db2(self, query, append):
        query = str(query) + str(append)
        print(query)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            for id in data:
                # print(id)
                pass
            # cursor.close()
            return id[0]
        except:
            print('Invalid Query')
            raise

    def get_list_from_db(self, query, append):
        query = str(query) + str(append)
        print(query)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            values = []
            for id in data:
                values.append(id[0])
            print(values)
            return values
        except:
            print('Invalid Query')
            raise

    def get_multiple_column_from_db(self, query, append):
        query = str(query) + str(append)
        print(query)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            values = []
            for id in data:
                values.append(id)
            return values
        except:
            print('Invalid Query')
            raise
