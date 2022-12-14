import json, os, time, requests, logging
from urllib import request
from flask import Flask
from healthcheck import Healthcheck, EnvironmentDump
import jmespath

print("The api is starting up")
app = Flask(__name__)
# health = HealthCheck()
# envdump = EnvironmentDump()
# app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())

bookstore = json.load(testdata.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

@app.route('/getBook')
def getBook():
    #Restrict functionality to only query by one parameter

    # if key doesn't exist, returns None
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    titleQuery = jmespath.search("books[*].title", title)
    authorQuery = jmespath.search("books[*].author", author)
    genreQuery = jmespath.search("books[*].genre", genre)

    if titleQuery is not None:
        print(titleQuery)
        return titleQuery

    if authorQuery is not None:
        print(authorQuery)
        return authorQuery
    
    if genreQuery is not None:
        print(genreQuery)
        return genreQuery