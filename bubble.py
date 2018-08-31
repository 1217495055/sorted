class SQList():
    def __init__(self,lis =  None):
        self.r = lis
    def swap(self,i,j):
        self.r[i],self.r[j] = self.r[j],self.r[i]

    def bubble_sort(self):
        lis = self.r
        length = len(self.r)
        for  i in range(length):
            for j in range(i + 1,length):
                if lis[i] > lis[j]:
                    self.swap(i,j)

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += ' ' + str(i)
        return ret


if __name__ == '__main__':
    sqlist = SQList([2,5,23,9,6,564,2,34,5,6,7,4,34])
    sqlist.bubble_sort()
    print(sqlist)