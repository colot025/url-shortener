from url_shortener import create_app
from url_shortener.extensions import db

# Create the Flask application instance
app = create_app()

# Initialize the database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

