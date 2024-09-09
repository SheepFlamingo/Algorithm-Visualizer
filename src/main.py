import pygame
import random
import sys
from const import width, height
from visualizer import Visualizer
from sorting_algorithms.bubble_sort import BubbleSort
"""
from sorting_algorithms.merge_sort import MergeSort
from sorting_algorithms.quick_sort import QuickSort
from sorting_algorithms.heap_sort import HeapSort
"""

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(( width, height ))
        pygame.display.set_caption("Algorithm Visualizer")
        self.visualizer = Visualizer(self.screen, width, height)

    def main_loop(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Get user input for array size
            arr_size = int(input("Please input the size of the array: "))
            array = [random.randint(1,100) for _ in range(arr_size)]

            # Ask user for algorithm choice
            print("Select sorting algorithm:")
            print("1. Bubble Sort")
            print("2. Merge Sort")
            print("3. Quick Sort")
            print("4. Heap Sort")
            algo_choice = int(input("Enter choice (1-4): "))

            if algo_choice == 1:
                algorithm = BubbleSort(array, self.visualizer)
            elif algo_choice == 2:
                algorithm = MergeSort(array, self.visualizer)
            elif algo_choice == 3:
                algorithm = QuickSort(array, self.visualizer)
            elif algo_choice == 4:
                algorithm = HeapSort(array, self.visualizer)
            else:
                print("Invalid choice.")
                return
            
            # Run the selected algorithm
            algorithm.sort()

            pygame.display.update()

""" Create an instance of Main, then run the main loop. """
main = Main()
main.main_loop()
