from graphics import *

class Button:
    def __init__(self, rect, label):
        """Initialize a new Button object.
        Parameters: rect, a Rectangle object defining
                        the extent and location 
                        of the button
                    label, a label to appear on top of       the rectangle
        Preconditions: 
            The rectangle should be in the correct 
            location relative to the window.
            The label should be centered on (0,0).
        """
        self.rect = rect
        self.label = label
        
    def getCenter(self):    
        """Return a Point representing the center of 
        this Button's rectangle
        """
        return self.rect.getCenter()
    
    def draw(self, win):
        """Draw the button rectangle and label 
        in the given GraphWin
        """
        # Draw the button's rectangle
        self.rect.draw(win)
        
        # Move the label into place and draw it too
        center = self.getCenter()
        self.label.move(center.getX(), center.getY())
        self.label.draw(win)
        
    def wasClicked(self, click):
        """Given a Point representing where the mouse was clicked, return True if this Button was clicked.
        """
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        return (p1.getX() <= click.getX() <= p2.getX()) and \
               (p1.getY() <= click.getY() <= p2.getY())
 
