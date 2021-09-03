EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    '''
    docstring
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    '''
    docstring
    '''
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    '''
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time
