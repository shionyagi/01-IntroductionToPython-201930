"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Shion.
"""
########################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg


Shion = rg.SimpleTurtle('turtle')
Shion.pen = rg.Pen('midnight blue', 3)
Shion.speed = 20  # Fast


# The first square will be 300 x 300 pixels:
size = 150

# Do the indented code 6 times.  Each time draws a square.
for k in range(6):

    # Put the pen down, then draw a square of the given size:
    Shion.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    Shion.pen_up()
    Shion.right(45)
    Shion.forward(10)
    Shion.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    Shion.pen_down()
    size = size - 12
########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
window = rg.TurtleWindow()
window.tracer(100)  # Bigger numbers make the animation run faster

another_turtle = rg.SimpleTurtle('triangle')
another_turtle.pen = rg.Pen('magenta', 1)
another_turtle.backward(50)
another_turtle.speed = 5
# The name k takes on the values 0, 1, 2, ... 499 as the loop runs
for k in range(500):
    another_turtle.left(90)
    another_turtle.forward(100)
    another_turtle.forward(k)
window.close_on_mouse_click()