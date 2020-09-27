#!/usr/bin/env python3
import logging
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Robosim(object):
    """
    """
    def __init__(self):
        pass

    def show_view(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        self.window = glutCreateWindow("Robosim")
        glutDisplayFunc(self.show_view)
        glutIdleFunc(self.show_view)
        glutMainLoop
        

def main():
    logging.basicConfig(format='%(asctime)s %(name)s'
                        ' %(levelname)s - %(message)s',
                        filename='robosim-trial.log',
                        level=logging.DEBUG)
    logging.info("Starting main execution.")
    R = Robosim()
    R.show_view()
    logging.info("Completing main execution")

    
main()
