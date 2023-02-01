from flask import Flask

### initialise flask
def create_app():
    app = Flask(__name__) # name of file thats run 
    app.config["SECRET_KEY"] = "rhfodjosdhsfhifhs" # secure/encript session data
    
    from .views import views
    #from .auth import auth
    # how to access url prefix
    app.register_blueprint(views, url_prefix="/")
    #app.register_blueprint(views, url_prefix="/experience")
    #app.register_blueprint(views, url_prefix="/projects")
    #app.register_blueprint(views, url_prefix="/contact")
    #app.register_blueprint(auth, url_prefix="/")
    
    return app

