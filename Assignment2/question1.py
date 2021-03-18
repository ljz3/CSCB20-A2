from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Add some text to the end of the url!'

@app.route("/<name_input>")
def dave_function(name_input):
    name = name_input
    output = ""
    hasNUM = False
    for letter in name:
        if not letter.isdigit():
            output = output + letter
        elif letter.isdigit():
            hasNUM = True

    if output.islower() and hasNUM == False:
        output = output.upper()

    elif output.isupper() and hasNUM == False:
        output = output.lower()
    
    return "Welcome, " + output + ", to my CSCB20 website"