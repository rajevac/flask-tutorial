from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'Blog post 1 copy',
        'date': 'April 20, 2020'
    },
    {
        'author': 'Vladimir Rajevac',
        'title': 'Blog Post 1',
        'content': 'Blog post 1 copy',
        'date': 'September 20, 2020'
    },
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
