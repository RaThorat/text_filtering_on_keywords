#importing necessary modules
import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=YOUR SERVER;'
                      'Database=YOUR DATABASE;'
                      'Trusted_Connection=yes;')


df = pd.read_sql_query('YOUR QUERY', conn)

df.columns

df.shape
#joining all words together from columns title, summary and keywords to create a corpus
df["Corpus"] = df["Title"] +" "+ df["Summary"] +" "+ df["Keywords"]


#dropping the nan values from summary 
df = df[df['Corpus'].notna()]
#dropping the punctuation from summary 
import string
string.punctuation
def remove_punctuation(txt):
    txt_nopunct ="".join([c for c in txt if c not in string.punctuation])
    return txt_nopunct
df['Corpus_clean']=df['Corpus'].apply(lambda x: remove_punctuation(x))
#tokenization
import re
def tokenize(txt):
    tokens= re.split('\W+', txt)
    return tokens
df['Corpus_clean_tokenized']=df['Corpus_clean'].apply(lambda x:tokenize(x.lower()))
#removing the stopwords
from nltk.corpus import stopwords
stop_words=stopwords.words('english')
df['Corpus_nostop']=df['Corpus_clean_tokenized'].apply(lambda x: [item for item in x if item not in stop_words])
#lemmatization
import nltk
#nltk.download('wordnet')
wn=nltk.WordNetLemmatizer()
def lemmatization(token_text):
    text= [wn.lemmatize(word) for word in token_text]
    return text
df['Corpus_lemmatized']=df['Corpus_nostop'].apply(lambda x: lemmatization(x))


#list from where words to search for


main_list = ['YOUR KEYWORD1', 'YOUR KEYWORD2']
print(main_list)


# In[86]:


#upper casing and lower casing of words
main_list_upper = [each_string.upper() for each_string in main_list]
main_list_lower= [each_string.lower() for each_string in main_list]


# In[87]:


#combining all the formats of the words to search for
main_list_1=main_list+main_list_upper+main_list_lower


# In[88]:


#filtering rows on the basis of words
df['Corpus_lemmatized_filter']=df['Corpus_lemmatized'].apply(lambda x: [item for item in x if item in main_list_1])


# In[89]:


df.shape


# In[90]:


df.head()


# In[91]:


#dropping the rows on the condition of the column 'Corpus_lemmatized_filter', which do not contain any of the words searched for.
df1 = df[df['Corpus_lemmatized_filter'].map(lambda d: len(d)) > 0]


# In[92]:


#check the dataframe
df1.head()


# In[93]:


#shape of the dataframe check
df1.shape


# In[94]:


df1 = df1.rename(columns={ 'Corpus_lemmatized_filter':'found words'})


# In[96]:

#save file to excel
df1.to_excel('filtering text on keywords.xlsx')