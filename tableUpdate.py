import requests
from pydantic import BaseModel
import mysql.connector


class SingleData(BaseModel):
    description: str



# Set up your MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="db"
)

cursor = conn.cursor()

# Fetch all articles from the table
cursor.execute("SELECT * FROM gnews_article")
articles = cursor.fetchall()

# Convert articles from DB to format expected by API
article_list = [{
    'id': a[0],
    'title': a[3],
    'description': a[1],
    'content': None,
    'url': a[4],
    'image': None,
    'publishedAt': a[2],
    'sentimentPoint': None
} for a in articles]

# Loop over each article and send to the API for sentiment analysis
for article in article_list:
    response = requests.post(
        "http://127.0.0.1:8000/analyze_sentiment_single",
        json={"description": str(article['description'])}  # Convert to string here

    )

    # Check if the API call was successful
    if response.status_code != 200:
        print(f"API call failed for article {article['id']} with status code: {response.status_code}")
        print(response.text)
        continue  # Skip updating the DB for this article and move to the next one

    # Decode the JSON response
    updated_data = response.json()

    # Update the article with the returned sentiment
    article['sentiment'] = updated_data['status']
    article['sentimentPoint'] = updated_data['compound']

    # Update the table with new sentiment and sentiment_point
    cursor.execute(
        "UPDATE gnews_article SET sentiment = %s, sentiment_point = %s WHERE id = %s",
        (article['sentiment'], article['sentimentPoint'], article['id'])
    )


# Commit the updates and close the connection
conn.commit()
cursor.close()
conn.close()
