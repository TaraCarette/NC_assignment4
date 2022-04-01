import os

def main():
    trainfile = open("snd-cert.train", "r")
    
    
    writefile= open("chunked/chucked_train.txt", 'w+')
    bashCommand = 'java -jar negsel.jar -c -l -n 10 -r 4 -alphabet file://snd-cert.train -self snd-cert.train <  chunked_test.txt | paste - chunked_snd-cert.1.labels '

    for count, line in enumerate(trainfile.readlines()):
        for chunk in chunkstring(line, 10):
            writefile.write(chunk + ' ')
            os.system(bashCommand)
        writefile.write('\n')
    
        for chunk in chunks:
            writefile.write(chunk+"\n")
    
    

        
    file = open("scores_unix.txt", 'r')
    writefile = open("score_unix_avg.txt", 'w')
    
    for line in file.readlines():
        avg = 0
        for count, num in enumerate(line.split()):
            avg += float(num)
            print(avg)
        avg = avg/ (count + 1)

        
        writefile.write(str(avg) +'\n')

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

main()