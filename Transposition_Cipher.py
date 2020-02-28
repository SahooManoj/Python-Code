''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    n=int(input())
    case=input("Input E for Encrypting and D for Decrypting : ")
    if  not [case=="D" or case=="E"]:
        print("Invalid Input")
        return
    a=1
    for i in range(n):
        key=input()
        text=input()
        key=list(key)
        for each in key:
            if key.count(each)>1:
                for i in range(key.count(each)-1):
                    key.reverse()
                    key.remove(each)
                    key.reverse()
        key=[ord(item) for item in key]
        countkey=len(key)
        if countkey and len(text)>=1 and countkey<=7 and len(text)<=255:
            original=[]
            m=65
            prev=65
            while m<=90:
                if 90-m<=countkey:
                    m=91
                else:
                    m+=countkey
                listval=[i for i in range(prev,m) if not key.__contains__(i)]
                if m<90:
                    while len(listval)<countkey:
                        if key.__contains__(m):
                            m+=1
                            continue
                        else:
                            listval.append(m)
                            m+=1
                original.append(listval)
                prev=m
            
            sortedkey=key[::]
            sortedkey.sort()
            dictionary={}
            m=65
            for eachkey in sortedkey:
                index=key.index(eachkey)
                if case=="D":
                    dictionary[chr(eachkey)]=chr(m)
                else:
                    dictionary[chr(m)]=chr(eachkey)
                m+=1
                for eachval in original:
                    if index<=len(eachval)-1:
                        if case=="D":
                            dictionary[chr(eachval[index])]=chr(m)
                        else:
                            dictionary[chr(m)]=chr(eachval[index])
                        m+=1
            dictionary[' ']=' '
            c=0
            for eachchar in text:
                c+=1
                if c==len(text) and a<n:
                    print(dictionary[eachchar])
                else:
                    print(dictionary[eachchar],end='')
            a+=1


main()

