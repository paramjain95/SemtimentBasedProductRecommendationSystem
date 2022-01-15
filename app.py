from flask import Flask, render_template, request
from model import recommend_product, get_all_username

app = Flask(__name__)  # intitialize the flaks app  # common 
all_users = get_all_username()
@app.route('/', methods = ['POST', 'GET'])
def home():
    data=[]
    user=""
    if request.method == 'POST':
        user = request.form["userid"]
        if user in all_users:
            data=recommend_product(user)
        else:
            return render_template("index.html", len=len(data), products=data, user=user, flag=False, flag1=True)
    return render_template("index.html", len=len(data),products=data, user=user,flag=False,flag1=False)


@app.route('/userList', methods = ['GET','POST'])
def userList():
    data=all_users
    return render_template("index.html", len=len(data), products=None, user=data,flag=True,flag1=False)


if __name__ == '__main__' :
    app.run()

