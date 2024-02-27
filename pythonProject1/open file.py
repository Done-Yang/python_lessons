"""
# structure of open file " open("file name", "mode", "password login(languages code)"
# type of mode : "r"="read", "w"="write", "a"="append", "x"="create new file", "t"="text file", "b"="binary text"
try:
    fl = open("score.txt", "r")
    print(fl.read())
except FileNotFoundError:
    print("can't found the file")

# write the text file
try:
    fw = open("score.txt", "w")
    fw.write("hello world\n")
    fw.writelines("please look at me\n")
    fw.writelines("here is the append line")
    print(fw)

    fw.close()
except FileNotFoundError:
    print("can't found the file")

# "a"=append
try:
    fa = open("score.txt", "a")
    for i in range(5):
        name = input("type your massage here: ")
        fa.writelines(name + "\n")
    fa.close()

except FileNotFoundError:
    print("can't found the file")

# how to delete the file
import os
try:
    if os.path.exists("student.txt"):
        os.remove("student.txt")
        print("file name: 'student.txt' removed")

    else:
        print("not define")
except FileNotFoundError:
    print("can't found your file")

# grade to student program
try:
    # g = open("grade.txt", "w")
    # while True:
    #     student_id = input("write student id: ")
    #     if student_id == "exit":
    #         print("..finish..")
    #         break
    #     score = input("write students score here: ")
    #     g.writelines(student_id + "\t" + score + "\n")
    # g.close()
    fr = open("grade.txt", "r")
    fw = open("std ifo.txt", "w")
    grade = None
    for line in fr.readlines():
        score = line[-4:].strip()   # part of students score
        Id = line[:-4]  # part of student id
        # print("Student ", Id, "Score is ", score)
        score = int(score)  # only integer can be calculated
        if score >= 28:
            grade = "A+"
        elif 25 <= score <= 27:
            grade = "A"
        elif 20 <= score <= 24:
            grade = "B"
        else:
            grade = "F"
        # print("Student ", Id, "Score is ", score, "grade", grade)   # to prnt the score in the output
        fw.writelines("student no " + Id + "\t" + "score: " + str(score) + "\t" + "grade: " + grade + "\n")
    fw.close()
    fr.close()

except FileNotFoundError:
    print("can't found your file")

try:
    w = open("Hang man.txt", "w")
    w.write("mouse")
    w.close()
except FileNotFoundError:
    print("Reset new name")

mutable_bytes = bytearray(b'abcd')
print(mutable_bytes)
print(type(mutable_bytes))

mutable_bytes[0] = 255
mutable_bytes.append(255)
print(n)

immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)
print(type(immutable_bytes))
mutable_bytes = bytearray(b'\xAF\xDE\x1A\xFF')
mutable_bytes[0] = 162
mutable_bytes.append(162)
print(mutable_bytes)
print(mutable_bytes[0:2])

# binary file "wb", "ab", "xb", "rb"
with open("byte_file.txt", "wb") as bnr_file:
    bnr_file.write("Hello World!".encode('utf8'))
    num_byte_writen = bnr_file.write(b'\xAD\xFF\xA1')

print("Wrote %d bytes" % num_byte_writen)

# read byte file line
with open("byte_file.txt", "rb") as readline_file:
    for line in readline_file:
        print(line)

# Get size of file
import os
lenght_file_as_byte = os.path.getsize("byte_file.txt")
print(lenght_file_as_byte)

# Seeking position of file
seek = open("byte_file.txt", "rb")
seek.seek(3, 0)
couple_file = seek.read(5)
print(couple_file)

# convert binary to text
binary_data = b'I am a text in binary'
convert_to_text = binary_data.decode('ascii')
print("binary text: ", binary_data)
print("text: ", convert_to_text)
x = bytearray(binary_data)
x.pop()
print(x)

binary_data = bytes([65, 66, 67])
convert = binary_data.decode('ascii')
print(convert)

# text to binary
text = "I am a binary text in normal tex"
to_binary_tex = text.encode('ascii')
print(to_binary_tex)

# encode to another language
import codecs
another_language_encoding = codecs.encode(text, 'rot-13')
print(another_language_encoding)
"""



