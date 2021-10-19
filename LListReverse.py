# reverse linked list in 'groups' - with given group size 
# ex 1>2>3>4>5>6>7>8 [group size = 3] result: 3>2>1>6>5>4>8>7

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Push(self, data):  # push to 'start'
        if (self.head is None):
            self.head = Node(data)
            self.tail = self.head
        else:
            head_prv = self.head
            self.head = Node(data)
            self.head.next = head_prv
    
    def Add(self, data):    # add to 'tail'
        if (self.head is None):
            self.Push(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        
    # reverse groups of elements
    def Reverse_in_group(self, grp_size):
        p_grp = Node()
        p_grp.next = self.head
        while(p_grp.next):
            p_grp = self.Reverse(p_grp, grp_size)
    
    # get list size
    @property
    def Count(self):
        count = 0
        node = self.head
        while(node):
            count = count + 1
            node = node.next
        return count

    def Show(self):
        count = 0
        node = self.head
        while(node):
            count = count + 1
            print(f"{count}: {node.val}")
            node = node.next
    
    def Add_range(self, fr, to):    # add to 'tail' numeric range from, from + 1, ...
        if (to < fr):
            to = fr + 1
        else:
            to = to + 1
        for ind in range(fr, to, 1 if fr <= to else -1):
            self.Add(ind) 
    
    # reverse group of nodes; return p-grp = last node in reversed group
    # update self.head and self.tail       
    def Reverse(self, p_grp, grp_size):
        nod = p_grp.next            # first node in original group
        prv_nod = None              # previous node in original group
        ind = 0
        revers_grp_fst = None       # first node in reversed group
        revers_grp_lst = p_grp.next # last node in reversed group

        if (grp_size == 0):         # if group size not set (i.e. 0), assume whole llist to be reversed
            grp_size = self.Count

        while(nod and ind < grp_size): 
            ind = ind + 1
            next_nod = nod.next
            nod.next = prv_nod
            revers_grp_fst = nod        # last scanned node => first in reversed group
            prv_nod = nod
            nod = next_nod

        if (p_grp.next == self.head):   #update self.head / tail
            self.head = revers_grp_fst

        if (prv_nod == self.tail):
            self.tail = p_grp.next

        p_grp.next = revers_grp_fst
        revers_grp_lst.next = nod
        return revers_grp_lst            # return [p_grp] - last node in the reversed group


         
