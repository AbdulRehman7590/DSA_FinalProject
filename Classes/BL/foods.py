# --------------------- Food CLass ---------------------------- #
class Food():
        def __init__(self,food_name,food_price,food_img_path,food_description,food_rating):
                
                self.__food_name = food_name
                self.__food_price = food_price
                self.__food_description = food_description
                self.__food_img_path = food_img_path
                self.__food_rating = food_rating
                self.__likes = 0

        # ------------------------ Getter ------------------------------ #
        @property
        def food_name(self)->str:
                return self.__food_name
        
        @property
        def food_price(self)->str:
                return self.__food_price
        
        @property
        def food_img_path(self)->str:
                return self.__food_img_path
        
        @property
        def food_description(self)->str:
                return self.__food_description
        
        @property
        def food_rating(self)->int:
                return self.__food_rating
        
        @property
        def likes(self)->int:
                return self.__likes

        # ------------------------ Setter ------------------------------ #
        @food_name.setter
        def food_name(self,food_name:str)->None:
                self.__food_name = food_name
        
        @food_price.setter
        def food_price(self,food_price:str)->None:
                self.__food_price = food_price
        
        @food_img_path.setter
        def food_img_path(self,food_img_path:str)->None:
                self.__food_img_path = food_img_path
        
        @food_description.setter
        def food_description(self,food_description:str)->None:
                self.__food_description = food_description


        # ------------------------ Methods ------------------------------ #
        def set_like_and_rate(self):
                self.__likes += 1
                if self.__likes > 2:
                        self.__food_rating += 1
                        self.__likes = 0
                if self.__food_rating > 5:
                        self.__food_rating = 5


