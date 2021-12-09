import random

immediates = [1024, 36, 628, 1968, 496, 0, 1, 8, 832, 255, 1792, 2032]
small_immediates = [0, 1, 7, 8, 15, 31]
neg_immediates = [-x for x in immediates]

reg_instructions = ["and", "or", "add", "sub", "sra", "srl", "sll"]
imm_non_neg_instructions = ["srai", "srli", "slli", "ori", "andi"]
imm_neg_instructions = ["addi"]

registers = ["t0", "t1", "t2", "s0", "s1", "s2", "s3", "s4", "s5", "s6", "a0", "a1", "a2", "sp", "ra"]

MAX = 512       #max # of instructions

f = open("testCase.s", "w") #create a file to write to

for i in range(MAX):
    #generate a number between 1 and 4 to decide which instruction to randomly generate
    #since imm_instructions has more than twice as many instructions as the other lists,
    #denote 1-2 to be for that list, and 3 and 4 to the other lists respectively
    num = random.randint(1, 5)
    if num == 5 or num == 4:
        #generate test using imm_non_neg_instructions
        instr = random.choice(imm_non_neg_instructions) + " " + random.choice(registers) + " " + random.choice(registers) + " " + str(random.choice(small_immediates))

        #don't add a newline character if its the last instruction
        if(i == MAX-1):
            f.write(instr)
        else:
            f.write(instr+'\n')
    elif num == 3:
        #generate test using imm_neg_instructions
        #these instructions can have a negative or positive instruction, so first randomly pick one
        neg = random.randint(0, 1)
        instr = ""

        if neg == 0:
            #use non-negative immediates
            instr = random.choice(imm_neg_instructions) + " " + random.choice(registers) + " " + random.choice(registers) + " " + str(random.choice(immediates))
        if neg == 1:
            #use negative immediates
            instr = random.choice(imm_neg_instructions) + " " + random.choice(registers) + " " + random.choice(registers) + " " + str(random.choice(neg_immediates))

        #don't add a newline character if its the last instruction
        if(i == MAX-1):
            f.write(instr)
        else:
            f.write(instr+'\n')

    else:
        #generate tests using reg_instructions
        instr = random.choice(reg_instructions) + " " + random.choice(registers) + " " + random.choice(registers) + " " + random.choice(registers)

        #don't add a newline character if its the last instruction
        if(i == MAX-1):
            f.write(instr)
        else:
            f.write(instr+'\n')

f.close()