class Solution(object):
    def getBar(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        bar_list = [0] * N
        for i in range(0, N):
            for j in range(0, M):
                if matrix[j][i] != 0:
                    bar_list[i] = bar_list[i] + matrix[j][i]
                else:
                    break
        # bar_list, Eg: [4,3,2,2]
        return bar_list

    def largestRectangleArea(self, height):
        stack = []
        area = 0

        for i in range(0, len(height)+1):
            curt = -1 if i == (len(height)) else height[i]
            while stack != [] and curt <= height[stack[len(stack) - 1]]:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width * height[curr])
            stack.append(i)

        return area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :N*N dimension
        :rtype: int
        """
        matrix = [[int(j) for j in i] for i in matrix]

        max_area = 0
        N = len(matrix)
        M = len(matrix[0])
        for i in range(0, N):
            m = matrix[i:N]
            l = self.getBar(m)
            max_area = max(max_area, self.largestRectangleArea(l))

        return max_area

#push_back in C++ means insert at the end of the vector
def main():
    matrix = ["10100","10111","11111","10010"]
    c = Solution()
    print c.maximalRectangle(matrix)
    return None


if __name__ == '__main__':
    main()
