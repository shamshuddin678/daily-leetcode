class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # hash set + prefix
        root = set(dictionary)
        result = []

        for word in sentence.split():
            replacement = word 
            for i in range(len(word)):
                prefix = word[ : i]
                if(prefix in root):
                    replacement = prefix
                    break
            result.append(replacement)
        return " ".join(result)