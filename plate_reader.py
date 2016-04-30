from openalpr import Alpr
list = ('BKW7165')
try:
    alpr = Alpr("eu", "/usr/share/openalpr/openalpr.default.conf", "/usr/share/openalpr/runtime_data") #laods alpr
    if not alpr.is_loaded():
        print("Error loading library (openalpr)")
    alpr.set_top_n(1) #determines which text to display with most confidence

    ##def email_alert(first): #definition of email alert system uses IFTTT to send a web request and then send an email
        #report = {}
        #report["value1"] = first
        #requests.post("https://maker.ifttt.com/trigger/plate_detected/with/key/dsyr5dpb8uON8UixB18Caw" , data=report)

    results = alpr.recognize_file("image.jpg")

    for plate in results['results']: #preliminary data to post canidate plate number
        for candidate in plate['candidates']:
             prefix = "-"
             if candidate['matches_template']:
                 prefix = "*"
             plate_text = (candidate['plate'])


    if plate_text not in list:#logic to test if number is database.
        print ("NOT IN LIST! NO PASSAGE!")
        alert = "Plate number is: " + plate_text
        print (alert)
    else:
        print ("Inside list. Allow entry.")
        alert = "Plate number is: " + plate_text
        print (alert)
except NameError:
    print ("No plates detected")
