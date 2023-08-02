#script to take 'states' list from an ARGEE.st or .txt project file and outputs multi-state display string


from tkinter import filedialog  
import os

#prompt user for file
path = filedialog.askopenfilename(title = ("SELECT ARGEE .st or .txt"),
                                  filetypes=(("ARGEE Project", "*.st"),("ARGEE Text Output", "*.txt"),("all files", "*.*")))
foundline = False
i=0
outputstring = ''
prefix = 'MULTI_STATE_DISPLAY_STRING("",state,"1.5","black","transparent",'
suffix = ')'

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
            i+=1
else:
    print('invalid file type')

#add prefix and suffix to output display string, slice final ',' character and print     
print(prefix+outputstring[:-1]+suffix)
file.close()
        
