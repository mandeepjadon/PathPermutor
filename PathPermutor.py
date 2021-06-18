from tld import get_tld
from itertools import permutations
import sys


def GetDirPaths(url):
    Temp_Dir_Paths=[]
    URL = get_tld(url, as_object=True)
    Temp = URL.parsed_url.path
    Temp_File_Path = ''
    Url_List = Temp.split("/")
    Url_List = list(filter(None, Url_List))   ## Little cleanup
    if "." in Url_List[len(Url_List)-1]:   ## This would avoid the files path
        Temp_File_Path = "/"+ Url_List[len(Url_List)-1] ## Saving file name for later use 
        Url_List.pop(len(Url_List)-1)
    
    for L in range(len(Url_List)+1):
        for subset in permutations(Url_List, L):
            Temp_Dir_Paths.append("/"+"/".join(subset))
    return [Temp_Dir_Paths,Temp_File_Path]


def Final(OutFile,Url_List):
    Final_Dir_Paths=[]
    Final_File_Paths=[]
    for Url in Url_List:
        try:
            Dir_File = GetDirPaths(Url)    
            if Dir_File[1] is None:     ## To handle NoneType returned for Filetypes
                Final_Dir_Paths = Final_Dir_Paths + (Dir_File[0])
            else:
                Final_Dir_Paths = Final_Dir_Paths + (Dir_File[0])
                Final_File_Paths.append(Dir_File[1])        
        except Exception as E:
            print (str(E))
    Final_Dir_Paths = set(Final_Dir_Paths)
    Final_Dir = list(filter(None, Final_Dir_Paths)) 
    Final_File_Paths = set(Final_File_Paths)
    Final_File = list(filter(None, Final_File_Paths))
    Final_Results = Final_Dir + Final_File
##    for Path in Final_Results:
##        print (Path)
    Out = open(OutFile,"a")
    for res in Final_Results:
        Out.writelines(res+"\n")
    Out.close()
    print ("%d possible paths found . Results saved to %s" %(LineCounter(OutFile),OutFile))

def LineCounter(FileName):
    count = len(open(FileName).readlines())
    return count

##for dirs in Final_Dir:
##    for files in Final_File:
##        print (dirs+"/"+files)
##        Final_Results.append(dirs+"/"+files)        ## Older Logic produced huge list
##for files in Final_File:
##    Final_Results.append("/"+files)
        

def main():
    print ("#############################################################################")
    print ("#########################PathPermuter v1.0########################################")
    print ("#############################################################################")
    print ("Author : Mandeep Jadon")
    print ("#############################################################################")
    print ("#############################################################################")
    if len(sys.argv)!=3:
        print ("Please enter the command as python3 pathpermuter.py InputFile.txt OutputWordlist.txt")
    else:
        InputFile = sys.argv[1]
        OutFile = sys.argv[2]
        print ("%d URLs loaded from the input File" %(LineCounter(InputFile)))
        Url_List = [line.rstrip() for line in open(InputFile)]
        Final(OutFile,Url_List)


if __name__ == "__main__":
    main()






    
    
