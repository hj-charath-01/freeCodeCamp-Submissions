def dfs_n_queens(n: int) -> list[list[int]]:
    if n < 1:
        return []

    valid_col = [True] * n
    valid_left_diag = [True] * (n * 2 - 1)
    valid_right_diag = [True] * (n * 2 - 1)

    placement = []
    result = []

    def backtrack(row):        
        if row == n:
            result.append(placement[:])
            return
            

        for col in range(n):
            left_diag = row + col
            right_diag = n - 1 -(row - col)

            if valid_col[col] and valid_left_diag[left_diag] and valid_right_diag[right_diag]:
                placement.append(col)
                valid_col[col] = valid_left_diag[left_diag] = valid_right_diag[right_diag] = False

                backtrack(row + 1)

                placement.pop()
                valid_col[col] = valid_left_diag[left_diag] = valid_right_diag[right_diag] = True

    backtrack(0)
    return result
