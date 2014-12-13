#Tom Lynch
#text generator, with option to change file saving location
#----------------------------------------------------
from Tkinter import * 
import os
root = Tk() #creates a new window
root.title("Note generator") #sets the windows title
root.iconbitmap("text_icon.ico") #window icon

def CheckLocation():
    try: #checks if there is a prior location file
        location_file = open("location.txt", "r")
        location = location_file.read()
        return location
    except:
        print "No prior location set"
    print "Location checked"
    
location = CheckLocation()
loc = StringVar() #tkinter variable http://effbot.org/tkinterbook/variable.htm
loc.set(location)

def SetFileLocation(): #the function to set file save location
    global loc
    location_f = open("location.txt", "w")
    location_f.write(dbox.get())
    location_f.close()
    top_loc = Toplevel()
    top_loc.title("Save Location Set")
    top_loc.iconbitmap("tick.ico")
    msg_loc = Label(top_loc, text="The file save location has been changed")
    msg_loc.pack()
    butt_loc = Button(top_loc, text="Dismiss", command=top_loc.destroy)
    butt_loc.pack()
    loc.set(dbox.get())
                    
    
    

def WriteToFile():
    global location
    location = CheckLocation()
    g = e.get()
    x = g+".txt"
    try: #if there is a location file set
        place = location
        addr_full = os.path.join(place, x)
        print "Full adress from WriteToFile", addr_full
        y = open(addr_full, "w")
        y.write(te.get("1.0", END)) #gets the value from a text widget, 1.0 is the characetr to start from and End goes all the way to the end
        y.close()
    except: #if there is not a location file set
        y = open(x, "w")
        y.write(te.get("1.0", END)) #gets the value from a text widget, 1.0 is the characetr to start from and End goes all the way to the end
        y.close()
    top_writ = Toplevel()
    top_writ.title("File created")
    top_writ.iconbitmap("tick.ico") #add icon
    msg = Label(top_writ, text="The file has been successfully created")
    msg.pack()
    closebutton = Button(top_writ, text="Dismiss", command=top_writ.destroy)
    closebutton.pack()


dummydummy = Label(root)
dummydummy.pack()

dbox = Entry(root, width=50)#file location entry window
dbox.pack()

dlab = Label(root, text="""This sets the location the file will save in.
(Copy the address over from the windows explorer window)
If you have set it before it will automatically save there.""")
dlab.pack()

dbutton = Button(root, text="Set Location", command=SetFileLocation)
dbutton.pack()

dummy = Label(root) #dummy label to add space between the above button and below text box
dummy.pack()

e = Entry(root, width="50") #file name text window (entry is just one line)
e.pack() #adds the text window to the root window

e.focus_set()

n = Label(root, text="File Name") 
n.pack()

te = Text(root, width="75") #file contents entry window
te.pack()

te.focus_set()

b = Button(root, text="Write To File", command=WriteToFile)
b.pack()

instructions = Label(root, text = """Enter the file name and text,
then click write to write to file""")
instructions.pack()

mainloop() #starts the program

