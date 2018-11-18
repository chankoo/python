class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()
    
    def push(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def pop(self):

        if self.head.next is None:
            # print('ERR: The queue is empty!!!')
            print(-1)
            return -1
        else:
            pop_node = self.head.next
            self.head.next = pop_node.next
            print(pop_node.data)
            return pop_node.data
            
    def disp(self):
        tmp = []
        self
        cur = self.head.next
        if cur is None:
            print([])
            return
        while cur.next is not None:
            tmp.append(cur.data)
            cur = cur.next
        tmp.append(cur.data)
        print(tmp)


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
    
    def front(self):
        if self.head.next is None:
            print(-1)
        else:
            print(self.head.next.data)

    def back(self):
        if self.head.next is None:
            print(-1)
        else:
            cur_node = self.head.next
            while cur_node.next is not None:
                cur_node = cur_node.next
            print(cur_node.data)


if __name__=='__main__':
    q = Queue()
    N = int(input())
    cmd_lst = [input() for i in range(N)]
    
    for line in cmd_lst:
        if ' ' in line:
            cmd, data = line.split()
        else:
            cmd, data = line, None

        if cmd == 'push':
            q.push(data)
        elif cmd == 'pop':
            q.pop()
        elif cmd == 'size':
            q.size()
        elif cmd == 'empty':
            q.empty()
        elif cmd == 'front':
            q.front()
        elif cmd == 'back':
            q.back()
        else:
            print('ERR')

