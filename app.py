from bottle import run, route, template, static_file, response

# Static file serving
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


# Main routes
@route('/')
def index():
    return template('index')

@route('/First-XI-vs-Westlake-22-07')
def FirstXIvsWestlake():
    return template('First-XI-vs-Westlake-22-07')

@route('/First-V-vs-Dilworth-23-07')
def FirstVvsDilworth():
    return template('First-V-vs-Dilworth-23-07')

@route('/First-V-vs-AGGS-25-07')
def FirstVvsAGGS():
    return template('First-V-vs-AGGS-25-07')

@route('/category-automotive')
def categoryautomotive():
    return template('category-automotive')

@route('/Training-15-05')
def Training1505():
    return template('Training-15-05')

@route('/Training-19-05')
def Training1905():
    return template('Training-19-05')

@route('/Choir-11-06')
def Choir1106():
    return template('Choir-11-06')  # Make sure you renamed your template to match this route

@route('/First-XV-14-06')
def FirstXV1406():
    return template('First-XV-14-06')  # Make sure you renamed your template to match this route

@route('/about')
def about():
    return template('about')

@route('/contact')
def contact():
    return template('contact')

@route('/googlec84cb0ca6911faab.html')
def google_verification():
    return template('googlec84cb0ca6911faab.html')

@route('/sitemap.xml')
def sitemap():
    response.content_type = 'application/xml'
    return template('sitemap.xml')


# Run the server
run(reloader=True)
