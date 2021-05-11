from app import db, Users

db.drop_all()
db.create_all()

user_1 = Users(first_name="Fardin" , last_name="Shah" )
db.session.add(user_1)
db.session.commit()