#！/usr/bin/env python
# Functions
def getlargest(num1,num2):
    if num1>num2:
        return(num1)
    else:
        return(num2)  
def trimstr(str1,num1):
    return(" "*getlargest(num1-len(str1),0)+str1)
# Main
import os
os.chdir("D:\\Smst2\\IBI1B\\IBI1_2019-20\\Practical10")
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
seq1=open(input("File name of seq1>"),"r")
seq2=open(input("File name of seq2>"),"r")
seq1_all=""
seq2_all=""
for seq1_ss in seq1.readlines():
    seq1_ss=seq1_ss.strip()
    if not seq1_ss.startswith(">"):
        seq1_all+=seq1_ss
    else:
        seq1_name=seq1_ss[1:]
for seq2_ss in seq2.readlines():
    seq2_ss = seq2_ss.strip()
    if not seq2_ss.startswith(">"):
        seq2_all+=seq2_ss
    else:
        seq2_name=seq2_ss[1:]
# Alignment
percentage=0
score=0
seqdiff=""
for i in range(len(seq1_all)):
    seq1_idx=code_line.index(seq1_all[i])
    seq2_idx=code_line.index(seq2_all[i])
    this_score=int(code_matrix[int(seq1_idx)][int(seq2_idx)])
    score+=this_score
    if (seq1_all[i] == seq2_all[i]):
        seqdiff+=seq1_all[i]
        percentage=percentage+1
    elif this_score>=0:
        seqdiff+="+"
    else:
        seqdiff+=" "
# Print
lt=getlargest(getlargest(len(seq1_name),len(seq1_name)),len("Alignment"))
print(trimstr(seq1_name,lt)+": "+seq1_ss)
print(trimstr("Alignment",lt)+": "+seqdiff)
print(trimstr(seq2_name,lt)+": "+seq2_ss)
print("Score: "+str(score)+" with percentage "+str(round(percentage/len(seq1_all)*100,2))+"%")
