''''''
'''
Dictionaries:
list:       mutable
tuple:      immutable
set:        mutable + unique
dictinory:  mutable 
'''
list = [12, 'cp', 34.5, 5678,]

list.append('test')                     # add
list.remove(12)                         # remove
list.insert(0,'element')                # insert at index
list.pop(1)                             # remove at index
list.clear()                            # empty
list.reverse()                          # reverse list
list.count(12)                          # count of element
new_list = list.copy()                  # shallow copy list



tuple = (12, 'hello world!', 'cp', 34.5, 5678)

tuple.count(12)                         # count of element
tuple.index('cp')                       # index of element

set = {12, 12, 'cp', 34.5, 5678}

set.add('hello')                        # add
set.remove('cp')                        # remove
set2 = set.copy()                       # shallow copy
set.clear()                             # empty set


dictionary = {'name': 'cp', 'age': 27, 'state': 'MH', 'city': 'mumbai'}

dictionary['surname'] = 'chaurasiya'    # add
del(dictionary['age'])                  # delete
dictionary.get('name')                  # get
dictionary['name']                      # get


'''
range:
      from, before
 range( 1,   10)
 
range :     strong evaluation (more memory)
xrange:     lazy evaluation   (less memory)

.........................................

Operators
Arithmatic :    +  -   *   /
Comparision:    <   >   <=  >=  ==  !=
Bitwise:        |   & ~ ^   <<
Logical:        and     or
Membership:     in
Identity:       is
.........................................
Single program is called as module.
Folder of programs is called as package.
.........................................

copy
shallow : effects other after copy
deep: do not effects other after copy
.......................................
first class object:
In python we can pass function as an object.

.......................................

Types of arguments:

position :                          def test(x,y)
default:                            def test(x=0,y=None)
variable length:                    def test(*values)
keword variable length argument:    def test(**values)

........................................

Array:
from array import *
arr = array('i', [1,2,3,4'])


'''