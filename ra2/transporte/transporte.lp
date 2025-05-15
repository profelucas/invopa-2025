\* transporte *\
Minimize
ct: 185 xc1c2 + 170 xc2c1 + 260 xf1t1 + 250 xf1t2 + 280 xf2t1 + 290 xf2t2
 + 255 xt1c1 + 249 xt1c2 + 267 xt2c1 + 270 xt2c2 + 160 xt2t1
Subject To
c1: xc1c2 - xc2c1 - xt1c1 - xt2c1 = -1250
c2: - xc1c2 + xc2c1 - xt1c2 - xt2c2 = -1380
f1: xf1t1 + xf1t2 = 1450
f2: xf2t1 + xf2t2 = 1180
t1: - xf1t1 - xf2t1 + xt1c1 + xt1c2 - xt2t1 = 0
t2: - xf1t2 - xf2t2 + xt2c1 + xt2c2 + xt2t1 = 0
Bounds
 0 <= xc1c2
 0 <= xc2c1
 0 <= xf1t1
 0 <= xf1t2
 0 <= xf2t1
 0 <= xf2t2
 0 <= xt1c1
 0 <= xt1c2
 0 <= xt2c1
 0 <= xt2c2
 0 <= xt2t1
Generals
xc1c2
xc2c1
xf1t1
xf1t2
xf2t1
xf2t2
xt1c1
xt1c2
xt2c1
xt2c2
xt2t1
End
