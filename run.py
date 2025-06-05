from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
# The above code initializes a Flask application and runs it in debug mode.
# The `create_app` function is imported from the `app` module, which sets up the application and registers the necessary routes.      