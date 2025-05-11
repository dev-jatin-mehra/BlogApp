import jwt
import time
from datetime import datetime
from flask import current_app
from app import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(50),nullable=False,default='default.jpeg')
    password = db.Column(db.String(60),nullable=False)
    post = db.relationship('Post',backref='author',lazy=True)

    def get_reset_token(self,expire_sec=1800):
        payload = {"user_id": self.id, "exp": int(time.time()) + expire_sec}
        return jwt.encode(payload, current_app.config['SECRET_KEY'],algorithm="HS256")
    
    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
        except jwt.ExpiredSignatureError:
            return None
        
        except jwt.InvalidTokenError:
            return None  
        
        return User.query.get(user_id)
         

    def __repr__(self): 
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default = datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    


