from django.shortcuts import render
import requests


def news(request):
    API_KEY = "97171abebc1c46628c710c22cd64949f" 

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
                "published": article["publishedAt"],
            })
            print(article["title"])
            print(article["description"])
            print(article["url"])
            print("-" * 50)
        
        return render(request, 'news/news.html', {'news': news})