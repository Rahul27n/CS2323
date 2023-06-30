#Nelakuditi Rahul Naga - AI20BTECH11029, V Rahul - AI20BTECH11030
.section .data
L1: .word 0 #This location indicates the error of the result. It is 0 if no error else 1.
.word 2,2 #Dimensions of MATRIX-1
.word 1,2,3,4 #Entries of MATRIX-1 in Row-major format
.word 2,2 #Dimensions of MATRIX-2
.word 1,2,3,4 #Entries of MATRIX-2 in Row-major format

.section .text
.global main
main:
la x3, L1 #The address of the data segment is available in x3
lw x1,4(x3) #x dimension of MATRIX-1
lw x2,8(x3) #y dimension of MATRIX-1

mul x4,x1,x2
addi x4,x4,2
slli x4,x4,2
add x4,x3,x4 #Here x4 contains address of last element of MATRIX-1

lw x5,4(x4) #x dimension of MATRIX-2
lw x6,8(x4) #y dimension of MATRIX-2

bne x2,x5,Error

mul x7,x5,x6
addi x7,x7,2
slli x7,x7,2
add x8,x4,x7 #Here x8 contains address of last element of MATRIX-2

sw x1,4(x8) #x dimension of product MATRIX
sw x6,8(x8) #y dimension of product MATRIX

addi x17,x8,12 #Here x17 contains address of first element of product MATRIX

addi x9,x3,12 #Here x9 contains address of first element of MATRIX-1
addi x10,x4,12 #Here x10 contains address of first element of MATRIX-2
add x18,x0,x10 #Temp register for base address of MATRIX-2

add x11,x0,x0
Loop1:
add x12,x0,x0
Loop2:
add x13,x0,x0
add x14,x0,x0
Loop3:
lw x15,0(x9)
lw x16,0(x18)
mul x15,x15,x16
add x14,x14,x15
addi x9,x9,4

add x18,x18,x6
add x18,x18,x6
add x18,x18,x6
add x18,x18,x6
addi x13,x13,1
blt x13,x2,Loop3

sw x14, 0(x17)
addi x17,x17,4

sub x9,x9,x2
sub x9,x9,x2
sub x9,x9,x2
sub x9,x9,x2
addi x10,x10,4
add x18,x0,x10
addi x12,x12,1
blt x12,x6,Loop2

add x9,x9,x2
add x9,x9,x2
add x9,x9,x2
add x9,x9,x2

sub x10,x10,x6
sub x10,x10,x6
sub x10,x10,x6
sub x10,x10,x6

add x18,x0,x10

addi x11,x11,1
blt x11,x1,Loop1

beq x0,x0,End

Error:
addi x31,x0,1
sw x31,0(x3)

End:
addi x0,x0,0

#Checking
lw x20,4(x8) #x8 contains address of last element of MATRIX-2
lw x21,8(x8)
lw x22,12(x8)
lw x23,16(x8)
lw x24,20(x8)
lw x25,24(x8)
lw x26,28(x8)
lw x27,32(x8)
lw x28,36(x8)
lw x29,40(x8)
lw x30,44(x8)

Lwhile1: j Lwhile1