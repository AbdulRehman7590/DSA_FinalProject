from Users import User
class Customers(User):
        def __init__(self,username,email,password,address):
                super().__init__(username, email, password, address)

