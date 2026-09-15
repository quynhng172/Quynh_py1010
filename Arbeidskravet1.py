# -*- coding: utf-8 -*-
"""
Arbeidskravet 1

Quynh.Thao.Nguyen
"""

km_per_år = 10000
# Deklarere kostnader for Elbin
elbil_forsikring = 5000
elbil_traffikkforsikring = 8.38 * 365
elbil_drivforbruk = km_per_år * 0.2* 2
elbil_bom = km_per_år* 0.1

#Beregn total kostnader for elbil
elbil_total = elbil_forsikring + elbil_traffikkforsikring + elbil_drivforbruk + elbil_bom

# Deklarere kostnader for bensinbil
bensin_forsikring = 7500
bensin_trafikkforsikring = 8.38 *365
bensin_drivforbruk = km_per_år * 1
bensin_bom = km_per_år* 0.3

#Beregn total kostnader for bensinbil
bensin_total = bensin_forsikring+ bensin_trafikkforsikring + bensin_drivforbruk + bensin_bom

print ('Årlige totalkosnadene for elbil er :', elbil_total,' kr/år')
print ('Årlige totalkosnadene for bensinbil er :',bensin_total,' kr/år')

# Beregn Kostnadsdifferanse mellom elbin og bensinbil 
print ('Kostnadsdifferanse mellom elbin og bensinbil er:',elbil_total - bensin_total, 'kr /år' )