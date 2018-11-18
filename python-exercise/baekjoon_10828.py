class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node()

    def push(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        return

    def display(self):
        els = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            els.append(cur_node.data)
        print(els)

    def size(self):
        cnt = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            cnt += 1
        print(cnt)
        return cnt

    def empty(self):
        if self.head.next is None:
            print(1)
        else:
            print(0)

    def pop(self):
        if self.head.next is None:
            # print("ERR: The stack is empty!!!")
            print(-1)
            return None
        else:
            cur_node = self.head
            while cur_node.next is not None:
                last_node = cur_node
                cur_node = cur_node.next
            last_node.next = None
            print(cur_node.data)
            return cur_node.data

    def top(self):
        if self.head.next is None:
            print(-1)
            return None
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        print(cur_node.data)


if __name__ == '__main__':
    s = Stack()
    N = int(input())
    cmd_lst = [input() for i in range(N)]
    
    for line in cmd_lst:
        if ' ' in line:
            cmd, data = line.split()
        else:
            cmd, data = line, None

        if cmd == 'push':
            s.push(data)
        elif cmd == 'pop':
            s.pop()
        elif cmd == 'size':
            s.size()
        elif cmd == 'empty':
            s.empty()
        elif cmd == 'top':
            s.top()
        else:
            print('ERR')
        


            
    