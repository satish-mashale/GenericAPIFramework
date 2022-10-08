from base.Base import Base
from config import BASE_URI


class Publisheronboarding(Base):
    def __init__(self):
        Base.__init__(self)
        self.url = BASE_URI

    def create_publisher(self,testname, endpoint, data_set):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'PubToken': ''
        }
        res = self.send_request(testname,
            Base.RequestMethod.POST,
            custom_url=f"{self.url}{endpoint}",
            payload=data_set,
            headers=headers
        )
        return res
