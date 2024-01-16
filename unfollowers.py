#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup

def print_unfollowers(followers_file='followers_1.html', following_file='following.html'):
    
    # Load HTML from a local files:
    with open(followers_file, 'r') as file:
        followers = file.read()

    with open(following_file, 'r') as file:
        following = file.read()
    
    html_following = BeautifulSoup(following, 'html.parser')
    html_followers = BeautifulSoup(followers, 'html.parser')
    
    _following = []
    _followers = []
    
    a_following = html_following.find_all('a')
    a_followers = html_followers.find_all('a')
    
    for anchor in a_followers:
        link_text = anchor.text.strip()  # Get the link text
        href = anchor['href']  # Get the href attribute (the link URL)

        # Do something with the link text and URL, e.g., print, store in a list, etc.
        _followers.append(link_text)


    for anchor in a_following:
        link_text = anchor.text.strip()  # Get the link text
        href = anchor['href']  # Get the href attribute (the link URL)

        _following.append(link_text)
        
    for following in _following:
        if following not in _followers:
            print(following)


# In[ ]:


print_unfollowers()

