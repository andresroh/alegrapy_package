from alegra.session import session

class actions:

    endpoint = ""

    def __init__(self) -> None:
        pass

    def read(self,id,**kwargs):
        """search by id

        Args:
            id (int): query id 
        """
        params = {}

        if kwargs:
            params = kwargs

        url = f"{session.url}{self.endpoint}/{id}"
        session.query('get',url,params=params)
        

    def list(self,start,limit,**kwargs):
        """search multiples results and returns a list

        Args:
            start (int): initial position
            limit (int): list lenght (max 30)
        """

        url = f"{session.url}{self.endpoint}"
        params = {'start':start,
                'limit':limit,
                'order_direction':'ASC',
                'order_field':'id'
                }
 
        if kwargs:
            params.update(kwargs)

        session.query('get',url,params=params)
        

    def create(self,params):
        """send information to create in alegra

        Args:
            params (dict): data to create
        """

        url = f"{session.url}{self.endpoint}"
        session.query('post',url,params=params)
        

    def delete(self,id):
        """delete by id

        Args:
            id (int): query id 
        """

        url = f"{session.url}{self.endpoint}/{id}"
        session.query('get',url)
    
        

