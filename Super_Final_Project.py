## Main 2
def input_matrix(matrix_size):
    if matrix_size == 1 or matrix_size < 1:
        input_matrix_values = [[[1,1,1]]]
    else:
        print("Enter Values in the matrix with number1[space]number2[space]number3 \n Example: 1 1 1 [enter]" )
        print("Enter the values of Matrix : \n")
        input_matrix_values = []

        for i in range(0,matrix_size):
            a = []   #temporaray list 
            for i in range(0,matrix_size):
                a.append([float(x) for x in input().split()])
            input_matrix_values.insert(i,a)
            del a
        print("\n Main Inputted Matrix is :\n",input_matrix_values)

    
#     Main 3
# Sum of Rows Column Wise
    b = []
    for j in range (0,matrix_size):
        b.append([0,0,0])
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            for k in range(0,3):
                b[i][k] = b[i][k] + input_matrix_values[i][j][k]

    length = len(b)//matrix_size
    sum1 = 0
    for i in range(0,matrix_size):
        print("SA",i+1,"is",b[sum1:length])
        sum1 = length
        length = length + 1
        
# Main 4
# Sum of All above matrix --> SA1 + SA2 + SA3
    c = [0,0,0]
    for i in range(0,matrix_size):
        for j in range(0,3):
            c[j] = c[j] + b[i][j]
            c[j] = round(c[j],4) 
    print("\n Sum of SA1 + SA2 + SA3 is:S.all. -->",c)
    
#     Main 5
# Reciprocal 1/S.all.
    for i in range(0,3):
        c[i] = 1/c[i]
        c[i] = round(c[i],4)  # round upto 4 decimal places
    print("\n Reciprocal [1/S.all.] is :\t ",c)
    
# Main 6
# swap the first with last element
    length = len(c)
    for i in range(length//2):
        c[i],c[length-i-1] = c[length-i-1],c[i]
    print("\n c is S.all.[after swapping]:\t",c)

#     Main 7
# multiply
    d = []
    for i in range(0,matrix_size):
        for j in range(0,3):
            var = c[j] * b[i][j]
            var = round(var,4) # round upto 4 decimal places
            d.append(var)  
    # print(d)  
    length1 = len(d)//matrix_size  # floor division means [5/2 --> 2.5 --> 2(floor value)]
    sum = 0
    f = []
    for i in range(0,matrix_size):
        print("SF",i+1,"is",d[sum:length1])
        a = d[sum:length1]
        f.append(a)
        sum = length1
        length1 = length1 + 3

#     Main 8
# Find the value of p` 
    P = []
    min_list = []
    for i in range(0,matrix_size):
        P = f[i]
        j = 0
        l1 = f[i][j]         #SF1
        m1 = f[i][j+1]
        u1 = f[i][j+2]
        for j in range(0,matrix_size):
            p = 99999
            if(f[i] == f[j]):
                min_list1 = min_list.append(p)
            else:
                k = 0
                l2 = f[j][k]
                m2 = f[j][k+1]
                u2 = f[j][k+2]
                if(m1 >= m2):
                    p = 1
                    min_list1 = min_list.append(p)
                elif(l2 >= u1):
                    p = 0
                    min_list1 = min_list.append(p)
                else:
                    l1 , l2 = l2 ,l1
                    u1 , u2 = u2 , u1
                    m1 , m2 = m2 , m1
                    var1 = p = ((l1 - u2)/((m2 - u2) - (m1 - l1)))
                    p = round(var1,4)
                    min_list1 = min_list.append(p)
    print("Final Min List is ",min_list)
    
    g = []
    sum = 0
    length2 = len(min_list) // matrix_size
    for i in range(0,matrix_size):
        a = min_list[sum:length2]
        g.append(a)
        sum = length2
        length2 = length2 + matrix_size
    store_p = []
    for j in range(0,matrix_size):
        p = min(g[j]) 
        store_p.append(p)
        print("p",j+1,"` is:",p)
    print("store_p is :",store_p)

    p_sum = 0
    for i in range(0,matrix_size):
        p_sum += store_p[i] 
    global norm_w , n_re , length3
    norm_w = []
    n_re = []
    for i in range(0,matrix_size):
        n_re = store_p[i] / p_sum
        n_re = round(n_re,4)
        norm_w.append(n_re)
    print("Normalized Weight is :",norm_w)
    length3 = len(norm_w)

# Find Reliability    
def for_reliability(reliability,length3,norm_w):
    R = 0.0000
    allreli = []
    global alloc 
    for j in range(0,length3):
        R = reliability ** norm_w[j]
        R = round(R,4)
        alloc.append(R)
        allreli.append(R)
        print("Reliability Allocation for F",j+1,"is :" "(",reliability,") ** ",norm_w[j]," :",R)
        print("F",j+1,"is :",R,"\n")
    print(allreli)
    return alloc
    

    
    
# Main 9

def module_case(matrix_size,alloc):
    for i in range(0,len(alloc)):
        print("F",i+1,"->",alloc[i],"is connected to how many modules")
        matrix_size1 = int(input())
        input_matrix(matrix_size1)

    
# Main 1
alloc = []
matrix_size = int(input("ENTER THE NUMBER OF ROWS AND COLUMN[Rows must be equal to column] :"))
reliability = float(input("Total Required reliability of System is :"))

if matrix_size > 1:
    input_matrix(matrix_size)
    for_reliability(reliability,length3,norm_w)
    a = int(input("Enter Number of Modules:"))
for i in range(len(alloc)):
        print("F",i+1,"is :",alloc[i])
        print("F",i+1,"is connected to how many modules:")
        matrix_size1 = int(input(""))
        input_matrix(matrix_size1)
        reliability = alloc[i]
        for_reliability(reliability,length3,norm_w)
        
    

      
        
    
