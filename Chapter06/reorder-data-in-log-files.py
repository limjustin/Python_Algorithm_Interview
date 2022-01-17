from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        dlist = list()
        slist = list()

        for i in range(len(logs)) :
            # print(logs[i].split()[1:])
            # print(''.join(logs[i].split()[1:]))
            # print(''.join(logs[i].split()[1:]).isdigit())
            
            if ''.join(logs[i].split()[1:]).isdigit() :
                dlist.append(logs[i])
            else :
                slist.append(logs[i])

        # num1 = [dlist[x] for x in range(len(dlist))]
        # num2 = [slist[x] for x in range(len(slist))]
        # print("num1 :", num1)
        # print("num2 :", num2)

        for i in range(len(slist)) :
            min_index = i
            for j in range(i+1, len(slist)) :
                if slist[j].split()[1:] < slist[min_index].split()[1:] or (slist[j].split()[1:] == slist[min_index].split()[1:] and slist[j].split()[0] < slist[min_index].split()[0]) :
                    min_index = j

            slist[i], slist[min_index] = slist[min_index], slist[i]

        num1 = [slist[x] for x in range(len(slist))]
        num2 = [dlist[x] for x in range(len(dlist))]

        return num1 + num2

# str1 = "art can heavy"
# str2 = "art zero two"
# str3 = "own kit dog"

# if str1 < str2 :
#     print("str2 is big")
# elif str1 > str2 :
#     print("str1 is big")
# else : 
#     print("Same")

# print(str1.split()[1:] > str2.split()[1:])