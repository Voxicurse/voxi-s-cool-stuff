import tkinter as tk
import random

#This is a simple program, which converts inputted text into freaky ahh text
#Example: Hello World -> H-hello... world..~

root = tk.Tk()
root.title("Freaky text generator")

#Pretty much the entire program is in this function
def submit_button_clicked():
    #Some stuff related to getting text from input box and shit
    text = text_input.get()
    words = text.split()
    converted_words = []
    #Check every word in the list and edit it randomly
    for word in words:
        if random.choice([True, False]):
            word = f"{word[0]}-{word.lower()}"
        if random.choice([True, False, False]):
            word += random.choice(["...", "..", "."])
        if random.choice([True, False, False]):
            word += random.choice(["~", "~~"])
        #Append the modified word to the converted_words list
        converted_words.append(word)
    #Joins all words from converted_wrods list into one string var
    text_output.delete(0, tk.END)
    text_output.insert(0, " ".join(converted_words))

    print(words, text, converted_words) #Testing if that shit works properly, you can remove it if you want

#Some graphics and stuff, no idea honestly why tf you reading allat bro if you do
#-------------------------------------------------------------------------
author_label = tk.Label(
    root,
    text="Voxicurse's\nCool stuff",
    font=("Arial", 20)
)
author_label.pack()

filler_frame = tk.Frame(root)
filler_frame.pack(pady=10)

input_label = tk.Label(
    root,
    text="Your text here:",
    font=("Arial", 15)
)
input_label.pack()

text_input = tk.Entry(
    root,
    width=30,
    font=("Arial", 20),
    justify="center"
)
text_input.pack(pady=10)

output_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 15)
)
output_label.pack()

text_output = tk.Entry(
    root,
    width=30,
    font=("Arial", 20),
    justify="center"
)
text_output.pack(pady=10)

submit_button = tk.Button(
    root,
    text="Convert",
    font=("Arial", 20),
    command=submit_button_clicked
)
submit_button.pack()
#--------------------------------------------------------------------------

#Starts the GUI shit or whatever
root.mainloop()