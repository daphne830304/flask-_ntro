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

    return """
    <!doctype html>
      <html>
        Hi! This is the home page.
        <a href="/hello">Click Here</a>
      </html>
    """


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
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <div>What compliment would you like?</div>
          <div><input type="radio" name="compliment" value="you rock">You rock!</input></div>
          <div><input type="radio" name="compliment" value="you're great">You're great!</input></div>
          <div><input type="radio" name="compliment" value="you're radiant">You're radiant!</input></div>
          <input type="submit"></input>
        </form>
        <form action="/diss">
          <div>Or do you want a diss?</div>
          <div>What's your name? <input type="text" name="person"></div>
          <div><input type="radio" name="diss" value="you stink">You stink!</input></div>
          <div><input type="radio" name="diss" value="you lost your towel">You lost your towel!</input></div>
          <div><input type="radio" name="diss" value="you suck">You suck!</input></div>
          <input type="submit"></input>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def diss_user():
  """Get user by name."""

  player = request.args.get("person")

  diss = request.args.get("diss")

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False, host="0.0.0.0")
