
# coding: utf-8

# Taking the input

video_search=[x for x in input("").split(' ')]


video_search


# URL that you want to search in
youtube_url="https://www.google.com/search?q={}"



# creating urls to be searched 
search_url=[]
i=0
for i in range(0,len(video_search)):
    search_url.append(youtube_url.format(video_search[i]))


search_url


# Import webbrowser package

import webbrowser


for i in range(0,len(search_url)):
    webbrowser.open(search_url[i])


# In[ ]:



