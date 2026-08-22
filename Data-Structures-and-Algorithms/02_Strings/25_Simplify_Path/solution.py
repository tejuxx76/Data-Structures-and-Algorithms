def simplify_path(path):
    parts = path.split("/")
    stack = []
    for part in parts:
        if part == "" or part == ".":
            continue
        if part == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)

# Tes
path = "/home/user/../documents"
result = simplify_path(path)
print("Simplified Path:", result)