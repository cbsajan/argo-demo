from flask import Flask, render_template, request
import os
app = Flask(__name__)
print('********')
@app.route('/')
def index():
    return render_template('name.html')

@app.route('/howdy', methods=['POST'])
def howdy():
    name = request.form['name']
    return """
    <h1>Hello!!!!<h1>
    <h1>{}<h1>
    """.format(name)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
