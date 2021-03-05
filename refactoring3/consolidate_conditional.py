# by Kami Bigdely
# Consolidate conditional expressions
SHIRAZI_SALAD_INGREDIENTS = ['cucumber', 'tomato', 'onion', 'lemon juice']

def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)
def has_required_ingredients(ingredients, required):
    for item in required:
        if item not in ingredients:
            return False
    return True

def make_shirazi_salad(ingredients):
    if not has_required_ingredients(ingredients, SHIRAZI_SALAD_INGREDIENTS):
        print('lacks ingredients.')
        return 
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
