from App import db

class Vuelos(db.Model):
    __tablename__ = 'vuelos'

    id = db.Column(db.Integer, primary_key=True)
    vuelo = db.Column(db.String())
    compañia = db.Column(db.String())
    hora = db.Column(db.Date())

    def __init__(self, vuelo, compañia, hora):
        self.vuelo = vuelo
        self.compañia = compañia
        self.hora = hora

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'vuelo': self.vuelo,
            'compañia': self.compañia,
            'hora':self.hora
        }
