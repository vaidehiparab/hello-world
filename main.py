# -*- coding: utf-8 -*-

#==============================================================================

#==============================================================================
import datetime

import GetBOFiles

def print_options():
    print("Main Menu:")
    print(" 'r' Run Program")
    print(" 'p' Print Options")
    print(" 't' System Time")
    print(" 'q' Quit Program") 

def mode_options():
    print("Options:")
    print(" 'p' Print Options")
    print(" '1' Run Offline BOD")
    print(" '2' Run BID-DA")
    print(" '3' Run BID-ID")
    print(" '4' Back-up Results")
    print(" 'q' Quit Run Time ")
   
 # Define the (temporary) storage on the local machine
lcldir     = 'C:/Users/vaidehi/Desktop/Intraday/'
choice = "p"
while choice != "q":
    if choice == "r":
        print("Progam has started. Choose run type.")
        #Program will run for curr_date but there could be an option in the future to choose the date. Especially for historical analysis
        while choice != "q":
            if choice == "1":
                 print("Checking Prerequisites.")
                 run_type= "OffBOD"
                 ext = 'InputFiles/BOFiles/'
                 #Check Local Directory to contains BOD/BUFF files from curr_date
                 ## CheckLocDir #return 0/1, 0 when files not there 
                 checklcl = 0  #temp setting 
                 if checklcl == 1:
                     #yes
                      print("BOD/BUFF files present. Ready for offline BOD run.")
                 else:
                     #no - #GetBOFiles for curr_date   #**APX settlement used for curr_date from BOD-BUF file** DECSION TO BE MADE
                     res = GetBOFiles.getBOFiles(run_type,lcldir,ext)
                #Check if DA position available from the database 
                    #yes - DA position avaialable. Ready for offline BOD run. 
                    #no - Warning: Will run based on APX settlement. You should have run DA yesterday. Ready for offline BOD run. 
                #Run Offline BOD    
                #Write output from new buffervullingfile to class BufferLine     
                 choice = input("option: ")
            elif choice == "2":
                 print("Checking Prerequistes.")
                 run_type = "DayAhead"
                 ext = 'InputFiles/BOFiles/'
                 #CheckDatabase:
                     #any changes to settings (cust, chp, buff temperature)?
                       #yes - Output class RunChanges, DateTime of run, TypeOfRun, which class, variable name, prev value, new value
                       #no - print no changes to settings. ready for DA
                     #Is data for curr_date present for Class BufferLine?
                       #no - You need to run offline BOD. Give option to run offline BOD. 
                       #yes - ready for DA
                 
                 #Get APX from getBOFiles - curr_date evening FTP folder in BOD-KTL - put in database
                 res = GetBOFiles.getBOFiles(run_type,lcldir,ext)
                       #throw error if BOD_KTL not seen. Check time. 
                     #Get LetsGrow and EET files - put in database
                       #throw error if EET not seen
                 print("Running BID-DA.")
                 #Run DA and output to class DA positions (**While running could give choice for which customers/CHP to want to run) 
                 #EET Output
                 print("No Errors. Done.")
                 choice = input("option: ")
            elif choice == "3":
                 print("Run intraday model")
                 choice = input("option: ")
                 #CheckDatabase:
                      #any changes to settings (cust, chp, buff temperature)?
                       #yes - Output class RunChanges, DateTime of run, TypeOfRun, which class, variable name, prev value, new value
                       #no - print no changes to settings. ready for ID
                      #Is data for curr_date present for Class BufferLine?
                       #no - You need to run offline BOD. Give option to run offline BOD. 
                       #yes - Buffer Line present. Ready for ID
                      #Check if APX settlement from curr_date is in the database (mostly should be there if DA was run on yest_date)
                       #no - Get APX from Local Directory/InputFiles/BOFiles - curr_date morning FTP folder in BOD-BUF - put in database 
                       #yes - APX settlement present. Ready to run ID.
                      #Is output for intraday DA present in database?
                       #no - Warning: will run based on APX Settlement present in the database for curr_date. You should have run intraday DA yest. 
                       #yes - intraday DA positions present. Ready to run ID.
                      #Get Lets Grow and EET files - put in database. 
                #Run ID and output to class Intraday positions.
                #EET Output.
            elif choice == "4":
                print("Back-up files and clean-up working directory")
                choice = input("option: ")
            else:
                choice = "p"
                mode_options()
                choice = input("option: ")
        print_options()
        choice = input("option: ")
    elif choice == "t":
        now=datetime.datetime.now()
        print(now.time())
        choice = input("option: ")
    else:
        choice = "p"
        print_options()
        choice = input("option: ")
         
    
#   if funcworks == 1:
#            print("All data has been retrieved and stored on database")
#            print ("Choose which mode to run")
#            choice = "p"
#        else: 
#            print("Error: Data Loading")
#            choice = "q"  
#have to write a check to make sure BOD-BUF and BOD-KTL APX settlements are the same. 
#difference between the BOD-BUF and BOD-KTL APX settlements (number of hours)




# directly run this code when GetBOFiles local folder is empty 
# i.e previous data has been back-up elsewhere. 
# check if current date files are there in the local folder 
    # if local folder is not empty
        # count files
        # if date == current date
             
            # if equivalent to morning files number (4178)
                #only need to copy afternoon files 
            #else if equivalent to total files (6130)
                # no need to copy files 
            #else (too many or too few files)
                #throw error (files missing)   
    # else (local) 
    
