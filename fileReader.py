import re

def ignore_commented_line(lines):
    clean_lines = []
    comment_pattern = re.compile("^#")
    for s in lt:
        m = comment_pattern.match(s)
        if m is None:
            s = s.replace("\t", "")
            s = s.replace(" ", "")
            s = s.replace("\n", "")
            clean_lines.append(s)
    return clean_lines

class OpenedFile:
    def __init__(self, name, mode) -> None:
        self.name = name
        self.mode = mode
        self.handler = open(self.name, mode, encoding="utf-8")

    def readfile(self,):
        if self.mode == "w" or self.mode == "w+":
            raise Exception("No premission to read")
        return self.handler.readlines()

    def writefile(self, lines):
        if self.mode == "r" or self.mode == "r+":
            raise Exception("No premission to write")
        self.handler.writelines(lines)
    
    def __del__(self, ):
        self.handler.close()

def readfile(name,):
    # with open(name, "r", encoding="utf-8") as f:
    #     return f.readlines()
    f = OpenedFile(name, "r")
    return f.readfile()


def writefile(name, lines, mode="w"):
    # with open(name, "w", encoding="utf-8") as f:
    #     f.writelines(lines)
    f = OpenedFile(name, mode)
    f.writefile(lines)

if __name__=="__main__":
    lt = readfile("files.txt")
    print(ignore_commented_line(lt))

    f = OpenedFile("aaa", "w+")
    f.writefile(['foo\n', '\tboo\n'])