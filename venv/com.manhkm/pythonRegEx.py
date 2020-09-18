# Python RegEx:
# using funtion: search -> what is format:
# using funtion: search -> what is format: | findall | search | split | sub.
# search()
# findall()
# split() -> return string split from string:
# sub() -> replace string from string:
# ------------------------------------
# Doc ve cach su dung cac toan tu Regex trong khi su ly du lieu:
# https://www.w3schools.com/python/python_regex.asp
import  re;

valRoot = "Hom nay troi khong mua";
valResult = re.findall("[H-m]", valRoot);       # function findall: return character true:
print(valResult);
