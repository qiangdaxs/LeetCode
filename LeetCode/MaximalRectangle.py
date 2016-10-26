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
        stack = [];
        i = 0;
        area = 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width * height[curr])
                i -= 1
            i += 1
        while stack != []:
            curr = stack.pop()
            width = i if stack == [] else len(height) - stack[len(stack) - 1] - 1
            area = max(area, width * height[curr])
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


def main():
    matrix = ["101101","111111","011011","111010","011111","110111"]
    c = Solution()
    print c.maximalRectangle(matrix)
    return None


if __name__ == '__main__':
    main()
