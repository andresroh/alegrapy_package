from alegra.session import session

class actions:

    endpoint = ""

    def __init__(self) -> None:
        pass

    def read(self,id):
        """search by id

        Args:
            id (int): query id 
        """
        url = f"{session.url}{self.endpoint}/{id}"
        session.query('get',url)
        

    def list(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass
        

