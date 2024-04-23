handle = open("soal.txt", "r").readlines()
for line in handle:
    soalteks,jawaban = line.split("||")
    soalteks = soalteks.strip()
    print(soalteks)
    menjawab = input("Jawab: ").lower().strip()
    if menjawab == jawaban.lower().strip():
        print("Jawaban benar!")
    else:
        print(f"Jawaban salah! jawaban yang benar adalah {jawaban}")