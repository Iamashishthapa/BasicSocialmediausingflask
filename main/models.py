from datetime import datetime
from main import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    image =db.Column(db.String(20),nullable=False,default="defaul.jpg")
    password = db.Column(db.String(100))
    posts=db.relationship('Post',backref='author',lazy=True)
    
    def __init__(self,name,email,password):
        self.name=name
        self.email=email 
        self.password=password
        db.create_all()

        
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    
    def __init__(self,title,content,author):
        self.title=title
        self.content=content
        self.user_id=author


db.create_all()