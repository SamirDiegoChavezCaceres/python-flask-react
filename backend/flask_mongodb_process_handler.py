from src.app.flask_mongodb.create_flask_mongodb_app \
    import create_flask_postgresql_app
from src.infra.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_postgresql_app(logger)
    flask_memory_app.run(debug=True)
