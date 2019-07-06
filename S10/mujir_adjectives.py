import re

fr=open('mujir.txt')
text = fr.read()
fr.close()

pat = r"Glory be to You O (.+?)![\.,]? Exalted are You O (.+?)!"
result = re.findall(pat , text)

print(len(result), result)