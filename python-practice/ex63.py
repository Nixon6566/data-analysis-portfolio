'''Loop through the List from exercise 2 and print out the full
information of even items in the List (ie the 2nd and 4th List in your
multidimensional List). '''

names = [["Darla", "2020 West Pine", "314.381.1212", "40 Years"], ["Jeanetta", "4035 Shreve Ave", "636.328.3495", "45 years"], ["Chris", "4035 Shreve Ave", "636.328.3497", "67 Years"] , ["Edna", "101 ridge Lane", "000.231.6549", "50 Years"] ]
for person in names[1::2]:
    print(f"Name: {person[0]} | Address: {person[1]} | Phone: {person[2]} | Age: {person[3]}")



