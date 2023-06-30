#Nelakuditi Rahul Naga - AI20BTECH11029, V Rahul - AI20BTECH11030
.section .data
L1: .word 500000
.section .text
.global main
main:
la x3, L1
#YOUR CODE FOLLOWS HERE. The ADDRESS of the data segment is available in x3
lw x4,0(x3)

addi x1,x0,32
lui x5,0x10012
addi x5,x5,4
addi x6,x5,4
addi x7,x6,4

sw x0,0(x5)
sw x1,0(x6)

Loop:
    sw x1,0(x7) #ON
    jal x1,Delay
    lw x10,0(x7) #Check
    sw x0,0(x7) #OFF
    jal x1,Delay
    lw x10,0(x7) #Check
    beq x0,x0,Loop

Delay:
    Run:
    beq x28,x4,Exit
    addi x28,x28,1
    beq x0,x0,Run
    Exit:
    addi x28,x0,0
    jalr x0,x1,0
#At the end, have a while(1) loop, as shown below
Lwhile1: j Lwhile1

