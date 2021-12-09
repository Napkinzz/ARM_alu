import os
import sys

#run commands needed to generate and run test cases
os.system("python3 generate.py")
os.system("rars testCase.s a dump .text Binary testCase.bin")
os.system("rars arm_alu.s pa testCase.bin")
os.system("rars ARMDisassembler.s pa out.bin > testCase.txt")

#open the file testCase.txt, convert it to ARM manually
#put the solution conversion into solution.txt, then compare testCase.txt and solution.txt
f = open("testCase.s", "r")
s = open("solution.txt", "w")

lines =  f.readlines()

#to make translating instructions easy
riscv_registers = ["t0", "t1", "t2", "s0", "s1", "s2", "s3", "s4", "s5", "s6", "a0", "a1", "a2", "sp", "ra"]
arm_registers = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14"]

translate = {
    "AND" : ["andi", "and"],
    "OR" : ["ori", "or"],
    "ADD" : ["addi", "add"],
    "SUB" : ["sub"],
    "LSL" : ["slli", "sll"],
    "LSR" : ["srli", "srl"],
    "ASR" : ["srai", "sra"]
}

for line in lines:
    translated_instr = ""           #translated ARM instruction to be built

    line = line.replace(",", "")    #remove commas
    line = line.strip()             #remove newline char
    line = line.split()             #list of the form [instruction, register, register, register/immediate]
    
    value3 = ""

    if(line[3] not in riscv_registers): #enter loop if dealing with immediates
        if(int(line[3]) >= 0):
            for key in translate:
                if line[0] in translate[key]:
                    translated_instr += key + " "
            value3 = int(line[3])
        else:
            #negative immediate guarantees a sub instruction for this lab
            translated_instr += "SUB "
            value3 = -int(line[3])
    else:
        for key in translate:
                if line[0] in translate[key]:
                    translated_instr += key + " "

        value3 = arm_registers[riscv_registers.index(line[3])]

    #translate registers
    value1 = arm_registers[riscv_registers.index(line[1])]
    value2 = arm_registers[riscv_registers.index(line[2])]
    
    #put translated instruction together and write to file
    translated_instr += value1 + ", " + value2 + ", " + str(value3) + "\n"
    s.write(translated_instr)

#close files
f.close()
s.close()

#compare manually calculated solution with assembly calculated solution
os.system("diff solution.txt testCase.txt")

#remove files if flag was set
if(len(sys.argv) > 1):
    if(sys.argv[1] == "-r"):
        os.system("rm -f solution.txt testCase.txt testCase.s out.bin testCase.bin")