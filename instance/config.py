import os

class Config(object):
	DEBUG=False
	TESTING=False
	SECRET=os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
	DEBUG=True
	DATABASE_URL="postgresql://localhost/law_db"

class TestingConfig(Config):
	DEBUG=True
	TESTING=True


class StagingConfig(Config):
	DEBUG=True

class ProductionConfig(Config):
	DEBUG=False
	TESTING=False

app_config = {
	"testing":TestingConfig,
	"development":DevelopmentConfig,
	"production":ProductionConfig,
	"staging":StagingConfig
}
