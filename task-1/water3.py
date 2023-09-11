def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[1]==4 and s[2]==4

def successors(s):
    x, y, z = s
    return []
