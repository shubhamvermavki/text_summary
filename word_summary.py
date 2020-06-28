#!/usr/bin/env python
# coding: utf-8

# In[28]:


mylines = []                             # Declare an empty list named mylines.
with open ('ann.txt', 'rt') as myfile: # Open .txt for reading text data.
    for myline in myfile:                # For each line, stored as myline,
        mylines.append(myline)           # add its contents to mylines.
print(mylines)


# In[29]:


#extracting line using keyword
usr_input = input("Enter your keyword word:")
temp_string = ''
for i in mylines:
    if usr_input in i.lower():
        temp_string += ' '+i


# In[30]:


text= " "
text = text+temp_string
print(text)
  


# In[31]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# In[32]:


stopwords= list(STOP_WORDS)


# In[33]:


nlp = spacy.load('en_core_web_sm')


# In[34]:


doc = nlp (text)    #tokenization


# In[35]:


# create list of token
tokens = [token.text for token in doc]


# In[36]:


#remove stop words as well as punctuation
punctuation = punctuation + '\n'


# In[37]:


#cteare word frequency |
word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text]+=1


# In[38]:


max_freq = max(word_freq.values())


# In[39]:


#nornalize frequency of each of the word present in text data
for word in word_freq.keys():
    word_freq[word] =word_freq[word]/max_freq


# In[40]:


#sentence tokenization
sentence_tokens = [sent for sent in doc.sents]


# In[41]:


#calculate sentence scores
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sentence_scores .keys():
                sentence_scores[sent] = word_freq[word.text.lower()]
            else:
                sentence_scores[sent] += word_freq[word.text.lower()]


# In[42]:


#getting 30% of the sentence with maximum score
from heapq import nlargest


# In[43]:


select_len = int(len(sentence_tokens)*0.3) 
#select_len


# In[44]:


summary = nlargest(select_len, sentence_scores, key=sentence_scores.get)


# In[45]:


#combining sentences together
final_summary = [word.text for word in summary] #final summary is a list


# In[46]:


summary = ''.join(final_summary) #converting list to a single paragraph


# In[47]:


summary


# In[ ]:




