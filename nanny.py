from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Craig has low standards!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run()