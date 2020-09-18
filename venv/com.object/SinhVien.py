class SinhVien:
    # Khai bao kieu tuong trung: Object: sv, attribution: ma, ten -> number, name
    def __init__ (sv, ma, ten):
        sv.number = ma;
        sv.name = ten;

    def showInformation(sv):
        print("My name: \t" +sv.name);
        print("My number: \t" + sv.number);

myName = input("Enter your Name: ");
myNumber = input("Enter your number: ");
sinhviena = SinhVien(myNumber, myName);
sinhviena.showInformation();