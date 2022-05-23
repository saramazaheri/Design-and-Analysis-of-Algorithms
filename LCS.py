class LCS_Variable:
    Len = 0  # length of  LCs
    arrow = ''  # will be shown in the table which will be printed  and shows  path of subsequences
    # the letters which are candidate to be in LCS (ordered based on the algorithm and their place in words)
    lcs = ''


class LCS:

    def __init__(self, Fw, Sw):

        self.Fw = Fw  # first input
        self.Sw = Sw  # second input
        self.m = len(Fw)  # length of  first inpput
        self.n = len(Sw)  # length of  second input
        # making a table with  length i  and  height j
        self.MTable = [[LCS_Variable() for i in range(self.n+1)]  # nested lists as a matrix which are the row and coloumn of table
                       for j in range(self.m+1)]

   # printing table
    def __str__(self) -> str:
        result = '|      '

        for i in range(self.n+1):
            if i == 0:
                result += '|{:^6}'.format(i)
            else:
                result += '| {:^2} {:^2}'.format(self.Sw[i-1], i)

        result += '|'
        result += '\n'
        result += '-------'*(self.n+2)
        result += '\n'

        for i in range(self.m+1):
            if i == 0:
                result += '|{:^6}'.format(i)
            else:
                result += '| {:^2} {:^2}'.format(self.Fw[i-1], i)

            for j in range(self.n+1):
                if self.MTable[i][j].arrow == '0':
                    result += '|{:^6}'.format(self.MTable[i][j].arrow)
                else:
                    result += '| {:^2} {:^2}'.format(
                        self.MTable[i][j].arrow, self.MTable[i][j].Len)

            result += '|'
            result += '\n'
            result += '-------'*(self.n+2)
            result += '\n'

        result += f'\n\nLCS : {self.MTable[self.m][self.n].lcs}\nLCS Length : {self.MTable[self.m][self.n].Len}\n'

        return result

    def LCS_main(self):
        # we assume that all the entries are 0 at first for len, LCS is not calculated and therefor the arrows are not set
        for row in range(0, self.m+1):
            self.MTable[row][0].Len = 0
            self.MTable[row][0].lcs = ''
            self.MTable[row][0].arrow = '0'
        for col in range(0, self.n+1):
            self.MTable[0][col].Len = 0
            self.MTable[0][col].lcs = ''
            self.MTable[0][col].arrow = '0'

        for row in range(1, self.m+1):
            for col in range(1, self.n+1):

                if self.Fw[row-1] == self.Sw[col-1]:
                    self.MTable[row][col].Len = self.MTable[row -
                                                            1][col-1].Len + 1
                    self.MTable[row][col].lcs = self.MTable[row -
                                                            1][col-1].lcs + self.Sw[col-1]
                    self.MTable[row][col].arrow = '↖'
                elif self.MTable[row-1][col].Len >= self.MTable[row][col-1].Len:
                    self.MTable[row][col].Len = self.MTable[row-1][col].Len
                    self.MTable[row][col].lcs = self.MTable[row-1][col].lcs
                    self.MTable[row][col].arrow = '↑'
                else:
                    self.MTable[row][col].lcs = self.MTable[row][col-1].lcs
                    self.MTable[row][col].Len = self.MTable[row][col-1].Len
                    self.MTable[row][col].arrow = '←'


First_word = input("please enter first word :")
Second_word = input("please enter second word :")

result = LCS(First_word, Second_word)
result.LCS_main()
print(result)
