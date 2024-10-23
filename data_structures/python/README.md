# Data Structures and Algorithms

This repository contains custom implementations of fundamental data structures such as Stacks, Queues, Trees, and Graphs. Each data structure has been implemented from scratch with unit tests included to verify the correctness of each implementation. This repository is a great resource for understanding the internals of common data structures.

## Tools and Technologies
- **Python**: Main programming language used for implementing the data structures.
- **Pytest**: A testing framework used to validate the implementations of the data structures.
- **Git**: Version control system to track changes and collaborate.

## Data Structures Implemented
1. **Stack**: A Last-In-First-Out (LIFO) data structure that supports `push`, `pop`, and `peek` operations.
2. **Queue**: A First-In-First-Out (FIFO) data structure that supports `enqueue` and `dequeue` operations.
3. **Binary Tree**: A hierarchical tree structure where each node has at most two children, implemented with insertion and search functionality.
4. **Graph**: An adjacency list representation of a graph, with methods to add vertices, edges, and perform Breadth-First Search (BFS) and Depth-First Search (DFS).

## How to Run the Project
To run the tests in this repository, you need to follow these steps:

1. **Clone the Repository**:
    ```bash
    git@github.com:amanimutangana/algorithms.git
    cd data-structures/python
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.x installed. Then install all required packages with:
    ```bash
    pip install -r requirements.txt
    ```

3. **Running the Tests**:
    Once the dependencies are installed, run the tests using `pytest` with the following command(make sure you are in the correct directory):
    ```bash
    pytest
    ```

## Future Plans

- Add additional data structures like Linked Lists, Hash Tables, and Heaps.
- Expand the unit tests to cover edge cases.
- Implement more algorithms using the provided data structures.

Contributions are welcome! If you find a bug or have a suggestion, feel free to submit an issue or pull request.
