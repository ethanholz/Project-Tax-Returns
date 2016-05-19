from openalpr import Alpr
import csv

plate_db = open('plates.txt').read()

try:
    alpr = Alpr("us", "/usr/share/openalpr/openalpr.default.conf", "/usr/share/openalpr/runtime_data") #laods alpr
    if not alpr.is_loaded():
        print("Error loading library (openalpr)")
    alpr.set_top_n(1) #determines which text to display with most confidence

    results = alpr.recognize_file("image.jpg")

    for plate in results['results']: #preliminary data to post canidate plate number
        for candidate in plate['candidates']:
             prefix = "-"
             if candidate['matches_template']:
                 prefix = "*"
             plate_text = str(candidate['plate'])


    if plate_text not in plate_db:#logic to test if number is database.
        print ("NOT IN LIST! NO PASSAGE!")
        alert = "Plate number is: " + plate_text
        print (alert)
        question = raw_input("Would you like to add to the database?  ")
        if question == "Yes" or question == "y" or question == "yes":
            plate_db = open('plates.txt', 'a');
            appendage = str(' ' + plate_text)
            plate_db.write(appendage)
            print ("Okay added")
        else:
            print("Okay end")
    else:
        print ("Inside list. Allow entry.")
        alert = "Plate number is: " + plate_text
        print (alert)
except NameError:
    print ("No plates detected")
