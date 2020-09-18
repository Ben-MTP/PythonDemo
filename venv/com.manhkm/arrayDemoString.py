arrName = ["ManhKM", 'ThangLV', 'AnhLD', "NEO Company"];
strIntroduction = "";
intIndex = 0;
for x in arrName:
    strIntroduction = strIntroduction + " - " + arrName[intIndex];
    intIndex = intIndex + 1;

print(strIntroduction);