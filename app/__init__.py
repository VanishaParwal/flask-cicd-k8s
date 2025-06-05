from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # In-memory "DB"
    app.books = []

    # Register all routes
    from app.routes import register_routes
    register_routes(app)

    @app.route("/test")
    def test():
        return "Hello, Flask is working!"

    return app
