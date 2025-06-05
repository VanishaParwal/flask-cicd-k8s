from flask import Blueprint

# Import each blueprint
from .books import books_bp

# Function to register all Blueprints
def register_routes(app):
    app.register_blueprint(books_bp, url_prefix="/api/books")
