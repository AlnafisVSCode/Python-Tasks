
# from genericpath import exists
# from sys import argv


# script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long")


# #I Assume Yes/False
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, Control-c to abort.")
# input()

# out_file = open(to_file, "w")
# out_file.write(indata)

# print("Allright, all done.")

# out_file.close()
# in_file.close()

#Now We Gon Try Our selves Creating what we did previosuly on our ownn Twin

#Also Comment out before last Comment as it's the real Example but leave this onward for us


from asyncore import write
from genericpath import exists
from sys import argv


script, file1, file2 = argv

print(f"The Files which you have selected are {file1} and {file2}")

infile = open(file1)
insfile = infile.read()

print("The number of bytes file one has totals:", len(insfile))

print(f"Does File one and File 2 Exist? {exists(file2)}")

outfile = open(file2, "w")
outfiles = outfile.write(insfile)
print(insfile)

#One of the reasons why it's necessary to close the file access - is to allow other prgrams to get access to it

infile.close()
outfile.close()

