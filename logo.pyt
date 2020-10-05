import turtle               
window = turtle.Screen()        
alex = turtle.Turtle()     

def rajz(szogek_szama,hossz,szin):
    alex.color(szin)
    for i in range(szogek_szama):
        alex.forward(hossz)           
        alex.left(360/szogek_szama)
    
rajz(70, 9, 'red')
rajz(60, 8, 'orange')
rajz(50, 7, 'yellow')
rajz(40, 6, 'green')
rajz(30, 5, 'blue')
rajz( 20, 4, 'purple')
