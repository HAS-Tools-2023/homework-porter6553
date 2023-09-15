#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)
print(x)
# 1.1 What is the length of x?
print(len(x))
# Comprehension question is this an attribute or a method or a function of x? How do we know?
## Function because it is a python built in function
#%%
# 1.2 Get the first value out of x and print it: 
print(x[0])
#%%
# 1.3. Get the last value out of x and print it?
print(x[26])
##OR
print(x[-1])
## OR
print(x[x.size-1])
#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?
## Need to do Slicing (function)
print(x[:5]) #Everything to 5 but not including 5 since it starts at 0
print(x[22:]) #Everything after 22
## OR if you don't know length of array
array_length = len(x)
print(x[(array_length - 5):])
## OR
print(x[(x.size-5):])

# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
print(x[0:9])
y = x[0:9].reshape(3,3)
print(y)

#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 
## Method
#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])
print(y[1,1])
#%%
# 2.3. Get the first row out of y and print it?
print(y[0,:])
# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 
## Array
#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)
print(y[:,0].size)
# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get its size (i.e. with two lines of code). And next where you combine thos commands into one line of code
a = y[:,0]
print(a.size)
#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns that has values 0-9
b = np.arange(6)
print(b)
b.reshape(3,2)

# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 
c = np.ones((4,4))
print(c)
# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   (Hint: you could do this with either addition or multiplication)
print(c*4)
#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))
print(z)
# 4.1 Use 'sum' to print the total of z
print(np.sum(z))
#Comprehension question -- is 'sum' a function a method or an attribute?  
## Sum is an attribute because it belongs to the package numpy
#%%
# 4.2. Print the sum along the first dimension of z?
print(np.sum(z[0,:]))
## Comprehension question -- is the 'first dimension' the rows or the columns of z? 
## The first dimension is the first row

# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numbered did you get back?)
print(z[0,:].size)
# How does this compare to the shape of z? 
print(z.size)
# %%
