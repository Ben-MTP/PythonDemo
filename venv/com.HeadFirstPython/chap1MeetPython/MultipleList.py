movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]];

each_item_i = "";
each_item = "";
#print(movies)
for each_item in movies:
    #print(isinstance(each_item, list));
    if(isinstance(each_item, list)):
        print("----value of list in LIST----")
        for each_item_i in each_item:
            print(each_item_i);
#Check list in list:
"""
names = ['ManhKM', 'TrangTT'];
print(isinstance(names, list));
"""

