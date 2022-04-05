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

    def print_equal_sum_pairs(self,):

        dict = {}

        for pair in self.lis:
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
print(obj1.length())
print(obj1.StringToList())

obj2 = PairsPossible("1357359")
print(obj2.possible_pairs())
# print(obj2.print_possible_pairs())
lis = obj2.possible_pairs()

obj3 = SearchCommonElements(obj1.str1, obj2.str1)
print(obj3.find_common())

obj4 = EqualSumPairs()
obj4.print_equal_sum_pairs(lis)

#     def  Pairs(self):
#         lis = StringClass.StringToList(self)
#         group = 2
#         Pair = [x for x in combinations(lis, group)]
#         print(*Pair)
#
# class SearchCommonElements(StringClass):
#
#     def common(self, st2, st):
#         removed = list(set(st2) & set(st))
#         print('Commons from two strings')
#         print(removed)
#
#
# class EqualSumPairs():
#     def count(self, res_list):
#         lst = []
#         for tup in res_list:
#             sum = 0
#             for i in tup:
#                 sum += int(i)
#             lst.append(sum)
#         print('Pairs having unique sums')
#         print(set(lst))
#         print(len(set(lst)))
#
# st = "12314532"
# send1 = StringClass(st)
# print('Length of string')
# print(send1.length())
# print('Convert string to list')
# print(send1.StringToList())
#
# # sc_list = send1.StringToList()
# send2 = PairsPossible(send1)
# # result = send2.Pairs(sc_list)
# print('All possible pairs')
# print(result)
#
# st2 = "12314532"
# send3 = SearchCommonElements(send1)
# send3.common(st2, st)
#
# send4 = EqualSumPairs()
# send4.count(result)

# class SearchCommonElements(StringClass):

    # def commonele(self):
    #     d = dict(Counter(list(self.str1)))
    #     ans = []
    #     for j in d:
    #         if d[j] >= 2:
    #             ans.append(j)
    #     print(ans)

# str1 = "12314532"
# list1 = []
# pp = PairsPossible(str1)
# pp.length()
# strlist = pp.StringToList()
# print(strlist)
# pp.Pairs()

# Obj = StringClass('12314532')
# print(Obj.length())
# print(Obj.StringToList())
# Obj1 = PairsPossible('12314532')
# # print(Obj1.Pairs())
# Obj2=SearchCommonElements('12314532')
# Obj2.commonele()

#     def __init__(self, str1, str2):
#         self.str1 = str1
#         self.str2 = str2
#
#     def commonelements(self):
#         dict1 = Counter(str1)
#         dict2 = Counter(str2)
#
#         commonDict = dict1 & dict2
#
#         if len(commonDict) == 0:
#             print(-1)
#             return
#
#         commonChars = list(commonDict.elements())
#         commonChars = sorted(commonChars)
#         print(list(commonChars))
#
#
# class EqualSumPairs(SearchCommonElements):
#
#     def __init__(self, strlist):
#         self.strlist = strlist
#
#     def countpairs(self):
#         count = 0
#         dict = {}
#         for i in range(len(strlist) - 1):
#             sum = int(strlist[i]) + int(strlist[i + 1])
#
#             if str(sum) in dict:
#                 dict[str(sum)] = dict[str(sum)] + 1
#             else:
#                 dict[str(sum)] = 1
#         for key, val in dict.items():
#             if val == 1:
#                 count = count + 1
#         print(count)
#
#
# if __name__ == "__main__":
#     str1 = "12314532"
#     str2 = "1231234"
#     SC = StringClass(str1)
#     SC.length()
#     strlist = SC.StringToList()
#     print(strlist)
#
#     PP = PairsPossible(str2)
#     PP.StringToList()
#     pairList = PP.Pairs()
#     print(pairList)
#     SCE = SearchCommonElements(str1, str2)
#     SCE.commonelements()
#
#     ESP = EqualSumPairs(strlist)
#     ESP.countpairs()