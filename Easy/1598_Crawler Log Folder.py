class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        thought:
        - we can do these steps:
            (1) set the list to store element of folder path by order
            (2) check the operation is which one
                - if the operation is '../' and list is not empty, pop out the last element in list
                - if the operation is '../' but list is empty, do not do anything
                - if the operation is './', do not do anything again
                - if the operation is 'x/', push 'x/' to the end of the list
            (3) at the end, the length of the list is the minimum number of operations needed to go back to the main folder after the change folder operations above
        """
        folders = []
        for log in logs:
            if log == "../": 
                if folders != []:
                    folders.pop()
                else:
                    pass
            elif log == "./":
                pass
            else:
                folders.append(log)
        return len(folders)
