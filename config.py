from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseConfig:
    """ Base env configuration."""

    # server settings
    DEBUG = False
    TESTING = False
    PORT = getenv("PORT", 5000)
    try:
        PORT = int(PORT)
    except ValueError:
        raise TypeError("PORT must be defined as an integer number.")

    SECRET_KEY = getenv("SECRET_KEY", None)

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 3600

    # Example:
    # Postgres: postgres://{db_user}:{db_password}@{db_endpoint}/{db_name}
    # SQLite: sqlite:///local_data.db
    DB_TYPE = getenv("DB_TYPE")
    DB_USERNAME = getenv("DB_USERNAME")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_ENDPOINT = getenv("DB_ENDPOINT")
    DB_NAME = getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}/{DB_NAME}"
    )


class ProductionConfig(BaseConfig):
    """Production configuration."""

    pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True


class StagingConfig(BaseConfig):
    """Staging configuration."""

    DEBUG = True


class LocalConfig(BaseConfig):
    """Local configuration."""

    DEBUG = True

    # in-memory sqlite database for easy usage/dev
    SQLALCHEMY_DATABASE_URI = "sqlite:///local_data.db"


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    # in-memory sqlite database for testing
    SQLALCHEMY_DATABASE_URI = "sqlite://"


def get_env_config() -> str:
    config_type = getenv("ENVIRONMENT_CONFIG", "local")
    if config_type not in ["local", "dev", "staging", "test", "production"]:
        raise ValueError(
            "The environment config value has to be within these values: local, dev, staging, test, production."
        )
    return CONFIG_MAP[config_type]


CONFIG_MAP = {
    "local": {"config": "config.LocalConfig", "port": LocalConfig.PORT},
    "dev": {"config": "config.DevelopmentConfig", "port": DevelopmentConfig.PORT},
    "staging": {"config": "config.StagingConfig", "port": StagingConfig.PORT},
    "test": {"config": "config.TestingConfig", "port": TestingConfig.PORT},
    "production": {"config": "config.ProductionConfig", "port": ProductionConfig.PORT},
}
