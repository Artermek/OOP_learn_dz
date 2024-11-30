from classes.product import Product
from classes.discount import Discount
from classes.order import Order
from classes.customer import Customer

iphone = Product ("iphone", 1000)
laptop = Product ("mac", 1500)
display = Product ("Samsung", 700)

print (iphone.price)
print (laptop)

print ('______________________\n')

order1 = Order([iphone])
order2 = Order([iphone, laptop])
order3 = Order ([iphone, laptop, display])
print (order1)
print (order2)
print(order1.total_price()) 

print ('______________________\n')

client1  = Customer ('John', order2.product_str, order2.price_str)
print (client1)
client2 = Customer ('Pedri', order3.product_str, order3.price_str)
print (client2)

print ('______________________\n')

discounted_price = Discount.winter_discounted_price(order2.total_price())
discounted_price = Discount.game_discounted_price(order3.total_price())

print ('______________________\n')

print(f"Всего заказов: {Order.total_orders()}") 
print(f"Всего заказов: {Order._total_prices}")