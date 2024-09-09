# Algorithm-Visualizer
Algorithm Visualizer
--------------------------------------------------------------
Project Overview

The Algorithm Visualizer is a Python-based application designed to provide visual feedback as popular sorting algorithms are applied to a randomly generated array of integers. The user can choose the size of the array and select from four sorting algorithms: Merge Sort, Bubble Sort, Quick Sort, and Heap Sort. As the algorithm progresses, the elements being compared are highlighted, and once sorted, they are marked in a different color to indicate completion.

This project was created to help users better understand how these sorting algorithms work through visual representation.
--------------------------------------------------------------
Features

Array Size Customization: Users can input the size of the array before it's generated.
Algorithm Selection: Users can choose between four different sorting algorithms.
    Bubble Sort
    Merge Sort
    Quick Sort
    Heap Sort
Visual Feedback: Elements being compared are highlighted in real-time. Once sorted, elements are colored differently to indicate that they are in the correct position.
Real-time Sorting: The sorting process is visualized step-by-step, allowing users to see how each algorithm works.
--------------------------------------------------------------
How to Use

Prerequisites
To run this project, you need Python installed on your system along with the following libraries:
Pygame
You can install Pygame by running:
pip install pygame

Running the Project
Clone this repository:
git clone https://github.com/sheepflamingo/Algorithm-Visualizer.git

Run the main script:
python main.py
You will be prompted to:
Enter the size of the array.
Select the sorting algorithm you want to visualize.
--------------------------------------------------------------
Controls

Start Sorting: The sorting process will begin immediately after you make your algorithm selection.
Pause/Stop: To stop the program, simply close the window.
--------------------------------------------------------------
Sorting Algorithms Overview

Bubble Sort: Simple comparison-based algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order.

Merge Sort: A divide-and-conquer algorithm that splits the array into smaller sub-arrays, sorts them, and then merges them back together.

Quick Sort: A divide-and-conquer algorithm that selects a pivot element and partitions the array into two sub-arrays before sorting them.

Heap Sort: Uses a binary heap data structure to sort elements by building a heap from the input data and extracting the elements one by one.
--------------------------------------------------------------
Future Enhancements

Speed Control: Add a slider for adjusting the sorting speed animation.
Additional Algorithms: Incorporate more sorting algorithms like Insertion Sort or Selection Sort (currently only bubble sort is implmmented).
Pause and Resume: Allow the user to pause and resume the sorting process with a button.
Detailed Algorithm Explanations: Display on-screen explanations of the algorithms during sorting.
--------------------------------------------------------------
Screenshots
--------------------------------------------------------------
License

This project is licensed under the GNU GPL License - see the LICENSE file for details.
--------------------------------------------------------------
Contributing

Suggestions, and bug reports are welcome!





