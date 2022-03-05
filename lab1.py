#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# a.Number


# In[135]:


1 + 1


# In[3]:


1 * 3


# In[4]:


1 / 2


# In[5]:


2 ** 4


# In[6]:


4 % 2


# In[7]:


5 % 2


# In[136]:


(2 + 3) * (5 + 5)


# In[ ]:


# b.Variable assignment


# In[10]:


# Can not start with number of special characters
name_of_var = 2


# In[11]:


x = 2
y = 3


# In[12]:


z = x + y


# In[137]:


z


# In[ ]:


# c.Strings


# In[14]:


'single quotes'


# In[16]:


"double quotes"


# In[138]:


"wrap lot's of other quotes"


# In[ ]:


# d.Printing


# In[18]:


x = 'hello'


# In[19]:


x


# In[20]:


print(x)


# In[21]:


num = 12
name = 'Sam'


# In[23]:


print ('My number is: {one}, and my name is: {two}'.format(one=num, two=name))


# In[139]:


print ('My number is: {}, and my name is: {}'.format(num,name))


# In[ ]:


# e.Lists


# In[26]:


[1,2,3]


# In[27]:


['hi',1,[1,2]]


# In[28]:


my_list = ['a','b','c']


# In[29]:


my_list.append('d')


# In[30]:


my_list


# In[31]:


my_list[0]


# In[32]:


my_list[1]


# In[33]:


my_list[1:]


# In[34]:


my_list[:1]


# In[35]:


my_list[0] = 'NEW'


# In[36]:


my_list


# In[37]:


nest = [1,2,3,[4,5,['target']]]


# In[38]:


nest[3]


# In[39]:


nest[3][2]


# In[140]:


nest[3][2][0]


# In[ ]:


# f.Dictionaries


# In[41]:


d = {'key1':'item1','key2':'item2'}


# In[42]:


d


# In[141]:


d['key1']


# In[ ]:


# g.Booleans


# In[44]:


True


# In[142]:


False


# In[ ]:


# h.Tuples


# In[46]:


t = (1,2,3)


# In[47]:


t[0]


# In[143]:


t[0] = 'NEW'


# In[ ]:


# i.Sets


# In[49]:


{1,2,3}


# In[144]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[ ]:


# j.Comparison Operators


# In[51]:


1 > 2


# In[52]:


1 < 2


# In[53]:


1 >= 1


# In[54]:


1 <= 4


# In[55]:


1 == 1 


# In[145]:


'hi' == 'bye'


# In[ ]:


# k.Logic Operators


# In[57]:


(1 > 2) and (2 < 3)


# In[58]:


(1 > 2) or (2 < 3)


# In[146]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[ ]:


# l.if, elif, else statement


# In[60]:


if 1 < 2:
    print('Yep!')


# In[61]:


if 1 < 2:
    print('yep!')


# In[63]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[64]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[147]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else: 
    print('last')


# In[ ]:


# m.For loops


# In[66]:


seq = [1,2,3,4,5]


# In[67]:


for item in seq:
    print (item)


# In[68]:


for item in seq:
    print('Yep')


# In[148]:


for jelly in seq:
    print(jelly+jelly)


# In[ ]:


# n.While loops


# In[149]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i + 1


# In[ ]:


# o.Range


# In[71]:


range(5)


# In[72]:


for i in range(5):
    print(i)


# In[150]:


list(range(5))


# In[ ]:


# p.List Comprehension


# In[74]:


x = [1,2,3,4]


# In[75]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[151]:


[item**2 for item in x]


# In[ ]:


# q.Functions


# In[77]:


def my_func(param1 = 'default'):
    """
    Docstring goes here 
    """
    print(param1)


# In[78]:


my_func


# In[79]:


my_func()


# In[80]:


my_func('new params')


# In[81]:


my_func(param1='new params')


# In[82]:


def square(x):
    return x**2


# In[84]:


out = square(2)


# In[152]:


print(out)


# In[ ]:


# r.Lambda expression


# In[86]:


def times2(var):
    return var*2


# In[87]:


times2(2)


# In[153]:


lambda var: var*2


# In[ ]:


# s.Map and filter


# In[90]:


seq = [1,2,3,4,5]


# In[92]:


map(times2,seq)


# In[93]:


list(map(times2,seq))


# In[94]:


list(map(lambda var: var*2, seq))


# In[95]:


filter(lambda item: item%2 == 0, seq)


# In[154]:


list(filter(lambda item: item%2 == 0, seq))


# In[ ]:


# t.Methods


# In[97]:


st = 'hello my name is Sam'


# In[98]:


st.lower()


# In[99]:


st.upper()


# In[100]:


st.split()


# In[101]:


tweet = 'Go Sports! #Sports'


# In[102]:


tweet.split('#')


# In[103]:


tweet.split('#')[1]


# In[104]:


d


# In[105]:


d.keys()


# In[106]:


d.items()


# In[107]:


lst = [1,2,3]


# In[108]:


lst.pop()


# In[109]:


lst


# In[110]:


'x' in [1,2,3]


# In[155]:


'x' in ['x','y','z']


# In[ ]:


#What is 7 to power of 4?


# In[156]:


7 ** 4


# In[ ]:


#Split this string s = "Hi there Sam!"


# In[113]:


s = 'Hi there Sam!'


# In[157]:


s.split()


# In[ ]:


#Given the variables planet = 'Earth' and diameter = 12742. Use format() to printf the following string "The diameter of Earth is 12742 kilometers"


# In[115]:


planet = 'Earth'
diameter = 12742


# In[158]:


s = "The diameter of {0} is {1} kilometers".format(planet,diameter)
print(s)


# In[ ]:


#Given this nested list, use indexing to grab the word "hello"


# In[118]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[159]:


lst[3][1][2][0]


# In[ ]:


#Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky


# In[121]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[160]:


d['k1'][3]['tricky'][3]['target'][3]


# In[ ]:


#What is the main difference between a tuple and list?


# In[161]:


#Tuple is immutable


# In[162]:


#Create a function that grabs the email website domain from a string in the form:
#    user@domain.com
#So for example, passing "user@domain.com" would return domain.com


# In[124]:


def domainGet(email):
    return email.split('@')[1]


# In[163]:


domainGet('user@domain.com')


# In[ ]:


#Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation beging attached to th word dog, but do account for capitalization


# In[126]:


def findDog(str):
    if 'dog' in str.lower():
        return True
    return False


# In[164]:


findDog('Is there a dog here?')


# In[ ]:


#Create a function that counts the number of times the word 'dog' occurs in a string. Again ignore edge cases


# In[128]:


def countDog(str):
    count = 0
    for element in str.lower().split():
        if element == 'dog':
            count += 1
    return count


# In[165]:


countDog('This dog runs faster than the other dog dude!')


# In[ ]:


#Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:
#   seq = ['soup','dog','salad','cat','greate']
#should be filtered down to: 
#   ['soup', 'salad']


# In[130]:


seq = ['soup','dog','salad','cat','greate']


# In[166]:


list(filter(lambda element: element[0] == 's', seq))


# In[ ]:


#Final problem


# In[132]:


def caught_speeding(speed,is_birthday):
    status=''
    if is_birthday == False:
        if speed <= 60:
            status = 'No ticket'
        elif speed > 60 and speed <= 80:
            status = 'Small ticket'
        else:
            status = 'Big ticket'
    else:
        if speed <= 65:
            status = 'No ticket'
        elif speed > 65 and speed <= 85:
            status = 'Small ticket'
        else:
            status = 'Big ticket'
    return status


# In[133]:


caught_speeding(81, True)


# In[134]:


caught_speeding(81, False)


# In[ ]:




