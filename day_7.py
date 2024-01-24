class FileTreeElement:
    def __init__(self, name):
        self.name = name
class File(FileTreeElement):
    def __init__(self, name: str, size: float):
        self.size = size

class Dir(FileTreeElement):
    def __init__(self, name):
        self.children = []
