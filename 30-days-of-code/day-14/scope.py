class Difference:
    def __init__(self, a):
        self.__elements = a
        #self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        minVal = min(self.__elements)
        maxVal = max(self.__elements)

        self.maximumDifference = abs(minVal - maxVal)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)