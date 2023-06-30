.data

.dword 6 #n

.text

lui x1, 0x10000 #Address of n
addi x2,x1,256 #Base address of squares sequence
ld x3,0(x1) #Loading n in x3

addi x4,x0,1 #x4 = 1

sd x4,0(x2) #Storing 1 as first number in squares sequence 

add x6,x4,x0 #Intializing first number in squares sequence as 1

addi x7,x0,0 #Initialize x7 as 0 arbitrarily
addi x10,x0,2 #x10 = 2, this stores value of n shown in recursive equation

addi x25,x0,1 #Initialize squares sum to 1

Loop:
    beq x3,x4, Exit #if x3 is 1, exit
    add x7,x10,x10 #x7 = 2*x10
    addi x7,x7,-1 #x7 = 2*x10 - 1 i.e; x7 = 2n-1
    addi x10,x10,1 #Increment x10
    add x8,x6,x7 #Implement the recursive formula
    sd x8,8(x2) #Store the new element obtained in memory
    add x25,x25,x8 #Increment the sum of the sequence 
    add x6,x8,x0 # x6 == x8
    addi x2,x2,8 #Increment base memory location
    addi x3, x3, -1 #x3--
    beq x0, x0, Loop #loop
Exit:
    addi x0, x1, 0

sd x25,16(x1) #Store squares sum at required location