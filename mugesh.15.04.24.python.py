##sorting


##def sorting(s):
##    n=dict(sorted(s.items()))
##    print(n)
##    
##s={1:'a',4:'b',3:'c'}
##sorting(s)




##key sorting


def keys_sorting(ks):
    key=ks.keys()
    sortt=dict(sorted(key.items()))
    return sortt
ks={1:'a',4:'b',3:'c'}
print(keys_sorting(ks))
