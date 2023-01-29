class LinkedList:
    """Linked list."""

    def __init__(self, node: int) -> None:
        if not isinstance(node, int):
            raise TypeError
        self._now = node
        self._next = None

    def __str__(self) -> str:
        return f"{self._now} -> {self._next}"

    def count(self) -> int: # return length of list
        count: int = 1
        nodelist: LinkedList = self
        while nodelist._next:
            count += 1
            nodelist = nodelist._next
        return count

    def append(self, element: int) -> None: # add element to the of list
        if not isinstance(element, int):
            raise TypeError
        nodelist: LinkedList = self
        while nodelist._next:
            nodelist = nodelist._next
        nodelist._next = LinkedList(element)

    def push(self, element: int) -> None:
        if not isinstance(element, int):
            raise TypeError
        nodelist: LinkedList = self

        all_nodes: list[int] = []
        while nodelist != None:
            now: LinkedList = LinkedList(nodelist._now)
            all_nodes.append(now)
            nodelist = nodelist._next

        self._now = element
        self._next = None

        nodelist = self
        node: LinkedList
        for node in all_nodes:
            nodelist._next = node
            nodelist = nodelist._next

    def pop(self, index: int = -1) -> int: # remove element from the end of list and return it 
        if self.count() == 1:
            return
        if index < -1 or index >= self.count():
            raise IndexError
        if not isinstance(index, int):
            raise TypeError
        data: int
        nodelist: LinkedList = self
        if index == -1:
            while nodelist._next._next:
                nodelist = nodelist._next
            data = nodelist._next._now
            nodelist._next = None
        else:
            all_nodes: list[int] = []
            count: int = -1
            while nodelist:
                count += 1
                if count == index:
                    data = nodelist._now
                else:
                    all_nodes.append(nodelist._now)
                nodelist = nodelist._next
            nodelist = self
            nodelist._now = all_nodes[0]
            node: LinkedList
            for node in all_nodes[1:]:
                nodelist._next = LinkedList(node)
                nodelist = nodelist._next
        return data

    def get(self ,index: int) -> int: # return the value for index 
        if not isinstance(index, int):
            raise TypeError
        if index < -self.count() or index >= self.count():
            raise IndexError
        nodelist: LinkedList = self
        if index < 0:
            index += self.count()
        while index != 0:
            index -= 1
            nodelist = nodelist._next
        return nodelist._now

    def join(self, node: 'LinkedList') -> None: # merges two lists into one
        if not isinstance(node, LinkedList):
            raise TypeError
        all_nodes: list[int] = []
        nodelist: LinkedList
        nodelist = self
        while nodelist:
            all_nodes.append(nodelist._now)
            nodelist = nodelist._next

        nodelist = node
        while nodelist:
            all_nodes.append(nodelist._now)
            nodelist = nodelist._next
        
        node: int
        data: LinkedList = LinkedList(all_nodes[-1])
        for node in all_nodes[:-1][::-1]:
            new_data = LinkedList(node)
            new_data._next = data
            data = new_data
        self._now = data._now
        self._next = data._next

    def sort(self) -> None: # sort the list
        nodelist: LinkedList = self
        all_nodes: list[int] = []
        while nodelist:
            all_nodes.append(nodelist._now)
            nodelist = nodelist._next
        all_nodes.sort()

        data: LinkedList = LinkedList(all_nodes[-1])
        node: int
        for node in all_nodes[:-1][::-1]:
            new_data = LinkedList(node)
            new_data._next = data
            data = new_data
        self._now = data._now
        self._next = data._next

    def reverse(self) -> None: # reverse the list
        nodelist: LinkedList = self
        all_nodes: list[int] = []
        while nodelist:
            all_nodes.append(nodelist._now)
            nodelist = nodelist._next
        all_nodes.reverse()

        data: LinkedList = LinkedList(all_nodes[-1])
        node: int
        for node in all_nodes[:-1][::-1]:
            new_data = LinkedList(node)
            new_data._next = data
            data = new_data
        self._now = data._now
        self._next = data._next