from flask import Flask , jsonify , request
import csv

all_articles = []

with open("articles.csv" , encoding="utf-8") as f :
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

liked_article = []
not_liked_article = []

@app.route("/get_article")

def get_article() :
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })
 
@app.route("/liked_article" , methods = ["POST"]) 

def liked_articles() :
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(movie)
    return jsonify({
        "status" : "success"
    }) , 201

@app.route("/not_liked_article" , methods = ["POST"]) 

def not_liked_articles() :
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_article.append(movie)
    return jsonify({
        "status" : "success"
    }) , 201

if __name__ == "__main__" :
    app.run() 
