#!/usr/bin/env python

import cherrypy
import foxy
import os
import subprocess




class Foxy(object):
    @cherrypy.expose
    def index(self):
        foxy.generate_app()
        return file("./Static/index.html")      
   




    @cherrypy.expose
    def start(self, container):
        output = subprocess.Popen(["docker", "start", container], stdout=subprocess.PIPE).communicate()[0]
        raise cherrypy.HTTPRedirect("/")
        #foxy.generate_app()
        #return file("./Static/index.html")




    @cherrypy.expose
    def stop(self, container):
        output = subprocess.Popen(["docker", "stop", container], stdout=subprocess.PIPE).communicate()[0]
        raise cherrypy.HTTPRedirect("/")
        #foxy.generate_app()
        #return file("./Static/index.html")




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
