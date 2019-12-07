# TFA_project_39

Project Overview:
This project is a web based application which tracks the squirrels located in central park. 
It uses a sqlite3 database to store publicly available squirrel data.

Description of files:
1. squirrel_tracker: Name of the app
2. project_39: Name of the project
3. Views in the app:
      a. /sightings : A view with links to edit all the squirrel id's and add a new squirrel; a form generates to update and add squirrels 
      b. /map  : A map with markers corressponding to squirrel location using laeflet library
      c. /sightings/stats: A view with interesting stats about the squirrel data
      d. /sightings/add: A form to add a new squirrel
      e. /sightings/<unique squirrel id>: A form to update an existing squirrel
4. Management commands: 
    a. import_squirrel_data: A command that can be used to import the data from the 2018 census file (in CSV format)
    b. export_squirrel_data:  A command that can be used to export the squirrel data in CSV format
    
 Group Name & Section:
        Group 39, Section 1
        
 Group Members:
        UNIs: [ag4182, ak4426]
        
 App link:
      https://magnificent-pen-255421.appspot.com/
    
