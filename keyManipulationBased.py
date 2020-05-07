from random import randint

def receiveCommands():
    database=[]     # [ word , [all_searchers] , [distinct_searchers] ]
    results=""
    while True:
        command=input().strip("\n")

        if command=="PALAVRAS": 
            aux=input().strip("\n")
            while (aux!="FIM."): 
                aux=aux.split(" ")
                index= isIn(database, aux[0])
                if index== -1: database.append([aux[0], [aux[1]], [aux[1]]])
                elif aux[1] not in database[index][1]:
                    database[index][1].append(aux[1])
                    database[index][2].append(aux[1])
                else: database[index][1].append(aux[1])
                aux=input().strip("\n")
            results+= "GUARDADAS\n"
        elif command=="PESQ_GLOBAL": 
            database= countingSort(database, 1)
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][1])==len(database[i][1]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="PESQ_UTILIZADORES": 
            database= countingSort(database, 2)
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][2])==len(database[i][2]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="TCHAU": break
        else: print("Incorrect command.")
    print(results, end='')

def isIn(database, word):
    for search in database:
        if word.upper()==search[0].upper(): return database.index(search)
    return -1
      
def countingSort(database, command):
    searchers_counter=[len(search[command]) for search in database]
    smaller=min(searchers_counter)
    diference_numbers=max(searchers_counter)-smaller+1
    indexArray= [0 for i in range(diference_numbers)]
    sortedArray=[]
    for number in searchers_counter: indexArray[number-smaller]+=1
    del smaller, diference_numbers, number, command
    for occurrences in range(len(indexArray)):
        while indexArray[occurrences]!=0: 
            greater=searchers_counter.index(max(searchers_counter))
            sortedArray.append(database[greater])
            indexArray[occurrences]-=1
            searchers_counter.pop(greater)
            database.pop(greater)
    return sortedArray
            
if __name__ == "__main__":
    receiveCommands()