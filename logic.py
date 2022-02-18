from xmlrpc.client import boolean


def bekes_allapot(allapot:dict) -> boolean:
    # ide ird a kodod, terjen vissza True-val, ha bekes az allapot, es False-szal, ha nem.
    pass


print( bekes_allapot({'bal':['F','f','f','D','d','d','R','r'], 'jobb':[], 'csonak_bal':True}) ) # True
print( bekes_allapot({'bal':['D','d','F','f','f','d','R','r'], 'jobb':[], 'csonak_bal':True}) ) # True
print( bekes_allapot({'bal':[], 'jobb':['D','d','F','f','f','d','R','r'], 'csonak_bal':True}) ) # True
print( bekes_allapot({'bal':['D','d','F','f','f','d','r'], 'jobb':['R'], 'csonak_bal':False}) ) # False
print( bekes_allapot({'bal':['F','f','f','d','R','r'], 'jobb':['D','d'], 'csonak_bal':True}) ) # False
print( bekes_allapot({'bal':['F','f','f','D','d','d','R'], 'jobb':['r'], 'csonak_bal':True}) ) # True




