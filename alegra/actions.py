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

        url = f"{session.url}{self.endpoint}"
        print(url)
        params = {'start':start,
                'limit':limit,
                'order_direction':'ASC',
                'order_field':'id'
                }
        print(params)
        if kwargs:
            params.update(kwargs)

        session.query('get',url,params=params)
        

    def create(self):
        pass

    def delete(self):
        pass
        

