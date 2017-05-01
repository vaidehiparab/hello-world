# -*- coding: utf-8 -*-
#Goal: automated copy of the BO in- and output files to IDProject/LocalFiles

#def getBOFiles():
    
    # FTP is needed for the BiedOptimaal server
    # Using the ftplib package for this, see documentation and example at https://docs.python.org/2/library/ftplib.html

    # Import the package
    
import ftplib
import datetime

# Also import os for operations on the local folder structure
import os
#define the type of run - options Offline BOD (OffBOD) or Day Ahead (DayAhead)


def getBOFiles(run_type,lcldir,ext):  
    
 
    lcldir = lcldir + ext
       
    # Define the FTP details
    bohost    = '81.18.12.55'
    bouser    = 'Biedoptimaal'
    bopasswd  = 'b0d'
    
    # state IPG of the installation groups 
    #igp = [10, 11,  652]    
    
    # Open the ftp connection
    boftp = ftplib.FTP(bohost, bouser, bopasswd)
    bonames = boftp.nlst()
    boftp.set_pasv(False)
    
    if not bonames:
        print("No folders or files present in top directory")
    
        boftp.quit()
        boftp.close()
    
    # find the current date and convert it to a string format (yyyymmdd) 
    curr_date = datetime.date.today().strftime('%Y%m%d')
    #------------ Test 1 -----------------------------
    #  test when current date is not part of ftp 
    #curr_date = "20150621"
    #--------------------------------------------------
    #------------ Test 2 -----------------------------
    # test for all files in a month  
    #curr_date = "20170411"
    #--------------------------------------------------
    
    
    # find folders matching with  the current date     
    match_fold = [foldname for foldname in bonames if curr_date in foldname]
    #------------ Test 2 -----------------------------
    # test match_fold =[] 
    #match_fold = []
    #--------------------------------------------------
    #if there are no folders matching the current date
    if match_fold == []:
         print("No folders present in the ftp with current date: " + curr_date)
         return "Not Successful"
    #if there are folders matching the current date    
    else:
        #initialise the ftp directory
        startftp = boftp.pwd()
        #initialise list to store the directories corresponding to each folder
        seedir = []
        if run_type == "OffBOD":
            #assign folder name
            foldname = match_fold[0]
        else:
            #assign folder name
            foldname = match_fold[1]
        
        #store directory corresponding to morning folder
        tempftp = startftp+foldname+'/'
        seedir.append(tempftp)
        #initialize list to store filenames of the files in the folders
        filenames = []
        #store the filenames in the list 
        for dirnow in seedir:
            boftp.cwd(dirnow)
            boftp.retrlines('NLST',filenames.append)
       
        #create local folder directory
        lclfold = os.path.join(lcldir,foldname)
        #create local folder
        print("File Transfer Started")
        if not os.path.exists(lclfold):
            os.makedirs(lclfold)
        
        for filename in filenames:
            lclname = os.path.join(lclfold,filename)
            lclfile = open(lclname,'wb')
            boftp.retrbinary('RETR '+filename, lclfile.write)
            lclfile.close()
        print("File Transfer Completed")
        return "Successful"
    boftp.quit()
    boftp.close()

    
    


#else:
#    #state number of folders (in the morning run, there will be 1 folder and afternoon run there will 2 folders)
#    num_fold = match_fold.__sizeof__
#------------ Exceptions--------------
#FTP folders dont always contain same number of folders        

    
#result = getBOFiles()    
