from flask import Flask, render_template, request, send_from_directory, jsonify

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('catch.html')
    elif request.method == 'POST':
        with open('file.webm', 'ab+') as vid:
            vid.write(request.data)
        return jsonify()


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.run(debug=True)
