import os
import data_processing as dp
import csv

FOLDER_LIST = ['a01','a02','a03','a04','a05','a06','a07','a08','a09','a10','b01','b02','b03','b04','b05','b06','b07','b08','b09','b10','c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','e01','e02','e03','e04','e05','e06','e07','e08','e09','e10','f01','f02','f03','f04','f05','f06','f07','f08','f09','f10','g01','g02','g03','g04','g05','g06','g07','g08','g09','g10','h01','h02','h03','h04','h05','h06','h07','h08','h09','h10','j01','j02','j03','j04','j05','j06','j07','j08','j09','j10','k01','k02','k03','k04','k05','k06','k07','k08','k09','k10','l01','l02','l03','l04','l05','l06','l07','l08','l09','l10','m01','m02','m03','m04','m05','m06','n01','n02','n03','n04','n05','n06','n07','n08','n09','n10','p01','p02','p03','p04','p05','p06','p07','p08','p09','p10','r01','r02','r03','r04','r05','r06','r07','r08','r09','z01']

csvFile = open('processed_data.csv','a',newline='')
writer = csv.writer(csvFile)

for folder in FOLDER_LIST[100:]:
	subFolders = os.listdir("original/"+folder)
	for sb in subFolders:
		file = os.listdir("original/"+folder+"/"+sb)
		deviation,time,gender = dp.processData("original/"+folder+"/"+sb+"/"+file[0])
		writer.writerow([deviation,time,gender])
		print("file: original/"+folder+"/"+sb+"/"+file[0]+" done")

csvFile.close()


