from tkinter import *
import googletrans
from googletrans import Translator, LANGUAGES
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from urllib.request import urlopen
import os

# Create the main window
strtwin = Tk()
w = 500
h = 340
sw = strtwin.winfo_screenwidth()
sh = strtwin.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
strtwin.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
strtwin.title("Translator")
strtwin.iconbitmap("translation.ico")
strtwin.configure(bg="lightyellow2")
label1 = Label(strtwin, text="Pick your Translator", font="Helvetica 20",)
label1.pack(pady=90)

# Function to show the main window
def show():
    strtwin.deiconify()

# Function to hide the main window
def hide():
    strtwin.withdraw()

# Function to create the Morse Code Translator window
def new():
    top = Toplevel()
    top.iconbitmap("translation.ico")
    top.title('Morse Code Translator!!')
    variable1 = StringVar(top)
    variable2 = StringVar(top)

    variable1.set("lang-code")
    variable2.set("lang-code")

    # Morse Code Dictionary
    DICTIONARY = {
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
        'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
        'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', 
        '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', 
        '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'
    }

    # Function to clear both text fields
    def clearAll():
        language1_field.delete(1.0, END)
        language2_field.delete(1.0, END)

    # Function to convert between Morse code and English
    def convert():
        language2_field.delete(1.0, END)
        message = language1_field.get("1.0", "end")[:-1].upper()

        if variable1.get() == variable2.get():
            messagebox.showerror("Error", "Can't Be Same Language")
            return
        elif variable1.get() == "Eng" and variable2.get() == "Morse":
            rslt = encrypt(message)
        elif variable1.get() == "Morse" and variable2.get() == "Eng":
            rslt = decrypt(message)
        else:
            messagebox.showerror("Error", "Please choose valid language code.")
            return

        language2_field.insert('end -1 chars', rslt)

    # Function to encrypt English text to Morse code
    def encrypt(message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += DICTIONARY[letter] + ' '
            else:
                cipher += ' '
        return cipher

    # Function to decrypt Morse code to English text
    def decrypt(message):
        message += ' '
        decipher = ''
        citext = ''
        for letter in message:
            if letter != ' ':
                citext += letter
            else:
                i = 0
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(DICTIONARY.keys())[list(DICTIONARY.values()).index(citext)]
                    citext = ''
        return decipher

    top.configure(background='light green')
    w = 400
    h = 500
    sw = top.winfo_screenwidth()
    sh = top.winfo_screenheight()
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)
    top.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

    # Create text fields for input and output
    language1_field = Text(top, height=5, width=25, font="Arial 20")
    language2_field = Text(top, height=5, width=25, font="Arial 20")
    language1_field.grid(row=1, column=1, padx=10)
    language2_field.grid(row=5, column=1, padx=10)

    languageCode_list = ["Eng", "Morse"]
    FromLanguage_option = OptionMenu(top, variable1, *languageCode_list)
    ToLanguage_option = OptionMenu(top, variable2, *languageCode_list)
    FromLanguage_option.grid(row=2, column=1, ipadx=10)
    ToLanguage_option.grid(row=4, column=1, ipadx=10)

    button1 = Button(top, text="Convert", bg="red", fg="white", command=convert)
    button1.grid(row=3, column=1)

    button2 = Button(top, text="Clear", bg="red", fg="white", command=clearAll)
    button2.grid(row=6, column=1)

    # Function to display the Morse code lookup window
    def lookup():
        global lookup
        lw = Toplevel()
        lw.title('Morse Code LookUp')
        lw.iconbitmap("translation.ico")
        w = 600
        h = 650
        sw = lw.winfo_screenwidth()
        sh = lw.winfo_screenheight()
        x = (sw/2) - (w/2)
        y = (sh/2) - (h/2)
        lw.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
        
        # Load and display the Morse code chart image
        imageUrl = "https://hackster.imgix.net/uploads/attachments/1013017/morse-table_1eZbJKMS4t.jpg?auto=compress%2Cformat&w=1280&h=960&fit=max"
        u = urlopen(imageUrl)
        raw_data = u.read()
        u.close()
        photo = ImageTk.PhotoImage(data=raw_data)
        label = Label(lw, image=photo)
        label.image = photo
        label.pack()

        def destroy():
            lw.destroy()

        button_quit = Button(lw, text='Close', command=lambda: [showtop(), destroy()], width=30, bg="Red", fg="white").pack()

    button = Button(top, text='Morse Code Lookup', command=lambda: [hide(), lookup()])
    button.grid(row=7, column=1)

    def destroy():
        top.destroy()

    button_quit = Button(top, text='Close', command=lambda: [show(), destroy()])
    button_quit.grid(row=8, column=1)

# Function to create the Language Translator window
def engtrans():
    root = Toplevel()
    root.iconbitmap("translation.ico")
    root.title("Language Translator")
    root.configure(bg="lightcyan2")
    w = 1200
    h = 500
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)
    root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

    # Function to perform the translation
    def translate():
        output_text.delete(1.0, END)
        try:
            translator = Translator()

            # Get language codes from user selections
            from_language_key = [key for key, value in languages.items() if value == originalcombo.get()][0]
            to_language_key = [key for key, value in languages.items() if value == translatedcombo.get()][0]

            words = input_text.get(1.0, END)
            translation = translator.translate(words, src=from_language_key, dest=to_language_key)
            output_text.insert(1.0, translation.text)

        except Exception as e:
            messagebox.showerror("Translator", str(e))

    # Function to clear text fields
    def clear():
        input_text.delete(1.0, END)
        output_text.delete(1.0, END)

    languages = LANGUAGES
    language_list = list(languages.values())

    # Create text fields for input and output
    input_text = Text(root, height=10, width=40, font="calibre 15")
    input_text.grid(row=0, column=0, pady=20, padx=10)

    translatebutton = Button(root, text="Translate", font=("Helvetica", 24), command=translate)
    translatebutton.grid(row=0, column=1, padx=10)

    output_text = Text(root, height=10, width=40, font="calibre 15")
    output_text.grid(row=0, column=2, pady=20, padx=10)

    # Combo boxes for selecting languages
    originalcombo = ttk.Combobox(root, width=50, value=language_list)
    originalcombo.current(21)  # Default language is English
    originalcombo.grid(row=2, column=0)

    translatedcombo = ttk.Combobox(root, width=50, value=language_list)
    translatedcombo.current(26)  # Default language is Spanish
    translatedcombo.grid(row=2, column=2)

    clearb = Button(root, text="Clear", width=20, command=clear)
    clearb.grid(row=3, column=1)

    def destroy():
        root.destroy()

    button_quit = Button(root, text='Close', bg="red", fg="white", width=20, command=lambda: [show(), destroy()])
    button_quit.grid(row=4, column=1)

# Create the main window buttons
myframe = Frame(strtwin)
myframe.pack()

b1 = Button(myframe, text="Language Translator", bg="royalblue1", command=lambda: [hide(), engtrans()])
b1.grid(row=0, column=1)

b2 = Button(myframe, text="Cypher Translator", bg="sandybrown", command=lambda: [hide(), new()])
b2.grid(row=0, column=2)

strtwin.mainloop()
