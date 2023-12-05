# ------------------------ Libraries ------------------------------- #
import typing

# ------------------------ User CLass ------------------------------ #
class User:
    def __init__(self,username:str ,email: str ,password: str,address: str ) -> None:
        self.__username = username
        self.__email = email
        self.__password = password
        self.__address = address
    
    # ------------------------ Getter ------------------------------ #
    @property
    def username(self)->str:
        return self.__username
    
    @property
    def email(self)->str:
        return self.__email
    
    @property
    def password(self)->str:
        return self.__password
    
    @property
    def address(self)->str:
        return self.__address
    
    # ------------------------ Setter ------------------------------ #
    @username.setter 
    def username(self, username: str)->None:
        self.__username = username

    @email.setter    
    def email(self, email :str) ->None:
        self.__email = email

    @password.setter    
    def password(self, password :str) ->None:
        self.__password = password

    @address.setter    
    def address(self, address : str)->None:
        self.__address = address


    # ------------------------ Methods ------------------------------ #
    def view_profile(self)->str:
        return f"Username: {self.__username}\nEmail: {self.__email}\nAddress: {self.__address}"


