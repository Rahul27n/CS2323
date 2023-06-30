.data
#The following line defines the 10 values present in the memory.
# We would use different values in our evaluation and
# hence you should try various combinations of these values in your testing.
.dword 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009
#(dword stands for doubleword)
.text
#The following line initializes register x3 with 0x10000000
#so that you can use x3 for referencing various memory locations.
lui x3, 0x10000
#your code starts here
# WRITE YOUR CODE HERE
ld x1,0(x3)
ld x2,8(x3)
ld x4,16(x3)
ld x5,24(x3)
ld x6,32(x3)
ld x7,40(x3)
ld x8,48(x3)
ld x9,56(x3)
ld x11,64(x3)
ld x12,72(x3)

add x10,x1,x2
add x10,x10,x4
add x10,x10,x5
add x10,x10,x6
add x10,x10,x7
add x10,x10,x8
add x10,x10,x9
add x10,x10,x11
add x10,x10,x12
#The final result (sum) should be in register x10