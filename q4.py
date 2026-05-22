def collatz(n: int) -> int:
    """
    A mathematically strict recursive function mapping the Collatz Conjecture 
    as referenced in Rosen's Discrete Mathematics text book.
    """
    print(n, end=" -> " if n > 1 else "\n")
    
    # Base case condition: tracking sequence terminates when 1 is reached
    if n == 1:
        return 0
        
    # Recursive case logic path configurations
    if n % 2 == 0:
        return 1 + collatz(n // 2)   # Even path rule execution
    else:
        return 1 + collatz(3 * n + 1) # Odd path rule execution

def main():
    print("=========================================")
    print("RUNNING RECURSIVE COLLATZ CONJECTURE TOOL")
    print("=========================================")
    
    starting_number = 6
    print(f"Processing Collatz Sequence for Starting Number: {starting_number}")
    print("Sequence: ", end="")
    
    total_steps = collatz(starting_number)
    print(f"Total Steps to Reach Base = {total_steps}")

if __name__ == "__main__":
    main()
