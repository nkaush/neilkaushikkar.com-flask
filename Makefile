SHELL := /bin/bash

debug: 
	source ./env.sh && flask run

production: 
	waitress-serve --call 'flaskr:app'