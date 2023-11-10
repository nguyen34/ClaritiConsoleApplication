class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()

    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.data)
            nodes += current_node.children[::-1]

    def children_data(self):
        return [child.data for child in self.children]

    def find_child(self, target):
        if self.data == target:
            return self
        else:
            for child in self.children:
                # if child data is a string, make it case insensitive matching
                if type(child.data) == str:
                    if child.data.lower() == target.lower():
                        return child
                else:
                    if child.data == target:
                        return child
        return None
