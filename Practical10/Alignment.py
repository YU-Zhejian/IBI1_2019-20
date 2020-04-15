#！/usr/bin/env python
# Functions
def getlargest(num1,num2):
    if num1>num2:
        return(num1)
    else:
        return(num2)  
def trimstr(str1,num1):
    while len(str1)<num1:
        str1=" "+str1
    return(str1)
# Main
import os
os.chdir(r"C:\Users\Admin\Documents\Smst2\IBI\IBI1_2019-20\Practical10")
# BLOSUM file retrived from https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
blos=open("BLOSUM62.txt","r")
blos_all=blos.readlines()
# Read BLOSUM
code_matrix=[]
code_line=[]
for line in blos_all:
    if line.startswith("#"):
        continue
    elif line.startswith(" "):
        code_line=line.strip().replace("  "," ").split(" ")
    else:
        code_matrix.append(line.strip().replace("  "," ").split(" ")[1:])
# Read Seq
seq1=open(input("The name of seq1>"),"r")
seq2=open(input("The name of seq2>"),"r")
seq1_all=""
seq2_all=""
for seq1_ss in seq1.readlines():
    if not seq1_ss.strip().startswith(">"):
        seq1_all+=seq1_ss.strip()
    else:
        seq1_name=seq1_ss[1:].strip()
for seq2_ss in seq2.readlines():
    if not seq2_ss.strip().startswith(">"):
        seq2_all+=seq2_ss.strip()
    else:
        seq2_name=seq2_ss[1:].strip()
# Alignment
edit_distance=0
score=0
seqdiff=""
for i in range(len(seq1_all)):
    seq1_idx=code_line.index(seq1_all[i])
    seq2_idx=code_line.index(seq2_all[i])
    this_score=int(code_matrix[int(seq1_idx)][int(seq2_idx)])
    score+=this_score
    if (seq1_all[i] == seq2_all[i]):
        seqdiff+=seq1_all[i]
    elif this_score>=0:
        seqdiff+="+"
    else:
        seqdiff+=" "
# Trim name
seqdiff_name="Alignment"
lt=getlargest(getlargest(len(seq1_name),len(seq1_name)),len(seqdiff_name))
seqdiff_name=trimstr(seqdiff_name,lt)
seq1_name=trimstr(seq1_name,lt)
seq2_name=trimstr(seq2_name,lt)
# Print
print(seq1_name+"/"+seq1_ss.strip())
print(seqdiff_name+"/"+seqdiff)
print(seq2_name+"/"+seq2_ss.strip())
print("Score: "+str(score))
