from registro_ig import app


@app.route('/')
def index():
    return 'esto funciona, flask mola'