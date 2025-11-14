# Lab_Report_1
This is a **Streamlit-based interactive visualizer** for demonstrating **graph traversal algorithms**: Breadth-First Search (BFS) and Depth-First Search (DFS).  

Users can:
- Upload or view a graph image.
- Select a starting node.
- Run BFS or DFS traversal.
- See the traversal order and visited nodes.
- Learn about algorithm complexity.

## Features
- Interactive UI using Streamlit.
- Placeholder image if graph image is missing.
- Deterministic traversal by sorting neighbors alphabetically.
- Real-time display of traversal order.
- Complexity summary included.

## Requirements
- Python ≥ 3.9
- Libraries:
  - `streamlit`
  - `Pillow`

Install dependencies:
```bash
pip install streamlit pillow
