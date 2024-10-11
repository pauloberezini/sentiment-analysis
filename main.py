from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nhl_api import get_nhl_standings
from nhl_api import get_previous_nhl_standings

app = FastAPI()
sia = SentimentIntensityAnalyzer()

class GNewsArticle(BaseModel):
    id: Optional[int]           # Optional since in a new entity, it may not be set yet
    title: str
    description: str
    content: Optional[str]      # Marked as optional using typing's Optional because of @Transient in Java
    url: str
    image: Optional[str]        # Marked as optional for the same reason
    publishedAt: str
    sentiment: Optional[str]    # Assuming sentiment can be optional as it's not marked as required in Java
    sentimentPoint: float


class SingleData(BaseModel):
    description: str


class ArticleWithSentiment(BaseModel):
    title: str
    description: str
    compound: float
    status: str

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

# then, in your route:
@app.post("/analyze_sentiment_arr")
def analyze_sentiment_arr(articles: list[GNewsArticle]):
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
        
        updated_article = GNewsArticle(
            id=article.id,
            title=article.title,
            description=article.description,
            content=article.content,
            url=article.url,
            image=article.image,
            publishedAt=article.publishedAt,
            sentiment=status,
            sentimentPoint=compound
        )
        result.append(updated_article)
    return result


@app.get("/nhl/standings")
def nhl_standings():
    return get_nhl_standings()

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

@app.get("/nhl/previousstandings")
def nhl_previous_standings():
    return get_previous_nhl_standings()