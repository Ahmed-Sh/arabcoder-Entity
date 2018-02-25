from flask import Flask
app=Flask(__name__)
@app.route("/SayHello/<name>")
def say_heloo(name):
    return "hello "+name
if __name__=='__main__':
	app.run(debug=True)