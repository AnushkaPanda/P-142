import csv
from flask import Flask,jsonify,request

movies=[]
with open('articles.csv', encoding='UTF8') as f:
    reader = csv.reader(f)
    data = list(reader)
    articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)

@app.route('/get_articles')
def get_articles():
    return jsonify({
        'data': articles[1:],
        'status': 'success'
    }),201

@app.route('/get_liked_articles',methods=['POST'])
def get_liked_articles():
    article = articles[0]
    articles = articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status':'success'
    }),201

@app.route('/get_disliked_articles',methods=['POST'])
def get_disliked_articles():
    article = articles[0]
    articles = articles[1:]
    disliked_movies.append(article)
    return jsonify({
        'status':'success'
    }),201

if __name__ == '__main__':
    app.run()
