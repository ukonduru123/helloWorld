from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Unnathi Konduru! I am adding my first code change. I am adding another code change!'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html', hello={'html': 'hello.html'})

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()
