import models
import store
from flask import Flask,render_template
post_store=store.PostStore()
post_store.add(models.Post("Life", "Life is alawys great"))
post_store.add(models.Post("Sunshine", "Sunshine is amazing"))
app=Flask(__name__)
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html",posts=post_store.get_all())
if __name__=='__main__':
	app.run(debug=True)