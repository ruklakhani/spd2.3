# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class pizza:
    def __init__ (obj, mybread_type, cheese_type, meat_type, pizza_toppings, size):
        obj.bread_type= mybread_type
        obj.cheese_type = cheese_type
        obj.meat_type= meat_type
        obj.toppings = pizza_toppings
        obj.size = size        
    @classmethod
    def create_chicago_pizza (class_type, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return class_type (bread, cheese, meat_type, toppings, size)    
    @classmethod
    def create_california_pizza(ct, meat_type,size):
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings =['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return ct(bread, cheese, meat_type, toppings, size) 
    def print_info(obj):
        print('bread type is: ', obj.bread_type)
        print('cheese type is: ', obj.cheese_type)
        print('meat type is: ', obj.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, obj.toppings)))

    
my_pizza = pizza.create_california_pizza('chicken', 'large')
my_pizza.print_info()