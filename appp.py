from flask import Flask , render_template , request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello_world():
    response = ""
    if request.method == 'POST':
        user_question = request.form['question']
        # Process the question (e.g., send it to an AI model)
        # For now, we'll just return the question as a simple response
        response = "ai says:" + user_question
    return render_template('indx.html', answer=response)
if __name__ == '__main__':
    app.run(debug=True)