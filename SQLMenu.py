
import SQLQueries as query
import sql03ConnectCartage as sqlConnection
import os 
import pandas as pd
from datetime import date
from datetime import datetime
import timeit
import random


def appendToFileDict(fName,tableList):
    with open(fName, 'a', encoding='utf-8', errors='ignore') as f:
         for t in tableList:
                print(t, end = ',')
                print(tableList[t])
                
def surroundBrackets(word):
    return '[' + word + ']'

def makeFolder(name):
    os.mkdir(name)
    
def writeResult(result,fName,ext):
          with open(fName+ext, 'w', encoding='utf-8', errors='ignore') as f: 
                for record in result: 
                    f.write(str(list(record)).strip('[').strip(']'))
                    f.write('\n')
          
def printResult(result):
       for record in result:
            print(str(list(record)).strip('[').strip(']'))
            print('\n') 

def mapResult(result):
    items =  []
    for record in result:
        items.append(list(record))
    return items

def main():
    extractSamples()
    # db = 'MASTER'
    # USdb2 = 'us1-geodev-db2.corp.expeditors.com'
    # laxSQL03 = r'lax-sql03\sqlserverlax'
    # print("Init")
    # engine = sqlConnection.establishConnection(db,USB)
    # databases = query.getDatabases(engine)
    # bigList = []
    # now = datetime.now()
    # current_time = str(date.today()) +now.strftime("%H:%M")
    # print(current_time)
    # tableList = []
    # for d in databases:
    #     engine = sqlConnection.establishConnection(d,laxSQL03)

    #     res = query.getTables(engine)
    #     for r in res : 
    #         print (str(res[0]) + " ", end = str(res [1]))
    #         print()

def extractSamples():
    db = 'MASTER'
    USdb2 = r'us1-geodev-db2.corp.expeditors.com'
    laxSQL03 = r'lax-sql03\sqlserverlax'
    print("Init")
    engine = sqlConnection.establishConnection(db,USdb2)
    databases = query.getDatabases(engine)
    bigList = []
    now = datetime.now()
    current_time = str(date.today()) +now.strftime("%H:%M")

    with open('USBDBsamples' + str(date.today()) + current_time + '.csv', 'w', encoding='utf-8', errors='ignore')as f:
        
        for d in databases:
            dataBaseStartTime =  timeit.default_timer()
            if (d.lower() in ('master', 'tempdb', 'msdb', 'model')):
                continue
            try:
                engine =   sqlConnection.establishConnection(d,USdb2)

                result = mapResult(query.getColumns(engine))
                writeNo = 1
                print(writeNo/len(d))
                for r in result:
                        resultStartTime = timeit.default_timer() 
                    
                        sample =  str(query.getSampleDataFrame(
                            engine, r[1], '[' + str(r[2]) + ']')).strip('[').strip(']').strip('(').strip(')').strip(',')
                    
                        f.write(','.join([str(r[0]),str(r[1]),str(r[2]),sample]))
                        f.write('\n')
                        print("The time difference is :", timeit.default_timer() -   resultStartTime)
                print("The time difference is :", timeit.default_timer() - dataBaseStartTime)
            except:
                print('error')
                    # f.write(str(r[0]) + ',')
                    # f.write(str(r[1]) + ',')
                    # f.write(str(r[2]) + ',')
                    # f.write(sample)
                    # f.write("\n")
                    # writeNo = writeNo + 1
                    # os.system('cls')
                    # print(d ,end = '.')
                    # os.system('cls')
                    # print(d , end ='..')
                # ext = '.csv'
                # subR = query.getColumns(engine)
                # printResult(subR)
                # writeResult(subR,'test',ext)

if __name__ == '__main__':
    overAllStart = timeit.default_timer()
    print("The start time is :",   overAllStart)
    main()
    print("The time difference is :", timeit.default_timer() -   overAllStart)
                
#def exportDataSamples():
    # for d in databases:
    #     db = d
    #     directory = d
    #     if not os.path.isdir(directory):
    #         os.mkdir(directory)
    #     if(d.lower() in ('master','tempdb','msdb','DistributionVisibility','model')): continue
    #     engine =  sqlConnection.establishConnection(db)  
    #     for tSmall in tableDict[db]:
    #         file_path = r'C:/Users/lax-rickyt/'+ db + r'/' +tSmall + '.csv'
    #         try:
    #              #query.getDataSampleCSV(engine,tSmall,file_path)
    #              all_files.append(file_path)
    #         except Exception as e:
    #               print(e)
    #     print(".")
        
    # writer = pd.ExcelWriter('out3.xlsx', engine='openpyxl')
    # fN = 0
    # for f in all_files:
    #         print(f)
    #         fN=fN+1
    #         try:
    #                 df = pd.read_csv(f)
    #                 df.to_excel(writer,sheet_name='sht'+str(fN))
    #         except Exception as e:
    #                 print(e)
   # writer.close()

                
