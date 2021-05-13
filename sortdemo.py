lis = [4,5,6,1,3,2]

'''
冒泡排序
'''
class Bubble():
    def sorte(s):
        i = len(s) - 1  
        while i > 0:
            j = 0
            while j<i:
                if Bubble.compare(s[j],s[j+1]) is False:
                    Bubble.exch(s, j, j+1)
                j += 1    
            i -= 1
    def compare(a, b):
        if  a > b:
            return False
    
    def exch(s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
# Bubble.sorte(lis)
# print(lis)
'''
选择排序
'''
class Selects():
    def compare(a, b):
        if a > b:
            return True
    
    def exch(s, i ,j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    
    def sorte(s):
        l = len(s)
        for i in range(0,l-2):
            minindex = i
            for j in range(i+1,l):
                if Selects.compare(s[minindex], s[j]):
                    minindex = j
            Selects.exch(s, i, minindex)
# Selects.sorte(lis)
# print(lis)
'''
插入排序
'''
class Insertion():
    def compare(a, b):
        if a > b:
            return True
    def exch(s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    def sorte(s):
        for i in range(1,len(s)):
            j = i 
            while j>0:
                if Insertion.compare(s[j-1],s[j]):
                    Insertion.exch(s,j-1,j)
                    j -= 1
                else:
                    break
Insertion.sorte(lis)
print(lis)