<p>
    <img src='https://raw.githubusercontent.com/khoatranrb/1920II_INT3401_11/master/Lec1/img/1.png'>
</p>

<p>
    <img src='https://raw.githubusercontent.com/khoatranrb/1920II_INT3401_11/master/Lec1/img/2.png'>
</p>

* Declare a NODE:

  ```python
  A = Node('A')
  ```

* Declare GRAPH:

  ```python
  X = Graph(first_Node = A)
  ```

  * Add node into Graph:

    ```python
    X.add_Node(B)
    ```

  * Connect two Node:

    ```python
    X.set_edge(A, B, direct=1)
    ```

* Search:

  ```python
  BFS_search(X, A, K)
  DFS_search(X, A, K)
  ```
