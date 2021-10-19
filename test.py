# 3-rd version:
from LListReverse import *

llst = LinkList()

llst.Add_range(1, 8)    # original list: 1>2>3>4>5>6>7>8

# test: reverse whole llst : (0)
# test: do nothing         : (1)
# test:                    : (3) result: 3>2>1>6>5>4>8>7
llst.Reverse_in_group(3)
llst.Show()

