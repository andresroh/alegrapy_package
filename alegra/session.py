import json,logging, base64 
from pprint import pprint
from requests import request

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="alegra.log",
                    filemode="a")

class session():
    
    user = None
    token = None
    url = "https://api.alegra.com/api/v1/"
    headers = {'Accept': 'application/json',
               'Content-type': 'application/json'}


    @classmethod 
    def create_auth(self):
        """return authorization"""

        api_key = base64.b64encode(f"{self.user}:{self.token}".encode()).decode()
        self.headers['Authorization'] = f"Basic {api_key}"

    @classmethod    
    def query(self,method,url,data={},params={}):
        """quey method

        Args:
            method (str): send query method (get,post,delete)
            url (str): endpoint
            data (dict, optional): query data. Defaults to {}.
            params (dict, optional): query params. Defaults to {}.

        Returns:
            (dict, None): if it's correct returns sever answer, for other hand returns None
        """
           
        self.create_auth()

        response = request(method,
                           url,
                           params=params,   
                           data=json.dumps(data),
                           headers=self.headers)

        
        if response.status_code == 200:

            logging.debug('Successful conection')
            logging.info(response.json())
            return json.loads(response.text)

        logging.warning(response.json())
        return None