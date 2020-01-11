#!/usr/bin/env python
# coding: utf-8

# Python Mega Assignment # 1

# 1. Which of the following terms are related to dictionaries?
# d. key
# 
# 2. Just like lists, + operator is used to extend dictionaries?
# b. False
# 
# 3. To access items from a dictionary, we specify the index of that item within [] like myDict[0]?
# a. True
# 
# 4. When we use [] to access the value from a dictionary which does not exist in that dictionary….?
# d. None of above
# 
# 5. What does return the pop method of a dictionary?
# d. value of the key, if it exists in the dictionary
# 
# 6. What does return popitem method return?
# b. tupple containing the pair of last item of the dictionary
# 
# 7. Which of the following 2 methods can be used to iterate through the items of a dictionary?
# a. items()
# d. keys()
# 
# 8. Which one of the following is used to enclose a dictionary?
# b. {} curly brackets

# In[2]:


# Q NO 9
#Write Python Program add key-value pair in dictionary and check if a 
#Given Key or Value or Both Exists in a Dictionary or Not.
d={'A':1,'B':2,'C':3}
key=raw_input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")


# In[8]:


# Q NO 10
X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[0:3] 
X[2:8]
X[4:9]
X[1:7:2]
X[-1:-7]
X[-7:7]
X[-1:-8:-2]
X[:4]


# In[9]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[2:8]


# In[10]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[4:9]


# In[11]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[1:7:2]


# In[12]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[-1:-7]


# In[13]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[-7:7]


# In[14]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[-1:-8:-2]


# In[15]:


X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]
X[:4]


# In[24]:


#Q NO 12
X = [9,2,8,4,5]
X.remove(9)


# In[25]:


# Q NO 13
p = 3
q = 'hello! '
print( q*p)


# In[26]:


# Q NO 14
y = "this is a random sentence"
print (y.upper())


# In[28]:


# Q NO 15
p = True
q = "True"
r = 2
s = 2.0
print(type(p))
print(type(q))
print(type(r))
print(type(s))


# In[ ]:


#Q NO 16
get_ipython().set_next_input(u'What are the optional arguments to the function');get_ipython().magic(u'pinfo function')
function_1(R1, q, p=None, R2= None)
2) p and R2


# In[ ]:


# Q NO 17
get_ipython().set_next_input(u'Which command invokes method X() of the object p');get_ipython().magic(u'pinfo p')
1) X(p)


# In[15]:


# Q NO 18
test_list = [[4, 1, 1], [5, 9, 0]]
for i in range(len(test_list)): 
    for x in test_list: 
        print(x[i]) 
    print() 


# In[21]:


# Q NO 19
tableData = [[4, 1, 1], [5, 9, 0]]
for v in zip(*tableData):
        print (*v)


# In[ ]:


# Q NO 20
tableData = [[4, 1, 1], [5, 9, 0]]
for i in range(2):
    e=name[i]
    f=speed[i]
    result=e + " was driving at " + f + "mph."
    print resul


# In[26]:


# Q NO 20
q = [10.62, 16.14, 6.45, 17.11]
for z in enumerate (q) :
    print( "Item" + str( j ) + "-", str ( z ))


# 21. Which of these about a dictionary is false?
# c) Dictionaries aren’t ordered

# In[34]:


# Q NO 22
D = dict()
for i in range (3):
    for j in range(2):
            D[i] = j
Ans: a. {0: 1, 1: 1, 2: 1}


# # Q No 23
# You are writing a function that increments player score in a soccer game
# If no value is specified for points, then point must start with 1
# If no value is specified for bonus, then bonus should be True
# 01 def increment_score ( bonus , score , points ):
# To meet the first requirement line 01 must be change to
# def increment_score ( bonus , score , points = 1 ): (True)
# To meet the second requirement line 01 must be change to
# def increment_score ( bonus = True , score , points = 1 ): (False)
# Once a parameter is defined with default value, any parameter to the right must also be defined with default values[True]

# In[37]:


# Q NO 24
def avg ( x , y , z = 50 ):
    adding = x + y + z
    avg_value = adding / 3
    return avg_value
y = avg ( x = 5 , y = 9 , z = 20 )
print(y)


# # Q NO 25
# def avg (opt_values , name ):
#     name = "Ali"
#     avg_value = sum (opt_values) / len(opt_values)
#     avg ( 5 , 9 , 20, 34, 87, 112 , "Ali" )
# print("name is:" + name + "Marks: " + str(avg_value))
# 

# # Q NO 26
# def display_result(winner, score,other_info):
#     print("The winner was " + winner)
#     print("The score was " + score)
# display_result(winner = "Manchester", score = "1-0", overtime = "yes", injuries = "none")
# 
# Function gets winner and score info 

# In[50]:


# Q NO 28
print("%06d"%123)


# In[51]:


# Q NO 29
print("%5.2f"%22.19)


# In[52]:


# Q NO 30
'{0:f}, {1:2f}, {2:05.2f}'.format(1.23456, 1.23456, 1.23456)


# # Q NO 31
# i = 1 # i assigned a value
# while False: # Checking the condition 
#     if i%2 == 0: # if given value is near zero
# break # stop iterations
#     print(i) # print the value
# i += 2 # adding the value for display

# # Q NO 32
# x = "abcdef"
# i = "a"
# while i in x:
#     x = x[:-1]
# 
# print(i)

# #Q NO 34
# for i in range(10):
#     if i == 5:
# else:
#     print(i)
# else:
#     print("Here")

# In[68]:


# Q NO 35
y = 6
z = lambda x: x * y
print z(8)


# In[74]:


# Q NO 36
i=0
def change(i):
    i=i+1
    return i

change(1) 
print(i)


# In[75]:


# Q NO 40
def change(one, *two):
    print(type(two))
    print(two)
change(1,2,3,4)


# In[76]:


# Q NO 41
def find(a, **b):
    print(type(b))
    
find('letters',A='1',B='2')


# In[81]:


# Q NO 42
def foo(i, x=[]):
    x.append(i)
    return x

for i in range(3):
        print(foo(i))


# In[ ]:


# Q NO 43
write which segment will execute first? 
Ans : (Brackets, Exponents, Multiplication, Addition / Subtraction, Left to right rule)


# In[ ]:


# Q NO 44
You are creating a function that manipulates a number. The function has the following requirements:
 A float is passed into the function
 The function must take the absolute value of the float
 Any decimal points after the integer must be removed

E. math.fabs(x)


# In[ ]:


# Q NO 45
45. You are writing code that generates a random integer with a minimum value of 5 and a maximum value of 11.
Which two functions should you use? Each correct answer presents a complete solution. (Choose two.)
A. random.randint(5, 12)

C. random.randrange(5, 12, 1)


# In[82]:


# Q NO 46
print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=0 and average<=40):
    	print("Your Grade is F");
    else:
    	print("Strange Grade..!!");


# In[ ]:




