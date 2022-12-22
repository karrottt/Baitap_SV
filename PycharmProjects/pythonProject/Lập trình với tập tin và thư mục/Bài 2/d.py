def write_to_file(file, num_array, m=10):
    n=len(num_array)
    for i in range(n//m + int(n%m>0)):
        file.write(','.join([str(i) for i in a[i*m:(i+1)*m]])+'\n')
# Nếu cần thử thì chương trình chính là (list a có n 27 ptử)
n=27; a=list(range(n))
file = open('z:\\tamtam1.txt','w')
write_to_file(file, a)
file.close()