# ------------------------------------------------------------
# Lab Report BSD3513 – Artificial Intelligence
# Chapter 2: Search Algorithms (BFS & DFS)
# Student Name: ZAHIN ZIKRI BIN ZAWAWI
# Student ID: SD23019
# Section: 02G
# ------------------------------------------------------------

import streamlit as st
from collections import deque
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ------------------------------------------------------------
# Streamlit App Header
# ------------------------------------------------------------
st.set_page_config(page_title="BFS & DFS Visualizer", layout="centered")
st.title(" BFS and DFS Graph Traversal Visualizer")
st.markdown("### BSD3513 – Lab Report 1")
st.markdown("*Name:* ZAHIN ZIKRI BIN ZAWAWI | *Student ID:* SD23019 | *Section:* 02G")

# ------------------------------------------------------------
# Display Graph Image
# ------------------------------------------------------------
st.subheader("Graph Reference Image")
st.info("Below is the sample graph used for BFS and DFS traversal demonstrations.")

script_dir = Path(".")      # Safer for Streamlit Cloud
candidates = ["LabReport_BSD2513_#1.jpg"]

img_path = None
for name in candidates:
    p = script_dir / name
    if p.exists():
        img_path = p
        break

if img_path:
    try:
        image = Image.open(img_path)
        st.image(image, caption=f"Graph used ({img_path.name})", use_column_width=True)
    except Exception:
        st.warning(f"⚠ Found '{img_path.name}' but failed to open it.")
else:
    # Placeholder image when file is missing
    W, H = 800, 400
    placeholder = Image.new("RGB", (W, H), color="white")
    draw = ImageDraw.Draw(placeholder)
    font = ImageFont.load_default()
    text = "Image not found\nPlace graph image in this folder"
    lines = text.split("\n")
    y_offset = 150

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text(((W - w) / 2, y_offset), line, fill="black", font=font)
        y_offset += h + 5

    st.image(placeholder, caption="(Placeholder) Graph not found", use_column_width=True)

# ------------------------------------------------------------
# Graph Definition
# ------------------------------------------------------------
graph = {

    "A": ["B", "D"],
    "B": ["C", "E", "G"],
    "C": ["A"],
    "D": ["C"],
    "E": ["H"],
    "F": [],
    "G": ["F"],
    "H": ["G", "F"]

}

st.subheader("1️. Graph Structure")
st.json(graph)

# Ensure deterministic traversal (alphabetical order)
for node in graph:
    graph[node] = sorted(graph[node])

# ------------------------------------------------------------
# BFS WITH LEVEL TRACKING
# ------------------------------------------------------------
def bfs_with_levels(graph, start):
    visited = []
    queue = deque([(start, 0)])  # store (node, level)
    levels = {}

    while queue:
        node, level = queue.popleft()

        if node not in visited:
            visited.append(node)

            # save node by level
            if level not in levels:
                levels[level] = []
            levels[level].append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, level + 1))

    return visited, levels

# ------------------------------------------------------------
# DFS WITH STEP TRACKING
# ------------------------------------------------------------
def dfs_with_steps(graph, start, visited=None, order=None, steps=None, depth=0):
    if visited is None:
        visited = set()
        order = []
        steps = []

    steps.append(f"{' ' * depth * 2}➡ Enter {start} (depth {depth})")

    if start not in visited:
        visited.add(start)
        order.append(start)

        for neighbour in graph[start]:
            dfs_with_steps(graph, neighbour, visited, order, steps, depth + 1)

    steps.append(f"{' ' * depth * 2}⬅ Backtrack from {start} (depth {depth})")
    return order, steps

# ------------------------------------------------------------
# Streamlit Interface
# ------------------------------------------------------------
st.subheader("2️. Choose Traversal Type")
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))
algorithm = st.radio("Choose Algorithm:", ["Breadth-First Search (BFS)", "Depth-First Search (DFS)"])

if st.button("Run Traversal"):
    st.markdown("---")

    # --- BFS ---
    if algorithm == "Breadth-First Search (BFS)":
        order, levels = bfs_with_levels(graph, start_node)

        st.success("Traversal Order (BFS): " + " → ".join(order))

        st.markdown("###  BFS Levels")
        for lvl in sorted(levels.keys()):
            st.write(f"**Level {lvl}:** {', '.join(levels[lvl])}")

    # --- DFS ---
    else:
        order, steps = dfs_with_steps(graph, start_node)

        st.success("Traversal Order (DFS): " + " → ".join(order))

        st.markdown("###  DFS Step-by-Step Process")
        for s in steps:
            st.write(s)

# ------------------------------------------------------------
# Explanation Section
# ------------------------------------------------------------
st.markdown("---")
st.subheader("3️. Algorithm Explanation")

st.markdown("""
###  Breadth-First Search (BFS)
- Explores neighbors **level-by-level**.
- Uses a **queue (FIFO)**.
- Good for shortest path in unweighted graphs.

###  Depth-First Search (DFS)
- Explores as **deep as possible** before backtracking.
- Uses **recursion (implicit stack)**.
- Good for topological sorting, component detection.
""")

st.markdown("###  Complexity Summary")
st.table({
    "Algorithm": ["BFS", "DFS"],
    "Time Complexity": ["O(V + E)", "O(V + E)"],
    "Space Complexity": ["O(V)", "O(V)"]
})

st.markdown("---")
st.caption("Developed with Streamlit for BSD3513 Lab Report 1 – AI Search Algorithms.")



