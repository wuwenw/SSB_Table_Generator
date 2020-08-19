import os
def converttbldatatocsvformat(filename, header):
 path = "../ssb_tables/"
 print("try to clean up csv")
 try:
     os. remove("".join([path, filename, ".csv"]))
     print("deleted " + filename + ".csv")
 except:
     print("no csv found")
 csv = open("".join([path, filename, ".csv"]), "w+")
 csv.write(header + "\n")
 tbl = open("".join([filename, ".tbl"]), "r")
 lines = tbl.readlines()
 for line in lines:
    length = len(line)
    line = line[:length - 2] + line[length-1:]
    line = line.replace(",","N")
    line = line.replace("|",",")
    csv.write(line)
 tbl.close()
 csv.close()
 print("generated " + filename + ".csv")

converttbldatatocsvformat("part", "0,1,2,3,4,5,6,7,8")
converttbldatatocsvformat("lineorder", "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
converttbldatatocsvformat("customer", "0,1,2,3,4,5,6,7")
converttbldatatocsvformat("date", "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
converttbldatatocsvformat("supplier", "0,1,2,3,4,5,6")