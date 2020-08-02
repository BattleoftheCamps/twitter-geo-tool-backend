# import os
from flask import Flask, jsonify, request, render_template
# template_dir = os.path.abspath('./src')
app = Flask(__name__, template_folder='../Front-End')

# @app.route('/')
# def render():
# 	# serve index template
# 	return render_template('index.html')

@app.route("/helloworld")
def output():
	return "Hello World!"

# if __name__ == "__main__":
#     app.run()
