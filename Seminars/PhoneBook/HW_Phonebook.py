import functions

filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
functions.main_menuu()

functions.searchcontact()

functions.input_firstname()

functions.input_lastname()

functions.newcontact()

