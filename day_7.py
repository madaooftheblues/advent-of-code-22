import input


class FileTreeNodeCat:
    pass


class FileTreeNode:
    def __init__(self, name: str, cat: FileTreeNodeCat):
        self.name = name
        self.cat = cat


class Dir(FileTreeNodeCat):
    children: list[FileTreeNode]

    def __init__(self, children: list[FileTreeNode]):
        self.children = children


class File(FileTreeNodeCat):
    size: int

    def __init__(self, size: int):
        self.size = size


class FileTree:
    root: FileTreeNode | None
    path: list[FileTreeNode]

    def __init__(self):
        self.root = None
        self.path = []

    def insert(self, name: str, cat: FileTreeNodeCat):
        if not self.root:
            self.root = FileTreeNode(name, cat)
            self.path.append(self.root)

    def add_to_current_dir(self, node: FileTreeNode):
        if not self.current or not isinstance(self.current.cat, Dir):
            return

        self.current.cat.children.append(node)

    def change_dir(self, name: str):
        if not self.current or not isinstance(self.current.cat, Dir):
            return
        for child in self.current.cat.children:
            if child.name == name:
                self.path.append(child)
                break

    def back(self):
        if len(self.path) > 0:
            self.path.pop()

    def print(self):
        que = [self.root]
        while len(que) > 0:
            dir = que.pop(0)
            if not dir:
                continue

            print(dir.name)

            if not isinstance(dir.cat, Dir):
                continue

            for child in dir.cat.children:
                if isinstance(child.cat, File):
                    print(" - " + child.name, f" (file, size = {child.cat.size})")
                elif isinstance(child.cat, Dir):
                    print(" - " + child.name, " (dir)")
                    que.append(child)
            print()

    def sizes(self, sizes: list[int]):
        FileTree.cal_dir_sizes(self.root, sizes)

    @property
    def current(self):
        if len(self.path) > 0:
            return self.path[-1]

    @staticmethod
    def cal_dir_sizes(node: FileTreeNode | None, sizes: list[int]):
        if not node or not isinstance(node.cat, Dir):
            return
        sum = 0
        for child in node.cat.children:
            if isinstance(child.cat, File):
                sum += child.cat.size
            elif isinstance(child.cat, Dir):
                sum += FileTree.cal_dir_sizes(child, sizes)
        # sizes.append(sizes[-1] + sum if sizes else sum)
        sizes.append(sum)
        return sum


lines = input.gen_line()


def generate_file_tree(ft: FileTree, lines):
    for line in lines:
        ins = line.strip().lstrip("$").split()
        if ins[0] == "cd":
            if ins[-1] == "/":
                dir = Dir([])
                name = ins[-1]
                ft.insert(name, dir)
            elif ins[-1] == "..":
                ft.back()
            else:
                ft.change_dir(ins[-1])
        elif ins[0] == "dir":
            dir = Dir([])
            name = ins[-1]
            ft.add_to_current_dir(FileTreeNode(name, dir))
        elif ins[0].isdecimal():
            file = File(int(ins[0]))
            name = ins[-1]
            ft.add_to_current_dir(FileTreeNode(name, file))


def process_file_tree() -> list[int]:
    """
    Generates a file tree according to the given instructions
    and returns a sorted list of integers that represent the sizes of the
    directories in the file tree
    """
    ft = FileTree()
    generate_file_tree(ft, lines)
    ft.print()
    sizes: list[int] = []
    ft.sizes(sizes)
    sizes.sort()
    print(sizes)
    return sizes


def silver(sizes: list[int]):
    total = 0
    for s in sizes:
        if s > 100000:
            break
        total += s
    return total


def gold(sizes: list[int]):
    total_space = 70000000
    required_space = 30000000
    unused_space = total_space - sizes[-1]

    for i in range(len(sizes) - 2, 0, -1):
        if unused_space + sizes[i] < required_space:
            return sizes[i + 1] if len(sizes) > i else 0


if __name__ == "__main__":
    sizes = process_file_tree()
    print("silver:", silver(sizes))
    print("gold:", gold(sizes))
