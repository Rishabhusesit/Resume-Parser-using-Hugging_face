from flask import Flask
from flask_cors import CORS
from backend.routes import init_routes
from backend.models import db
from flask_migrate import Migrate
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()


CORS(app)  
init_routes(app)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)