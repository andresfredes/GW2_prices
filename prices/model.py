from prices import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Item {self.id}>"