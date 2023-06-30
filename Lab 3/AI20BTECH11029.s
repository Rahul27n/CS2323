.data
.dword 6

.text
bne t2,zero,Exit #Condition for terminating the program
lui t3,0x10000
ld a0,0(t3)

Factorial:
    addi sp,sp,-16
    sd ra,8(sp)
    sd a0,0(sp)
    addi t0,a0,-1
    bge t0,zero,Recurse
    addi a0,zero,1
    addi sp,sp,16
    jalr zero,ra,0
Recurse:
    addi a0,a0,-1
    jal ra,Factorial
    addi t1,a0,0
    ld a0,0(sp)
    ld ra,8(sp)
    addi sp,sp,16
    mul a0,a0,t1
    addi t2,t2,1
    jalr zero,ra,0
Exit:
    sd a0,16(t3)