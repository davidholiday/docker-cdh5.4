#!/usr/bin/env python

import cherrypy
import foxy
import os

class Foxy(object):
    @cherrypy.expose
    def index(self):
        foxy.generate_app()
        return file("./Static/index.html")      
    
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/Static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './Static'
        },
        '/Data': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './Data'
        }
    }
    cherrypy.quickstart(Foxy(), '/', conf)
