from itertools import combinations
from collections import Counter

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
    def possible_pairs(self):
        lis = StringClass.StringToList(self)
        group = 2
        Pair = [x for x in combinations(lis, group)]
        print(*Pair)
        return Pair

    # def print_possible_pairs(self):
    #     print(*self.Pair)



class SearchCommonElements:

    def __init__(self, a, b):
        self.StringClass_string = a
        self.PossiblePair_string = b
        self.common_list = list()

    def find_common(self):
        dict = {}

        for ele in self.StringClass_string:
            if ele in self.PossiblePair_string:
                if ele in dict:
                    continue
                else:
                    dict[ele] = 1

        for key in dict:
            self.common_list.append(key)

        return self.common_list


class EqualSumPairs():

    def print_equal_sum_pairs(self,lis):

        dict = {}

        for pair in lis:
            pairs_list = list(pair)
            sum = 0
            for num in pairs_list:
                sum = sum + int(num)

            if sum in dict:
                dict[sum] = dict[sum] + 1
            else:
                dict[sum] = 1

        for key in dict:
            if dict[key] == 1:
                print(key, end=" ")


obj1 = StringClass("12314532")
print("Length of String: ",obj1.length())
print("String converted to list: ",obj1.StringToList())

obj2 = PairsPossible("13532783")
print("Possible Pairs: ")
lis = obj2.possible_pairs()

obj3 = SearchCommonElements(obj1.str1, obj2.str1)
print("Common elements: ")
print(obj3.find_common())

obj4 = EqualSumPairs()
print("Equal sum Pair: ")
obj4.print_equal_sum_pairs(lis)