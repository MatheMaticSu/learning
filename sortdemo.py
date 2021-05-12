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

lis = [4,5,6,1,3,2]
Bubble.sorte(lis)
print(lis)