t = 5
sentences = []
while t:
    sentences.append(input("Podaj zdanie")+"\n")
    t -= 1

f = open("sentence.txt", "w")
for i in sentences:
    f.write(i)
f.close()

f = open("sentence.txt", "a")
f.writelines(sentences)
f.close()

f = open("sentence.txt", "r")
for line in f:
    print(line, end="")
f.close()

f = open("sentence.txt", "r")
x = f.readline()
print(x)
f.close()

with open("sentence.txt", "r") as f:
    f.write("Hello from context")
