


# N x N 크기의 2차원 배열을 시계방향으로 90도씩 회전하려 합니다. 
# 다음은 2x2 크기의 2차원 배열을 시계방향으로 90도씩 회전하는 예시입니다.
# 배열 A 
# A[0][0] = 1 
# A[0][1] = 2 
# A[1][0] = 3
# A[1][1] = 4

# A[0][0] = 3
# A[0][1] = 1
# A[1][0] = 4 
# A[1][1] = 2

# A[0][0] = 4
# A[0][1] = 3
# A[1][0] = 2
# A[1][1] = 1

# A[0][0] = 2
# A[0][1] = 4
# A[1][0] = 1
# A[1][1] = 3

# A[0][0] = 1
# A[0][1] = 2
# A[1][0] = 3
# A[1][1] = 4

# NxN 크기의 배열 A가 주어질 때, 시계방향으로 90도씩 회전한 횟수 r이 매개변수로 주어질 때, matrix가 시계방향으로 r번 회전한 결과를 리턴하도록 
# solution 함수를 완성해주세요. 

# N은 100이하의 자연수 입니다. r은 1000000이하입니다. 

def rotate_matrix(matrix, r):
    N = len(matrix)
    for _ in range(r % 4):
        matrix = [list(row) for row in zip(*matrix[::-1])]
    return matrix

# Example usage:
N = 2
matrix_A = [
    # tc1
    # [1, 2],
    # [3, 4]

    # tc2
    [4,1,2], [7,3,4], [3,5,6]

]
# tc1
# r = 2
# tc2
r = 3
result = rotate_matrix(matrix_A, r)
print(result)