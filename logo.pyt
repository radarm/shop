import turtle               
window = turtle.Screen()        
alex = turtle.Turtle()     

def rajz(szogek_szama,hossz,szin):
    hossz = 60
    alex.color(szin)
    for i in range(szogek_szama):
        alex.forward(hossz)           
        alex.left(360/szogek_szama)
    
rajz(3, 70, 'lime')
rajz(4, 100, 'cyan')
rajz(5, 120, 'blue')
