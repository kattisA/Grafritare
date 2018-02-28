#!/usr/bin/python
# -*- coding: cp1252 -*-

'''
Information Technology (1DT051) 2014
Project assignment

Amanda Forsman and Katarina Lejonlid

'''

# Import all the necessary functions and classes for creating graphics.
from graphics import *

# Importing the math package.
import math

# We want to implement random colours.
import random

#Global variables
w_Width = 800
w_Height = 800
half_Width = 0
half_Height = 0

# Settings for the x coordinates and declaration of global variables for y_Max
# and y_Min that will be calculated dynamically in the main loop.

x_Max = 10
x_Min = -10

def main():
    '''
    The start-up main function.
    '''

    # Create a graphical window.

    w = GraphWin("Grafritare", w_Width, w_Height)
    w.setBackground("white")


##    w2_Width = 200
##    w2_Height = 100
##    w2 = GraphWin ("Ange funktion", w2_Width, w2_Height)
##    w2.setBackground("white")
##
##    e = Entry(Point(100, 50), 20)
##    e.draw(w2)
##    w2.getMouse()


    xs = values_X()
    ys = values_Y(function,values_X())
    yxs = values_XY(values_X(),values_Y(function,values_X()))


    points = positions_XY(xs,ys)
     #Divide the values of the window width and height.
    half_Width = divide(w_Width)
    half_Height = divide(w_Height)

    #Create two crossing lines throughout the window.

    p1 = Point(0,half_Height)
    p2 = Point(half_Width,0)
    p3 = Point(w_Width,half_Height)
    p4 = Point(half_Width,w_Height)

    line_X = Line(p1,p3)
    line_Y = Line(p2,p4)
    line_X.draw(w)
    line_Y.draw(w)
    line_X.setWidth(2)
    line_Y.setWidth(2)

    # Draw arrows.
    line_X.setArrow("both")
    line_Y.setArrow("both")

    # Printing a list of x values
    # Printing a list of y values

    print (xs)
    print (ys)
    print (yxs)
    print (points)
    print (make_circles(points, w))
    print (draw_line (points,w))

    # Here we have to add a relevant while loop for our program

    while True:
        # Wait for mouse click
        p = w.getMouse()


def divide(x):
    '''
    Arguments:

    x ::


    Returns :: int
    half of x (axis)

    '''

    half = x / 2
    return half

def values_X():
    '''
    Arguments:


    Returns :: list
    With the value of x min and x max.

    '''

    xs = range(x_Min,x_Max +1)

    return xs

def values_Y(f,xs):
    '''
    Arguments:

    f ::

    xs ::

    Returns :: list
    Create a list with the y variables.

    '''

    ys =[]

    for x in xs:
        ys.append(f(x))

    return ys

def values_XY(xs, ys):
    '''
    Arguments:

    xs ::

    ys ::

    Returns :: list
    Create a list with x- and y varibles (points).

    '''

    yxs = []

    for index in range(len(xs)):
        yxs.append((xs[index],ys[index]))

    return yxs

def positions_XY(xs, ys):
    '''
    Arguments:

    xs ::

    ys ::

    Returns :: list
    With positions for poin10, 10000)]ts.

    '''
    # Y-axis in the coordinate system and the height go to opposite directions.
    # In the case of transforming the y-value to a pixel value we have to turn it
    # around.

    # The values of y_Max will be calculated in relation to the
    # y-values calculated in the ys list. The y_Min is set to the neg of y_Max.
    y_Max = max(ys)
    y_Min = -max(ys)

    print (y_Max)
    print (y_Min)
    delta_X = x_Max - x_Min
    delta_Y = float(y_Max) - float(y_Min)

    print (delta_Y)

    scale_X = w_Width / delta_X
    scale_Y = w_Height / delta_Y


    positions = []

    for index in range(len(xs)):
        px = xs[index] - x_Min
        px = px * scale_X
        py_neg = ys[index] - y_Min
        py_neg= py_neg * scale_Y
        py = w_Height - py_neg

        positions.append([px, py])

    return positions

def make_circles(positions, w):
    '''
    Arguments:

    positions ::

    w ::

    Returns :: list
    With circles to pint out the points in the right position.

    '''

    for pos in positions:
        p = Point(pos[0],pos[1])
        c = Circle(p, 10)
        c.setFill("red")
        c.draw(w)

def draw_line (positions,w):
    '''
    Arguments:

    positions ::

    w ::

    Returns :: list
    with positions for one point and positions from another point. Draws a line between them.

    '''
    # The list of positions holds a value of x and y for every instance of the list.
    # Therefor we need to extract two points to draw a line in between. The range goes
    # to the length -1 to avoid list out of range.

    for index in range(len(positions)- 1):
        pos1 = positions[index]
        p1 = Point(pos1[0], pos1[1])

        pos2 = positions[index + 1]
        p2 = Point (pos2[0], pos2[1])
        l = Line (p1, p2)
        l.setWidth (3)
        l.draw(w)

def function(x):
    '''
    Arguments:

    x ::

    Returns :: Function with points and lines between them.

    '''

    function = x ** 4
    return function


main()
