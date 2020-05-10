from myapp import app

@app.route('/')
@app.route('/index')
def startpage():
    return "My first response object"