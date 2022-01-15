from flask import Flask, render_template, request
from model import recommend_product, get_all_username

app = Flask(__name__)  # intitialize the flaks app  # common 

@app.route('/', methods = ['POST', 'GET'])
def home():
    data=[]
    user=""
    if request.method == 'POST':
        user = request.form["userid"]
        if user.lower() in get_all_username():
            data=recommend_product(user.lower())
    return render_template("index.html", len=len(data),products=data, user=user,flag=False)


@app.route('/userList', methods = ['GET','POST'])
def userList():
    data=get_all_username()
    return render_template("index.html", len=len(data), products=None, user=data,flag=True)


if __name__ == '__main__' :
    app.run(debug=True)

