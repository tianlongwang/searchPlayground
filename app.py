from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

annot_test = ['test query1', 'test query2']
import json
import pandas as pd
current_search = pd.DataFrame(json.load(open('test_search.json', 'rw')))
predict_search = pd.DataFrame(json.load(open('test_search.json', 'rw')))



@app.route('/')
@app.route('/search')
def search():
    return render_template('search.html', test_queries=annot_test)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/test/<test_query>')
def render_test_query(test_query):
    return render_template('search_result.html',            query=test_query, my=predict_search.to_html(), current=current_search.to_html())

@app.route('/result', methods=['POST'])
def search_result():
    return render_template('search_result.html', query=request.form['query'], my=predict_search.to_html(), current=current_search.to_html())

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
