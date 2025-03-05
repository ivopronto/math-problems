import random 
def rand_math(a,b): 
    """Generate a random math problem in the format of a + b""" 
    op = random.choice(['+','-','*','/']) 
    if op == '/': 
        return str(random.randint(1,10))+' / '+str(random.randint(2,5)) 
    else: 
        return str(random.randint(1,10))+' '+op+' '+str(random.randint(2,5))