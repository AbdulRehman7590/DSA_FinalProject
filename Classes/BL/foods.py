# ------------------------ Libraries ------------------------------- #
import typing

# --------------------- Food CLass ---------------------------- #
class Food():
        def __init__(self,food_name,food_price,food_description,food_id):
                
                self.__food_rating = []
                self.__food_id = food_id
                self.__food_name = food_name
                self.__food_price = food_price
                self.__food_description = food_description

        # ------------------------ Getter ------------------------------ #
        @property
        def food_name(self)->str:
                return self.__food_name
        
        @property
        def food_price(self)->str:
                return self.__food_price
        
        @property
        def food_description(self)->str:
                return self.__food_description
        
        @property
        def food_id(self)->str:
                return self.__food_id
        
        @property
        def food_rating(self)->int:
                return sum(self.__food_rating)/len(self.__food_rating)

        # ------------------------ Setter ------------------------------ #
        @food_name.setter
        def food_name(self,food_name:str)->None:
                self.__food_name = food_name
        
        @food_price.setter
        def food_price(self,food_price:str)->None:
                self.__food_price = food_price
        
        @food_description.setter
        def food_description(self,food_description:str)->None:
                self.__food_description = food_description
        
        @food_id.setter
        def food_id(self,food_id:str)->None:
                self.__food_id = food_id


        # ------------------------ Methods ------------------------------ #
        def add_rating(self,rating:int)->None:
                self.__food_rating.append(rating)

