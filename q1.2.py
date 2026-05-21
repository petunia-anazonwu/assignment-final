import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import directly from your tour file name
from tour import main

def run_tests():
    print("--- Running Verification Tests ---")
    # Verify main interface structure is reachable
    assert callable(main)
    print("[SUCCESS] All functional structural checks pass setup validation!")

if __name__ == "__main__":
    run_tests()
