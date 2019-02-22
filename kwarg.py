def test1():    
    a = {}
    
    a['t1'] = 11
    a['t2'] = 12
    a['t3'] = 13
    a['t4'] = 14
    a['t5'] = 15
    
    test2(**a)
    
    
def test2(t1, t2, t3, t5, t):
    print('t1 {0} t2 {1} t3 {2} t4 {3} t5 {4}'.format(t1, t2, t3, t4, t5))

print(test1())
