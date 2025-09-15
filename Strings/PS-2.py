
letter = """Dear <name>
You are selected 
<date>"""


print(letter.replace("<name>","Tarang").replace("<date","12/10/2007"))

#or 

a = input("Enter your Name: ")
b = input("Enter the date : ")

print(f"\" Dear {a}\nYou are selected!!\n{b}\" ")