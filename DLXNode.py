class DLXNode:
    def __init__(self, rowID=None, colID=None):
        self.rowID = rowID
        self.colID = colID
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.column = None

    def hook_right(self, node):
        node.right = self.right
        node.right.left = node
        node.left = self
        self.right = node

    def hook_down(self, node):
        node.down = self.down
        node.down.up = node
        node.up = self
        self.down = node

    def unlink_left_right(self):
        self.left.right = self.right
        self.right.left = self.left

    def relink_left_right(self):
        self.left.right = self
        self.right.left = self

    def unlink_up_down(self):
        self.up.down = self.down
        self.down.up = self.up

    def relink_up_down(self):
        self.up.down = self
        self.down.up = self

    def right_iter(self):
        node = self.right
        while node != self:
            yield node
            node = node.right

    def left_iter(self):
        node = self.left
        while node != self:
            yield node
            node = node.left

    def down_iter(self):
        node = self.down
        while node != self:
            yield node
            node = node.down

    def up_iter(self):
        node = self.up
        while node != self:
            yield node
            node = node.up

class DLXColumn(DLXNode):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.size = 0

    def cover(self):
        self.unlink_left_right()
        for i in self.down_iter():
            for j in i.right_iter():
                j.unlink_up_down()
                j.column.size -= 1

    def uncover(self):
        for i in self.up_iter():
            for j in i.left_iter():
                j.column.size += 1
                j.relink_up_down()
        self.relink_left_right()
