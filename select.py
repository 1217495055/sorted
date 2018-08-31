class SQList:
    def __init__(self,lis = None):
        self.r = lis

    def swap(self,i,j):
        self.r[i],self.r[j] = self.r[j],self.r[i]

    def select_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            mymin = i 
            for j in range(i + 1,length):
                if lis[mymin] > lis[j]:
                    mymin = j
            if i != mymin:
                self.swap(i,mymin)

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += ' ' + str(i)
        return ret

if __name__ == '__main__':
    sqlist = SQList([9,7,65,3,2,21,1,43,4,5,6])
    sqlist.select_sort()
    print(sqlist)