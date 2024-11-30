class Order:
    """ Класс `Order` определяет объект заказа, который содержит информацию о
    продуктах, их цене и количестве. Давайте разберем каждый метод класса:
    
    1. `__init__(self, products)`: Этот метод инициализирует объект заказа. 
    Он принимает список продуктов и увеличивает общее количество заказов на 1. 
    
    2. `total_orders(cls)`: Этот метод класса возвращает общее количество заказов.
    Он использует классовую переменную `_total_orders`, чтобы хранить количество заказов.
    
    3. `total_price(self)`: Этот метод вычисляет общую цену заказа. Он суммирует 
    цены всех продуктов в заказе.
    
    4. `all_products(self)`: Этот метод возвращает количество всех продуктов в заказе.
    
    5. `__str__(self)`: Этот метод возвращает строковое представление объекта заказа. 
    Он выводит общую цену заказа и количество продуктов.

    """
    _total_orders = 0
    _total_prices = 0
    
    def __init__(self, products):
        self.products = products
        Order._total_orders += 1
        
    
    @classmethod
    def total_orders (cls):
        return cls._total_orders
    
    def total_price (self):
        Order._total_prices += sum(product.price for product in self.products)
        return sum(product.price for product in self.products)
    
    def all_products (self):
        return [product.product for product in self.products]
      
    def all_prices (self):
        return [product.price for product in self.products]
    
    def product_str (self):
        product_str = ", ".join(self.all_products())   
        return product_str
    
    def price_str(self):
        total_price = sum (self.all_prices())
        return total_price
    
    def __str__ (self):
        return f"Заказ (Общая цена = {self.total_price()}, продукты: {self.product_str()})"
    