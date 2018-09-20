# import necessary libraries
import json
from flask import Flask, render_template, redirect, jsonify,\
    url_for
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
db.mars.drop()   # uncomment to delete data


@app.route("/")
def index():

    res = list(db.mars.find())

    if len(res) == 0:
        scrape()
        res = list(db.mars.find())
    
    return render_template("index.html",marsdata=res[0])
    

@app.route("/scrape")
def scrape():

    scrape_dict = scrape_mars.scrape()

    scrape_dict['docid'] = 'mars_data'

    db.mars.update_one({ "docid":"mars_data"},{
        "$set": scrape_dict },upsert=True)
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
