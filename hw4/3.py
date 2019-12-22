class AffineTransformations:
    def __init__(self, M, v):
        self.M = M
        self.v = v
    def transformation(self, x):
        self.x = x
        number_of_columns = len(self.M[0])
        number_of_rows = len(self.v)
        answer = [0] * number_of_rows
        for i in range(0, number_of_rows):
            for j in range(0, number_of_columns):
                answer[i] += self.M[i][j] * self.x[j]
            answer[i] += self.v[i]
        return answer
    def __add__(self, right_aff_transformaion):
        number_of_columns = len(self.M[0])
        number_of_rows = len(self.v)
        answer_M = []
        answer_v = [0] * number_of_rows
        temp = []
        sum = 0
        for k in range (0, number_of_rows):
            for j in range (0, number_of_columns):
                for i in range (0, number_of_columns):
                    sum += right_aff_transformaion.M[i][j] * self.M[k][i]
                temp.append(sum)
                sum = 0
                answer_v[k] += right_aff_transformaion.M[k][j] * self.v[j]
            answer_M.append(temp)
            temp = []
            answer_v[k] += right_aff_transformaion.v[k]
        return AffineTransformations(answer_M, answer_v)

if __name__ == '__main__':
    trans1 = AffineTransformations([[1, 2], [3, 4]], [5, 6])
    x1 = (4, 5)
    x2 = trans1.transformation(x1)
    trans2 = AffineTransformations([[4, 5], [3, 8]], [3, 9])
    x3 = trans2.transformation(x2)
    trans3 = trans2 + trans1
    x4 = trans3.transformation(x1)
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    
