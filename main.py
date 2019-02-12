from flask import Flask, render_template, request, send_from_directory, jsonify, session
from flask_session import Session

app = Flask(__name__, static_url_path='')
# Check Configuration section for more details
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('catch.html')
    elif request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            if 'filename' in request.json.keys():
                filename = f"videos/{request.json['filename']}"
                session['vid_file'] = filename
        elif content_type == 'video/webm':
            with open(session['vid_file'], 'ab+') as f:
                f.write(request.data)
        return jsonify()


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.secret_key = "Your_secret_string"
    app.config['SESSION_TYPE'] = 'redis'
    app.run(debug=True)
