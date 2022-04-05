from itertools import combinations


class StringClass:

    def __init__(self, str1):
        self.str1 = str1

    def length(self):
        length = self.str1
        return len(length)

    def StringToList(self):
        List = list(self.str1)
        return List

# obj = StringClass('12314532')
# print(obj.length())
# print(obj.StringToList())

class PairsPossible(StringClass):

    def  Pairs(self):
        lis = StringClass.StringToList(self)
        group = 2
        Pairs = [x for x in combinations(lis, group)]
        print(*Pairs)

str1="12314532"
list1=[]
pp=PairsPossible(str1)
pp.length()
strlist=pp.StringToList()
print(strlist)
pp.Pairs()