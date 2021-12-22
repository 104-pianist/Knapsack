from queue import PriorityQueue



class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.rate = value/weight
    # non-increasing sort
    def __lt__(self, other):
        return self.rate < other.rate 

class Node:
    def __init__(self, layer, acc_weight, acc_value, upper_bound, rest_items, left=None, right=None):
        self.layer = layer
        self.acc_weight = acc_weight  # accumulated weight
        self.acc_value = acc_value  # accumulated value
        self.upper_bound = upper_bound
        '''the rest of items to be selected
            , when layer increase by one, the size of items decrease by one.
        '''
        self.rest_items = rest_items
    # non-increasing sort
    def __lt__(self, other):
        return self.upper_bound > other.upper_bound

class Knapsack:
    def __init__(self, quantity, capacity):
        self.quantity = quantity
        self.capacity = capacity
        self.items = []
        self.node_pq = PriorityQueue()
        
    def add_item(self, item):
        self.items.append(item)
        
    def sort_item(self):
        self.items.sort()

    def calculate_optimum_value(self):
        # initialize
        optimum_value = 0.0  
        self.node_pq.put(Node(0, 0, 0.0, self.items[-1].rate*self.capacity, self.items))
        
        while True:
            pre = self.node_pq.get()
            # print(pre.layer, pre.acc_weight, pre.acc_value, pre.upper_bound)
            optimum_value = max(optimum_value, pre.acc_value)
            if pre.layer == self.quantity:
                if self.node_pq.qsize() == 0:
                    break
                elif not pre.rest_items:
                    continue
                else:
                    pre = self.node_pq.get()
            item = pre.rest_items.pop()
            
            l = pre.layer+1
            if (w_L := pre.acc_weight+item.weight) <= self.capacity:
                p_L = pre.acc_value+item.value
                if not pre.rest_items:
                    ub_L = pre.acc_value
                else:
                    ub_L = p_L+(self.capacity-w_L)*pre.rest_items[-1].rate
                items_L = pre.rest_items.copy()
                
                left = Node(l, w_L, p_L, ub_L, items_L)
                # print("l: ", left.layer, left.acc_weight, left.acc_value, left.upper_bound)
                pre.left = left
                self.node_pq.put(left)
            
            w_R = pre.acc_weight
            p_R = pre.acc_value
            if not pre.rest_items:
                ub_R = pre.acc_value
            else:
                ub_R = pre.acc_value+(self.capacity-pre.acc_weight)*pre.rest_items[-1].rate
            items_R = pre.rest_items.copy()
            right = Node(l, w_R, p_R, ub_R, items_R)
            # print("r: ", right.layer, right.acc_weight, right.acc_value, right.upper_bound)
            pre.right = right
            self.node_pq.put(right)
            
        return optimum_value

def main():
    """测试用例0
    item0 = Item(16, 45)
    item1 = Item(15, 25)
    item2 = Item(15, 25)

    k = Knapsack(3, 30)
    k.add_item(item0)
    k.add_item(item1)
    k.add_item(item2)
    """
    item1 = Item(4, 40)
    item0 = Item(7, 42)
    item3 = Item(5, 25)
    item2 = Item(3, 12)

    k = Knapsack(4, 10)
    k.add_item(item0)
    k.add_item(item1)
    k.add_item(item2)
    k.add_item(item3)

    k.sort_item()
    optimum_value = k.calculate_optimum_value()
    print("The maximum value of the sum of all alternatives is {}.".format(optimum_value))

if __name__ == "__main__":
    main()
