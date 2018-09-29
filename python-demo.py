from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html');

@app.route('/hello', methods=['POST'])
def cal_value():
    if request.method == 'POST':
        a = request.form.get('a', 0, type=int)
        b = request.form.get('b', 0, type=int)
        return jsonify(result = a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
