#script to take 'states' list from an ARGEE.st or .txt project file and outputs multi-state display string


prefix = 'MULTI_STATE_DISPLAY_STRING("",state,"1.5","black","transparent",'

suffix = ')'


from tkinter import filedialog  
import os

path = filedialog.askopenfilename()
foundline = False
i=0
outputstring = ''
if path.endswith('.txt') or path.endswith('.st'):
    file = open(path,'r')
    contents = file.readlines()
    for line in contents:
        line = line.lower()
        if 'end_enum' in line:
            foundline = False
            
            file.close()
            break
        
        if 'enum' in line:
            foundline = True
            continue
        elif foundline and not 'end_enum' in line:
            outputstring =  (outputstring + str(i) +',"'+line[1:].replace('_',' ').upper()+'","black","transparent",').replace('\n','')
            
        
            
    print(prefix+outputstring[:-1]+suffix)
    file.close()
        
