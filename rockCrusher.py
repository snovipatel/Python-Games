# Name: Snovi Patel
# Rock Crusher

'''
Purpose: This program creates a simple game where a ball bounces around the screen. 
The player clicks to place rocks, and the ball hits them. When the ball hits a rock, 
the rock changes color based on how many times it has been hit (first hit = yellow, second or more = green)
The game continues until the ball moves a certain number of times.

'''

from graphics import * # Imports graphics library
from math import *     # Imports math library
import random          # Imports random library


# Purpose: Prompts the user to click n times to place rocks on the screen.
# Inputs: n - Number of rocks to place
# Output: A list of rock objects placed by the user

def generateRocks(n, win):
    rockList = []
    
    for i in range(n):
        click_point = win.getMouse()  # Wait for user click to place a rock
        rock = Circle(click_point, 20)  # Create a rock (circle with radius 20)
        rock.setFill("red")    # Initial color is red
        rock.draw(win)
        rockList.append(rock)  # Add rock to the list
        
    return rockList  # Return the list of rocks




# Purpose: Creates a list to track number of times each rock is hit
# Input: (n) Number of rocks
# Output: returns a list with n zeroes

def buildHitList(n):
    hitList = [0] * n  # Make a list of zeros, one for each rock
    return hitList




# Purpose: Calculates the distance between two points
# Inputs: point1 and point2
# Output: distance between the two points

def distance(point1, point2):
    x1, y1 = point1.getX(), point1.getY() # Get x and y from point1
    x2, y2 = point2.getX(), point2.getY() # Get x and y from point2
    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Use the distance formula 
    return dist # Return the distance




# Purpose: Checks if the ball and rock are touching
# Input: ball (Circle), rock (Circle)
# Output: True if they touch, otherwise False

def didCollide(ball, rock):
    ball_center = ball.getCenter() # Get center of the ball
    rock_center = rock.getCenter() # Get center of the rock
    dist = distance(ball_center, rock_center) # Calculate distance between centers
    
    # Return True if distance is less than or equal to the sum of the radii
    return dist <= (ball.getRadius() + rock.getRadius())




# Purpose: Checks if the ball hit the left or right wall
# Input: ball (Circle)
# Output: True if it hits a vertical wall, else False

def hitVertical(ball, win):
    ball_center = ball.getCenter() # Get the center of the ball
    ball_x = ball_center.getX() # Get x coordinate of the center
    
    #if the ball touches the left or right edge
    if ball_x <= ball.getRadius() or ball_x >= win.getWidth() - ball.getRadius():
        return True
    else:
        return False
    
    
    
    
# Purpose: Checks if the ball hit the top or bottom wall
# Input: ball (Circle)
# Output: True if it hits a horizontal wall, else False

def hitHorizontal(ball, win):
    ball_center = ball.getCenter()
    ball_y = ball_center.getY()
    
    #if the ball touches the top or bottom edge
    if ball_y <= ball.getRadius() or ball_y >= win.getHeight() - ball.getRadius():
        return True
    else:
        return False
    
    
    
    
# Purpose: Creates and returns a random RGB color
# Input: None
# Output: A random color using color_rgb()

def randomColor():
    r = random.randint(0, 255) # Random red value (0–255)
    g = random.randint(0, 255) # Random green value
    b = random.randint(0, 255) # Random blue value
    
    return color_rgb(r, g, b) # Return the color



# Purpose: Runs the Rock Crusher game

def playGame():
    
    win = GraphWin("Rock Crusher", 800, 600) # Create a window 800x600
    win.setBackground("lightblue") # Set background color to light blue
    
    instructions = Text(Point(400, 20), "Click to place 5 rocks.") # Create instruction text
    instructions.setTextColor("black") # Set text color to black
    instructions.setSize(17) # font size
    instructions.draw(win)
    
    # Create ball
    ball = Circle(Point(400, 300), 15) # Make a ball at center with radius 15
    ball.setFill(randomColor()) # Give the ball a random color
    ball.draw(win)
    
    num_rocks = 5 # Number of rocks to place
    rocks = generateRocks(num_rocks, win) # Ask user to place rocks by clicking
    hit_counts = buildHitList(num_rocks) # Track how many times each rock is hit
    
    # Set starting horizontal and vertical speed
    dx = random.choice([-4, 4])
    dy = random.choice([-4, 4])

    instructions.setText("Game Started! Try to turn rocks green!") # Update instructions

    
    for i in range(1000):  # number of movement steps
        ball.move(dx, dy) # Move the ball by dx and dy
        time.sleep(0.03) # Pause for a short time
        

        # Wall collision: reverse direction + random color
        if hitVertical(ball, win):
            dx *= -1 # Reverse horizontal direction
            ball.setFill(randomColor()) # Change the ball’s color

        if hitHorizontal(ball, win):
            dy *= -1 # Reverse vertical direction
            ball.setFill(randomColor())
            
            

        # Rock collisions
        for i in range(num_rocks): # each rock
            if didCollide(ball, rocks[i]):  # If ball touches rock increase hit count
                hit_counts[i] += 1

                
                dx = random.choice([-4, -3, 3, 4, 5]) # Change horizontal speed
                dy = random.choice([-4, -3, 3, 4, 5]) # Change vertical speed
                
                ball.move(dx, dy)  

                # Update rock color based on hits
                if hit_counts[i] == 1:
                    rocks[i].setFill("yellow") # First hit = yellow
                elif hit_counts[i] >= 2:
                    rocks[i].setFill("green") # Second or more = green

    # End of game, update instruction and click to close window
    instructions.setText("Game Over! Click anywhere to exit.")
    win.getMouse()
    win.close()

playGame() 