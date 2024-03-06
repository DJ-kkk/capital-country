from tkinter import *
import random


root=Tk()
root.title("Country Capitals")
root.geometrey("1400x1400")

enter_country = Entry(root)
enter_country.pack()

enter_capital = Entry(root)
enter_capital.pack()

display_country_list = Label(root)
display_capital_list = Label(root)

display_random_capital_list = Label(root)
display_random_country_list = Label(root)

capital_list = []
country_list = []

def random_country:
    length = len(list1)
    random_country = random.randint(0, length-1)
    random_capital_label["text"] = str(random_no)
    generated_random_country = list1[random_no]
    lucky_friend["text"] = "your lucky country is " + str(generated_random_number)

root.mainloop()