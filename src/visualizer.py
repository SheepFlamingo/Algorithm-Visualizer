from const import white, blue, red, green
import pygame

class Visualizer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw_array(self, array, highlight=None, sorted_idx=None):
        """
        DESCRIPTION
            This method is responsible for drawing the current state of the array on the screen

        PARAMETERS:
            array: list of numbers to be drawn
            highlight: list of indexes that are being compared or swapped. these indexes are visually highlighted
            sorted_idx: the index (or range) of elements that have been sorted. These elements are displayed in a different color to indicate completion.
        """
        bar_width = self.width // len(array) #calcs width of each bar representing to an element of the array by ensures the screen width is divided evenly across all array elements.
        max_val = max(array) #used to normalize the height of the bars relative to the largest value in the array.
        self.screen.fill(white)

        for i, val in enumerate(array):
            color = blue
            if highlight and i in highlight:
                color = red
            elif sorted_idx and i >= sorted_idx:
                color = green

            bar_height = val * (self.height / max_val)  # Normalize bar height
            pygame.draw.rect(self.screen, color, 
                            (i * bar_width, self.height - bar_height,  # x and y positions
                            bar_width, bar_height))  # width and height of bar
        pygame.display.update()