from flask import Flask, render_template #uppercase is a module from lowercase flask library ----render_template allows external html file to be used in python
app = Flask(__name__) #application with whatever name

@app.route('/') #function will be run everytime home page is visited
def index():
    return '<h1>Hello from Flask!</h1>'

@app.route('/subpage') #because subpage function is before name, it runs first
def subpageFuction():
  return '<h1>This is a subpage!</h1>'

@app.route('/<string:name>') #whatever person puts into url, it is now a string value and treated as a variable
def hello_name(name):
  return render_template('index.html', name = name) #creating a variable that can be passed into index.html
  
@app.route('/<int:number>')
def half(number):
  return 'This number cut in half is ' + str(number/2)
  
app.run(host='0.0.0.0', port=81) #replit runs and posts app
