from pathlib import Path

import re
import os
import xlwt
import xlrd

with open('jointStates.txt','r') as f:
    data=f.readlines()
#判断有无文件存在，并进行清空操作
if not Path('position.txt').is_file() \
   or not Path('velocity.txt').is_file() \
   or not Path('effort.txt').is_file() :
    os.mknod('position.txt')
    os.mknod('velocity.txt')
    os.mknod('effort.txt')

fr=open('position.txt',"w")
fr.close()
fr=open('velocity.txt',"w")
fr.close()
fr=open('effort.txt',"w")
fr.close()
for i in range(0,len(data)//12 -1):
    position=data[i*12+8]
    p1="position\:\s\[.*\]"
    pattern1=re.compile(p1)
    postext=pattern1.findall(position)
    after_text=re.sub(r"\['position\:\s\[",'',str(postext))
    pos_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('position.txt',"a")
    fr.write(pos_val+'\n')
    fr.close()
    print(pos_val)

    velocity=data[i*12+9]
    p2="velocity\:\s\[.*\]"
    pattern2=re.compile(p2)
    veltext=pattern2.findall(velocity)
    after_text=re.sub(r"\['velocity\:\s\[",'',str(veltext))
    vel_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('velocity.txt',"a")
    fr.write(vel_val+'\n')
    fr.close()
    print(vel_val)

    effort=data[i*12+10]
    p3="effort\:\s\[.*\]"
    pattern3=re.compile(p3)
    eftext=pattern3.findall(effort)
    after_text=re.sub(r"\['effort\:\s\[",'',str(eftext))
    eft_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('effort.txt',"a")
    fr.write(eft_val+'\n')
    fr.close()
    print(eft_val)

my_Workbook=xlwt.Workbook(encoding='utf-8')
position=my_Workbook.add_sheet('position information')

pos_val.count
