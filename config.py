# config.py

class Config(object):
	"""
	Common configuration parameters
	"""

	# Put any configuration information common to all environments

class DevelopmentConfig(Config):
	"""
	Development configuration parameters
	"""

	# Enable Flask debug mode
	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production configuration parameters
	"""

	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
