from flask import Flask
from flask import Flask, request, render_template, jsonify
#from passwordCheck import passwordCheck

app = Flask(__name__)
guess = ""
@app.route('/', methods =["GET", "POST"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       inputFromTextBox = request.form.get("textBox")
       guess = inputFromTextBox
       #if passwordCheck(guess):
       #   return "here"
       
    
       
       
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')