import turtle               
window = turtle.Screen()        
alex = turtle.Turtle()     

def rajz(szogek_szama,hossz, szin):
    hossz = 50
    alex.color(szin)
    for i in range(szogek_szama):
        alex.forward(hossz)           
        alex.left(360/szogek_szama)
    
rajz(3, 70 'cyan')
rajz(3, 100 'lime')
rajz(3, 120 'blue') 
