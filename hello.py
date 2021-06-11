from flask import Flask
from flask import render_template
import redis

app = Flask(__name__)
r = redis.Redis(host = 'redis-server', port=6379)
r.set('visit',0)
test = 0

def visitcount():
    visit = int.from_bytes(r.get('visit'),"little") - 48
    r.set('visit', visit+1)
    return visit

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result    

@app.route("/")
def hello_world():
    return render_template('hello.html', test = visitcount())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)

