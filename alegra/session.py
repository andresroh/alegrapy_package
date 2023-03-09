import json,logging, base64
from requests import request

class session():
    
    user = None
    token = None
    url = "https://api.alegra.com/api/v1/"
    headers = {'Accept': 'application/json',
               'Content-type': 'application/json'}


    @classmethod 
    def create_auth(self):
        "return auth"
        api_key = base64.b64encode(f"{self.user}:{self.token}".encode()).decode()
        self.headers['Authorization'] = f"Basic {api_key}"
        print(">>> header: ",self.headers)

    @classmethod    
    def query(self,method,url,data={}):

        print('>>> request API')
           
        self.create_auth()
        response = request(method,
                           url,  
                           data=json.dumps(data),
                           headers=self.headers
                           )

        print(response.json())
        if response.status_code == 200:
            print('successful conection')
            return json.loads(response.text)

        print('wrong conection')
        return False