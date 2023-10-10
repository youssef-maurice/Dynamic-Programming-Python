import numpy as np

def same_letter(matrix, row, col):
    if (matrix[row][0] == matrix[0][col]):
        return True
    return False

def get_max(arr):
    if max(arr)==arr[0]:
        return ["d", arr[0]]
    if max(arr)==arr[1]:
        return ["u", arr[1]]
    if max(arr)==arr[2]:
        return ["l", arr[2]]
    
def rev(s):
    new_s=""
    for char in s:
        new_s= char + new_s
    return new_s

def score(match, mismatch, cs, cn):

    seq=""
    human= "TCATAAATAATTTTGCTTGCTGAAGGAAGAAAAAGTGTTTTTCATAAACCCATTATCCAGGACTGTTTATAGCTGTTGGAAGGACTAGGTCTTCCCTAGCCCCCCCAGTGTGCAAGGGCAGTGAAGACTTGATTGTACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTC"
    mouse= "TACTTCATAAATAATTTTGCTTGCTGAAGGAAGAGAACATATTTTTCATGAACTCATAATCTTGGACTGTTTATAGATATTGGGGGGAGTAGGTCTTCTCTGGCCCCCCCCAGTATGCAAGGGCAATGGAGACCTGATTATATAAAGTATGTTTATAAATGCTGTGCTGTTAATACTGCAAATAAACTAAATAGCAAACA" #CCCTCTT
    human_len= len(human) #length of human seq
    mouse_len= len(mouse) #length of mouse seq
    
    #BUILD MATRIX
    rows=[]
    matrix=[]
    for i in range(len(mouse)+2):
        rows.append(0)
    for i in range(len(human)+2):
        matrix.append(rows.copy())
    for i in range(2, len(mouse)+2):
        matrix[0][i]= mouse[i-2]
    for i in range(2, len(human)+2):
        matrix[i][0]= human[i-2]
    for i in range(2, len(mouse)+2):
        if(matrix[0][i]==matrix[0][i-1]):
            matrix[1][i]= matrix[1][i-1]+cs
        else:
            matrix[1][i]= matrix[1][i-1]+cn
    for i in range(2, len(human)+2):
        if(matrix[i][0]==matrix[i-1][0]):
            matrix[i][1]= matrix[i-1][1]+cs
        else:
            matrix[i][1]= matrix[i-1][1]+cn
            
    matrix2=[]
    rows=[]
    for i in range(len(mouse)+2):
        rows.append(0)
    for i in range(len(human)+2):
        matrix2.append(rows.copy())
    for i in range(2, len(mouse)+2):
        matrix2[0][i]= mouse[i-2]
    for i in range(2, len(human)+2):
        matrix2[i][0]= human[i-2]
    for i in range(2, len(mouse)+2):
        if(matrix2[0][i]==matrix2[0][i-1]):
            matrix2[1][i]= "l"
        else:
            matrix2[1][i]= "l"
    for i in range(2, len(human)+2):
        if(matrix2[i][0]==matrix2[i-1][0]):
            matrix2[i][1]= "u"
        else:
            matrix2[i][1]= "u"
    
    order=[]
    for row in range(2, len(human)+2):
        for col in range(2, len(mouse)+2):
            if same_letter(matrix, row, col):
                if(matrix[row][0]==matrix[row-1][0]):
                    if(matrix[0][col]==matrix[0][col-1]):
                        max1= get_max([matrix[row-1][col-1]+match, matrix[row-1][col]+cs, matrix[row][col-1]+cs])
                        matrix[row][col]= max1[1]
                        matrix2[row][col]= max1[0]
                        order.append(max1[0])
                    else:
                        max2= get_max([matrix[row-1][col-1]+match, matrix[row-1][col]+cs, matrix[row][col-1]+cn])
                        matrix[row][col]= max2[1]
                        matrix2[row][col]= max2[0]
                        order.append(max2[0])
                else:
                    if(matrix[0][col]==matrix[0][col-1]):
                        max3= get_max([matrix[row-1][col-1]+match, matrix[row-1][col]+cn, matrix[row][col-1]+cs])
                        matrix[row][col]= max3[1]
                        matrix2[row][col]= max3[0]
                        order.append(max3[0])
                    else:
                        max4= get_max([matrix[row-1][col-1]+match, matrix[row-1][col]+cn, matrix[row][col-1]+cn])
                        matrix[row][col]= max4[1]
                        matrix2[row][col]= max4[0]
                        order.append(max4[0])
            else:
                if(matrix[row][0]==matrix[row-1][0]):
                    if(matrix[0][col]==matrix[0][col-1]):
                        max5= get_max([matrix[row-1][col-1]+mismatch, matrix[row-1][col]+cs, matrix[row][col-1]+cs])
                        matrix[row][col]= max5[1]
                        matrix2[row][col]= max5[0]
                        order.append(max5[0])
                    else:
                        max6= get_max([matrix[row-1][col-1]+mismatch, matrix[row-1][col]+cs, matrix[row][col-1]+cn])
                        matrix[row][col]= max6[1]
                        matrix2[row][col]= max6[0]
                        order.append(max6[0])
                else:
                    if(matrix[0][col]==matrix[0][col-1]):
                        max7= get_max([matrix[row-1][col-1]+mismatch, matrix[row-1][col]+cn, matrix[row][col-1]+cs])
                        matrix[row][col]= max7[1]
                        matrix2[row][col]= max7[0]
                        order.append(max7[0])
                    else:
                        max8= get_max([matrix[row-1][col-1]+mismatch, matrix[row-1][col]+cn, matrix[row][col-1]+cn])
                        matrix[row][col]= max8[1]
                        matrix2[row][col]= max8[0]
                        order.append(max8[0])
    #TRACEBACK
    row= len(human)+1
    col= len(mouse)+1
    curr= matrix2[row][col]
    order=""
    human_seq=""
    mouse_seq=""
    while(True):
        if type(curr)== type(0): #integer
            break
        order+=curr
        if curr=="d":
            human_seq+= matrix[row][0]
            mouse_seq+= matrix[0][col]
            row-=1
            col-=1
            curr= matrix2[row][col]
            continue
        if curr=="u":
            human_seq+= matrix[row][0]
            mouse_seq+= "_"
            row-=1
            curr= matrix2[row][col]
            continue
        if curr=="l":
            human_seq+= "_"
            mouse_seq+= matrix[0][col]
            col-=1
            curr= matrix2[row][col]
            continue
    
    human_seq= rev(human_seq)
    mouse_seq= rev(mouse_seq)
                        
                        
    
    
    
    
    #PRINT MATRIX    
    '''for row in matrix:
        # Join elements in the row as strings and separate them with tabs or spaces
        row_str = "\t".join(map(str, row))  # Use "\t" for tab separation or " " for space separation
        print(row_str)
    #END OF PRINTING
    print("\n MATRIX2 2 \n ")
    for row in matrix2:
        # Join elements in the row as strings and separate them with tabs or spaces
        row_str = "\t".join(map(str, row))  # Use "\t" for tab separation or " " for space separation
        print(row_str)'''
        
        
    print("\n")
    score= matrix[len(human)+1][len(mouse)+1]
    print("The score is: ", score)
    print("\n")
    print("The human seq is: \n")
    print(human_seq)
    print("\n")
    print("The mouse seq is: \n")
    print(mouse_seq)

score(1,-1,-1,-2)

    