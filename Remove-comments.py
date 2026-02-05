class Solution:
    def removeComments(self, source):
        result = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            while i < len(line):
              
#we're Currently inside a block comment:
                if in_block:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 2
                    else:
                        i += 1

#we're Not inside a block comment
                else:
                    # then it's a line Comment:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break

                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 2

                    # normal
                    else:
                        buffer += line[i]
                        i += 1

            # we Add line if it is Valid and not inside block
            if not in_block and buffer:
                result.append(buffer)
                buffer = ""

        return result
