#coding=utf-8
keyWordList = {
    'begin':' 1',
    'end':' 2',
    'integer':' 3',
    'if':' 4',
    'then':' 5',
    'else':' 6',
    'function':' 7',
    'read':' 8',
    'write':' 9'
     }
singleTerminalList = {
    '=':'12',
    '<':'15',
    '>':'17',
    '-':'18',
    '*':'19',
    '(':'21',
    ')':'22',
    ';':'23',
    ':':'temp'
}
doubleTerminalList = {
    '<>':'13',
    '<=':'14',
    '>=':'16',
    ':=':'20'
}
allList = dict(keyWordList.items() + singleTerminalList.items() + doubleTerminalList.items())

def analysisLine(line):
     wordlist1 = []
     wordlist2 = []
     for word  in line.strip().split():
         if word in keyWordList:
              #此时元素在关键字列表匹配，进行一些操作
             wordlist1.append(word)
         else:
             # 此时要对每个word进行字符串分析，看是否出现双终结符号或者单终结符号，之后进行字符串分割
             for singleTerminal in singleTerminalList:
                 word = word.replace(singleTerminal,' '+ singleTerminal + ' ')
             wordlist2=word.split()

             for tempword in wordlist2:
                    if (tempword == '<' and wordlist2[wordlist2.index(tempword) + 1] == '>' ) or (tempword == '<' and wordlist2[wordlist2.index(tempword) + 1] == '=' ) or (tempword == '>' and wordlist2[wordlist2.index(tempword) + 1] == '=' ) or (tempword == ':' and wordlist2[wordlist2.index(tempword) + 1] == '=' ):
                        tempindex = wordlist2.index(tempword)
                        wordlist2[wordlist2.index(tempword)] = wordlist2[wordlist2.index(tempword)] + wordlist2[wordlist2.index(tempword)+1]
                        wordlist2.pop(tempindex+1)
             for w in wordlist2:
                 wordlist1.append(w)
     #print wordlist1 #wordlist1就是现在需要的list

     for wd in wordlist1:
        if wd in allList:
            f = open('1.dyd','a')
            f.write(str((16-len(wd)) * ' ' + wd + ' '+ allList.get(wd)+'\n'))
            f.close()
            print (16-len(wd)) * ' ' + wd + ' '+ allList.get(wd)
        elif wd.isdigit():
            f = open('1.dyd', 'a')
            f.write((16-len(wd)) * ' ' + wd + ' '+ '11'+'\n')
            f.close()
            print (16-len(wd)) * ' ' + wd + ' '+ '11'
        else:
            f = open('1.dyd', 'a')
            f.write((16 - len(wd)) * ' ' + wd + ' ' + '10'+'\n')
            f.close()
            print (16-len(wd)) * ' ' + wd + ' '+ '10'
     return wordlist1


#清空文件内容
fileError = open('1.err','r+')
fileError.truncate()
fileError.close()
fileStandard = open('1.dyd','r+')
fileStandard.truncate()
fileStandard.close()
fileName = raw_input("请输入要进行词法分析的文件路径:\n")
file_opened = open(fileName,'r')
if file_opened:
    #file exists,do sth.
    lineNum =1
    for line in file_opened.readlines():
        for w in analysisLine(line):
            try:
                if w == ':' and analysisLine(line)[analysisLine(line).index(w) + 1] == ';':
                    fErr = open('1.err','a')
                    fErr.write('***LINE:' + '%d' % lineNum + '  ' + 'Illegal Operator\n')
                    fErr.close()
                w.decode('ascii')
            except UnicodeDecodeError :
                fErr = open('1.err','a')
                fErr.write('***LINE:' + '%d'% lineNum +'  ' + 'Unknown Character\n')
                fErr.close()
        f = open('1.dyd', 'a')
        f.write(' '*12 + 'EOLN' + ' ' + '24'+'\n')
        f.close()
        print ' '*12 + 'EOLN' + ' ' + '24'
        lineNum = lineNum + 1
    print ' '*13 + 'EOF' + ' ' + '25'
    f = open('1.dyd', 'a')
    f.write(' ' * 13 + 'EOF' + ' ' + '25'+'\n')
    f.close()
    file_opened.close()

else:
    #file not exists ,do sth.
    file_opened.close()
    print "file not exists"





