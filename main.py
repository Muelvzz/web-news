import streamlit as st
import random
from functions import extract_news

# Our personal API
api = "0fc34c3d866047af97b8ce3de77d7391"

# URL sections
apple = "https://newsapi.org/v2/everything?q=apple&from=2025-06-05&to=2025-06-05&sortBy=popularity&apiKey=0fc34c3d866047af97b8ce3de77d7391&language=en"
tesla = "https://newsapi.org/v2/everything?q=tesla&from=2025-05-06&sortBy=publishedAt&apiKey=0fc34c3d866047af97b8ce3de77d7391&language=en"
business = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0fc34c3d866047af97b8ce3de77d7391&language=en"
techcrunch = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0fc34c3d866047af97b8ce3de77d7391&language=en"
wallstreet = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0fc34c3d866047af97b8ce3de77d7391&language=en"

apple_news = extract_news(apple)

st.set_page_config(layout="centered")

st.title("Muelvz Daily NEWS")

for item in apple_news["articles"][:20]:
    st.subheader(item["title"])
    st.write(item["content"].encode('utf-8'))
