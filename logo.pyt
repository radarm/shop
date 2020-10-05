import turtle               
window = turtle.Screen()        
alex = turtle.Turtle()     

def rajz(szogek_szama,hossz,szin):
    hossz = 8
    alex.color(szin)
    for i in range(szogek_szama):
        alex.forward(hossz)           
        alex.left(360/szogek_szama)
    
rajz(70, 70, 'red')
rajz(60, 100, 'orange')
rajz(50, 120, 'yellow')
rajz(40, 140, 'green')
rajz(30, 160, 'blue')
rajz( 20, 180, 'purple')
