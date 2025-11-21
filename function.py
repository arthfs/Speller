from pathlib import Path 
class w_word():
    line = 0
    column = 0
    word = ''
    path = ''

    def __init__(self,word):
        self.word = word
    
    def parse(self):
        numalpha = 0
        for l in self.word:
            if l.isalpha():
                numalpha+=1

        if numalpha == 0:
            self.word = ''

        ignored_beginning = ["'","(",")",'[',']','{','}','`','"']        
        
        i,j = 0, len(self.word)-1
        while i<j:
            if self.word[i] in ignored_beginning:
                i+=1

            if not (self.word[j].isdigit() or self.word[j].isspace() or self.word[j].isalpha() ):
                j-=1 
            
            if self.word[i] not in ignored_beginning and (self.word[j].isdigit() or self.word[j].isspace() or self.word[j].isalpha() ):
                self.word = self.word[i:j+1]
                break


def validate_args(arg):
    
    temp = arg.rsplit()
    #print(temp)
    if len(temp) <1:
        print('no dictionary path was provided')
        return -99
    
    for i in range(len(temp)):
        if temp[i] == '-s' and i>0:
            print("invalid suffix position")
            return -99
        
    if temp[0] == '-s' and len(temp)<2:
        print('no dictionary was provided')
        return -99

    if temp[0] != '-s':
        #print(temp)
        if not Path(temp[0]).is_file():
            print('invalid dictionary path')
          
            return -99
        
    elif temp[0] == '-s':
        if temp[1][0] == '.'and temp[1] !='..':
            if not Path(temp[2]).is_file():
                print('invalid dictionary path')
                #print('here')
                return -99
            else :
                return 1
            
        if not Path(temp[1]).is_file():
            print('invalid dictionary path')
            return -99
        
        return 0
        

def read_from_files(files_path, input_path,words,suffix):
        
    while input_path!=[]:
        current = input_path.pop(0)
        if current.exists():
            if current.is_dir():
                for new_path in current.iterdir():
                    if new_path.is_dir() or new_path.is_file():
                        input_path.append(new_path)

            else:
                if current.absolute().suffix == suffix:
                    files_path.append(current.absolute())
            
        else:
            #print(current.absolute().name)
            #print(res,argv_list)
            print('invalid path')
        
    #print(files_path)
    #input_path = 'C:\\Users\\arthu\\Documents\\speller\\file1.txt'

    for f in files_path:

        input_file = open(f,'r')
        cur_line = 1
        cur_column = 1
        for line in input_file.readlines():
            temp = line.rsplit()

            for w in temp:
                
                nword = w_word(w)
                nword.parse()
                if len(nword.word) > 0 :
                    nword.column = cur_column
                    nword.line = cur_line
                    nword.path = f
                
                    words.append(nword)
                cur_column+= len(nword.word)+1
            cur_line+=1
            cur_column = 1
        
        input_file.close()

def search(ref,target):
    temp = target.lower()
    i , j = 0, len(ref)-1

    while i<=j:
        m = int (i+ (j-i)/2)
        if temp == ref[m].lowercase:
            if ref[m].original.islower():
                return m 
            else:
                return 0 if ref[m].original == target else -1
        
        elif ref[m].lowercase < temp:
            i = m+1

        elif ref[m].lowercase > temp:
            j = m-1 

    return -1