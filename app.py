import os,time,json
#import datetime
from datetime import datetime
from flask import Flask, request,jsonify
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#in procfile to specify the python run the app
#web: FLASK_APP = server.py python -m flask run --host=0.0.0.0 --port=$PORT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name



class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80))
    buildtime = db.Column(db.String(80))
    status = db.Column(db.String(80))
    task = db.Column(db.String(120))
    project = db.Column(db.String(120))
    plantime = db.Column(db.String(120))
    finishtime = db.Column(db.String(120))

    def __init__(self,task,buildtime,user="yangming",status="unfinished",project="inbox",plantime="unspecified",finishtime="0"):
        self.task = task
        #self.buildtime = str(datetime.now())
        self.buildtime =buildtime
        self.status = status
        self.user = user
        self.project = project
        self.plantime = plantime
        self.finishtime = finishtime


    def __repr__(self):
        return '<Name %r>' % self.name

#crete table!
db.create_all()
print("i have crete database")

@app.route('/xiajian')
def law():
    return render_template('law.html')


@app.route("/",methods=['GET','POST'])
def usersystem():
    if request.method == 'GET':
        return render_template("user.html")








@app.route('/gtdcli',methods=['GET','POST'])
def gtdcli():
    try:
        if request.method == 'POST':
            #print(request.json
            body = request.get_json()
            inboxthing1 =body['inbox']
            now = datetime.now()
            year,month,day = now.year,now.month,now.day
            buildtime = str(year)+str(month)+str(day)
            inboxthing = body['inbox']
            taskstatus = body['task-status']
            plantime = body['plantime']
            project =  body['project']
            print("i am print inbox",inboxthing)
            try:
                taskcontent = task(inboxthing,buildtime,plantime=plantime,project=project)
                db.session.add(taskcontent)
                db.session.commit()
                return json.dumps({'status':'u have uploaded successfully'})
            except Exception as e :
                print("erro=======>",e)
                return json.dumps({'status':'db error'})    
        else:
            return json.dumps({'status':'upload fail'})
    except Exception as e:
        print('error info',str(e))
        return json.dumps({'errorindo':str(e)})


@app.route('/today')
def today():
    now = datetime.now()
    year,month,day = now.year,now.month,now.day
    querytime = str(year)+str(month)+str(day)
    allinbox = task.query.filter_by(user="yangming",buildtime=str(querytime)).all()
    alltask ={}
    for k in allinbox:
        alltask[str(k.id)] = [k.status,k.user,k.buildtime,k.task,k.project,k.plantime,k.finishtime ]
    
    return json.dumps(alltask)





@app.route('/update',methods=['GET','POST'])
def update():
    try:
        if request.method == 'POST':
            body = request.get_json()
            taskstatus = body['taskstatus']
            idcli = body['id']
            project = body['project']
            plantime = body['plantime']
            if taskstatus == "finish":
                now = datetime.now()
                year,month,day = now.year,now.month,now.day
                finishtime = str(year)+str(month)+str(day)
            #database update instaruct
            target_task = task.query.filter_by(id=idcli).first()
            target_task.project = project
            target_task.plantime = plantime
            target_task.finishtime = finishtime
            target_task.status =taskstatus
            db.session.commit()
            return json.dumps({'status':'u have uploaded successfully'})
    except Exception as e:
        print(e)
        return json.dumps({'status':'u have uploaded fail'})   

    
      
@app.route('/load')
def load():
    allinbox = task.query.order_by(task.id).all()
    for k in allinbox:
        print(k.task)
    return render_template("loadhtmlfromdb.html",my_list = allinbox)




@app.route('/inbox')
def inbox():
    allinbox = task.query.filter_by(project='inbox').order_by(task.id).all()
    for k in allinbox:
        print(k.task)
    return render_template("inbox.html",my_list = allinbox)











@app.route('/everyday1')
def everyday():
    alltask = task.query.order_by(task.project).all()
    #alltask = task.query.order_by(task.id).all()
    plantime = list(set([task.plantime for task in alltask if task.plantime!="unspecified"]))
    everyday = {}
    for time in plantime:
        everyday["time"]=[task for task in alltask if task.plantime==time]
    return render_template('everyday1.html',everyday=everyday)








@app.route('/in')
def hello_world():
    return render_template('in.html')


@app.route('/todoist')
def todo():
    return render_template('toist.html')



@app.route('/everyday')
def everydayfordb():
    #alltask = task.query.all()
    #http://flask-sqlalchemy.pocoo.org/2.3/queries/
    '''
    allproject = task.query.order_by(task.project).all()
    plantime = list(set([task.plantime for task in alltask if task.plantime!="unspecified"]))
    everyday = {}
    for time in plantime:
        everyday["time"]=[task for task in alltask if task.plantime==time]
    return render_template('everyday1.html',everyday=everyday)
    '''
    alltask = task.query.order_by(task.id).all()
    #http://flask-sqlalchemy.pocoo.org/2.3/queries/
    plantime =list(set([k.plantime for  k in alltask if k.plantime!="unspecified"]))
    everyday = {}
    for k  in plantime:
        everyday[k]=[d for d in alltask if d.plantime==k]

    return render_template('everyday1.html',everyday=everyday)


@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/project')
def project(): 
    allproject = task.query.order_by(task.project).all()
    #http://flask-sqlalchemy.pocoo.org/2.3/queries/
    project_name =list(set([k.project for  k in allproject if k.project!="inbox"]))
    project_dict = {}
    for k  in project_name:
        project_dict[k]=[d for d in allproject if d.project==k]
    
    return render_template('project1.html',project=project_dict)
'''
@app.route('/everyday')
def everyday():
    alltask = task.query.order_by(task.project).all()
    #alltask = task.query.order_by(task.id).all()
    plantime = list(set([task.plantime for task in alltask if task.plantime!="unspecified"]))
    everyday = {}
    for time in plantime:
        everyday["time"]=[task for task in alltask if task.plantime==time]
    return render_template('everyday1.html',everyday=everyday)
'''
#a=requests.post("https://gtdofdream.herokuapp.com/info/",data={'foo':'bar','input':'yangming is here'})


#python flask deal with flask post
# requests.post('http://:5000/info',data={'user':'yangming','userinput':'yangming is here','content':'yangming'}).text

'''
@app.route('/info',methods=['GET', 'POST'])
def info():
    print("i have no word")
    if request.method == 'POST':
        username = request.values.get('user')
        print(username)
        #req_data = request.get_json()
        content = request.values.get('foo')
        #print(content)
        userinput = request.values.get('input')
        taskcontent = task(str(userinput)
    db.session.add(taskcontent)    
    db.session.commit()    
    content = "yangming"
    a = {'test':'yangming is hereko','userinput':str(userinput),'time':str(time.time()),'user':str(username)}
    #print(content)
    #print(userinput)
    return json.dumps(a)
'''

@app.route('/info',methods=['GET','POST'])
def information():
    if request.method == 'POST':
        content = request.values.get('input')
        #user = User(str(time.time()), str(content)+str(time.time()))
        #db.session.add(user)
        taskcontent = task(str(content))
        db.session.add(taskcontent)
        db.session.commit()
        print(content)
        #all_users = User.query.all()
        #print(all_users)
        '''
        for k in all_users:
            print(str(k.email)+'email')
        '''    
        #content = task(content)
        #print(content)
        return json.dumps({'content':str(content),'time':str(time.time())})

#ios requests http post  
@app.route('/info1',methods=['GET','POST'])
def information1():
    if request.method == 'POST':
        info = []
        try:
            #content = request.values.get('input')
            #print(content,"yangming+++++++++++++=")
            print(request.get_json())
            a = request.get_json()
            print(a["inbox"])
        except:
            info1 = "request json have no data"
            info.append(info1)    
        try:
            a=request.get_data()
            #print(a["input"])
            taskcontent = task(str(a))
            db.session.add(taskcontent)
            db.session.commit()
            try:
                with open('./templates/freewriting.md','a') as f:
                    f.write(str(a))
            except:
                print("write file error")     
        except:
            a = ("request.data() error")
            info.append(a)    
        try:
            print(json.loads(request.data))
        except:
            b = "json parser fail" 
            info.append(b)   
        #content = request.values.get('input')
        #user = User(str(time.time()), str(content)+str(time.time()))
        #db.session.add(user)
        #taskcontent = task(str(content))
        #db.session.add(taskcontent)
        #db.session.commit()
        #print(content)
        #all_users = User.query.all()
        #print(all_users)
        '''
        for k in all_users:
            print(str(k.email)+'email')
        '''    
        #content = task(content)
        #print(content)
        return jsonify(input1=str("yangmingis=====here"),info1 =str(info))








@app.route('/test')
def info1():

    a={'test':'yangming is hereko','time':str(time.time())}

    return json.dumps(a)


@app.route('/testpost')
def info2():

    a={'test':'++++++++++++','time':str(time.time())}

    return json.dumps(a)






@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)
