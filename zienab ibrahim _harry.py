
#parent class
class wizard:
    def __init__ (self,health,energy)
    self.health=health
    self.energy=energy


#child class
class harry(wizard) :
    HarrySpells= {"Avadakedavra":100 ,"Crucio":40,"Imperio":20,"Sheild":0 ,"Reductu":60 , "Friendfyre":50 , "Nebulus":40 }

    def HarrydecEnergy(self):
        self.energy -=HarrySpells[HSpell]

#child class
class voldmort(wizard) :
    VoldmortSpells={"Avadakedavra":100 ,"Crucio":40,"Imperio":20,"Sheild":0 ,"Taboo": 80 ,"Expulso" : 60 ,"confringo":55}



    def VoldmorddecEnergy(self):
        self.energy -=VoldmortSpells[VSpell]




Harry=harry(100,500)           #create opject
Voldmort=voldmort(100,500)      #create opject



while Harry.health !=0 and Voldmort.health !=0

    print("Enter the two spells(harry than voldmort):")

    Hspell,Vspell=input().split()

    print("\t\t\t\t\tHarry\t\t\t\t\tVoldmort")










if harry_health=0:
    print("Voldmort is the winner")

if voldmort_health =0:
    print("harryis the winner")










