<<<<<<< HEAD
import csv
import pandas as pd

# list for storing u', v' and w'
import csv
l1 = []
l2 = []
l3 = []
# list for storing time, u, v and w
t = []
u = []
v = []
w = []

# opening file in read mode
uu_sum = vv_sum = ww_sum = 0.0
numb = 29746.0
with open('octant_input.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    reader = csv.reader(file)

    for row in reader:
        if (row[1] != 'U'):
@@ -25,32 +18,34 @@
        if (row[3] != 'W'):
            ww_sum += float(row[3])

# finding the u average, v average and w average and storing in list l4, l5 and l6
# u Average , v Average, w Average is calculated.

    u_Average = uu_sum/numb
    v_Average = vv_sum/numb
    w_Average = ww_sum/numb
    lst4 = [u_Average]
    lst5 = [v_Average]
    lst6 = [w_Average]

    u_avg = uu_sum/numb
    v_avg = vv_sum/numb
    w_avg = ww_sum/numb
    lst4 = [u_avg]
    lst5 = [v_avg]
    lst6 = [w_avg]
# inserting time, u, v and w values in lists t, u, v and w
# inserting u', v' and w' values in lists l1, l2 and l3
ln1 = ln2 = ln3 = ln4 = 0
t = []
u = []
v = []
w = []
with open('octant_input.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    reader = csv.reader(file)

    for row in reader:
        # print(row)
        if (row[1] != 'U'):
            l1.insert(ln1, float(row[1])-u_avg)
            l1.insert(ln1, float(row[1])-u_Average)
            u.insert(ln1, row[1])
            ln1 += 1
        if (row[2] != 'V'):
            l2.insert(ln2, float(row[2])-v_avg)
            l2.insert(ln2, float(row[2])-v_Average)
            v.insert(ln2, row[2])
            ln2 += 1
        if (row[3] != 'W'):
            l3.insert(ln3, float(row[3])-w_avg)
            l3.insert(ln3, float(row[3])-w_Average)
            w.insert(ln3, row[3])
            ln3 += 1
        if (row[0] != "Time"):
@@ -62,8 +57,9 @@
    lst5.append(None)
    lst6.append(None)

# creating a dataframe using pandas and storing the lists
# creating a dataframe using pandas
data_frame = pd.DataFrame()
# storing the lists
data_frame["Time"] = t
data_frame["U"] = u
data_frame["V"] = v
@@ -77,7 +73,7 @@
OCT_LST = []
len5 = 0
print(data_frame)
# code for counting the no of overall octant count and storing octant ids in OCT_LST
# counting overall count 
i = 0
o_cp1 = o_cp2 = o_cp3 = o_cp4 = o_cn1 = o_cn2 = o_cn3 = o_cn4 = 0
while (i < len(l1)):
@@ -120,48 +116,48 @@
    i = i+1


# funtion definition
# we define the func
def octant_identification(mod):
    j = k = 0
    interval = mod

    while (j < round):
    while (j < rnd):


        cn1 = cn2 = cn3 = cn4 = cn1 = cn2 = cn3 = cn4 = 0
        cn1 = cn2 = cn3 = cn4 = cn_1 = cn_2 = cn_3 = cn_4 = 0
        while (k < mod and k < len(l1)):
            if (l1[k] > 0 and l2[k] > 0):
                if (l3[k] > 0):
                    cn1 += 1
                else:
                    cn1 += 1
                    cn_1 += 1
            elif (l1[k] < 0 and l2[k] > 0):
                if (l3[k] > 0):
                    cn2 += 1
                else:
                    cn2 += 1
                    cn_2 += 1
            elif (l1[k] < 0 and l2[k] < 0):
                if (l3[k] > 0):
                    cn3 += 1
                else:
                    cn3 += 1
                    cn_3 += 1
            elif (l1[k] > 0 and l2[k] < 0):
                if (l3[k] > 0):
                    cn4 += 1
                else:
                    cn4 += 1
                    cn_4 += 1
            k = k+1

        mod = mod+interval
        # appending the values of octant cn in val1, val_1, val2, val_2, val3, val_3, val4 and val_4 lists for all intervals
        # appending the values of octant cn 
        val1.append(cn1)
        val_1.append(cn1)
        vaneg1.append(cn_1)
        val2.append(cn2)
        val_2.append(cn2)
        vaneg2.append(cn_2)
        val3.append(cn3)
        val_3.append(cn3)
        vaneg3.append(cn_3)
        val4.append(cn4)
        val_4.append(cn4)
        vaneg4.append(cn_4)
        j = j+1


@@ -173,80 +169,87 @@ def octant_identification(mod):
    mod_list.insert(i+2, None)
data_frame[""] = mod_list
# taking input from user
print("Enter any value")
print("Enter the mod value")
mod = int(input())
ltemp = []
ltemp.insert(0, "Overall Count")
strr = "Mod "
strr += str(mod)
ltemp.insert(1, strr)
L_TMp = []
L_TMp.insert(0, "Overall Count")

stng1 = "Mod "
stng1 += str(mod)
L_TMp.insert(1, stng1)
num = 30000
round = int(num/mod)
modulo_val = num % mod
rnd = int(num/mod)
MOD_VALUE = num % mod
len6 = 2
for i in range(round):
    strr = str(mod*i)
    strr += "-"
    strr += str(mod*(i+1)-1)
    ltemp.insert(len6, strr)
    len6 += 1
if (modulo_val):
    strr = str(num-modulo_val)
    strr += "-"
    strr += str(num)
    ltemp.insert(len6, strr)
    len6 += 1
while len6 < len(u):
    ltemp.insert(len6, None)
    len6 += 1
data_frame["octant ID"] = ltemp
# creating lists for storing octant count
val1 = []
val_1 = []
vaneg1 = []
val2 = []
val_2 = []
vaneg2 = []
val3 = []
val_3 = []
vaneg3 = []
val4 = []
val_4 = []
vaneg4 = []
# storing overall count of octants
val1.insert(0, o_cp1)
val_1.insert(0, o_cn1)
vaneg1.insert(0, o_cn1)
val2.insert(0, o_cp2)
val_2.insert(0, o_cn2)
vaneg2.insert(0, o_cn2)
val3.insert(0, o_cp3)
val_3.insert(0, o_cn3)
vaneg3.insert(0, o_cn3)
val4.insert(0, o_cp4)
val_4.insert(0, o_cn4)
# leaving a box blank
vaneg4.insert(0, o_cn4)



val1.insert(1, None)
val_1.insert(1, None)
vaneg1.insert(1, None)
val2.insert(1, None)
val_2.insert(1, None)
vaneg2.insert(1, None)
val3.insert(1, None)
val_3.insert(1, None)
vaneg3.insert(1, None)
val4.insert(1, None)
val_4.insert(1, None)
# mod=5000
# function callling
vaneg4.insert(1, None)
octant_identification(mod)


while len(val1) < len(l1):
    val1.append(None)
    val_1.append(None)
    vaneg1.append(None)
    val2.append(None)
    val_2.append(None)
    vaneg2.append(None)
    val3.append(None)
    val_3.append(None)
    vaneg3.append(None)
    val4.append(None)
    val_4.append(None)
# inserting columns corresponding to the octant value
    vaneg4.append(None)


for i in range(rnd):
    stng1 = str(mod*i)
    stng1 += "-"
    stng1 += str(mod*(i+1)-1)
    L_TMp.insert(len6, stng1)
    len6 += 1
if (MOD_VALUE):
    stng1 = str(num-MOD_VALUE)
    stng1 += "-"
    stng1 += str(num)
    L_TMp.insert(len6, stng1)
    len6 += 1


while len6 < len(u):
    L_TMp.insert(len6, None)
    len6 += 1
data_frame["octant ID"] = L_TMp
# inserting all columns of their octant value
data_frame["1"] = val1
data_frame["-1"] = val_1
data_frame["-1"] = vaneg1
data_frame["2"] = val2
data_frame["-2"] = val_2
data_frame["-2"] = vaneg2
data_frame["3"] = val3
data_frame["-3"] = val_3
data_frame["-3"] = vaneg3
data_frame["4"] = val4
data_frame["-4"] = val_4
# storing output in csv file
data_frame["-4"] = vaneg4
# printing in csv file
data_frame.to_csv("octant_output.csv", index=False)
=======
<<<<<<< HEAD
def octact_identification(mod=5000):
###Code


mod=5000
octact_identification(mod)
=======
def factorial(int x):
#here we write python code.
    

x=int(input("Enter the number whose factorial is to be found"))
factorial(x)
#here we write python code.
>>>>>>> b6a60bedf8828b8961b2b88090291968ec4ff8d1
>>>>>>> 926254a826d967fb059089308f3c59d9c9905a8c
