from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Article(BaseModel):
    title: str
    description: str

class SingleData(BaseModel):
    description: str

app = FastAPI()
sia = SentimentIntensityAnalyzer()

class ArticleWithSentiment(BaseModel):
    title: str
    description: str
    compound: float
    status: str

# then, in your route:
@app.post("/analyze_sentiment_arr")
def analyze_sentiment_arr(articles: list[Article]):
    result = []
    for article in articles:
        text = f"{article.title} {article.description}"
        senti = sia.polarity_scores(text)
        compound = senti['compound']
        status = "neutral"
        if compound > 0.05:
            status = "positive"
        elif compound < -0.05:
            status = "negative"
        
        result.append(ArticleWithSentiment(
            title=article.title,
            description=article.description,
            compound=compound,
            status=status
        ))
    return result


@app.post("/analyze_sentiment_single")
def analyze_sentiment_single(data: SingleData):
    text = data.description
    senti = sia.polarity_scores(text)
    compound = senti['compound']
    status = "neutral"
    if compound > 0.05:
        status = "positive"
    elif compound < -0.05:
        status = "negative"
    
    return {"compound": compound, "status": status}
