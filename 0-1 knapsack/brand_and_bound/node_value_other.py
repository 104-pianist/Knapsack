from copy import deepcopy
from queue import PriorityQueue



class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.rate = value/weight
        
    def __lt__(self, other):
        return self.rate > other.rate

class Node:
    def __init__(self):
        self.layer = 0
        self.info = []
        self.optimum_value = 0
        self.total_weight = 0
        
    def __lt__(self, other):
        return self.optimum_value > other.optimum_value


class Knapsack:
    def __init__(self, quantiy, capacity):
        self.quantiy = quantiy
        self.items = []
        self.capacity = capacity
        self.max_value = 0
        self.pq = PriorityQueue()

    def add_item(self, item):
        self.items.append(item)

    def sort_item(self):
        self.items.sort()
    
    def calculate_optimum_value(self, node):
        weights = 0
        values = 0
        for i in node.info:
            weights += i.weight
            values += i.value
        # 超出背包容量（剪枝）
        if weights > self.capacity:
            node.optimum_value = 0
            return
        node.total_weight = weights
        for j in range(node.layer, self.quantiy):
            if weights + self.items[j].weight <= self.capacity:
                weights += self.items[j].weight
                values += self.items[j].value
            else:
                values += self.items[j].rate * (self.capacity-weights)
                break
        node.optimum_value = values

    def knapsack(self):
        node = Node()
        self.calculate_optimum_value(node)
        self.max_value = node.optimum_value
        self.pq.put(node)
        while True:
            node = self.pq.get()
            if node.layer == self.quantiy:
                break
            node_L = deepcopy(node)
            node_L.layer += 1
            node_L.info.append(self.items[node_L.layer-1])
            self.calculate_optimum_value(node_L)
            if node_L.optimum_value>0  and node_L.optimum_value<=self.max_value:
                self.pq.put(node_L)
            
            node_R = deepcopy(node)
            node_R.layer += 1
            self.calculate_optimum_value(node_R)
            if node_R.optimum_value>0  and node_R.optimum_value<=self.max_value:
                self.pq.put(node_R)    
        return node

def main():
    item1 = Item(4, 40)
    item2 = Item(7, 42)
    item3 = Item(5, 25)
    item4 = Item(3, 12)
    k = Knapsack(4, 10)
    k.add_item(item1)
    k.add_item(item2)
    k.add_item(item3)
    k.add_item(item4)
    
    k.sort_item()
    nn = k.knapsack()
    print("所有挑选方案价值总和的最大值是: {}".format(nn.optimum_value))
    # print(nn.total_weight)
    # for i in nn.info:
    #     print(i.w)


if __name__ == "__main__":
    main()