#This is super easy programer for Beginners to start 
#you git clone this and develop it from here...

class Madlibs:
    def __init__(self,noun,verb,verb2, adj) -> None:
        self.noun = noun
        self.verb = verb
        self.verb2= verb2
        self.adj = adj

    def __repr__(self):
        return f"""

        Blood is a >{self.noun} >{self.verb} in the circulatory system of humans and other vertebrates that delivers necessary substances such as nutrients and oxygen to the cells,
        and transports metabolic waste products away from those same cells. lood in the circulatory system is also known as peripheral blood, and the blood cells it carries,
        peripheral blood cells.
        Blood is >{self.adj} of blood cells suspended in blood plasma. Plasma, which constitutes 55% of blood fluid,
        is mostly water (92% by volume) and contains proteins, glucose, mineral ions, hormones, carbon dioxide (plasma being the main medium for excretory product transportation),
        and blood cells themselves. Albumin is the main protein in plasma, and it functions to regulate the colloidal osmotic pressure of blood.The blood cells are mainly red blood cells
        (also called RBCs or erythrocytes), white blood cells (also called WBCs or leukocytes), and in mammals platelets (also called thrombocytes) The most abundant cells in vertebrate blood are red blood cells. hese contain hemoglobin,
        an iron-containing protein, which >{self.verb2} oxygen transport by reversibly binding to this respiratory gas thereby increasing its solubility in blood. n contrast,
        carbon dioxide is mostly transported extracellularly as bicarbonate ion transported in plasma. 
        """

def main():
    noun = input("Enter Noun: ")
    verb = input("Enter Verb: ")
    verb2 =  input("Enter Verb2: ")
    adj = input("Enrer adjectives: ")

    #Print the Class
    test = Madlibs(noun,verb,verb2,adj)
    print(test)


if __name__ == '__main__':
    main()


#Inspeard by  12 Beginner Python Projects - Coding Course 
# Link for the video (https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org)