class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"];
    all = [];

    def __init__(self, nm, tp, ownr=None):
        self.name = nm;
        self.setType(tp);
        self.owner = ownr;
        self.all.append(self);
    
    def getType(self): return self._pet_type;

    def setType(self, val):
        throwerror = False;
        if (val == None): throwerror = True;
        elif (val in self.PET_TYPES): self._pet_type = val;
        else: throwerror = True;
        if (throwerror): raise Exception("the pet type must be on the list of valid pet types!");

    pet_type = property(getType, setType);

class Owner:
    def __init__(self, nm):
        self.name = nm;
        self.mpets = self.pets();

    def add_pet(self, pt):
        if (isinstance(pt, Pet)):
            pt.owner = self;
            self.mpets.append(pt);
        else: raise Exception("the pet must be a PET!");

    def pets(self): return [pt for pt in Pet.all if (pt.owner == self)];

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pt: pt.name);
