#invoer
d_vrachtwagens = float(input('geef d van vrachtwagens: '))
v_vrachtwagens = float(input('geef v van vrachtwagens: '))
d_auto = float(input('geef d van auto: '))
v_auto = float(input('geef v van auto: '))

#berekenen
p_file_vrachtwagens = min((d_vrachtwagens * v_vrachtwagens) / 40, 1)
p_file_auto = min((d_auto * v_auto)/ 40, 1)
minumum_pv_pa = min(p_file_auto, p_file_vrachtwagens)
maximum_pv_pa = max(p_file_auto, p_file_vrachtwagens)
verschil_pv_pa = abs(p_file_vrachtwagens - p_file_auto)

#kleuren
if minumum_pv_pa > 0.7:
    print('zwart')
elif maximum_pv_pa > 0.7 and verschil_pv_pa < 0.2:
    print('rood')
elif verschil_pv_pa > 0.7:
    print('geel')
else:
    print('groen')