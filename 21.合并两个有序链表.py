#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# @way python link-list
# @from https://www.cnblogs.com/dbf-/p/11382398.html
# @description 
# @result ac
# @O max(l1,l2)
# @time 2020-08-04 22:30:01
# @lc code=start
# Definition for singly-linked list.
# 定义链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 将list数组 以链表形式存储 创建链表
class linkList:

    def __init__(self):
        self.head=None
    def initList(self,data):
        # 创建头节点
        self.head=ListNode(data[0])
        r=self.head
        p=self.head
        for i in data[1:]:   
            # 遍历list 1到end
            node=ListNode(i)
            p.next=node
            p=p.next
        return r
    # def printLink(self,head):
    #     if head == None: return 
    #     node = head
    #     while node !=None:
    #         print (node.val,end=' ')
    #         node=node.next    

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 头插法 建立新的链表
        # print(l2)
        head=ListNode(0)
        key=head
        # 两个数组均非空
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2

                l2=l2.next
            head=head.next
            # 第一个数组非空 第二个数组为空
        if l1 != None:
                head.next=l1
            # 第2个数组非空 第1个数组为空
        
        elif l2 != None:
                head.next=l2
        return key.next


# @lc code=end
if __name__ == "__main__":
    
    list1=[]
    list2=[0]
    lists=linkList()
    l1=lists.initList(list1)
    l2=lists.initList(list2)
    # L1=lists.printLink(l1)
    # print('\r')
    # L2=lists.printLink(l2)
    # print('\r')
    s=Solution()
    mergeLink=s.mergeTwoLists(l1,l2)
    # links=lists.printLink(mergeLink)

