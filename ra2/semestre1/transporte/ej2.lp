\* ej2 *\
Minimize
z: 210 xC1C2 + 190 xC2C1 + 200 xac + 180 xad + 160 xba + 150 xbc + 140 xbd
 + 150 xbe + 160 xcC2 + 130 xcd + 120 xce + 150 xdC1 + 180 xdC2 + 140 xde
 + 180 xeC1 + 170 xeC2 + 140 xed + 260 xp1a + 250 xp1b + 280 xp1c + 280 xp2a
 + 290 xp2b + 260 xp2c
Subject To
a: xac + xad - xba - xp1a - xp2a = 0
b: xba + xbc + xbd + xbe - xp1b - xp2b = 0
c: - xac - xbc + xcC2 + xcd + xce - xp1c - xp2c = 0
c1: xC1C2 - xC2C1 - xdC1 - xeC1 = -3150
c2: - xC1C2 + xC2C1 - xcC2 - xdC2 - xeC2 = -3600
d: - xad - xbd - xcd + xdC1 + xdC2 + xde - xed = 0
e: - xbe - xce - xde + xeC1 + xeC2 + xed = 0
pr1: xp1a + xp1b + xp1c = 3500
pr2: xp2a + xp2b + xp2c = 3250
Bounds
 0 <= xC1C2
 0 <= xC2C1
 0 <= xac
 0 <= xad
 0 <= xba
 0 <= xbc
 0 <= xbd
 0 <= xbe
 0 <= xcC2
 0 <= xcd
 0 <= xce
 0 <= xdC1
 0 <= xdC2
 0 <= xde
 0 <= xeC1
 0 <= xeC2
 0 <= xed
 0 <= xp1a
 0 <= xp1b
 0 <= xp1c
 0 <= xp2a
 0 <= xp2b
 0 <= xp2c
Generals
xC1C2
xC2C1
xac
xad
xba
xbc
xbd
xbe
xcC2
xcd
xce
xdC1
xdC2
xde
xeC1
xeC2
xed
xp1a
xp1b
xp1c
xp2a
xp2b
xp2c
End
