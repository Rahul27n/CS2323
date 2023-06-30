def binary_to_decimal(string,Immediate=False):
  ans = 0
  if Immediate and string[0] == '1':
    for i in range(len(string)):
      ans += (2**(i))*abs(int(string[len(string)-i-1])-1)
    ans = -(ans+1)
  else:
    for i in range(len(string)):
      ans += (2**(i))*int(string[len(string)-i-1])
  return ans

def binary_to_hexadecimal(string):
  lis = []
  for i in range(len(string)):
    if i % 4 == 0:
      substring = string[i:i+4]
      if substring == '0000':
        lis.append('0')
      elif substring == '0001':
        lis.append('1')
      elif substring == '0010':
        lis.append('2')
      elif substring == '0011':
        lis.append('3')
      elif substring == '0100':
        lis.append('4')
      elif substring == '0101':
        lis.append('5')
      elif substring == '0110':
        lis.append('6')
      elif substring == '0111':
        lis.append('7')
      elif substring == '1000':
        lis.append('8')
      elif substring == '1001':
        lis.append('9')
      elif substring == '1010':
        lis.append('a')
      elif substring == '1011':
        lis.append('b')
      elif substring == '1100':
        lis.append('c')
      elif substring == '1101':
        lis.append('d')
      elif substring == '1110':
        lis.append('e')
      elif substring == '1111':
        lis.append('f')
  ans = ''
  for char in lis:
    ans += char
  return ans

def hexadecimal_to_binary(string):
  lis = []
  for i in range(len(string)):
    if string[i] == '0':
      lis.append('0000')
    elif string[i] == '1':
      lis.append('0001')
    elif string[i] == '2':
      lis.append('0010')
    elif string[i] == '3':
      lis.append('0011')
    elif string[i] == '4':
      lis.append('0100')
    elif string[i] == '5':
      lis.append('0101')
    elif string[i] == '6':
      lis.append('0110')
    elif string[i] == '7':
      lis.append('0111')
    elif string[i] == '8':
      lis.append('1000')
    elif string[i] == '9':
      lis.append('1001')
    elif string[i] == 'a' or string[i] == 'A':
      lis.append('1010')
    elif string[i] == 'b' or string[i] == 'B':
      lis.append('1011')
    elif string[i] == 'c' or string[i] == 'C':
      lis.append('1100')
    elif string[i] == 'd' or string[i] == 'D':
      lis.append('1101')
    elif string[i] == 'e' or string[i] == 'E':
      lis.append('1110')
    elif string[i] == 'f' or string[i] == 'F':
      lis.append('1111')
  ans = ''
  ans = ans.join(lis)
  return ans

def instruction_array_decoder(string_array):
  for i in range(len(string_array)):
    string = string_array[i]
    binary_string = hexadecimal_to_binary(string)
    opcode = binary_string[25:32]
    operation = ''
    if opcode == '0110011': #R-format
      funct7 = binary_string[:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      rd = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      dest_register = binary_to_decimal(rd)
      if funct7 == '0000000' and funct3 == '000':
        operation = 'add' 
      elif funct7 == '0100000' and funct3 == '000':
        operation = 'sub' 
      elif funct7 == '0000000' and funct3 == '100':
        operation = 'xor' 
      elif funct7 == '0000000' and funct3 == '110':
        operation = 'or' 
      elif funct7 == '0000000' and funct3 == '111':
        operation = 'and'
      elif funct7 == '0000000' and funct3 == '001':
        operation = 'sll'
      elif funct7 == '0000000' and funct3 == '101':
        operation = 'srl'
      elif funct7 == '0100000' and funct3 == '101':
        operation = 'sra'   
      print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',','x' + str(register_2),sep='')  
    elif opcode == '0010011' or opcode == '0000011' or opcode == '1100111': #I-format
      imm = binary_string[:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      rd = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      immediate_value = binary_to_decimal(imm,True)
      dest_register = binary_to_decimal(rd)
      if opcode == '0010011':
       if funct3 == '000':
         operation = 'addi'          
       elif funct3 == '100':
         operation = 'xori'
       elif funct3 == '110':
         operation = 'ori'
       elif funct3 == '111':
         operation = 'andi'
       elif funct3 == '001' and binary_to_decimal(imm[:6]) == 0:
         operation = 'slli'
         immediate_value = binary_to_decimal(imm[6:12])
       elif funct3 == '101' and binary_to_decimal(imm[:6]) == 0:
         operation = 'srli'
         immediate_value = binary_to_decimal(imm[6:12])
       elif funct3 == '101' and binary_to_decimal(imm[:6]) != 0:
         operation = 'srai'
         immediate_value = binary_to_decimal(imm[6:12])
       print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')
      elif opcode == '0000011':
       if funct3 == '000':
         operation = 'lb'
       elif funct3 == '001':
         operation = 'lh'
       elif funct3 == '010':
         operation = 'lw'
       elif funct3 == '011':
         operation = 'ld'
       elif funct3 == '100':
         operation = 'lbu'
       elif funct3 == '101':
         operation = 'lhu'
       elif funct3 == '110':
         operation = 'lwu'
       print(operation + ' ','x' + str(dest_register) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')
      elif opcode == '1100111':
        operation = 'jalr'
        print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')
    elif opcode == '0100011': #S-format
      imm_1 = binary_string[:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      imm_2 = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      imm = imm_1 + imm_2
      immediate_value = binary_to_decimal(imm,True)
      if funct3 == '000':
        operation = 'sb'
      elif funct3 == '001':
        operation = 'sh'
      elif funct3 == '010':
        operation = 'sw'
      elif funct3 == '011':
        operation = 'sd'
      print(operation + ' ','x' + str(register_2) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')
    elif opcode == '0110111': #U-format
      imm = binary_string[:20]
      rd = binary_string[20:25]
      dest_register = binary_to_decimal(rd)
      operation = 'lui'
      immediate_value = binary_to_hexadecimal(imm)
      print(operation + ' ','x' + str(dest_register) + ',','0x' + immediate_value,sep='')
    elif opcode == '1100011': #B-format
      imm_first = binary_string[0]
      imm_third = binary_string[1:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      imm_last = binary_string[20:24]
      imm_second = binary_string[24]
      imm = imm_first + imm_second + imm_third + imm_last + '0'
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      immediate_value = binary_to_decimal(imm,True)
      if funct3 == '000':
        operation = 'beq'
      elif funct3 == '001':
        operation = 'bne'
      elif funct3 == '100':
        operation = 'blt'
      elif funct3 == '101':
        operation = 'bge'
      elif funct3 == '110':
        operation = 'bltu'
      elif funct3 == '111':
        operation = 'bgeu'
      print(operation + ' ','x' + str(register_1) + ',','x' + str(register_2) + ',',immediate_value,sep='')
    elif opcode == '1101111': #J-format
      imm_temp = binary_string[:20]
      rd = binary_string[20:25]
      imm_first = imm_temp[0]
      imm_last = imm_temp[1:11]
      imm_third = imm_temp[11]
      imm_second = imm_temp[12:20]
      imm = imm_first + imm_second + imm_third + imm_last + '0'
      operation = 'jal'
      dest_register = binary_to_decimal(rd)
      immediate_value = binary_to_decimal(imm,True)
      print(operation + ' ','x' + str(dest_register) + ',',immediate_value,sep='')
    else:
      print('The given RISC-V machine code does not match with any instruction format')
      break
  return None

def instruction_array_decoder_with_text_support(string_array):
  label_index = []
  labels = []
  for i in range(len(string_array)):
    string = string_array[i]
    binary_string = hexadecimal_to_binary(string)
    opcode = binary_string[25:32]
    operation = ''
    if opcode == '0110011': #R-format
      funct7 = binary_string[:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      rd = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      dest_register = binary_to_decimal(rd)
      if funct7 == '0000000' and funct3 == '000':
        operation = 'add' 
      elif funct7 == '0100000' and funct3 == '000':
        operation = 'sub' 
      elif funct7 == '0000000' and funct3 == '100':
        operation = 'xor' 
      elif funct7 == '0000000' and funct3 == '110':
        operation = 'or' 
      elif funct7 == '0000000' and funct3 == '111':
        operation = 'and'
      elif funct7 == '0000000' and funct3 == '001':
        operation = 'sll'
      elif funct7 == '0000000' and funct3 == '101':
        operation = 'srl'
      elif funct7 == '0100000' and funct3 == '101':
        operation = 'sra'
      if i not in label_index:
        print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',','x' + str(register_2),sep='')
      else:
        print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',','x' + str(register_2),sep='')      
    elif opcode == '0010011' or opcode == '0000011' or opcode == '1100111': #I-format
      imm = binary_string[:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      rd = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      immediate_value = binary_to_decimal(imm,True)
      dest_register = binary_to_decimal(rd)
      if opcode == '0010011':
       if funct3 == '000':
         operation = 'addi'          
       elif funct3 == '100':
         operation = 'xori'
       elif funct3 == '110':
         operation = 'ori'
       elif funct3 == '111':
         operation = 'andi'
       elif funct3 == '001' and binary_to_decimal(imm[:6]) == 0:
         operation = 'slli'
         immediate_value = binary_to_decimal(imm[6:12])
       elif funct3 == '101' and binary_to_decimal(imm[:6]) == 0:
         operation = 'srli'
         immediate_value = binary_to_decimal(imm[6:12])
       elif funct3 == '101' and binary_to_decimal(imm[:6]) != 0:
         operation = 'srai'
         immediate_value = binary_to_decimal(imm[6:12])
       if i not in label_index:
         print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')
       else:
         print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')
      elif opcode == '0000011':
       if funct3 == '000':
         operation = 'lb'
       elif funct3 == '001':
         operation = 'lh'
       elif funct3 == '010':
         operation = 'lw'
       elif funct3 == '011':
         operation = 'ld'
       elif funct3 == '100':
         operation = 'lbu'
       elif funct3 == '101':
         operation = 'lhu'
       elif funct3 == '110':
         operation = 'lwu'
       if i not in label_index:
         print(operation + ' ','x' + str(dest_register) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')
       else:
         print('L'+ str(label_index.index(i)) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')    
      elif opcode == '1100111':
        index = int(i + (immediate_value/4))
        if index not in label_index:
          label_index.append(index)
          labels.append('L'+ str(len(label_index)))
        operation = 'jalr'
        if i not in label_index:
          print(operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')
        else:
          print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',','x' + str(register_1) + ',',immediate_value,sep='')        
    elif opcode == '0100011': #S-format
      imm_1 = binary_string[:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      imm_2 = binary_string[20:25]
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      imm = imm_1 + imm_2
      immediate_value = binary_to_decimal(imm,True)
      if funct3 == '000':
        operation = 'sb'
      elif funct3 == '001':
        operation = 'sh'
      elif funct3 == '010':
        operation = 'sw'
      elif funct3 == '011':
        operation = 'sd'
      if i not in label_index:
        print(operation + ' ','x' + str(register_2) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')
      else:
        print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(register_2) + ',',immediate_value,'(' + 'x' + str(register_1)+')',sep='')      
    elif opcode == '0110111': #U-format
      imm = binary_string[:20]
      rd = binary_string[20:25]
      dest_register = binary_to_decimal(rd)
      operation = 'lui'
      immediate_value = binary_to_hexadecimal(imm)
      if i not in label_index:
        print(operation + ' ','x' + str(dest_register) + ',','0x' + immediate_value,sep='')
      else:
        print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',','0x' + immediate_value,sep='')    
    elif opcode == '1100011': #B-format
      imm_first = binary_string[0]
      imm_third = binary_string[1:7]
      rs2 = binary_string[7:12]
      rs1 = binary_string[12:17]
      funct3 = binary_string[17:20]
      imm_last = binary_string[20:24]
      imm_second = binary_string[24]
      imm = imm_first + imm_second + imm_third + imm_last + '0'
      register_1 = binary_to_decimal(rs1)
      register_2 = binary_to_decimal(rs2)
      immediate_value = binary_to_decimal(imm,True)
      index = int(i + (immediate_value/4))
      if index not in label_index:
        label_index.append(index)
        labels.append('L'+ str(len(label_index)))
      if funct3 == '000':
        operation = 'beq'
      elif funct3 == '001':
        operation = 'bne'
      elif funct3 == '100':
        operation = 'blt'
      elif funct3 == '101':
        operation = 'bge'
      elif funct3 == '110':
        operation = 'bltu'
      elif funct3 == '111':
        operation = 'bgeu'
      if i not in label_index:
        print(operation + ' ','x' + str(register_1) + ',','x' + str(register_2) + ',',labels[label_index.index(index)],sep='')
      else:
        print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(register_1) + ',','x' + str(register_2) + ',',labels[label_index.index(index)],sep='')
    elif opcode == '1101111': #J-format
      imm_temp = binary_string[:20]
      rd = binary_string[20:25]
      imm_first = imm_temp[0]
      imm_last = imm_temp[1:11]
      imm_third = imm_temp[11]
      imm_second = imm_temp[12:20]
      imm = imm_first + imm_second + imm_third + imm_last + '0'
      operation = 'jal'
      dest_register = binary_to_decimal(rd)
      immediate_value = binary_to_decimal(imm,True)
      index = int(i + (immediate_value/4))
      if index not in label_index:
        label_index.append(index)
        labels.append('L'+ str(len(label_index)))
      if i not in label_index:
        print(operation + ' ','x' + str(dest_register) + ',',labels[label_index.index(index)],sep='')
      else:
        print('L'+ str(label_index.index(i) + 1) + ':' + ' ',operation + ' ','x' + str(dest_register) + ',',labels[label_index.index(index)],sep='')
    else:
      print('The given RISC-V machine code does not match with any instruction format')
      break
  return None

input = []

#Reading the input text file and copying the contents into a list
with open('data.txt') as f:
  input = [line.rstrip() for line in f]

#instruction_array_decoder(input)
instruction_array_decoder_with_text_support(input)