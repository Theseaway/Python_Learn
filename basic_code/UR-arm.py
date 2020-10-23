import re
import os
import xlwt
import xlrd
from pathlib import Path

with open('jointStates.txt','r') as f:
    data=f.readlines()

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
maxnum=len(data)//12

for i in range(0,maxnum -1):
    position=data[i*12+8]
    p1="position\:\s\[.*\]"
    pattern1=re.compile(p1)
    postext=pattern1.findall(position)
    after_text=re.sub(r"\['position\:\s\[",'',str(postext))
    pos_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('position.txt',"a")
    fr.write(pos_val+'\n')
    fr.close()

    velocity=data[i*12+9]
    p2="velocity\:\s\[.*\]"
    pattern2=re.compile(p2)
    veltext=pattern2.findall(velocity)
    after_text=re.sub(r"\['velocity\:\s\[",'',str(veltext))
    vel_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('velocity.txt',"a")
    fr.write(vel_val+'\n')
    fr.close()

    effort=data[i*12+10]
    p3="effort\:\s\[.*\]"
    pattern3=re.compile(p3)
    eftext=pattern3.findall(effort)
    after_text=re.sub(r"\['effort\:\s\[",'',str(eftext))
    eft_val=re.sub(r"\]'\]",'',str(after_text))
    fr=open('effort.txt',"a")
    fr.write(eft_val+'\n')
    fr.close()

my_Workbook=xlwt.Workbook(encoding='utf-8')
sheet_position=my_Workbook.add_sheet('position_information')

with open('position.txt') as File1:
    position_info=File1.readlines()
array=position_info[0].split(',')
column=len(array)
for i in range(0,maxnum-1):
    temp=position_info[i].split(',')
    for j in range(0,column):
        posnum=float(temp[j])
        sheet_position.write(i,j,posnum)
my_Workbook.save('position.xls')