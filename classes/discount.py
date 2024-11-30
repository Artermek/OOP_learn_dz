    
class Discount:
    winter_discounted = 10
    winter_discounted_description = 'Новогодняя скидка 10%!'
    game_discounted = 25
    game_discounted_description = 'Скидка для настоящих геймеров 25%!'    
    @staticmethod
    def winter_discounted_price(price):
        print (Discount.winter_discounted_description)
        print (price * (1 - Discount.winter_discounted / 100))
    @staticmethod
    def game_discounted_price(price):
        print (Discount.game_discounted_description)
        print (price * (1 - Discount.game_discounted / 100))    
        
        
    @staticmethod
    def calculate_discounted_price(price, discount):
        return price * (1 - discount / 100)