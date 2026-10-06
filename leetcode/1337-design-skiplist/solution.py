import random

class Node:
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level


class Skiplist:

    def __init__(self):
        self.head = Node(-1, 16)

    def search(self, target: int) -> bool:
        curr = self.head

        for level in range(15, -1, -1):
            while curr.next[level] and curr.next[level].val < target:
                curr = curr.next[level]

        curr = curr.next[0]

        return curr is not None and curr.val == target


    def add(self, num: int) -> None:
        curr = self.head
        update = [None] * 16

        # Find where num belongs at every level
        for level in range(15, -1, -1):
            while curr.next[level] and curr.next[level].val < num:
                curr = curr.next[level]

            update[level] = curr

        # Randomly choose how tall the new node is
        height = 1
        while height < 16 and random.random() < 0.5:
            height += 1

        new = Node(num, height)

        # Insert at every level the node participates in
        for level in range(height):
            new.next[level] = update[level].next[level]
            update[level].next[level] = new


    def erase(self, num: int) -> bool:
        curr = self.head
        update = [None] * 16

        # Find node before num at every level
        for level in range(15, -1, -1):
            while curr.next[level] and curr.next[level].val < num:
                curr = curr.next[level]

            update[level] = curr

        target = curr.next[0]

        if target is None or target.val != num:
            return False

        # Remove target from every level where it exists
        for level in range(len(target.next)):
            if update[level].next[level] == target:
                update[level].next[level] = target.next[level]

        return True
