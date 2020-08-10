from  application import  *
from  flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application.common import db
from  application.model import model


app = create_app('default')
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)





if __name__ == '__main__':

    manager.run(debug = True)