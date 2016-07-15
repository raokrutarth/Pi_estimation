from graphics import *
import random
import math

## Krutarth Rao
# Plots a square on the center of the screen with given squareLength
# window: Your window, type: GraphWin object
# squareLength: Length of one side of your square, type: integer
def plotSquare(window, squareLength):        
        
        second_corner =(500-squareLength)/2
        first_corner = ((500-squareLength)/2) + squareLength         
        
        square = Rectangle(Point(first_corner, first_corner), Point(second_corner, second_corner))	
        square.setWidth(5)        
        square.draw(window)
 
# Plots a circle on the center of the screen with given circleRadius and color
# window: Your window, type: GraphWin object
# circleRadius: Radius of your circle, type: integer
# color: Color that your circle will be filled in with, type: string


def plotCircle(window, circleRadius, color):

        center_point = Point(250, 250) 
        circle = Circle(center_point, circleRadius)
        circle.setFill(color)
        circle.draw(window)


    
# Plots random points into the square with appropriate colors
# window: Your window, type: GraphWin object
# squareLength: Length of one side of your square, type: integer
# numberOfPoints: Number of points to plot, type integer
# RETURNS: (integer, integer) tuple, first one is yellow and second is black
def plotPoints(window, squareLength, numberOfPoints):

                second_corner = int((500-squareLength)/2)
                first_corner = int(((500-squareLength)/2) + squareLength)
                yellow_counter = 0
            
                for i in range(numberOfPoints):

                    point = Point( random.randint(second_corner,first_corner),
                                   random.randint(second_corner,first_corner))
                    
                    point_x_minusC = point.getX() - 250
                    point_y_minusC = point.getY() - 250

                    test_value = math.sqrt((math.pow(point_x_minusC,2) + math.pow(point_y_minusC,2)))                
                    

                    if test_value < (squareLength/2):
                        point.setFill('yellow')
                        yellow_counter = yellow_counter + 1

                    point.draw(window)

                
                black_counter = int(numberOfPoints - yellow_counter)                
                return yellow_counter , black_counter

                    
# Estimates the Pi using the number of yellow and black points
# yellow: Number of yellow points, type: integer
# black: Number of black points, type: integer
# RETURNS: estimated Pi, type: float
def estimatePi(yellow,black):

        estimated_pi = float((4.0*yellow) / (yellow + black))       
        return estimated_pi
        
 
def main():
 
	# Set length of the sides of window
	winlength = 500	
 
	# Get length of the sides of square from user
	squareLength = eval(input("What is the size of one side of the square (0<n<500): "))
	
	# Get circle color from user
	circleColor = input("What is the color for circle (red,green,blue): ")

	# Get number of points from user
	numberOfPoints = eval(input("How many random points: "))
 
	# Create your window: GraphWin object
	window = GraphWin("My Window", winlength, winlength)	
 
	# Plot square with given length
	plotSquare(window, squareLength)	
 
	# Plot circle with given color inside square
	plotCircle(window, (squareLength/2), circleColor)	
 
	# Plot points into the square, use plotPoints() function.
	yellow , black = plotPoints(window, squareLength, numberOfPoints)
 
	# Estimate pi using number of yellow and black points
	# you get from plotPoints() function. Use estimatePi() function.   	
	estimate_pi = estimatePi(yellow, black)
	# Print estimated pi
	print("Estimated pi : %.4f " % estimate_pi)
	
	# Print number of points plotted
	print("Number of random points plotted: ",numberOfPoints)
 
	# window.getMouse()
	# window.close()
	window.getMouse()
	window.close()
## Krutarth Rao 
 
main()
