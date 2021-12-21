from queue import PriorityQueue


class Item:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.rate = price/weight

    def __lt__(self, other):
        return self.rate < other.rate

class Node:
    def __init__(self, layer, weight, price, upper_bound, left=None, right=None):
        self.layer = layer
        self.weight = weight
        self.price = price
        self.upper_bound = upper_bound   

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

    def calculate_optimum_value(self):
        optimum_value = 0
        self.items.sort()
        while True:
            item = self.items.pop()
            if self.node_pq.qsize() == 0:
                pre = Node(0, 0, 0, item.rate*self.capacity)
            else:
                pre = self.node_pq.get()
            
            if (w := item.weight+pre.weight) < self.capacity:
                if not self.items:
                    optimum_value = pre.price
                    break
                left = Node(pre.layer+1, w, (p := pre.price+item.price)
                            , p+(self.capacity-w)*self.items[-1].rate)
                # print("l: ", left.layer, left.weight, left.price, left.upper_bound)
                pre.left = left
                self.node_pq.put(left)
            
            print(pre.layer, pre.weight, pre.price, pre.upper_bound)
            if not self.items:
                    optimum_value = pre.price
                    break
            right = Node(pre.layer+1, pre.weight, pre.price
                         , pre.price+(self.capacity-pre.weight)*self.items[-1].rate)
            # print("r: ", right.layer, right.weight, right.price, right.upper_bound)
            pre.right = right

            self.node_pq.put(right) 
        return optimum_value

def main():
    item1 = Item(4, 40)
    item0 = Item(7, 42)
    item3 = Item(5, 25)
    item2 = Item(3, 12)

    k = Knapsack(4, 10)
    k.add_item(item0)
    k.add_item(item1)
    k.add_item(item2)
    k.add_item(item3)

    optimum_value = k.calculate_optimum_value()
    print("所有挑选方案价值总和的最大值是:{}".format(optimum_value))

if __name__ == "__main__":
    main()

