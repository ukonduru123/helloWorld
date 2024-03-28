from flask import Flask, render_template, request
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

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        return render_template('contact.html',
                               submitted=True,
                               first_name=first_name,
                               last_name=last_name,
                               email=email,
                               date_of_birth=date_of_birth)
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
