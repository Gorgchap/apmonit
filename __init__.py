from datetime import datetime, timedelta
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


class Item:
    def __init__(self, type, name, state, last_change):
        self.type = type
        self.name = name
        self.state = state
        delta = (datetime.now() - last_change).total_seconds() 
        self.last_change = '{0} h {1} min ago'.format(int(delta/3600), int(delta/60) % 60)


@app.route('/')
def hello():
    aplist=[]
    for line in open('result.txt').readlines():
        arr = line.split('; ')
        aplist.append(Item(type=arr[0], name=arr[1], state=arr[2], last_change=datetime.strptime(arr[3], "%Y-%m-%d %H:%M:%S")))
    return render_template("index.html", aplist=aplist)

if __name__ == '__main__':
    app.run()
