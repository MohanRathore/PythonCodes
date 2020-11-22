class Dad:
    basketball = 1
    pass

class Son(Dad):
    dance = 1
    def isDance(self):
        return f"yes i dance {self.dance} number of time"
    pass

class GrandSon(Son):    #method overrideing of isDance fuction
    dance = 6
    basketball = 11
    def isDance(self):
        return f"yes i dance mast  {self.dance} number of time"

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.isDance())
print(harry.basketball)