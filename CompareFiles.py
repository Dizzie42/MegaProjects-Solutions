file1 = input("Enter first(main) file name: ") + ".txt"
file2 = input("Enter second(comparison) file name: ") + ".txt"
result = input("Enter results file name: ") + ".txt"

outfile = open('results/'+result, 'w')

comp_file = open(file2,'r')
main_file = open(file1,'r')
# = header info on file


comp_file_raw = comp_file.read()
main_file_raw = main_file.read()
# = data


comp_file_words = comp_file_raw.split()
main_file_words = main_file_raw.split()
#contains each individual word in a set of values [x,y,z...etc]


list = set(main_file_words).difference(set(comp_file_words))		
#unique words from main which are not in comparison


for item in list:
	outfile.write(item+'\n')
outfile.close()
