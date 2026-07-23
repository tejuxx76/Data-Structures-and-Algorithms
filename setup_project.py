import os

# Project Root
project_name = "Data-Structures-and-Algorithms"

# Folder Names
folders = [
    "01_Arrays",
    "02_Strings",
    "03_Hash_Map",
    "04_Two_Pointers",
    "05_Sliding_Window",
    "06_Linked_List",
    "07_Stack",
    "08_Queue",
    "09_Binary_Search",
    "10_Recursion",
    "11_Backtracking",
    "12_Trees",
    "13_Binary_Search_Tree",
    "14_Heap_Priority_Queue",
    "15_Graphs",
    "16_Greedy",
    "17_Dynamic_Programming",
    "18_Bit_Manipulation",
    "19_Math",
    "20_Trie",
    "21_Union_Find",
    "Notes"
]

# Create Project Folder
os.makedirs(project_name, exist_ok=True)

# Create Topic Folders
for folder in folders:
    path = os.path.join(project_name, folder)
    os.makedirs(path, exist_ok=True)

    # Create README.md inside each folder
    readme = os.path.join(path, "README.md")
    with open(readme, "w", encoding="utf-8") as f:
        title = folder.replace("_", " ")
        f.write(f"# {title}\n\n")
        f.write("Problems Solved: 0\n")

# Main README
main_readme = os.path.join(project_name, "README.md")

with open(main_readme, "w", encoding="utf-8") as f:
    f.write("# Data Structures and Algorithms\n\n")
    f.write("Python solutions for LeetCode problems.\n\n")
    f.write("## Topics\n\n")

    for folder in folders[:-1]:
        f.write(f"- {folder.replace('_', ' ')}\n")

print("Project structure created successfully!")