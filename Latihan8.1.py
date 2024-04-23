handle0 = open("filepertama.txt").readlines()
handle1 = open("filekedua.txt").readlines()
garis = max(len(handle0),len(handle1))
for i in range(garis):
    if i < len(handle0) and i < len(handle1):
        if handle0[i] == handle1[i]:
            print(f"pada baris ({i+1}) sama dengan dua file itu")
        else:
            print(f"pada baris ini ({i+1})tidak sama")
            print(f"perbedaan tersebut ada di {handle0[i]} pada file pertama dan {handle1[i]} pada file kedua")
