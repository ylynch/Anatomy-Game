# need to refresh memory on coding the while/break loop
greeting = input("Hello, would you like to play a game (Y/N)? ")  
if greeting.lower() == "y":
    print("Great, let's learn about human anatomy.  Which part of the body would you like to learn about?")
else:
    print("Okay, maybe next time.")

# not working in order of project road map; plan is to get the basic code down and fancy/pretty it up later

anatomylist = ["Circulatory", "Digestive", "Endocrine", "Immune", "Integumentary", "Lymphatic", "Muscular", "Nervous", "Reproductive", "Respiratory", "Skeletal", "Urinary"]
print("Anatomy Options:")
for anatomy in anatomylist:
    print(anatomy)
selection = input("Please review the list and make your selection: ")

# do we need to create a separate file for each anatomy question list for import?
