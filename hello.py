import codecs
def app(environ, start_response):
    """A barebones WSGI application.

    This is a starting point for your own Web framework :)
    """
    path = environ['PATH_INFO']
    print path

    str=path.split('.',1)
    str1=path.split('/',1)
    routes = ["/a.html", "/hello.html"]
    if len(str)==2:
        if str[1] == "html":
            if path in routes:
                print path
                status = '200 OK'
                response_headers = [('Content-Type', 'text/html')]
                start_response(status, response_headers)
                f = codecs.open(str1[1], "r", "utf-8")
                content = f.read()
                f.close()
                return content
            else:
                status = '404 Not Found'
                response_headers = [('Content-Type', 'text/plain')]
                start_response(status, response_headers)
                return '404 Not Found!'
        else:
            start_response('200 OK', [('Content-Type', 'text/html')])
            str2=str1[1].split('.',1)
            return '<h1>Hello, %s!</h1>' % (str2[0] or 'web')
    else:
        #status = '200 OK'
        #response_headers = [('Content-Type', 'text/plain')]
        #start_response(status, response_headers)
        #print "aaaaaaaa"
        start_response('200 OK', [('Content-Type', 'text/html')])
        return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
        #return ['Hello world from a simple WSGI application!\n']

