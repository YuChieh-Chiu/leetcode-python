import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        thought:
        - from the problem description, we can infer the following properties of a Unix-style file system:
            (a) a single period '.' signifies the current directory.
            (b) a double period '..' denotes moving up one directory level.
            (c) multiple slashes such as '//', '///', etc., are interpreted as a single slash '/'.
            (d) sequences of periods like '...' are valid names for files or directories.
        - therefore, we can follow these steps:
            (1) check if `path` is '/' or any combination of multiple slashes. If so, return '/' directly; otherwise, continue.
            (2) create an empty list to store the processed path components.
            (3) split `path` by the slash '/' to get each directory level of the file path.
            (4) handle each property mentioned above:
                - if the current directory equals '.', skip it.
                - if the current directory equals '..', pop the last directory from the list created in step (2).
                - if the current directory is '', skip it.
                - otherwise, append it to the list created in step (2).
            (5) finally, join all the directory components together using a single slash '/'.
        - tips: The technique used here is a `LIFO (Last-In-First-Out)` technique, which is a property of the `stack` data structure.
        """
        if re.fullmatch(r"/+", path):
            return "/"
        simplified_path = []
        for dir in path.split("/"):
            if dir == ".":
                pass
            elif dir == "..":
                if simplified_path == []:
                    pass
                else:
                    simplified_path.pop()
            elif dir == "":
                pass
            else:
                simplified_path.append(dir)
        return "/" + "/".join(simplified_path)
