class Product:
    """
    метод __init__ инициализирует обьект Product с двумя аргументами, 
 
    """
    sold_out = 'товара нет в налиции'
    def __init__(self, product: str, price: float):
        self.__product = product

        self.price = price 

        
   
    @property
    def product(self):
        return self.__product
    
    def __str__(self):
        return f"Наименование товара: {self.__product}, Цена товара: {self.price} "