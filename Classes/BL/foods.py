# --------------------- Food CLass ---------------------------- #
class Food():
        def __init__(self,food_name,food_price,food_img_path,food_description,food_rating):
                
                self.__food_name = food_name
                self.__food_price = food_price
                self.__food_description = food_description
                self.__food_img_path = food_img_path
                self.__food_rating = food_rating
                self.__food_likes = 0

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
        def food_likes(self)->int:
                return self.__food_likes

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

        @food_likes.setter
        def food_likes(self,food_likes:int)->None:
                self.__food_likes = food_likes
        
        
        # ------------------------ Methods ------------------------------ #
        def add_like_and_rate(self):
                self.__food_likes += 1
                if self.__food_likes > 2:
                        self.__food_rating += 1
                        self.__food_likes = 0
                if self.__food_rating > 5:
                        self.__food_rating = 5
                print("Thanks for liking the food")

        def remove_like_and_rate(self):
                self.__food_likes -= 1
                if int(self.__food_likes) < 0:
                        self.__food_rating -= 1
                        self.__food_likes = 3
                if int(self.__food_rating) < 0:
                        self.__food_rating = 0
                print("Sorry for disliking the food")


