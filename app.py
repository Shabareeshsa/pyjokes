from flask import Flask
import pyjokes

app=Flask(__name__)


@app.route("/")
def home():
    joke=pyjokes.get_joke()  #It only returns one joke. We get random joke each time. 
    return f'<h2>{joke}</h2>'

@app.route("/MultipleJokes")
def jokes():
    jokes=pyjokes.get_jokes()  #Here, we get a list of jokes.  
    return f'<h2>{jokes}</h2>'

if __name__ == "__main__":
    app.run(debug=True)