


##popitem
def pop_item(dictinory1):
    return dictinory1.popitem()
dictinory1={1:'a',2:'b',3:'c'}
print("popitem",pop_item(dictinory1))

#setdefult
def set_defult(dictinory):
    dictinory.setdefault(4,'d')
    return dictinory
dictinory={1:'a',2:'b',3:'c'}
print("setdefult",set_defult(dictinory))

##clear()
def clear(dictinory):
    dictinory.clear()
    return dictinory
dictinory={1:'a',2:'b'}
print("clear",clear(dictinory))

##copy()
def copy(dictinory):
    new=dictinory.copy()
    return new
dictinory={1:'a',2:'b'}
print("copy",copy(dictinory))

##fromkey()
def from_key(dictinory):
    return dict.fromkeys(dictinory,None)
dictinory={1:'a',2:'b',3:'c'}
print("fromkey",from_key(dictinory))

##get()
def get(dictinory):
    return dictinory.get(1)
dictinory={1:'a',2:'b',3:'c'}
print("get",get(dictinory))

##items()
def items(i):
    return i.items()
i={1:'a',2:'b',3:'c'}
print("items",items(i))

##keys()
def keys(k):
    return k.keys()
k={1:'a',2:'b',3:'c'}
print("keys",keys(k))

##values()
def values(v):
    return v.values()
v={1:'a',2:'b',3:'c'}
print("values",values(v))

##pop()
def pop(p):
    p.pop(1)
    return p
p={1:'a',2:'b',3:'c'}
print("pop",pop(p))

##updat()
def update(u):
    (u).update(u2)
    return u
u={1:'a',2:'b',3:'c'}
u2={3:'a'}
print("updat",update(u))


































