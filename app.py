from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/analyze_sentiment_arr', methods=['POST'])
def analyze_sentiment_arr():
    data = request.json  # This is an array of dictionaries
    for article in data:
        text = article.get('title', '') + ' ' + article.get('description', '')
        senti = sia.polarity_scores(text)
        compound = senti['compound']
        
        status = "neutral"
        if compound > 0.05:
            status = "positive"
        elif compound < -0.05:
            status = "negative"
        
        # Add compound and status to each dictionary in the array
        article['compound'] = compound
        article['status'] = status
    
    return jsonify(data), 200  # Return the updated array of dictionaries


@app.route('/analyze_sentiment_single', methods=['POST'])
def analyze_sentiment_single():
    data = request.json  # assuming the client sent JSON payload
    text = data.get('description', '')  # Use an empty string as a default value
    senti = sia.polarity_scores(text)
    compound = senti['compound']
    
    status = "neutral"
    if compound > 0.05:
        status = "positive"
    elif compound < -0.05:
        status = "negative"
    
    
    # Prepare the response
    response = {}
    response['compound'] = compound
    response['status'] = status
    
    return jsonify(response), 200  # Return the updated array of dictionaries

if __name__ == '__main__':
    app.run(debug=True)

