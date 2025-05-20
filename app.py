from bottle import run,route,template, static_file, response
import requests
import cloudinary
import cloudinary.api
import json

# 🔐 Your Cloudinary credentials
cloudinary.config(
    cloud_name='dfqreujbo',
    api_key='467879367759351',
    api_secret='tgJspwPABIOzKQrG3YSeb7YAx2g'
)

@route('/images')
def get_images():
    folder = 'Training 19-05'  # Your Cloudinary folder
    try:
        result = cloudinary.api.resources(type='upload', prefix=f'{folder}/', max_results=100)
        urls = [item['secure_url'] for item in result['resources']]
        response.content_type = 'application/json'
        return json.dumps(urls)
    except Exception as e:
        response.status = 500
        return str(e)


@route('/static/<filepath:path>')
def server_static(filepath):
     return static_file(filepath, root='./static')


@route('/')
def index():
     return template('index')


@route('/category-sports')
def categorysports():
     return template('category-sports')

@route('/category-automotive')
def categoryautomotive():
     return template('category-automotive')

@route('/Training-15-05')
def Training1505():
     return template('Training-15-05')

@route('/Training-19-05')
def Training1905():
     return template('Training-19-05')

@route('/Training-15-05')
def Training1505():
     return template('Training-15-05')

@route('/about')
def about():
     return template('about')

@route('/contact')
def contact():
     return template('contact')

@route('/googlec84cb0ca6911faab.html')
def googlec84cb0ca6911faab():
     return template('googlec84cb0ca6911faab.html')

@route('/sitemap.xml')
def sitemap():
     return template('sitemap.xml')


#main
run(reloader=True)