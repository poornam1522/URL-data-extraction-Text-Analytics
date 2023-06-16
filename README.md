# URL-data-extraction-Text-Analytics
Introduction:
This project focuses on extracting data from given URLs and performing text analysis on the extracted data.
The input.xlsx contains the URLs and URL IDs from which we have to scrape the Article title and Article text. This has about 150 URLs on total.
Data Extraction: 
The provided code extracts data from the given URLs using the BeautifulSoup library. 
The code sends GET requests to the URLs and checks the response status code to ensure successful connection.
The article title and main text are extracted from the HTML content. 
The extracted article text is saved in separate files named after the URL_ID in the "articles" directory. 
Text Analysis:
The code utilizes various libraries, including TextBlob, NLTK, Spacy, and pyphen, for performing text analysis. 
The following metrics and scores are calculated for each extracted article: 
Positive score 
Negative score 
Polarity score
Subjectivity score
Average sentence length
Percentage of complex words
Fog index
Average number of words per sentence
Complex word count 
Word count Syllables per word 
Personal pronouns count
Average word length 
Instructions for Running the Code: 
Ensure that the required libraries (specified in the code) are installed with the recommended versions. 
Prepare the input data in an Excel file, named "input.xlsx," with appropriate columns (URL_ID, URL).
Create an empty directory named "articles" in the same location as the code file.
Run the code and wait for it to complete the data extraction and text analysis process.
Once the code finishes, the calculated metrics and scores will be saved in an Excel file named "output_file.xlsx." 
Output and Deliverables: The output file, "output_file.xlsx," contains the calculated metrics and scores for each URL. 
The columns in the output file include URL_ID, Positive Score, Negative Score, Polarity Score, Subjectivity Score, Average Sentence Length, Percentage of Complex Words, Fog Index, Average Number of Words Per Sentence, Complex Word Count, Word Count, Syllables per Word, Personal Pronouns, and Average Word Length. 
Conclusion:
This process demonstrates the process of extracting data from URLs and performing text analysis using Python. The extracted data and calculated metrics provide insights into the sentiment, linguistic complexity, and structural characteristics of the articles.
