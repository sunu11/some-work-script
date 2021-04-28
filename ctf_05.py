import itertools
import hashlib
m = hashlib.md5()

flag = ["" for _ in range(10)]

flag[1] = "FbCCv_DxxK#XZhxF"
flag[2] = "L9_CpNBjGS##14V_"
flag[3] = "TF4vWhE1lD4dd4Vg"
flag[4] = "crbZX=u4Ct7JJSwu"

com2 = list(itertools.combinations(flag[2], 3))
com3 = list(itertools.combinations(flag[3], 3))
com4 = list(itertools.combinations(flag[4], 3))

com2 = com2[::-1]
com3 = com3[::-1]
com4 = com4[::-1]

for x in com2:
    for y in com3:
        for z in com4:
            result = "n#D" + "".join(x)  + "".join(y) + "".join(z)
            md5 = hashlib.md5(result.encode('utf-8')).hexdigest()
            if md5 == "xxxxx":
                print(result)
