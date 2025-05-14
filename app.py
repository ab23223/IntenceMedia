from bottle import run,route,template, static_file
import requests

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