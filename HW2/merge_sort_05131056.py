#使用merge sort
class Solution(object):
    M=[]
    #nums為要排列之陣列
    def merge_sort(self,nums):
        self.M=nums
        self.merge(0,len(self.M))
        return self.M
    #先將陣列平分為二 直到剩餘一項再開始合併(若為奇數則後陣列多一項)
    def merge(self,f,l):
        if f+1<l:
            m=int((f+l)/2)
            self.merge(f,m)
            self.merge(m,l)
            self.com(self.M[f:m],self.M[m:l],f)
    #合併過程(由左至右兩個陣列互相比較(同一陣列必定左小又大))
    def com(self,L,R,index):
        Lx=0
        Rx=0
        while True:
            if Lx<len(L) and Rx<len(R):
                if L[Lx]<R[Rx]:
                    self.M[index]=L[Lx]
                    Lx+=1
                else:
                    self.M[index]=R[Rx]
                    Rx=Rx+1
            elif Lx<len(L) and Rx==len(R):
                self.M[index]=L[Lx]
                Lx+=1
            elif Lx==len(L) and Rx<len(R):
                self.M[index]=R[Rx]
                Rx+=1
            else:
                break
            index+=1
'''
#以下為示範
N=[56,-5,1,64,-1,1,-1,-6357,-1,0,54,1,-453,13,-75,13,0,0]
N2=Solution().merge_sort(N)
print(N2)
'''
#參考資料:http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
