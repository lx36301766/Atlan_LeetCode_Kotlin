
"""

    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

    示例 1:

    输入:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

    示例 2:

    输入:
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    输出:
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

    进阶:

    一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？

"""

class Solution(object):

    # Approach 1: Additional Memory Approach
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    # Approach 2: Brute O(1) space
    def setZeroes2(self, matrix):

        modify = -999999

        vl = len(matrix)
        hl = len(matrix[0])

        for i in range(vl):
            for j in range(hl):
                if matrix[i][j] == 0:
                    for x in range(hl):
                        if matrix[i][x] != 0:
                            matrix[i][x] = modify
                    for y in range(vl):
                        if matrix[y][j] != 0:
                            matrix[y][j] = modify

        for i in range(vl):
            for j in range(hl):
                if matrix[i][j] == modify:
                    matrix[i][j] = 0

    # Approach 3: O(1) Space, Efficient Solution
    def setZeroes3(self, matrix):
        vl = len(matrix)
        hl = len(matrix[0])

        replaceFirstColum = False
        for i in range(vl):
            if matrix[i][0] == 0:
                replaceFirstColum = True
            for j in range(1, hl):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, vl):
            if matrix[i][0] == 0:
                for j in range(hl):
                     matrix[i][j] = 0
        for j in range(1, hl):
            if matrix[0][j] == 0:
                for i in range(vl):
                     matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(hl):
                matrix[0][j] = 0
        if replaceFirstColum:
            for i in range(vl):
                matrix[i][0] = 0


def main():
    print('this message is from main function')
    solution = Solution()
    matrix = [
        [5, 1, 2, 0],
        [4, 1, 0, 3],
        [0, 5, 2, 3],
        [1, 5, 2, 3],
    ]
    solution.setZeroes3(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
    # print(__name__)
