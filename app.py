from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    # Initialize the database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Import Blueprints inside create_app to avoid circular imports
    from routes.home import bp as home_bp
    from routes.random import bp as random_bp
    from routes.search import bp as search_bp
    from routes.add import bp as add_bp

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(random_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(add_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
