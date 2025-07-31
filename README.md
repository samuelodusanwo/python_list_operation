# 🐍 Python List Operations Assignment

## Project Description
This repository contains a simple Python script demonstrating fundamental operations and methods used with Python lists. This assignment is designed to practice creating, modifying, and querying lists, which are essential data structures in Python.

## 🎯 Objective
The primary objectives of this assignment were to:
* Understand how to create and initialize a Python list.
* Practice common list modification methods (`append`, `insert`, `extend`, `pop`).
* Learn how to sort a list in ascending order.
* Discover how to find the index of a specific element within a list.

## ✨ Features / Tasks Performed
The `list_operations.py` script performs the following sequence of operations on a single list:

1.  **List Creation:** Creates an empty list.
2.  **Element Appending:** Adds multiple elements (10, 20, 30, 40) to the end of the list.
3.  **Element Insertion:** Inserts a specific value (15) at a designated position (second position/index 1).
4.  **List Extension:** Appends all elements from another list ([50, 60, 70]) to the current list.
5.  **Element Removal:** Removes the last element from the list.
6.  **List Sorting:** Sorts the list in ascending numerical order.
7.  **Index Finding:** Locates and prints the index of a specific value (30) within the sorted list.

## 🚀 How to Run the Program
To run this Python script on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/python-list-operations-assignment.git](https://github.com/your-username/python-list-operations-assignment.git)
    cd python-list-operations-assignment # Navigate into the project directory
    ```
    *(Replace `your-username` with your actual GitHub username.)*

2.  **Execute the Python Script:**
    ```bash
    python list_operations.py
    ```
    **Note:** If you don't have Python installed on your machine, you'll need to download and install it first. You can find instructions and downloads on the official Python website: [python.org](https://www.python.org/downloads/)

### Expected Output Example:
(The exact output might vary slightly depending on your Python version or if you added more print statements, but the core list transformations will be the same.)

Initial list: []
After appending 10, 20, 30, 40: [10, 20, 30, 40]
After inserting 15 at index 1: [10, 15, 20, 30, 40]
After extending with [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]
After removing the last element: [10, 15, 20, 30, 40, 50, 60]
After sorting in ascending order: [10, 15, 20, 30, 40, 50, 60]
The index of the value 30 in my_list is: 3


## 📂 Project Structure
.
├── list_operations.py   # The main Python script demonstrating list operations
└── README.md            # This README file


## 🧠 Key Concepts Demonstrated
* **List Initialization:** Creating an empty list.
* **List Mutability:** Lists can be changed after creation.
* **`list.append()`:** Adding elements to the end of a list.
* **`list.insert()`:** Adding an element at a specific index.
* **`list.extend()`:** Adding all elements from another iterable.
* **`list.pop()`:** Removing elements by index (or the last element by default).
* **`list.sort()`:** Sorting the list in-place.
* **`list.index()`:** Finding the index of a specific value.

## 💡 Future Improvements (Ideas for expansion)
* Add error handling for `list.index()` if the value is not found.
* Experiment with other list methods like `remove()`, `count()`, `clear()`.
* Explore creating lists using list comprehensions.
* Implement user input to dynamically create and modify the list.

## ✍️ Author

**Samuel Odusanwo**  
📧 Email: [odusanwosamuel6@gmail.com]  
