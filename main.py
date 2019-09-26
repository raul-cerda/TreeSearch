# Raul Cerda
# Python Version 3.7
# Slides L02 were used as reference for tree structure and ordering


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def get_val(self):
        return self.value

    def set(self, value):
        self.value = value

    def get_children(self):
        return self.children

    def add_child(self, new_node):
        self.children.append(new_node)


class Tree:
    def __init__(self, node):
        self.root = node

    def set_root(self, value):
        self.root = Node(value)

    # this is the BFS
    def find(self, value):
        opened = [self.root]
        closed = []
        while opened:
            x = opened[len(opened)-1]
            if x.get_val() == value:
                return True
            else:
                children = x.get_children()
                opened.remove(x)
                closed.insert(0, x)
                while children:
                    child = children[0]
                    if child not in opened and child not in closed:
                        opened.insert(0, child)
                    children.remove(child)

            # print the trace for opened and closed
            print('Open = ', end='')
            for i in range(len(opened)-1, -1, -1):
                print(opened[i].get_val(), end='')
            print('; Closed = ', end='')
            for elem in closed:
                print(elem.get_val(), end='')
            print()

        return False


def main():
    a = Node('A')

    b = Node('B')
    c = Node('C')
    d = Node('D')

    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    j = Node('J')

    k = Node('K')
    l = Node('L')
    m = Node('M')
    n = Node('N')
    o = Node('O')
    p = Node('P')
    q = Node('Q')
    r = Node('R')

    s = Node('S')
    t = Node('T')
    u = Node('U')

    a.add_child(b)
    a.add_child(c)
    a.add_child(d)
    b.add_child(e)
    b.add_child(f)
    c.add_child(g)
    c.add_child(h)
    d.add_child(i)
    d.add_child(j)
    e.add_child(k)
    e.add_child(l)
    f.add_child(l)
    f.add_child(m)
    g.add_child(n)
    h.add_child(o)
    h.add_child(p)
    i.add_child(p)
    i.add_child(q)
    j.add_child(r)
    k.add_child(s)
    l.add_child(t)
    p.add_child(u)

    test_tree = Tree(a)
    if test_tree.find('U'):
        print('found')
    else:
        print('not found')


main()
