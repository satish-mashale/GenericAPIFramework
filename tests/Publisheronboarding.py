import Base
from config import BASE_URI


class Publisheronboarding():
    def __init__(self):
        Base.__init__(self)
        self.url = BASE_URI

    def create_publisher(self, endpoint, data_set):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'PubToken': ''
        }
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.url}{endpoint}",
            payload=data_set,
            headers=headers
        )
        print(res)
        return res
