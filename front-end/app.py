from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

# # path of "send_email"-file must be changed to the path on your computer
import sys
sys.path.append("C:/Users/Osman Ibrahim/Desktop/TicTacToe - Web-App/back-end") 
from send_email import send_email


sys.path.append("C:/Users/Osman Ibrahim/Desktop/TicTacToe - Web-App/back-end/RA-L") 
from working_policy import tictactoe


from database import db, Users, Games




# TODO: index.html cant be found when because app(......, template_folder="template") is not being imported somehow and the html templates are not execceble  
# more information here: https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists#:~:text=When%20render_template()%20function%20is,folder%20does%20not%20exist
# as a result this error appears:
    # jinja2.exceptions.TemplateNotFound
    # jinja2.exceptions.TemplateNotFound: index.html

# solution: maybe is not very efficiant but it works: 
# insert/have "app=Flask(__name__, template_folder="template")" in app.py/here
app=Flask(__name__, template_folder="template", static_folder="static",)

# -----------
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:EF-Informatik0@localhost/tictactoe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
# -----------


@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/credentials")
def credentials():
    return render_template("credentials.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method=="POST": 
        email=request.form["email_name"] 
        pwd=request.form["pwd_data"]
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        gender=request.form["gender"]
        age=request.form["age"]
        print(email, pwd, first_name, last_name, gender, age) 
      
        if db.session.query(Users).filter(Users.email_==email).count() ==0: 
            user=Users(email, pwd, first_name, last_name, gender, age) 
            db.session.add(user) 
            db.session.commit() 
            # TODO: Don't need this: average_age, probably 
            # average_age=db.session.query(func.avg(Users.age_)).scalar() 
            # average_age=round(average_age,1) 
            # TODO: count_ does not work 
            # count_=db.session.query(Users.uId).count()
            send_email(email, pwd, first_name, last_name)
            return render_template("success.html")
        else: 
           return render_template("credentials.html", 
                                  text = "This email has already submitted. Try with another email" )  



# @app.route('/board', methods=['GET', 'POST'])
# def board():
#     if request.method == 'POST':
#         print(request.form.get('first_name'))
#      return render_template("board.html")

# # sources = {"source_0" : "/static/assets/o-icon-100.png"}
# sources = {"0 0" : "source_0"} 

listX = []
pos = ""

# # listY = [(0, 0), (0, 0)]
# listY = {"0 0" : "source_0", "0 1": "source_1","0 2": "source_2","1 0": "source_3","1 1": "source_4","1 2": "source_5","2 0": "source_6","2 1": "source_7","2 2": "source_8"}
# # listY = np.array([[0, 0],[0, 1], [0, 2], [1, 0],[1, 1], [1, 2], [1, 0],[2, 1],[2, 2]])
# imgDic = {"source_0":"static/assets/o-icon-100.png", "source_1": "static/assets/o-icon-100.png", "source_2": "static/assets/o-icon-100.png", "source_3": "static/assets/o-icon-100.png", 
#           "source_4" : "static/assets/o-icon-100.png", "source_5": "static/assets/o-icon-100.png", "source_6": "static/assets/o-icon-100.png", "source_7": "static/assets/o-icon-100.png", "source_8": "static/assets/o-icon-100.png"}


# def findPos():
#     global x
#     pos = request.form.get('pos')
#     if request.method == 'POST':
#         # x = listY[pos]
#         x = str(listY[pos])
#         print(x)
#         return (x)   

@app.route('/board', methods=['POST'])
def board():
    global pos
    global listX
    # global listY
    # global imgDic
    # global y
    # listX.clear()
    
    
    
    if request.method == 'POST':
        # pos = request.form.get('pos')
        pos = tuple(map(int, request.form.get("pos").split(' ')))  # there must be a "leerschlag" in "split(' ')"
        # pos = request.form.get("pos").split(' ')
        # print("position =" + str(pos))
        print(pos)
        position = str(pos)
        position = position[0] + position[2]
        for i in range(2):
            moves = moves.append(position[i])
            print(moves)
        tictactoe()
        return render_template("board.html")
        
    # if request.method == 'Post':
    #     request.form.get('game_stats')
    #     print(request.form.get('game_stats'))
    #     return render_template("credentials.html")
        
        # if request.method == 'POST':
        # pos = request.form.get('pos')
        #     findPos()
            # z = request.form.get('img')
            # z = imgDic[x]
            # print("image name =" + str(z))
            # return render_template("board.html", source_0="/static/assets/o-icon-100.png", source_1="/static/assets/o-icon-100.png", source_2="/static/assets/o-icon-100.png",)
            # return render_template("board.html", x=z)

            
        # if  pos == "0 0":
        #     return render_template("board.html", source_0='/static/assets/o-icon-100.png')

        # if  pos == "0 1":
        #     return render_template("board.html", source_1='/static/assets/o-icon-100.png')
        
        # if pos == "0 2":
        #     return render_template("board.html", source_2='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "1 0":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_3='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "1 1":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_4='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "1 2":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_5='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "2 0":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_6='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "2 1":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_7='/static/assets/o-icon-100.png')
        
        # if request.method == 'POST' and pos == "2 2":
        #     pos = request.form.get('pos')
        #     return render_template("board.html", source_8='/static/assets/o-icon-100.png')
    
    
if __name__ == "__main__":
    app.debug = True
    # TODO: app.debug = True to see error on localhost/website (!not safe after building app)
    # app.debug = False
    app.run() 
    
