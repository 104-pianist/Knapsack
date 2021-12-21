import copy
from queue import PriorityQueue



class Item:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

class Node:
    def __init__(self, layer, weight, price, items, left=None, right=None):
        self.layer = layer
        self.weight = weight
        self.price = price
        self.items = items

    def __lt__(self, other):
        return self.price > other.price
    

class Knapsack:
    def __init__(self, quantity, capacity):
        self.quantity = quantity
        self.capacity = capacity
        self.items = []
        self.node_pq = PriorityQueue()

    def add_item(self, item):
        self.items.append(item)

    def calculate_optimum_value(self):
        optimum_value = 0
        self.node_pq.put(Node(0, 0, 0.0, self.items))

        while True:
            pre = self.node_pq.get()
            if pre.layer == self.quantity:
                if self.node_pq.qsize() == 0:
                    break
                else:
                    pre = self.node_pq.get()
                    print(pre.layer)
            # print(pre.weight, pre.price)
            item = pre.items[0]
            
            optimum_value = max(optimum_value, pre.price)
            
            l = pre.layer+1
            if (w := pre.weight+item.weight) < self.capacity:
                items_L = pre.items.copy()
                items_L.remove(item)
                left = Node(l, w, pre.price+item.price, items_L)
                print("l: ", left.layer, left.weight, left.price, len(left.items))
                pre.left = left
                self.node_pq.put(left)
            items_R = pre.items.copy()
            items_R.remove(item)
            right = Node(l, pre.weight, pre.price, items_R)
            print("r: ", right.layer, right.weight, right.price, len(right.items))
            pre.right = right
            self.node_pq.put(right)

        return optimum_value

def main():
    item0 = Item(16, 45)
    item1 = Item(15, 25)
    item2 = Item(15, 25)

    k = Knapsack(3, 30)
    k.add_item(item0)
    k.add_item(item1)
    k.add_item(item2)
    # for item in k.items:
    #     print(item.weight, item.price)
    optimum_value = k.calculate_optimum_value()
    print("所有挑选方案价值总和的最大值是:{}".format(optimum_value))

if __name__ == "__main__":
    main()