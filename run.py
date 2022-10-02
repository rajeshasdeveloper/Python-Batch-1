from app import app
from waitress import serve

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=4444)
    # serve(app, host="0.0.0.0", port=4444)
    gunicorn_app = app()
else:
    gunicorn_app = app()