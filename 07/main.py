class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.subs = {}
        self.filesSize = 0

    def get_size(self):
        return self.filesSize + sum([x.get_size() for x in self.subs.values()])

    def get_most(self, most):
        base = self.get_size()
        base = base if base < most else 0
        for u in self.subs.values():
            base += u.get_most(most)
        return base

    def get_dir(self, levels):
        curr = self
        if levels == []:
            return curr
        if len(levels) == 1:
            if not levels[0] in self.subs.keys():
                self.subs[levels[0]] = Directory(levels[0])
        return self.subs[levels[0]].get_dir(levels[1:])
    
    def get_smallest(self,max):
        minimal = self.get_size()
        for sub in self.subs.values():
            val = sub.get_smallest(max)
            if val < minimal and val >= max:
                minimal = val
        return minimal

with open("input") as f:
    root = Directory("root")
    levels = []
    lines = [x.strip() for x in f.readlines()]
    commands_list = [(i,x.split("$ ")[1]) for i,x in enumerate(lines) if "$" in x]
    for (index,command) in commands_list:
        if command.startswith("cd"):
            dir = command.split()[1]
            if dir == "/":
                levels = []
            elif dir == "..":
                levels.pop()
            else:
                levels.append(dir)

        if command == "ls":
            startIndex = index+1
            cmd = (index, command)
            commands_list_index = commands_list.index(cmd)
            endIndex = len(lines)
            if len(commands_list) > commands_list_index+1:   
                endIndex = (commands_list[commands_list.index(cmd)+1][0])
            content = lines[startIndex:endIndex]
            dir_size = sum([int(x.split()[0]) for x in content if not x.startswith("dir")])
            dir = root.get_dir(levels)
            dir.filesSize = dir_size
    print("Total sum with most 100 000: ", root.get_most(100_000))
    print("Smallest : ", root.get_smallest(30000000 - (70000000 - root.get_size())))
            


