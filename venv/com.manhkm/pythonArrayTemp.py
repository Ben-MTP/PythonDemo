movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"];

lengOfArray = len(movies);
# print(movies.index(x));
#
#
for x in movies:
    valIndex = (movies.index(x) % 2)
    if (valIndex == 0):
        movies.insert(valIndex + 1, 12);

print(movies)

# count number of item in Array:
#print(len(movies));

# add item in Array:
#movies.append("Co be ban diem");
#print(movies);

# function pop() -> delete the end:
#print(movies.pop());
#print(movies);

# function extend(sb, sb);
#movies.extend(["ManhKM", "ThangLV"]);
#print(movies);

# function remove(): remove(item):
#movies.remove("ManhKM");
#print(movies);
