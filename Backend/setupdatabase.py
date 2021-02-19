from app import db,Meme

# delete all data
db.session.query(Meme).delete()
db.session.commit()

# create all the tables
db.create_all()
