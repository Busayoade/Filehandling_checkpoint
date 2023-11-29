#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1
f = open("C:/Users/oluwa/OneDrive/Desktop/GoMyCode/president_heights_party.csv")
print(f.read())


# In[7]:


# Question 2
# Open the file in read mode
with open("C:/Users/oluwa/OneDrive/Desktop/GoMyCode/president_heights_party.csv", 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

    # Get the last line using negative indexing (-1)
    last_line = lines[-1]

    # Print or do something with the last line
    print("Last line of the file:", last_line)


# In[8]:


#Question 3
with open("C:/Users/oluwa/OneDrive/Desktop/GoMyCode/president_heights_party.csv", 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

    # Get the last line using negative indexing (-1)
    First_line = lines[0]

    # Print or do something with the last line
    print("Last line of the file:", First_line)


# In[16]:


#Question 4
# creating variable to store the
# number of words
number_of_words = 0
 
# Opening our text file in read only
# mode using the open() function
with open("C:/Users/oluwa/OneDrive/Desktop/GoMyCode/president_heights_party.csv",'r') as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
 
    # Splitting the data into separate lines
    # using the split() function
    lines = data.split()
 
    # Iterating over every word in
    # lines
    for word in lines:
 
        # checking if the word is numeric or not
        if not word.isnumeric():          
 
            # Adding the length of the
            # lines in our number_of_words
            # variable
            number_of_words += 1
 
# Printing total number of words
print(number_of_words)


# In[ ]:




