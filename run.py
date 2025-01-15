from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)


'''
!!!  before launching the create the database !!! 

from flaskblog import db, create_app

app = create_app()
with app.app_context():
    db.create_all()
'''