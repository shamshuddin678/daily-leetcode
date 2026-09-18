class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ""
        i = 0
        while(i < len(command)):
            if(command[i] == 'G'):
                res += 'G'
                i += 1
            elif(command[i : i + 2] == '()'):
                res += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                res += 'al'
                i += 4

        return res