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
        logging.debug(f'Robosim instantiation {self}')
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        self.window = glutCreateWindow("Robosim")
        if not self.window:
            logging.debug('Failed to create self.window')

        glutDisplayFunc(self.show_view)
        glutIdleFunc(self.show_view)
        glutMainLoop()
        logging.debug('Robosim completeed instantiation')

    def iterate(self):
        glViewport(0, 0, 500,500)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()

    def square(self):
        # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
        glBegin(GL_QUADS) # Begin the sketch
        glVertex2f(100, 100) # Coordinates for the bottom left point
        glVertex2f(200, 100) # Coordinates for the bottom right point
        glVertex2f(200, 200) # Coordinates for the top right point
        glVertex2f(100, 200) # Coordinates for the top left point
        glEnd()

    def show_view(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glColor3f(3.0, 0.0, 3.0) ;# Set the color to pink
        self.square()
        glutSwapBuffers()

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
