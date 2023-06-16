# Importing necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests, os
from time import time

start = time()

# Open the file input.xlsx and iterate through each row
file = pd.read_excel('input.xlsx')
for index, row in file.iterrows():
    URL_ID, URL = row['URL_ID'], row['URL']
    # Get the response from the URL
    resp = requests.get(URL, timeout=5)
    if resp.status_code != 200:
        print(f'Error for URL_ID: {URL_ID} with status code: {resp.status_code}')
        continue
    
    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Get the h1 of the article
    title = soup.find('h1').text.strip()
    # print(f'Title: {title}')
    
    # Find the main article text in the <div> tag with class 'tdb-block-inner td-fix-index' with all the <p> tags
    
    article_text = ''
    for p in soup.find_all('p'):
        # check if the <p> tag is inside the <div> tag with class 'tdb-block-inner td-fix-index' or 'td-post-content tagdiv-type'
        if p.parent.name == 'div':
            if p.parent.get('class') == ['tdb-block-inner', 'td-fix-index'] or p.parent.get('class') == ['td-post-content', 'tagdiv-type']:
                article_text += p.text.strip() + '\n'
        
    # print(f'Article Text: {article_text}')
    print(f'URL_ID: {URL_ID}, words: {len(article_text.split())}')
        
    # create directory 'articles' if it doesn't exist
    if not os.path.exists('articles'):
        os.makedirs('articles')
    # save the article text in a file with the name as URL_ID
    with open(f'articles/{URL_ID}.txt', 'w', encoding='utf-8') as file:
        file.write(f'Title: {title}\n\n{article_text}')
    

# Time taken in minutes
print(f'Time taken: {(time() - start) / 60} min')