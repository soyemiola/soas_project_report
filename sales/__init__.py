from flask import Flask
from sales.config import Config
import os
import geocoder



baseURL = 'http://localhost:5000/api/v1/'


def get_country_from_ip(ip_address):
	g = geocoder.ip(ip_address)

	ip_country = g.country

	return ip_country


def countries():
	file_path = os.path.join(os.path.dirname(__file__)+'\\static\\assets\\country.txt')
	
	try:
		with open(file_path, 'r') as file:
			lines = file.readlines()
			file.close()
			
			val = ','.join(lines)
			country = val.split(',')
			print(country)
			return country
	except FileNotFoundError:
		return None



def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	from sales.users.user import user
	from sales.users.team.member import member
	from sales.users.team.department import department
	from sales.users.clients.client import client
	from sales.users.project.project import project


	app.register_blueprint(user, url_prefix='/')
	app.register_blueprint(member, url_prefix='/')
	app.register_blueprint(department, url_prefix='/')
	app.register_blueprint(client, url_prefix='/')
	app.register_blueprint(project, url_prefix='/')


	return app

	