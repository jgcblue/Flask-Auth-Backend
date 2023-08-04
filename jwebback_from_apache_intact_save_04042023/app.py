import flask
from flask import Flask, jsonify, send_file, Response
from flask_restful import Api, Resource, reqparse
import flask_sqlalchemy
from flask_cors import CORS, cross_origin
import flask_praetorian
import json
import time
from werkzeug.security import safe_str_cmp
from io import StringIO, BytesIO
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import base64
import pandas as pd
from itertools import combinations

#instantiations
db = flask_sqlalchemy.SQLAlchemy()
guard = flask_praetorian.Praetorian()

app = flask.Flask(__name__)
app.debug = True
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active



app.config['SECRET_KEY'] = 'top secret'
app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the flask-praetorian instance for the app
guard.init_app(app, User)


# Initialize a local database for the example
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////<YourURL>'


db.init_app(app)


with app.app_context():
    db.create_all()
    if db.session.query(User).filter_by(username='a_username').count() < 1:
        db.session.add(User(
          username='a_username',
          password=guard.hash_password('a_password'),
          roles='admin'
		))
    db.session.commit()







#from models.user import UserModel


#Toook out parser

class UserRegister(Resource):
    def post(self):#from yasoob
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class User(Resource):
    def post(self):
        """
        $ curl http://localhost:5000/api/login -X POST \
        -d '{"username":"jc","password":"mikasico"}'
        """
        req = flask.request.get_json(force=True)
        username = req.get('username', None)
        password = req.get('password', None)
        user = guard.authenticate(username, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        response = flask.jsonify(ret)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def get(self):
        return ("hello")
    




class Time(Resource):
    #Can we have different functions depending on the type of request
    def get(self):
        print(type ({'time':time.time()}))
        return {'time': time.time()}
# INteresting
   
#    user = guard.authenticate(username, password)
#    ret = {'access_token': guard.encode_jwt_token(user)}

class UserLogin(Resource):
    def post(self):
        req = flask.request.get_json(force=True)
        username = req.get('username', None)
        password = req.get('password', None)
        user = guard.authenticate(username, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret

class Download(Resource):
    '''
    580, in dispatch_request
    meth = decorator(meth)
    '''
    #method_decorators=[cross_origin(supports_credentials=True)]
    def post(self):
        #For windows you need to use drive name [ex: F:/Example.pdf]
        path = "./cdIntro.pdf"
        return send_file(path, as_attachment=True)

class MathDownload(Resource):
    '''
    580, in dispatch_request
    meth = decorator(meth)
    '''
    #method_decorators=[cross_origin(supports_credentials=True)]
    def post(self,filename):
        #For windows you need to use drive name [ex: F:/Example.pdf]
        path = "./math_files/{}.pdf".format(filename)
        return send_file(path, as_attachment=True)


def readCsvFunction():
    df=pd.read_csv(f'./{csvName}', thousands=',')#f string (string interpolation)
    dfTwo=dfList(df)
    print("Remember what the return value is")
    return dfTwo



class CrimeProj(Resource):
    def get(self):# with response
        """
        Summary:

        Returns a plot that can be rendered in a browser.

        Extended Description of Function:

        Parameters:

        Returns:
        a string (encoded in base64) encoding an image
        """
        plt.rcParams["figure.figsize"]=(10,8)
        plt.rcParams['figure.dpi'] = 140
        plt.style.use('ggplot')
        mydfOne=readCsvFunctionNow()
        y=mydfOne.iloc[:,1:5].plot.bar(rot=0, subplots= True)
        print(type(y))
        img = BytesIO()# okay now we pass the result of saving...
        #try,except statement will attempt to have pyplot call its save fig method, using the bytes buffer
        #______________________________
        try:
            plt.savefig(img, format='png')
        except:
                print("I wasn't able to save the figure...")
        img.seek(0)#You can think of the img/StringIO.StringIO object as a
        plot_url=base64.b64encode(img.getvalue()).decode('utf8')
        #Now for creating the Response object, storing the plot url inside of it and adding the cross_origin headers 
        #______________________________
        x = flask.Response(plot_url)
        x.headers.add('Access-Control-Allow-Origin', '*')
        return x



def dfList(yFrame):
    """
    Summary:

    Parameters: 
    A single dataframe

    Returns:
    a tuple of dataframes
    """

    cc = list(combinations(yFrame.columns,2))
    a =[]
    print(cc, "hey the length of cc is", f'len(cc)')
    for i in range(len(cc)):
        a.append(pd.concat((yFrame[cc[i][0]], yFrame[cc[i][1]]), axis=1))
    return a , cc; # returns a tuple. So you need to use the return value properly as well.

def readCsvFunctionNow():
    df = pd.read_csv('/var/www/hb/jose_prac_two.csv', thousands=',')
    return df # just return the thang itself, not a list of combination 
#practicing making a docstring as well. Be careful with when an instance of a
#plto actually exists.


def csvFunc():
    """
    Summary: 
    This function just returns the result of applying defList to a dataframe
    obtained from one of our crime csv files.
    
    Detailed Summary:
    The combinations library is used to create a tuple of lists of dataframes
    comprised of two columns from the original csv file.

    Returns:
    A tuple with each member a list, where each list member is a DataFrame
    """
    df=pd.read_csv('/var/www/hb/jose_prac_two.csv', thousands=',')#f string (string interpolation)
    dfTwo=dfList(df)
    print("Remember what the return value is")
    return dfTwo

def plotterTuples(x):
    '''
    Summary:
    Recall that the return value of 
    This function takes in a  two values that correspond to which members you want
    to have plotted.

    Parameters: 
    Two integers

    Returns:
    '''
    plt.rcParams["figure.figsize"]=(6,4)
    plt.rcParams['figure.dpi'] = 140
    plt.style.use('ggplot')
    mydfOne=readCsvFunctionNow()
    mydfTwo=csvFunc()
    print("type of mydfTwo", type(mydfTwo))
    w = mydfTwo[0][x] #the datafame of two columns
    print(w)
    try:
        w.plot.bar()
    except:
        print("Anal")
    #y=mydfOne.iloc[:,1:5].plot.bar(rot=0, subplots= True)
    img = BytesIO()# okay now we pass the result of saving...
    #try,except statement will attempt to have pyplot call its save fig method, using the bytes buffer
    #______________________________
    try:
        plt.savefig(img, format='png')
        plt.savefig('foo.png')
    except:
            print("I wasn't able to save the figure...")
    img.seek(0)#You can think of the img/StringIO.StringIO object as a
    plot_url=base64.b64encode(img.getvalue()).decode('utf8')
    #Now for creating the Response object, storing the plot url inside of it and adding the cross_origin headers 
    #______________________________
    x = flask.Response(plot_url)
    x.headers.add('Access-Control-Allow-Origin', '*')
    return plot_url

def runPlotterTuples():
        '''
        Summary:
        Takes in nothing and creates a list of four plots by calling plotterTuples. This list is then 
        converted to a dictionary and returned as such. The output will be jsonified (or can be) and
        attached to a response in a Flask application

        Detailed Summary:

        Parameters:
        None

        Returns:
        Returns a dictionary of plots (in string format base64 etc)
        '''
        a =[plotterTuples(0), plotterTuples(1), plotterTuples(2), plotterTuples(3)]
        b = listToDict(a)
        return b #return the dictionary passed through json.dumps ... 

def listToDict(yourList):
        return dict(enumerate(yourList))




api = Api(app)

api.add_resource(TestingTwo,'/testingtwo')
api.add_resource(TestingFeb,'/testingfeb')
api.add_resource(CrimeProj,'/crimeproj')
api.add_resource(UserLogin,'/login')
api.add_resource(Download,'/download')
api.add_resource(MathDownload,'/download/<string:filename>')
api.add_resource(Time,'/time')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3008)

