
# coding: utf-8

# # Strings
# 
# ## We can do things with strings
# 
# We've already seen  in Data 8 some operations that can be done with strings.

# In[ ]:


first_name = "Franz"
last_name = "Kafka"
full_name = first_name + last_name
print(full_name)


# Remember that computers don't understand context.

# In[ ]:


full_name = first_name + " " + last_name
print(full_name)


# ## Strings are made up of sub-strings
# 
# You can think of strings as a [sequence](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#sequence) of smaller strings or characters. We can access a piece of that sequence using square brackets `[]`.

# In[ ]:


full_name[1]


# <div class="alert alert-danger">
# Don't forget, Python (and many other langauges) start counting from 0.
# </div>

# In[ ]:


full_name[0]


# In[ ]:


full_name[4]


# ## You can slice strings using  `[ : ]`
# 
# If you want a range (or "slice") of a sequence, you get everything *before* the second index, i.e,. Python slicing is *exclusive*:

# In[ ]:


full_name[0:4]


# In[ ]:


full_name[0:5]


# You can see some of the logic for this when we consider implicit indices.

# In[ ]:


full_name[:5]


# In[ ]:


full_name[5:]


# If we want to find out how long a string is, we can use the `len` function:

# In[ ]:


len(full_name)


# ## Strings have methods
# 
# * There are other operations defined on string data. These are called **string [methods](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#method)**. 
# * The Jupyter Notebooks lets you do tab-completion after a dot ('.') to see what methods an [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) (i.e., a defined variable) has to offer. Try it now!

# In[ ]:


str.


# Let's look at the `upper` method. What does it do? Let's take a look at the documentation. Jupyter Notebooks let us do this with a question mark ('?') before *or* after an object (again, a defined variable).

# In[ ]:


get_ipython().run_line_magic('pinfo', 'str.upper')


# So we can use it to upper-caseify a string. 

# In[ ]:


full_name.upper()


# You have to use the parenthesis at the end because upper is a method of the string class.
# <p></p>
# <div class="alert alert-danger">
# Don't forget, simply calling the method does not change the original variable, you must *reassign* the variable:
# </div>

# In[ ]:


print(full_name)


# In[ ]:


full_name = full_name.upper()
print(full_name)


# For what it's worth, you don't need to have a variable to use the `upper()` method, you could use it on the string itself.

# In[ ]:


"Franz Kafka".upper()


# What do you think should happen when you take upper of an int?  What about a string representation of an int?

# In[ ]:


1.upper()


# In[ ]:


"1".upper()


# ## Challenge 1: Write your name
# 
# 1. Make two string variables, one with your first name and one with your last name.
# 2. Concatenate both strings to form your full name and [assign](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#assign) it to a variable.
# 3. Assign a new variable that has your full name in all upper case.
# 4. Slice that string to get your first name again.

# In[ ]:


first_name = "Elizabeth"
last_name = "Fraysse"
full_name = first_name + last_name
print(full_name)


# In[ ]:


full_name.upper()


# In[ ]:


full_name.split()


# ## Challenge 2: Try seeing what the following string methods do:
# 
#     * `split`
#     * `join`
#     * `replace`
#     * `strip`
#     * `find`

# In[107]:


my_string = "It was a Sunday morning at the height of spring."


# In[108]:


my_string.split()


# In[109]:


"-".join(my_string)


# In[110]:


my_string.replace("Sunday", "Monday")


# In[111]:


my_string.strip(".")


# In[112]:


my_string.find(".")


# ## Challenge 3: Working with strings

# Below is a string of Edgar Allen Poe's "A Dream Within a Dream":

# In[113]:


poem = '''Take this kiss upon the brow!
And, in parting from you now,
Thus much let me avow —
You are not wrong, who deem
That my days have been a dream;
Yet if hope has flown away
In a night, or in a day,
In a vision, or in none,
Is it therefore the less gone?  
All that we see or seem
Is but a dream within a dream.

I stand amid the roar
Of a surf-tormented shore,
And I hold within my hand
Grains of the golden sand —
How few! yet how they creep
Through my fingers to the deep,
While I weep — while I weep!
O God! Can I not grasp 
Them with a tighter clasp?
O God! can I not save
One from the pitiless wave?
Is all that we see or seem
But a dream within a dream?'''


# What is the difference between `poem.strip("?")` and `poem.replace("?", "")` ?

# In[114]:


poem.strip("?")


# In[115]:


poem.replace("?", "")


# At what index does the word "*and*" first appear? Where does it last appear?

# The two lines are exactly the same and the two functions create the same thing.  

# How can you answer the above accounting for upper- and lowercase?

# You could change the contents of the string to account for only upper or lower case.

# ## Challenge 4: Counting Text

# Below is a string of Robert Frost's "The Road Not Taken":

# In[ ]:


poem = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.'''


# Using the `len` function and the string methods, answer the following questions:
# 
# How many characters (letters) are in the poem?

# In[116]:


poem.


# In[117]:


poem.upper()


# In[118]:


poem.find('A')


# In[119]:


poem.find('B')


# In[120]:


poem.find('C')


# In[121]:


poem.find('D')


# In[122]:


poem.find('E')


# In[123]:


poem.find('F')


# In[124]:


poem.find('G')


# In[125]:


poem.find('H')


# In[126]:


poem.find('I')


# In[127]:


poem.find('J')


# In[128]:


poem.find('K')


# In[129]:


poem.find('L')


# In[130]:


poem.find('M')


# In[131]:


poem.find('N')


# In[132]:


poem.find('O')


# In[133]:


poem.find('P')


# In[134]:


poem.find('Q')


# In[135]:


poem.find('R')


# In[136]:


poem.find('S')


# In[137]:


poem.find('T')


# In[138]:


poem.find('U')


# In[139]:


poem.find('V')


# In[140]:


poem.find('W')


# In[141]:


poem.find('X')


# In[142]:


poem.find('Y')


# In[143]:


poem.find('Z')


# 2201

# `split`
# * `join`
# * `replace`
# * `strip`
# * `find

# In[ ]:





# How many words?

# In[144]:


x= str("Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth; Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same, And both that morning equally lay In leaves no step had trodden black. Oh, I kept the first for another day! Yet knowing how way leads on to way, I doubted if I should ever come back. I shall be telling this with a sigh Somewhere ages and ages hence: Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference.")
print(x)
words= x.split()
number_of_words= len(words)
print(number_of_words)


# How many lines? (HINT: A line break is represented as  `\n`  )

# In[145]:


poem.count("\n")


# How many stanzas?

# In[146]:


x= poem.count("\n")/5
round(x)


# How many unique words? (HINT: look up what a `set` is)

# In[147]:


sorted([(w, poem[w]) for w in poem.keys()], key=lambda i: i[1], reverse=True)


# Remove commas and check the number of unique words again. Why is it different?

# In[148]:


sorted([(w, poem[w]) for w in words.keys()], key=lambda i: i[1], reverse=True)

