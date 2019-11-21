class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    
    #return TreeNode
    def insert(self,root,val):
        if root.val>=val:
            if root.left==None:
                root.left=TreeNode(val)
                return root.left
            else:
                return self.insert(root.left,val)
        else:
            if root.right==None:
                root.right=TreeNode(val)
                return root.right
            else:
                return self.insert(root.right,val)
            
    #return TreeNode
    def search(self,root,target):
        if root.val==target:
            return root
        elif root.val>target and root.left!=None:
            return self.search(root.left,target)
        elif root.val<target and root.right!=None:
            return self.search(root.right,target)
        return None
    
    #return complete TreeNode
    def delete(self,root,target):
        while self.search(root,target)!=None:
            self.find_del(root,target)
        return root
    def find_del(self,root,target):
        if root.val==target:
            if root.left==None and root.right==None:
                return None
            elif root.left!=None and root.right==None:
                return root.left
            elif root.left==None and root.right!=None:
                return root.right
            else:
                if root.left.left==None and root.left.right==None:
                    root.val=root.left.val
                    root.left=None
                else:
                    root.val=self.find_large(root.left)
                return root
        elif root.val>target and root.left!=None:
            if root.left.val!=target:
                self.find_del(root.left,target)
            else:
                root.left=self.find_del(root.left,target)
        elif root.val<target and root.right!=None:
            if root.right.val!=target:
                self.find_del(root.right,target)
            else:
                root.right=self.find_del(root.right,target)
    def find_large(self,root):
        if root.right!=None:
            if root.right.left==None and root.right.right==None:
                a=root.right.val
                root.right=None
                return a
            else:
                return self.find_large(root.right)
        else:
            a=root.val
            root.val=root.left.val
            root.right=root.left.right
            root.left=root.left.left
            return a
    
    #return complete TreeNode
    def modify(self,root,target,new_val):
        self.delete(root,target)
        self.insert(root,new_val)
        return root
'''
print("build BST--------------------")
#第一格擺1
N=TreeNode(1)
print("第一格擺1:",N.val==1)
#剩下的依序insert
print("insert--------------------依序擺入")
M=[-44,0,4444,1,-1,4,-1,44,-4,-1,0]
for i in range(len(M)):
    Solution().insert(N,M[i])
print("依序擺入:",M)
print("-1位置正確:",N.left.right.left.left.val==-1)
print("44位置正確:",N.right.left.right.val==44)

#尋找是否存在0或2
print("search--------------------")
print("0存在:",Solution().search(N,0).val==0)
print("2不存在:",Solution().search(N,2)==None)

#刪除所有-1
print("delete--------------------刪除所有-1")
print("-1不存在(刪除前)",Solution().search(N,-1)==None)
Solution().delete(N,-1)
print("-1不存在(刪除後)",Solution().search(N,-1)==None)

#先刪除後新增
print("modify--------------------刪除44，新增2")
Solution().modify(N,44,2)
print("44不存在(刪除後):",Solution().search(N,44)==None)
print("2存在(新增後):",Solution().search(N,2).val==2)
'''
'''
#輸出結果
build BST--------------------
第一格擺1: True
insert--------------------依序擺入
依序擺入: [-44, 0, 4444, 1, -1, 4, -1, 44, -4, -1, 0]
-1位置正確: True
44位置正確: True
search--------------------
0存在: True
2不存在: True
delete--------------------刪除所有-1
-1不存在(刪除前) False
-1不存在(刪除後) True
modify--------------------刪除44，新增2
44不存在(刪除後): True
2存在(新增後): True
'''
