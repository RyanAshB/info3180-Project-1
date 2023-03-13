from . import db

class Property(db.Model):

    # Attributes
    __tablename__ = 'properties'  # Table Name

    id = db.Column(db.Integer, primary_key=True)
    propTitle = db.Column(db.String(80))
    description = db.Column(db.Text())
    roomNum = db.Column(db.String(2))
    bathroomNum = db.Column(db.String(2))
    price = db.Column(db.String(20))
    propType = db.Column(db.String(20))
    location = db.Column(db.String(200), unique=True)
    file = db.Column(db.String(150))

    # Constructor
    def __init__(self, propTitle, description, roomNum, bathroomNum, price, propType, location, file):
        self.propTitle = propTitle
        self.description = description
        self.roomNum = roomNum
        self.bathroomNum = bathroomNum
        self.price = price
        self.propType = propType
        self.location = location
        self.file = file
    # --------------------------------------------------------------------

    # Other Methods
    def __repr__(self):
        return '<Property %r>' % self.propTitle

    def get_id(self):
        return str(self.id)

