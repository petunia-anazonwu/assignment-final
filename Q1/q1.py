# Q1/q1.py
# Needleman-Wunsch global alignment (match=+1, mismatch==1, gape=-1)
def needleman_wunsch(A, B, match=1, mismatch=-1, gap=-1):
    n = len(A)
    m = len(B)
    M = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        M[i][0] = M[i-1][0] + gap
    for j in range(1, m + 1):
        M[0][j] = M[0][j-1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = M[i-1][j-1] + (match if A[i-1] == B[j-1] else mismatch)
            up = M[i-1][j] + gap
            left = M[i][j-1] + gap
            M[i][j] = max(diag, up, left)

    i, j = n, m
    aligned_A = []
    aligned_B = []
    traceback = []
    while i > 0 or j > 0:
        current = M[i][j]
        # prefer diagonal when tied (deterministic)
        if i > 0 and j > 0:
            diag = M[i-1][j-1] + (match if A[i-1] == B[j-1] else mismatch)
            if current == diag:
                aligned_A.append(A[i-1])
                aligned_B.append(B[j-1])
                traceback.append(('diag', i-1, j-1))
                i -= 1
                j -= 1
                continue
        if i > 0:
            up = M[i-1][j] + gap
            if current == up:
                aligned_A.append(A[i-1])
                aligned_B.append('-')
                traceback.append(('up', i-1, j))
                i -= 1
                continue
        if j > 0:
            left = M[i][j-1] + gap
            aligned_A.append('-')
            aligned_B.append(B[j-1])
            traceback.append(('left', i, j-1))
            j -= 1
            continue

    aligned_A.reverse()
    aligned_B.reverse()
    traceback.reverse()
    return M, aligned_A, aligned_B, traceback, M[n][m]

def align_strings(A, B, match=1, mismatch=-1, gap=-1):
    """
    Returns (alignedA_str, alignedB_str, score)
    Deterministic tie-breaking: diagonal preferred over up/left.
    """
    _, aA, aB, _, score = needleman_wunsch(A, B, match, mismatch, gap)
    return "".join(aA), "".join(aB), score

# Optional CLI for quick manual checks (won't run during pytest import)
if __name__ == "__main__":
    A, B = "RENT", "TREN"
    aA, aB, score = align_strings(A, B)
    print("A:", A)
    print("B:", B)
    print("Aligned A:", aA)
    print("Aligned B:", aB)
    print("Score:", score)

