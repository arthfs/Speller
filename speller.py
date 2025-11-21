from pathlib import Path
from function import validate_args, read_from_files,search ,w_word,read_stdin
class dword():
    lowercase = ''
    original = ''

    def __init__(self,word):
        self.lowercase = word.lower()
        self.original = word
    


  

test = [
        '-s .txt C:/Users/arthu/Documents/speller/dictionary.txt',
        '-s .txt C:/Users/arthu/Documents/speller/dictionary.txt C:/Users/arthu/Documents/speller/file1.txt',
        '-s .py dict file1.txt',
        '-s .py dict',
        '-s .py C:/Users/arthu/Documents/speller/dictionary.txt dir',
        '-s C:/Users/arthu/Documents/speller/dictionary.txt  file1.txt',
        '-s dict  ',
        '-s.py C:/Users/arthu/Documents/speller/dictionary.txt file1.txt',
        'dict2',
        '-s .pydict2 dir',
        '-s',
        'C:/Users/arthu/Documents/speller/dictionary.txt -s .py',
        'C:/Users/arthu/Documents/speller/dictionary.txt -s'
        ]
argv = test[0]
#argv = input("Provide the path of the dictionarry\nfollowed by the desired extension eg -s .py (optional)\nfollowed by the path (s) of file/directory (otherwise it will read from stdinput)\n")

#for a in test:
#    result = validate_args(a)
#    print(a,result)
#    print('\n')

res = validate_args(argv)
if res <0 :
    exit()
#get_dict
argv_list = argv.rsplit()
dict_path = argv_list[res+1]
suffix = '.txt' if res == 0  else argv_list[res]

print(dict_path,suffix)
ref = []
words = []
dict_file = open(dict_path,'r')
for line in dict_file.readlines():
    #temp = line.removesuffix('\n').removesuffix(" ")
    
    #print(temp,len(temp))
    nword = dword(line.removesuffix('\n').removesuffix(' '))
    ref.append(nword)


if res+2 < len(argv_list):
    #get_files
    p = Path(argv[res+2])
    input_path = [p]
    files_path = []
    read_from_files(files_path, input_path,words,suffix)
else:
   
    read_stdin(words)
    

dict_file.close()
#for w in words:
#        print(w.path, w.word,w.line,w.column)
    #print('\n\n')
ref = sorted(ref,key = lambda x: x.lowercase)
#for i in ref:
#    print(i.original)


for w in words:
    #print(w.word,w.line,w.column)
    
    result = search(ref , w.word)
    if result < 0:
        if w.path != '':
            base = "{}:{}:{}".format(w.path, w.line,w.column)
            print("{} {}".format(base.ljust(60),w.word))
        else:
            print("{}:{} {}".format(w.line,w.column,w.word))
    
