from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    

    def __init__(self,password, username, name):
        self.set_password(password)
        self.username=username
        self.name=name

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'name': self.name
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


