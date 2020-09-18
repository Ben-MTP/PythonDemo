class MyClass:
    "Đây là class thứ 2 được khởi tạo"
    a = 10

    def __int__(self, a = 1, b = 1, c = 1):
        self.numbera = a;
        self.numberb = b;
        self.numberc = c;

    def showInfo(self):
        print("{} +' - '+ {} +' - '+ {}".format(self.a, self.b, self.c));


myClass = MyClass(1,2,3);
print(myClass.a);
myClass.showInfo();