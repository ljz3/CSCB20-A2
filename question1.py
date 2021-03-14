from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Add some text to the end of the url!'

@app.route("/<name_input>")
def dave_function(name_input):
    name = name_input
    output = ""
    for letter in name:
        if not letter.isdigit():
            output = output + letter

    if output.islower():
        return output.upper()

    else if output.isupper():
        return output.lower()
    
    return output