# Lists are like arrays
# List in list:
#
#
#
#
#

print("Create simple Python lists");
cast = ["Cleese", 'Palin', 'Jones', "Idle"];
cast.append("ManhKM");
cast.append("ThangLV");
cast.append(["dsad", "eeee", "eeeeeeeeewewewe"]);
print(cast[6][1]);

mattrix = [[1,2,4,5,6,7,8,9], [33,22,33,44,55,66,77,65]];
for tempmattrix in mattrix:
    print(tempmattrix);

print(len(cast))