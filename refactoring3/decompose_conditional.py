# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    print('made alert sound.')
def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')
    print('made acceptance sound')

def contains_toxins(ingredients):
    return 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients\
            or 'sodium oxide' in ingredients

ingredients = ['sodium benzoate']
if contains_toxins(ingredients):
    make_alert_sound()
else:
    make_accept_sound()
