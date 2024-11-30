class Customer:
    
    def __init__ (self, name_customer: str, orders, cust_prices):
        self.name_customer = name_customer
        self.orders = orders
        self.cust_prices = cust_prices


    
    def __str__(self):
        return f"Клиент: {self.name_customer}, список заказов: {self.orders()}, на сумму: {self.cust_prices()} "
    

