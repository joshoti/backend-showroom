from home.helper.config import create_flask_app

app = create_flask_app(__name__)

if __name__ == '__main__':
    app.run()