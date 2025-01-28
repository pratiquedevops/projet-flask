from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
db = SQLAlchemy(app)
@app.route('/')
def home():
    return "Hello, Docker with PostgreSQL!"


@app.route('/profile/<username>')
def lihat_profile(username):
    return "welcome to profile page %s" % username

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
