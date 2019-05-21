from app import create_app
from flask_script import Manager, Server
# We import the Manager class from flask-script that will initialize
# our extension and the Server class that helps us launch
# our application.

# Creating app instance 
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
