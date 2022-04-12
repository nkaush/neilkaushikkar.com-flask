APP_EXPORT = export FLASK_APP='flaskr/app.py'

DEBUG_ENV_EXPORT = export FLASK_ENV=development
PROD_ENV_EXPORT = export FLASK_ENV=production

DEBUG = export FLASK_DEBUG=1

debug: 
	$(APP_EXPORT) && $(DEBUG_ENV_EXPORT) && $(DEBUG) && flask run

prod: 
	$(APP_EXPORT) && $(PROD_ENV_EXPORT) && python3 -m flask run --host=0.0.0.0