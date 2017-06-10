
# coding: utf-8

# In[1]:

url='http://www.dayonecapital.com/blog/'


# In[2]:

from bs4 import BeautifulSoup
import urllib
import urllib.request
import warnings
warnings.filterwarnings('ignore')
 
blog_url=url


# In[3]:

html=urllib.request.urlopen(url).read()
html=html.decode('utf8')
soup=html
blog_url=url
soup = BeautifulSoup(html, 'html.parser')


# In[4]:

blog_url


# In[5]:

scriptTags = soup.findAll('h1' )
print(len(scriptTags))
 
 


# In[6]:

blof_dayone=[]
for     tag in range(1,len(scriptTags)):
    url=scriptTags[tag]
    href=url.findAll('a')[0]['href']
    title=url.text
    link=href
    html=urllib.request.urlopen(link).read()
    html=html.decode('utf8')
    soup=html
    #blog_url=url
    soup = BeautifulSoup(html, 'html.parser')
    author=soup.findAll('p')[0].text[2:]
    date=soup.findAll('ul',attrs={'class':'info'})[0]
    data=date.findAll('li')[1].text[3:]
    author=date.findAll('li')[0].text[9:]
    corpus=''
    corp=soup.findAll('p')
    for  txt in  range(2,len(corp)-2):
        corpus=corpus+corp[txt].text
    blof_dayone.append((blog_url ,data,title,author,corpus))
    
    
  


# In[7]:

blog_dayone=blof_dayone
 


# In[8]:

blog_url


# In[9]:

#########################################################################################################


# In[10]:

url='http://www.garage.com/blog/'


# In[11]:

from bs4 import BeautifulSoup
import urllib
import urllib.request
import warnings
warnings.filterwarnings('ignore')
 
blog_url=url


# In[12]:

import requests
from bs4 import  BeautifulSoup
r = requests.get(url)
html=r.text
soup = BeautifulSoup(html, 'html.parser')


# In[13]:

h=soup.findAll('h2')
 


# In[14]:

h[0].findAll('a')[0]['href']


# In[15]:

h[0].text


# In[16]:

authors=[]
auth=soup.findAll('a',attrs={'rel':'author'})
for i in range(len(auth)):
    authors.append(auth[i].text)


# In[17]:

dates=[]
date=soup.findAll('div',attrs={'class':'fusion-alignleft'})
for i in   range(len(date)):
    dates.append(date[i].findAll('span')[2].text)


# In[18]:

blog_garage=[]


# In[19]:

for  i in range(len(h)):
       data=dates[i]
       author=authors[i]
       url=h[i].findAll('a')[0]['href']
       title=h[i].text
       r = requests.get(url)
       html=r.text
       soup = BeautifulSoup(html, 'html.parser')
       corpus=''
       corp=soup.findAll('p')
       for txt in  range(2,len(corp)):
           corpus=corpus+corp[txt].text
       blog_garage.append((blog_url ,data,title,author,corpus))


# In[21]:

###############################################################################################################


# In[93]:

url='https://pmeenan.com'
blog_url=url
file=open('/media/cc/A80C461E0C45E7C0/scrap/pmen.txt',encoding = "ISO-8859-1")
data=file.read()


# In[94]:

soup = BeautifulSoup(data, 'html.parser')
 


# In[95]:

tags=soup.findAll('a',attrs={'rel':'bookmark'})
 


# In[105]:

blog_pmen=[]
for  tag in  range(len(tags)):
    url=tags[tag]['href']
    title=tags[tag].text
    author='Patrick Meenan'
    html=urllib.request.urlopen(url).read()
    html=html.decode('utf8')
    soup=html
 
    soup = BeautifulSoup(html, 'html.parser')
    data=soup.findAll('time')[0].text
    corpus=''
    corp=soup.findAll('p')
    for txt in range(len(corp)-5) :
        content=corp[txt].text
        corpus=corpus+content
    corpus=corpus.replace('\xa0','')
        
    blog_pmen.append((blog_url ,data,title,author,corpus))
    
    


# In[ ]:




# In[ ]:




# In[230]:

##############################################################################################################


# In[143]:

url='http://www.joshhannah.com'


# In[144]:

from bs4 import BeautifulSoup
import urllib
import urllib.request
import warnings
warnings.filterwarnings('ignore')
 
blog_url=url


# In[145]:

import requests
from bs4 import  BeautifulSoup
r = requests.get(url)
html=r.text
soup = BeautifulSoup(html, 'html.parser')


# In[146]:

tags=soup.findAll('h4')


# In[147]:

len(tags) 


# In[ ]:




# In[148]:

blog_josh=[]
for i  in range(len(tags)):
    title=tags[i].text
    url=tags[i].findAll('a')[0]['href']
    data=url.split('/')[3]+'-'+url.split('/')[4]
    author='Josh Hannah '
    r = requests.get(url)
    html=r.text
    soup = BeautifulSoup(html, 'html.parser')
    corpus=''
    corp=soup.findAll('p',attrs={'id':True})
    for txt in range(len(corp)-2):
        corpus=corpus+corp[txt].text
    blog_josh.append((blog_url ,data,title,author,corpus))
    
    
    
 


# In[152]:

##############################################################################################################
len(blog_josh)


# In[151]:

import  pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['partial_blogs']
collection = db['partial_blogs']


# In[153]:

for post in range(len(blog_josh)):
    
 
 
    document={"blog_name":blog_josh[post][0],
              'post_date':blog_josh[post][1],
              'Title':blog_josh[post][2],
              'Author':blog_josh[post][3],
              'corpus':blog_josh[post][4]}
 
    db.partial_blogs.update_one({"Title":blog_josh[post][2],
                                 "blog_name":blog_josh[post][0],
                                 "post_date":blog_josh[post][1],
                                 "Author":blog_josh[post][3],
                                 "corpus":blog_josh[post][4],
                                 
                                },
                                
                                
                                {"$set":
                                 {"Title":blog_josh[post][2],
                                  "blog_name":blog_josh[post][0],
                                  "post_date":blog_josh[post][1],
                                  "Author":blog_josh[post][3],
                                  "corpus":blog_josh[post][4],
                                  
                                 }
                                }, 
                                upsert=True)
    


# In[154]:

for post in range(len(blog_pmen)):
    
 
 
    document={"blog_name":blog_pmen[post][0],
              'post_date':blog_pmen[post][1],
              'Title':blog_pmen[post][2],
              'Author':blog_pmen[post][3],
              'corpus':blog_pmen[post][4]}
 
    db.partial_blogs.update_one({"Title":blog_pmen[post][2],
                                 "blog_name":blog_pmen[post][0],
                                 "post_date":blog_pmen[post][1],
                                 "Author":blog_pmen[post][3],
                                 "corpus":blog_pmen[post][4],
                                 
                                },
                                
                                
                                {"$set":
                                 {"Title":blog_pmen[post][2],
                                  "blog_name":blog_pmen[post][0],
                                  "post_date":blog_pmen[post][1],
                                  "Author":blog_pmen[post][3],
                                  "corpus":blog_pmen[post][4],
                                  
                                 }
                                }, 
                                upsert=True)
    


# In[155]:

for post in range(len(blog_garage)):
    
 
 
    document={"blog_name":blog_garage[post][0],
              'post_date':blog_garage[post][1],
              'Title':blog_garage[post][2],
              'Author':blog_garage[post][3],
              'corpus':blog_garage[post][4]}
 
    db.partial_blogs.update_one({"Title":blog_garage[post][2],
                                 "blog_name":blog_garage[post][0],
                                 "post_date":blog_garage[post][1],
                                 "Author":blog_garage[post][3],
                                 "corpus":blog_garage[post][4],
                                 
                                },
                                
                                
                                {"$set":
                                 {"Title":blog_garage[post][2],
                                  "blog_name":blog_garage[post][0],
                                  "post_date":blog_garage[post][1],
                                  "Author":blog_garage[post][3],
                                  "corpus":blog_garage[post][4],
                                  
                                 }
                                }, 
                                upsert=True)
    


# In[157]:

for post in range(len(blof_dayone)):
   


   document={"blog_name":blof_dayone[post][0],
             'post_date':blof_dayone[post][1],
             'Title':blof_dayone[post][2],
             'Author':blof_dayone[post][3],
             'corpus':blof_dayone[post][4]}

   db.partial_blogs.update_one({"Title":blof_dayone[post][2],
                                "blog_name":blof_dayone[post][0],
                                "post_date":blof_dayone[post][1],
                                "Author":blof_dayone[post][3],
                                "corpus":blof_dayone[post][4],
                                
                               },
                               
                               
                               {"$set":
                                {"Title":blof_dayone[post][2],
                                 "blog_name":blof_dayone[post][0],
                                 "post_date":blof_dayone[post][1],
                                 "Author":blof_dayone[post][3],
                                 "corpus":blof_dayone[post][4],
                                 
                                }
                               }, 
                               upsert=True)
   


# In[ ]:


