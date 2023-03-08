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
    def query(self,**kwargs):
        
        # self.create_auth()
        # response = request(kwargs['method'],
        #                    kwargs['url'], 
        #                    params=kwargs['params'], 
        #                    data=kwargs['data'],
        #                    headers=self.headers
        #                    )

        print('>>> request API')
        self.create_auth()
        print(">>> user: ",self.user)


        # if response.status_code == 200:
        #     print('successful conection')
        #     return json.loads(response.text)
        # elif response.status_code == 201:
        #     print('successful conection')
        #     return json.loads(response.text) 
        # else:
        #     print('wrong conection')
        #     print(response.json())
        #     return False