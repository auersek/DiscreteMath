def count(A, x):
    count = 0
    for i in range(len(A)):
        if A[i] == x:
            count += 1
    return count

def majority(A):
    if len(A) == 1:
        return A[0]

    mid = len(A) // 2

    left_maj = majority(A[:mid])
    right_maj = majority(A[mid:])

    if left_maj == right_maj:
        return left_maj

    left_count = count(A, left_maj)
    right_count = count(A, right_maj)

    if left_count > len(A) // 2:
        return left_maj
    if right_count > len(A) // 2:
        return right_maj
    return None

if __name__ == '__main__':
    # A = [1, 2, 2, 1, 2, 1, 1, 1]
    A = [3, 2, 3, 3, 1, 1, 3, 3]
    print(majority(A))