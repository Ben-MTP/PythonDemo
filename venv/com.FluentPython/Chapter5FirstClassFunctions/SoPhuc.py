class SoPhuc:

    def __init__(self, r=0, i=0):
        self.phanthuc   = r;
        self.phanao     = i;

    def getData(self):
        print("{}+{}j".format(self.phanthuc, self.phanao))

#---------------
c1 = SoPhuc(2,3);
c1.getData();