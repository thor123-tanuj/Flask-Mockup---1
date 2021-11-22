from flask import Flask , jsonify , request
import csv

all_movies = []


with open("movies.csv" , encoding="utf-8") as f :
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)

liked_movie = []
not_like_movie = []
did_not_watch = []

@app.route("/getmovie")

def getmovie() :
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })

@app.route("/liked_movie" , methods = ["POST"]) 

def liked_movies() :
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movie.append(movie)
    return jsonify({
        "status" : "success"
    }) , 201

@app.route("/not_like_movie" , methods = ["POST"]) 

def not_like_movies() :
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_like_movie.append(movie)
    return jsonify({
        "status" : "success"
    }) , 201

@app.route("/did_not_watch" , methods = ["POST"]) 

def did_not_watch_movie() :
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status" : "success"
    }) , 201

if __name__ == "__main__" :
    app.run() 