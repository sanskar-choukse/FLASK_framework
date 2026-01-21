# __init__.py ka main kaam package banane ke saath saath doosre modules/files ko import karna aur Flask app initialize karna hai.

from flask import Flask
from routes.auth import auth_bp  #login blueprint



def create_app():
    app=Flask(__name__)
    
    app.secret_key='my-secret-key'
    
    app.register_blueprint(auth_bp)
    
    return app









