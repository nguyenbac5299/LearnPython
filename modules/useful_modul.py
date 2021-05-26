from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li=[1,1,2,3,4,5,5]
sentence='bac ba'
print(Counter(li))
print(Counter(sentence))

dic=defaultdict(lambda : 'item not exit',{'a':3,'b':4})
print(dic['c'])
print(dic['a'])


d1=OrderedDict()
d1['a']=2
d1['b']=3

d2=OrderedDict()
d2['b']=3
d2['a']=2


print(d1==d2) # if is dictionary return true because dictionary not orderd


# time
print(datetime.time(10,2,3))
print(datetime.date.today())


# array
arr=array('i',[1,2,3,4])
print(arr)
print(arr[0])


