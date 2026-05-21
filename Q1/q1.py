# Q1: Starter file
# Implement solve_q1(arr) below.

def solve_q1(arr):
    # Placeholder implementation: returns sum of elements
    return sum(arr)

if __name__ == "__main__":
    import sys, json
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = [1, 2, 3]
    print(solve_q1(data))


