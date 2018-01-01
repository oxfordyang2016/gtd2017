



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
