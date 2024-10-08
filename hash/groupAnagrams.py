from collections import Counter
def groupAnagrams(strs):
    groups = []
    dict_ords = {}
    group_num = 0
    for string in strs:
        count_dict = frozenset(Counter(string).items())
        if count_dict not in dict_ords:
            dict_ords[count_dict] = group_num
            groups.append([string])
            group_num+=1
        else:
            group = dict_ords[count_dict]
            groups[group].append(string)


strs = ["act","pots","tops","cat","stop","hat"]

 # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

groupAnagrams(strs)

                

            



        