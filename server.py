"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
      Hi! This is the home page.
      <a href="/hello">Go to hello</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" "/diss">
          What's your name? <input type="text" name="person">
          Select a compliment 
          <select name="compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="wowza">Wowza</option>
            <option value="coolio">Coolio</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
        <a href="/diss">Go to insult</a>
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Get user by name, get insult, and mock according to insult level."""

  return f"""
  <!doctype html>
  <html>
    <head>
      <title>Oh. It's You.</title>
    </head>
    <body>
      <p>
        Hahahahahahaha
      </p>
    </body>
  </html>
  """



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
