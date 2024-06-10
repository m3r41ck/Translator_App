from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def translate():
    if request.method == 'POST':
        input_translation = request.form['inputText']
        print(input_translation)
        return render_template('index.html')

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)