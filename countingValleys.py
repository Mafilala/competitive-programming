def countingValleys(steps, path):
    # Write your code here
    vc = 0
    height = 0
    for le in path:
        height += 1 if le == "U" else -1
        if height == 0 and le == "U":
            vc += 1
    return vc
        
