# from models import User, db
# from app import app

# # Create all tables
# db.drop_all()
# db.create_all()

# # If table isn't empty, empty it
# User.query.delete()

# # Add users
# alan_alda = User(first_name='Alan', last_name="Alda")
# joel_burton = User(first_name='Joel', last_name="Burton")
# jane_smith = User(first_name='Jane', last_name="Smith")

# # Add new objects to session, so they'll persist
# db.session.add(alan_alda)
# db.session.add(joel_burton)
# db.session.add(jane_smith)

# # Commit--otherwise, this never gets saved!
# db.session.commit()
