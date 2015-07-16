from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <p>Hi! This is the home page.<p>
            <a href="/hello"> Say Hello!</a>
        </body>
    <html>
    """


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="POST">
                <label>What's your name?<input type="text" name="person"></label>
                

                <br>
                <br>

                <label>Select a compliment: 
                    <input type="radio" name="selection" value="awesome">awesome
                    <input type="radio" name="selection" value="terrific">terrific
                    <input type="radio" name="selection" value="fantastic">fantastic
                </label>
                
                <br>
                <br>

                <input type="submit">
            </form>

            <p>Alternatively...</p>
            <form action="/diss" method="POST">
                <label>Grrr...Tell me your name:<br>
                    <input type="text" name="person">
                </label>
                <br>
                <label>Wanna hear something mean? Tell me your name. 
                Then click here instead:  
                <input type ="submit">
                </label>
              
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods = ["POST"])
def greet_person():
    player = request.form.get("person")
    select = request.form.get("selection")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s.
            I also think you're %s, as you suggested!

        </body>
    </html>""" % (player, compliment, select)

@app.route('/diss', methods = ["POST"])
def diss_person():
    player = request.form.get("person")
    DISS = ["Why are you here?", "You're annoying!", "GO AWAY"]
    diss = choice(DISS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Dissing</title>
        </head>
        <body>
            Hi %s. %s
        </body>
    </html>
    """ %(player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
