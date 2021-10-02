from Bookstore import db

class Book(db.Model):
    
    __tablename__ = 'Books'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    

    def __init__(self,name,author):
       
        self.name = name
        self.author = author

    def __repr__(self):
        return f"Book Name: {self.name} Author Name: {self.author}"