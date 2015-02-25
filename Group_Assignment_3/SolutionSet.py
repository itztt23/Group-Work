__author__ = 'Zachary'


class SolutionSet:

    def __init__(self):
        self._array = []
        self._solution = float('inf')
        self._startIndex = -1
        self._endIndex = -1
        self._subset = []

    def prettyprint(self):
        print("GIVEN SOLUTION")
        #print(self._array)
        print("Solution: ", self._solution)
        print("Start Index: ", self._startIndex)
        print("End Index: ", self._endIndex)
        print("Subset: ", self._subset)

    def loadfromfile(self, index):
        with open("test_cases_with_solutions.txt") as f:
            content = f.readlines()
        lineIndex = 0
        for line in content:
            if lineIndex != index:
                lineIndex += 1
                continue
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.split(",")
            for num in line:
                self._array.append(int(num))
            self._endIndex = self._array[len(self._array)-1]
            self._startIndex = self._array[len(self._array)-2]
            self._solution = self._array[len(self._array)-3]
            self._array = self._array[0:len(self._array)-3]             #remove index/solution from array
            self._subset = self._array[self._startIndex:self._endIndex+1]
            break

    def load_from_no_solution_file(self, index):
        with open("test_cases_without_solutions.txt") as f:
            content = f.readlines()
        lineIndex = 0
        for line in content:
            if lineIndex != index:
                lineIndex += 1
                continue
            line = line.replace("[", "")
            line = line.replace("]","")
            line = line.split(",")
            for num in line:
                self._array.append(int(num))
            break

    def savetofile(self):
        with open("answers.txt", 'w') as f:
            str = "%u %u %u" % (self._solution, self._startIndex, self._endIndex)
            f.write(str)