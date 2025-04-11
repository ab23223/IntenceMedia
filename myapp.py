from bottle import run,route,template, static_file
import requests

@route('/static/<filepath:path>')
def server_static(filepath):
     return static_file(filepath, root='./static')


@route('/')
def index():
     return template('index')

@route('/gallery')
def gallery():
     return template('gallery')

@route('/competitions')
def competitions():
     return template('competitions')

@route('/competitions1')
def competitions1():
     return template('competitions1')

@route('/hi2')
def hi2():
     return template('hi2')

@route('/services')
def services():
     return template('services')

@route('/packages')
def packages():
     return template('packages')

@route('/portfolio')
def portfolio():
     return template('portfolio')

@route('/work')
def work():
     return template('work')

@route('/work')
def work():
     return template('work')

@route('/contact')
def contact():
     return template('contact')

@route('/googlec84cb0ca6911faab.html')
def googlec84cb0ca6911faab():
     return template('googlec84cb0ca6911faab.html')


#main
run(reloader=True)