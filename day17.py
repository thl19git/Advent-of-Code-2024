from utils import get_input

def combo(operand, A, B, C):
    if operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    
def execute(program, regA, regB, regC):
    ip = 0
    output = []

    while(ip < len(program)):
        instr = program[ip]
        operand = program[ip+1]
        if instr in [0, 2, 5, 6, 7]:
            operand = combo(operand, regA, regB, regC)
        if instr == 0:
            regA = regA // (2**operand)
        elif instr == 1:
            regB ^= operand
        elif instr == 2:
            regB = operand % 8
        elif instr == 3:
            if regA != 0:
                ip = operand
                continue
        elif instr == 4:
            regB ^= regC
        elif instr == 5:
            output.append(operand % 8)
        elif instr == 6:
            regB = regA // (2**operand)
        elif instr == 7:
            regC = regA // (2**operand)

        ip += 2

    return output

def find_regA(program, regB, regC):
    regA = 2 ** ((len(program)-1) * 3)
    while True:
        output = execute(program, regA, regB, regC)
        found = True
        for i in range(len(output)-1, -1, -1):
            if output[i] != program[i]:
                offset = 2 ** (3 * i)
                regA += offset - (regA % offset)
                found = False
                break
        if found:
            return regA
        
input = get_input(17)

regA = int(input[0].split()[-1])
regB = int(input[1].split()[-1])
regC = int(input[2].split()[-1])

program = [int(x) for x in input[-1].split()[1].split(",")]

part1 = ",".join([str(x) for x in execute(program, regA, regB, regC)])

print("Part 1:", part1)
print("Part 2:", find_regA(program, regB, regC))