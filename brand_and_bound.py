from copy import copy,deepcopy
class Item:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w
    def __lt__(self, other):
        return self.r < other.r

class Node:
    def __init__(self):
        self.layer = -1
        self.info = []
        self.optimum_value = -1
        self.total_weight = 0
    def __lt__(self, other):
        return self.optimum_value < other.optimum_value


class Knapsack:
    def __init__(self, N, max_weight):
        self.N = N
        self.items = []
        self.max_weight = max_weight
        self.max_value = 0
        self.queue = []

    def add_item(self, item):
        self.items.append(item)

    def sort_item(self):
        self.items.sort(reverse=True)
    
    def calculate_optimum_value(self, node):
        weight = 0
        value = 0
        for i in node.info:
            weight += i.w
            value += i.v
        # 超出背包容量（剪枝）
        if weight > self.max_weight:
            node.optimum_value = -1
            return
        node.total_weight = weight
        for j in range(node.layer + 1, self.N):
            if weight + self.items[j].w <= self.max_weight:
                weight += self.items[j].w
                value += self.items[j].v
            else:
                value += self.items[j].r * (self.max_weight - weight)
                break
        node.optimum_value = value

    def knapsack(self):
        node = Node()
        self.calculate_optimum_value(node)
        self.max_value = node.optimum_value
        self.queue.append(node)
        flag = False
        while self.queue:
            if not flag:
                node = self.queue.pop()
            flag = True
            node_L = deepcopy(node)
            node_L.layer += 1
            node_L.info.append(self.items[node_L.layer])
            self.calculate_optimum_value(node_L)
            if node_L.optimum_value>0  and node_L.optimum_value <=self.max_value:
                self.queue.append(node_L)
            
            node_R = deepcopy(node)
            node_R.layer += 1
            self.calculate_optimum_value(node_R)
            if node_R.optimum_value>0  and node_R.optimum_value <=self.max_value:
                self.queue.append(node_R)
            
            self.queue.sort()
            node = self.queue.pop()
            
            if node.layer == 3:
                break
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
    print(nn.optimum_value)
    print(nn.total_weight)
    for i in nn.info:
        print(i.w)


if __name__ == "__main__":
    main()