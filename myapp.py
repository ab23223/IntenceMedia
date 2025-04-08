from bottle import run,route,template, static_file
import requests

@route('/static/<filepath:path>')
def server_static(filepath):
     return static_file(filepath, root='./static')


@route('/')
def index():
     return template('homepage')

@route('/index')
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

#main
run(reloader=True)