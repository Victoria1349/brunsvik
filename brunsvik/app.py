from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def post_list():
    return render_template('post_list.html')

@app.route("/new/", methods=['POST'])
def new():
    return render_template('templates/blog/new.html');