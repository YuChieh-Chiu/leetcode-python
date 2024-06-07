import re
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        thought:
        - sort dictionary by length according to `If a derivative can be replaced by more than one root, replace it with the root that has the shortest length`
        - split sentence by space according to `Every two consecutive words in sentence will be separated by exactly one space.` and `sentence does not have leading or trailing spaces.`
        - for loop traverse splitted sentence to replace the word with derivative using regular expression
        """
        dictionary = sorted(dictionary, key=lambda x: (len(x), x), reverse=False)
        derivative_list = []
        for word in sentence.split(" "):
            replaced = False
            for root in dictionary:
                if re.match(root, word):
                    derivative_list.append(root)
                    replaced = True
                    break
                else:
                    pass
            if replaced:
                pass
            else:
                derivative_list.append(word)
        derivative_sentence = " ".join(derivative_list)
        return derivative_sentence
