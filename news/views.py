from django.shortcuts import redirect, render
from django.utils.dateparse import parse_datetime

import requests

import random

API_KEY = "97171abebc1c46628c710c22cd64949f" 

def news(request):

    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "language": "en",       
        "country": "us",        
        "pageSize": 5,        
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    news = []

    if response.status_code == 200:
        data = response.json()
        for article in data["articles"]:
            news.append({
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "image": article["urlToImage"],
                "source": article["source"]["name"],
                "published": parse_datetime(article["publishedAt"]),
            })
            print(article["title"])
            print(article["description"])
            print(article["url"])
            print("-" * 50)
        
        

        return render(request, 'news/news.html', {'news': news})
    
def random_article_view(request):
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    all_articles = []

    for category in categories:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "language": "en",
            "country": "us",
            "category": category,
            "pageSize": 20,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params).json()
        articles = response.get("articles", [])
        all_articles.extend(articles)

    if not all_articles:
        return redirect('news:news')  

    random_article = random.choice(all_articles)
    random_url = random_article.get("url")

    return redirect(random_url)