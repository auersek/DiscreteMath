import matplotlib.pyplot as plt
import numpy as np
import time


def recursive(n):
    if n <= 2:
        return 1
    else:
        return recursive(n - 1) + recursive(n - 2)


def table(n):
    nums = [1, 1]
    for i in range(n - 2):
        nums.append(nums[i] + nums[i + 1])
    return nums[-1]


def keep_last2(n):
    nums = [1, 1]
    for i in range(n - 2):
        tmp = nums[1]
        nums[1] = nums[0] + nums[1]
        nums[0] = tmp
    return nums[1]


def analytic(n):
    return 0.45 * (1.617 ** n)


def matrix_lin(n):
    mat = np.array([[1, 1], [1, 0]])
    mat_result = np.array([[1, 1], [1, 0]])

    for i in range(n):
        mat_result = np.matmul(mat_result, mat)
        # print(mat_result)


def multiply(mat1, mat2):
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w

def matrix_power(mat, n):
    if n == 0 or n == 1:
        return
    mat2 = [[1, 1], [1, 0]]
    matrix_power(mat, n // 2)
    multiply(mat, mat)
    if n % 2 != 0:
        multiply(mat, mat2)

def matrix(n):
    if n <= 1:
        return n
    mat = [[1, 1], [1, 0]]
    matrix_power(mat, n - 1)
    return mat[0][0]


def timeit(n):
    start = time.time()
    # recursive(n)
    # table(n)
    # keep_last2(n)
    # analytic(n)
    # matrix_lin(n)
    matrix(n)
    end = time.time()
    return end - start


if __name__ == '__main__':
    N = [0, 5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700]
    # matrix(0)
    T = [timeit(n) for n in N]
    plt.plot(N, T)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('matrix')
    plt.show()
