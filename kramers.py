import os
import re
import binascii

from pystyle import Center, Anime, Colors, Colorate, System, Write

banner = '''
 /$$   /$$ /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$   /$$$$$$ 
| $$  /$$/| $$__  $$ /$$__  $$| $$$    /$$$| $$_____/| $$__  $$ /$$__  $$
| $$ /$$/ | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$      | $$  \ $$| $$  \__/
| $$$$$/  | $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$$$$   | $$$$$$$/|  $$$$$$ 
| $$  $$  | $$__  $$| $$__  $$| $$  $$$| $$| $$__/   | $$__  $$ \____  $$
| $$\  $$ | $$  \ $$| $$  | $$| $$\  $ | $$| $$      | $$  \ $$ /$$  \ $$
| $$ \  $$| $$  | $$| $$  | $$| $$ \/  | $$| $$$$$$$$| $$  | $$|  $$$$$$/
|__/  \__/|__/  |__/|__/  |__/|__/     |__/|________/|__/  |__/ \______/ 
'''[1:]

text = '''
                                                                                    
`7MMF' `YMM' `7MM"""Mq.        db      `7MMM.     ,MMF'`7MM"""YMM  `7MM"""Mq.   .M"""bgd 
  MM   .M'     MM   `MM.      ;MM:       MMMb    dPMM    MM    `7    MM   `MM. ,MI    "Y 
  MM .d"       MM   ,M9      ,V^MM.      M YM   ,M MM    MM   d      MM   ,M9  `MMb.     
  MMMMM.       MMmmdM9      ,M  `MM      M  Mb  M' MM    MMmmMM      MMmmdM9     `YMMNq. 
  MM  VMA      MM  YM.      AbmmmqMA     M  YM.P'  MM    MM   Y  ,   MM  YM.   .     `MM 
  MM   `MM.    MM   `Mb.   A'     VML    M  `YM'   MM    MM     ,M   MM   `Mb. Mb     dM 
.JMML.   MMb..JMML. .JMM..AMA.   .AMMA..JML. `'  .JMML..JMMmmmmMMM .JMML. .JMM.P"Ybmmd"   

                                a Kramer deobfuscator
'''[1:]

System.Clear()
System.Title("Kramers by ꧁𝕆𝕧𝕖𝕣𝕡𝕠𝕨𝕖𝕣༄꧂#2524")
System.Size(140, 45)
Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)
System.Size(130, 30)
print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))

file_path = Write.Input("Drag your Python file -> ", Colors.red_to_yellow, interval=0.005)
name = os.path.basename(file_path)

os.system(f"pycdas.exe {name} > dis.txt")

with open("dis.txt", "r") as file:
    file_contents = file.read()
    match = re.search(f"24      LOAD_CONST              1: .*", file_contents)
    key = int(match.group().replace(f"24      LOAD_CONST              1: ", ""))
    codeMatch = re.findall("('.*')", file_contents)
    code = str(codeMatch[len(codeMatch) - 2].replace("'", ""))

with open("dis.txt", "r") as file:
    for line in file:
        for word in line.split():
            try:
                num = int(word)
                if num > 1000:
                    key = num
            except ValueError:
                pass

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

def _decode(_bit: str):
	return "".join(binascii.unhexlify(str(_eval)).decode() for _eval in str(_bit).split('/'))
def _bits (_bits: str, key: int):
	return "".join(_bits if _bits not in chars else chars[chars.index(_bits) + 1 if chars.index(_bits) + 1 < len(chars) else 0] for _bits in "".join(chr((ord(t) - key)% 128) if t != "Î¶" else "\n" for t in _decode(_bits)))

deobfuscated = _bits(code, key)

with open("output.py", "w") as deobfuscated_file:
    deobfuscated_file.write(deobfuscated)

Write.Print("Done! \n", Colors.red_to_yellow, interval=0.005)
os.remove("dis.txt")
Write.Input("Press enter for exit...", Colors.red_to_yellow, interval=0.005)
exit()
