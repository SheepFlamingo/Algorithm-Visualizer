import pygame
import time

class BubbleSort:
    def __init__(self, array, visualizer):
        self.array = array
        self.visualizer = visualizer


    def sort(self):
        print(self.array)
        
        if len(self.array) < 2:
            return self.array
        
        indexing_length = len(self.array) - 1 #Cannot apply comparision starting with the last item of list bc there is no item to the right of it.
        sorted = False
        while not sorted:

            sorted = True

            for i in range(0, indexing_length):
                print(f"Comparing: {self.array[i]} and {self.array[i + 1]}")

                # Visualize the comparison between two elements
                self.visualizer.draw_array(self.array, highlight=[i, i+1])
                pygame.time.delay(100)

                if self.array[i] > self.array[i+1]: #if current element is greater than the element to the right, then it needs to be sorted.
                    sorted = False
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i] #swapping places

                    print(f"Swapping: {self.array[i]} and {self.array[i + 1]}")
                    
                    # Visualize the array after the swap
                    self.visualizer.draw_array(self.array, highlight=[i, i+1])
                    pygame.time.delay(100)
            
            # Reduce the range of comparison since the largest element is sorted.
            indexing_length -= 1

            # Visualize the sorted portion of the array
            self.visualizer.draw_array(self.array, sorted_idx=len(self.array) - indexing_length - 1)
            pygame.time.delay(100)
        
        # Final visual when sorting is complete
        self.visualizer.draw_array(self.array, sorted_idx=0)
        pygame.time.delay(100)

        print(self.array)

        return self.array