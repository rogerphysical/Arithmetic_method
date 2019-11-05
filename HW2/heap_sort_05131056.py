#先建立Heap Tree
class Tree(object):
    M=[]
    #add為新增資料
    def add(self,a):
       self.M.append(a)
    #get為得到該點值
    def get(self,a):
        if a<len(self.M):
            return self.M[a]
        else:
            return False
    #getL為得到該點的left child
    def getL(self,index):
        aa=2*index+1
        if aa<len(self.M):
            return self.M[aa]
        else:
            return False
    #getR為得到該點的right child
    def getR(self,index):
        aa=2*index+2
        if aa<len(self.M):
            return self.M[aa]
        else:
            return False
    #changemax為交換最大者 直到排完
    def changemax(self,index):
        L=len(self.M)
        if self.get(index)<=self.getR(index) and 2*index+2<L:
            maxN=2*index+2
        else:
            maxN=index
        if self.get(maxN)<=self.getL(index) and 2*index+1<L:
            maxN=2*index+1
        if self.get(index)!=self.get(maxN):
            temp=self.M[index]
            self.M[index]=self.M[maxN]
            self.M[maxN]=temp
            self.changemax(maxN)
    #maxheap為進行maxheap
    def maxheap(self):
        a=int((len(self.M)-2)/2)
        for i in range(a,-1,-1):
            self.changemax(i)
    #changemin為交換最小者 直到排完
    def changemin(self,index):
        L=len(self.M)
        if self.get(index)>=self.getR(index) and 2*index+2<L:
            minN=2*index+2
        else:
            minN=index
        if self.get(minN)>=self.getL(index) and 2*index+1<L:
            minN=2*index+1
        if self.get(index)!=self.get(minN):
            temp=self.M[index]
            self.M[index]=self.M[minN]
            self.M[minN]=temp
            self.changemin(minN)
    #minheap為進行minheap
    def minheap(self):
        a=int((len(self.M)-2)/2)
        for i in range(a,-1,-1):
            self.changemin(i)
    #delTOP為刪除第一項值 將最後一項值填入第一項
    def delTOP(self):
        self.M[0]=self.M[len(self.M)-1]
        self.M.pop()

#heapsort是運用heap tree 進行sort
class Solution(object):
    def heap_sort(self,nums):
        t=Tree()
        M=[]
        for i in range(len(nums)):
            t.add(nums[i])
        for i in range(len(nums)):
            t.minheap()
            M.append(t.M[0])
            t.delTOP()
        return M
'''
#以下為示範
N=[56,-5,1,64,-1,1,-1,-6357,-1,0,54,1,-453,13,-75,13,0,0]
N2=Solution().heap_sort(N)
print(N2)
'''
#參考資料:自己1年前用C++寫的程式
