from flask_project import db

class Note(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

class Loggin_User(db.Model):
    __tablename__ = 'loggin_user_info'
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    passwd = db.Column(db.String(64))

class Face_Image_Store(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    imageData = db.Column(db.LargeBinary(length=65536))
    imageName = db.Column(db.String(length=500))
    imageFeature = db.Column(db.String(length=500))
    peopleName = db.Column(db.String(length=500))
#
# class Face_Task_List(db.Model):
#     __table_args__ = {"extend_existing": True}
#     id = db.Column(db.Integer, primary_key=True)
#     videoType = db.Column(db.Integer) # 0离线, 1实时
#     videoAddress = db.Column(db.String(length=1000))
#     taskState = db.Column(db.Integer) # 0未开始, 1正在运行, 2等待运行, 3已完成
#     taskResult = db.Column(db.Integer)
#     taskId = db.Column(db.String(length=500), unique=True)

# class Face_Task_Result_Image(db.Model):
#     __table_args__ = {"extend_existing": True}
#     id = db.Column(db.Integer, primary_key=True)
#     taskId = db.Column(db.String(length=500), unique=True, index=True)
#     imageData = db.Column(db.LargeBinary(length=65536))
#     imageFeature = db.Column(db.String(length=500), unique=True)
#     imageDateTime = db.Column(db.DateTime)

# class Face_Task_Result_Features(db.Model):
#     __table_args__ = {"extend_existing": True}




