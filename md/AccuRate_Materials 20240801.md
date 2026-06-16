

# **Material Properties Used in NatHERS Software Tools** 

Dong Chen 

## CSIRO Energy 

April 2012 (updated in May 2022, updated in July 2024) 

This document lists the material properties used in NatHERS software tools. It is documented in accordance with AccuRate help file. The properties for the following material groups are listed in this document: 

Normal materials Insulation (bulk) materials Air gaps, vertical, unventilated Air gaps, vertical, ventilated Air gaps, horizontal, unventilated Air gaps, horizontal, ventilated Air gaps inclined 45°, unventilated Air gaps inclined 45°, ventilated Air gaps inclined 22.5°, unventilated Air gaps inclined 22.5°, ventilated Air gaps, other 

## **Important Disclaimer** 

While all due care and attention has been taken to establish the accuracy of the material presented, CSIRO and the author disclaim liability for any loss which may arise from any person acting in reliance upon the contents of this document. 


## **Overview** 

In what follows, 'materials' includes air gaps. 

All materials used in AccuRate are fully described by a thermal resistance (or resistances for non-vertical air gaps - see below) and a thermal capacitance. The values used are listed in various tables according to the material type. 

The units of thermal resistance are m².K/W. 

The thermal capacitance is the product of the density and specific heat, and its units in the material tables are kJ/m³.K (note the use of kJ, not J). 

Except for non-vertical air gaps, the thermal resistance and capacitance do not change during the simulation. 

Non-vertical air gaps (i.e. Horizontal, Inclined 45°, and Inclined 22.5°) are characterised by _**two**_ thermal resistances: one for heat flow up and one for heat flow down. At each time step in the simulation, the heat flow direction in these air gaps is determined and the appropriate value of the thermal resistance is used. The up and down values are fixed (i.e. they do not change according to the temperature difference or other factors). 

Air gap properties are given for fixed ranges of thicknesses, emissivities and inclinations. Choose the closest match to the air gap required (e.g. choose the thickness closest to one of the available thicknesses). With respect to emissivities, the key parameter is the effective emissivity, E, rather than the individual surface emissivities, and emissivity matching should be based on E. If the two surfaces have emissivities e1 and e2, then the effective emissivity is calculated as: 


## _**Air gaps with thicknesses below 13 mm**_ 

For an air gap with a thickness of less than 13 mm, a single thermal resistance that does not depend on heat flow direction may be estimated as follows. Let 

L = thickness of air gap (mm) tm = mean temperature of air gap (°C) 

R = resistance of air gap (m².K/W) 

## Then 


For example, if L = 5 mm, tm = 20°C and E = 0.82, then R = 0.108 m².K/W. 

This air gap can then be used in a construction as follows. 

1. Calculate R as above. 

2. Calculate an _effective_ thickness (mm) as Leff = 100*R. 

3. To represent this air gap, select the material Generic resistance (k = 0.1) from the materials list. 

4. Enter the thickness for this material as Leff . 


Properties of the following material groups are listed in this document: 

Normal materials Insulation (bulk) materials Air gaps, vertical, unventilated Air gaps, vertical, ventilated Air gaps, horizontal, unventilated Air gaps, horizontal, ventilated Air gaps inclined 45°, unventilated Air gaps inclined 45°, ventilated Air gaps inclined 22.5°, unventilated Air gaps inclined 22.5°, ventilated Air gaps, other 


## **Normal materials** 

The following table lists the material properties of all the 'normal' materials (i.e. materials other than bulk insulation and air gaps) available from the Material Selector, which is accessed via the button in the Constructions page, details section. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the 'Resistance (heat flow down)' column indicates that the resistance for heat flow down is the same as for heat flow up. 

## **Normal materials** 

|Name|**Thickness**<br>**required**|<br>**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|<br>**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Aerated autoclaved concrete block|Y|7.700||525.0|
|Aluminium|Y|0.005||2358.4|
|Bituminous roof membrane|Y|6.250||1646.4|
|Bottom Ash|Y|3.360||964.0|
|Brickwork:extruded brick(generic)|Y|1.630||1484.9|
|Brickwork: pressed brick (generic)|Y|1.110||1929.2|
|BST lightweight concrete|Y|3.333||1128.0|
|Carpet|Y|17.600||147.7|
|Carpet underlay (felt)|Y|25.000||147.7|
|Carpet underlay (rubber)|Y|12.500||470.9|
|Carpet 10 + felt underlay 10|Y|21.300||147.7|
|Carpet10 +rubberunderlay 8|Y|15.330||279.2|
|Ceramic tile|Y|0.880||1600.0|
|'Concrete block 190 denseweight (not core-filled)'|Y|0.963||968.9|
|'Concrete block 190 denseweight (core-filled at 1500 centres)'|Y|0.942||1052.5|
|'Concrete block 190 denseweight (fully core-filled)'|Y|0.795||1970.3|
|'Concrete block 190lightweight (not core-filled)'|Y|1.211||799.9|
|'Concrete block 190 lightweight (core-filled at 1500 centres)'|Y|1.226||883.5|
|'Concrete block 190 lightweight (fully core-filled)'|Y|1.002||1802.2|
|'Concrete block 140 denseweight (not core-filled)'|Y|1.150||1096.5|
|'Concrete block 140 denseweight (core-filled at 1500 centres)'|Y|1.093||1167.8|
|'Concrete block 140 denseweight (fully core-filled)'|Y|0.799||1963.3|
|'Concrete block 140 lightweight (not core-filled)'|Y|1.493||905.5|
|'Concrete block 140lightweight (core-filled at1500 centres)'|Y|1.471||976.8|
|'Concrete block 140 lightweight (fully core-filled)'|Y|1.024||1772.3|
|'Concrete block 110 denseweight (not core-filled)'|Y|1.273||1449.4|
|'Concrete block 110 denseweight (solid)'|Y|0.843||1918.4|
|'Concrete block 110 lightweight (not core-filled)'|Y|1.727||1196.8|
|'Concrete block 110lightweight (solid)'|Y|1.340||1584.0|
|'Concrete block 90 denseweight (not core-filled)'|Y|1.311||1449.4|
|'Concrete block 90 denseweight (solid)'|Y|0.843||1918.4|
|'Concrete block 90 lightweight (not core-filled)'|Y|1.867||1196.8|
|'Concrete block 90 lightweight (solid)'|Y|1.340||1584.0|
|Concrete:standard (2400kg/m³)|Y|0.690||2112.0|
|Conpolcrete|Y|12.800||329.0|
|Copper|Y|0.003||3516.0|
|Cork tile|Y|12.500||900.0|
|Felt (undercarpet)|Y|21.700||165.6|
|Fibre-cement sheet|Y|3.125||1251.6|
|Fibre-cement sheet (compressed)|Y|2.000||1680.0|
|Fibre reinforced concrete (k=0.28)|Y|3.571||1600|
|Generic resistance (k=0.1)|Y|10.000||8.8|
|Generic resistance (k=0.3)|Y|3.333||8.8|




## **Normal materials (continued)** 

|Name|**Thickness**<br>**required**|<br>**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|<br>**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Glass|Y|0.950||2108.4|
|Granite|Y|0.345||2385.0|
|Hempcrete block|Y|15.361||281|
|Hollowcore precast concrete panel 200|Y|0.850||1478.4|
|Hollowcore precast concrete panel 150|Y|0.893||1478.4|
|Lead|Y|0.029||1436.4|
|Light earth method (density: 650 kg/m³)|Y|5.56||640|
|Limestone|Y|1.075||2184.0|
|Linoleum|Y|4.545||1092.0|
|Low density COB/mudbrick (density: 1000 kg/m³)|Y|3.23||920|
|Lowdensityrammed earth(density: 1600kg/m³)|Y|1.69||1400|
|Magnesium Oxide Fiberglass Reinforced Board (k=0.12)|Y|8.333||1480|
|Marble|Y|0.667||2393.6|
|Masonite|Y|4.550||1716.9|
|Mud brick|Y|1.300||1500.0|
|Particleboard|Y|8.300||1280.0|
|Plaster (cement:sand 1:4)|Y|0.909||1590.0|
|Plasterboard|Y|5.900||924.0|
|Plywood|Y|7.140||795.0|
|Polycarbonate|Y|4.400||1380.0|
|Rammed earth|Y|0.800||1940.0|
|Reflective blind|N|0.001||0.0|
|Rooftiles (clay)|Y|1.190||1770.2|
|Roof tiles (concrete)|Y|0.690||2112.0|
|Sand (building)|Y|3.333||1200.0|
|Sandstone|Y|0.769||1840.0|
|Scoria|Y|2.950||1459.0|
|Slate|Y|0.667||1987.5|
|Softboard|Y|16.700||400.0|
|Soil (average)|Y|0.830||1613.0|
|Steel|Y|0.020||3900.0|
|Straw board|Y|12.350||336.0|
|Strawbalerendered|Y|10.100||125.0|
|Styrocon|Y|4.270||500.0|
|Timbercrete (solidlow-density:900kg/m³)|Y|4.274||663.3|
|Timbercrete (solid mid-density: 1000 kg/m³)|Y|3.185||850.0|
|Timbercrete (solid high-density: 1100 kg/m³)|Y|2.415||834.9|
|Timbercrete (hollow low-density:900kg/m³)|Y|3.760||544.0|
|Timbercrete (hollow mid-density: 1000 kg/m³)|Y|2.920||692.0|
|Timbercrete (hollow high-density: 1100kg/m³)|Y|2.320||684.0|
|Timber (softwood)|Y|10.000||1057.5|
|Timber (hardwood)|Y|6.250||1414.9|
|Timber (Jarrah)|Y|5.000||1801.6|
|Timber (Mountain ash)|Y|6.250||1414.9|
|Timber(Radiata pine)|Y|10.000||1057.5|
|Vinyl (floor tiles)|Y|1.270||1722.0|
|Water|Y|1.667||4192.0|
|Window film|N|0.001||0.0|




## **Insulation (bulk)** 

The following tables list the material properties of all the bulk insulation materials available from the Material Selector, which is accessed via the button in the Constructions page, details section. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Two types of bulk insulation are provided: 

- Specified resistance (as indicated in the name, e.g. R1.5) Use this if the resistance required corresponds to one of the resistances provided. The thickness cell in the Construction details table will show the thickness used, but will be disabled. 

- Specified thermal conductivity ( _k_ ) and (sometimes) density (as indicated in the name, e.g. k = 0.057, density = 7 kg/m³). 

   - Use this if the required  insulation resistance does not correspond to one of the  resistances provided. The thickness cell in the Construction details table will be enabled. The required thickness is calculated as follows. If the required resistance is _R_ (m².K/W) and the specified conductivity is _k_ (W/m.K), then the required thickness, in mm, is 1000* _k_ * _R_ . 

## **Bulk insulation** 

|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|175 mm waffle pod insulation|Y|25.641||5.4|
|225 mm waffle pod insulation|Y|25.641||5.4|
|300 mm waffle pod insulation|Y|25.641||5.4|
|375mm waffle podinsulation|Y|25.641||5.4|
|Cellular insulation (not including air gaps): R0.14|N|0.140||0.0|
|Cellulose fibre: loose fill (k=0.04)|Y|25.000||0.0|
|Cellulose fibre (loose fill): R1.0|Y|25.000||50.2|
|Cellulose fibre (loose fill): R1.5|Y|25.000||50.2|
|Cellulosefibre (loosefill): R2.0|Y|25.000||50.2|
|Cellulose fibre (loose fill): R2.5|Y|25.000||50.2|
|Cellulose fibre (loose fill): R3.0|Y|25.000||50.2|
|Cellulose fibre (loose fill): R3.5|Y|25.000||50.2|
|Cellulose fibre (loose fill): R4.0|Y|25.000||50.2|
|Cellulosefibre (loosefill): R4.5|Y|25.000||50.2|
|Cellulose fibre (loose fill): R5.0|Y|25.000||50.2|
|Cellulosefibre (loosefill): R5.5|Y|25.000||50.2|
|Cellulose fibre (loose fill): R6.0|Y|25.000||50.2|
|Cellulose fibre (loose fill): R6.5|Y|25.000||50.2|
|Cellulosefibre (loosefill): R7.0|Y|25.000||50.2|
|Glass fibre batt (k=0.057 density=7 kg/m3)|Y|17.544||6.2|
|Glassfibre batt (k =0.044density= 12 kg/m3)|Y|22.727||10.6|
|Glass fibre batt: R1.0|Y|22.727||10.6|
|Glass fibre batt: R1.5|Y|22.727||10.6|
|Glass fibre batt: R2.0|Y|22.727||10.6|
|Glass fibre batt: R2.5|Y|22.727||10.6|
|Glassfibre batt: R3.0|Y|22.727||10.6|
|Glass fibre batt: R3.5|Y|22.727||10.6|
|Glass fibre batt: R4.0|Y|22.727||10.6|
|Glass fibre batt: R4.5|Y|22.727||10.6|




|Glass fibre batt: R5.0|Y|22.727||10.6|
|---|---|---|---|---|
|Glass fibre batt: R5.5|Y|22.727||10.6|
|Glass fibre batt: R6.0|Y|22.727||10.6|
|Glassfibre batt: R6.5|Y|22.727||10.6|
|Glass fibre batt: R7.0|Y|22.727||10.6|
|High performance glass fibre batt (90mm): R2.5|Y|27.778||17.3|
|High performance glass fibre batt (90mm): R2.7|Y|30.0||29.0|
|Polyethylene foam (k=0.04)|Y|25.000||10.8|
|Polyesterorpolyester/woolblanket (k =0.063 density=8kg/m3)|Y|15.873||8.0|
|Polyester or polyester/wool blanket (k=0.045 density=16 kg/m3)|Y|22.222||16.0|
|Polyesterorpolyester/woolblanket: R1.0)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R1.5)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R2.0)|Y|22.222||16.0|
|Polyesterorpolyester/woolblanket: R2.5)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R3.0)|Y|22.222||16.0|
|Polyesterorpolyester/woolblanket: R3.5)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R4.0)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R4.5)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R5.0)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R5.5)|Y|22.222||16.0|
|Polyesterorpolyester/woolblanket: R6.0)|Y|22.222||16.0|
|Polyester or polyester/wool blanket: R6.5)|Y|22.222||16.0|
|Polyesterorpolyester/woolblanket: R7.0)|Y|22.222||16.0|




## **Bulk insulation (continued)** 

|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Polyisocyanurate (PIR) aged foam (K=0.022)|Y|45.455||53.7|
|Polystyrene expanded (k=0.039)|Y|25.641||5.4|
|Polystyrene expanded: R1.0|Y|25.641||5.4|
|Polystyrene expanded: R1.5|Y|25.641||5.4|
|Polystyrene expanded: R2.0|Y|25.641||5.4|
|Polystyrene expanded: R2.5|Y|25.641||5.4|
|Polystyrene expanded: R3.0|Y|25.641||5.4|
|Polystyrene expanded: R3.5|Y|25.641||5.4|
|Polystyrene expanded: R4.0|Y|25.641||5.4|
|Polystyrene expanded: R4.5|Y|25.641||5.4|
|Polystyrene expanded: R5.0|Y|25.641||5.4|
|Polystyrene expanded: R5.5|Y|25.641||5.4|
|Polystyrene expanded: R6.0|Y|25.641||5.4|
|Polystyrene expanded: R6.5|Y|25.641||5.4|
|Polystyrene expanded: R7.0|Y|25.641||5.4|
|Polystyrene extruded (k=0.028)|Y|35.714||10.9|
|Polystyrene extruded: R1.0|Y|35.714||10.9|
|Polystyrene extruded: R1.5|Y|35.714||10.9|
|Polystyrene extruded: R2.0|Y|35.714||10.9|
|Polystyrene extruded: R2.5|Y|35.714||10.9|
|Polystyrene extruded: R3.0|Y|35.714||10.9|
|Polystyrene extruded: R3.5|Y|35.714||10.9|
|Polystyrene extruded: R4.0|Y|35.714||10.9|
|Polystyrene extruded: R4.5|Y|35.714||10.9|
|Polystyrene extruded: R5.0|Y|35.714||10.9|
|Polystyrene extruded: R5.5|Y|35.714||10.9|
|Polystyrene extruded: R6.0|Y|35.714||10.9|
|Polystyrene extruded: R6.5|Y|35.714||10.9|
|Polystyrene extruded: R7.0|Y|35.714||10.9|
|Polyurethane rigid foamed aged (k=0.028)|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R1.0|Y|35.714||10.8|
|Polyurethanerigidfoamed aged: R1.5|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R2.0|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R2.5|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R3.0|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R3.5|Y|35.714||10.8|
|Polyurethanerigidfoamed aged: R4.0|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R4.5|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R5.0|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R5.5|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R6.0|Y|35.714||10.8|
|Polyurethanerigidfoamed aged: R6.5|Y|35.714||10.8|
|Polyurethane rigid foamed aged: R7.0|Y|35.714||10.8|
|Rockwool loosefill(k =0.04)|Y|25.000||58.9|
|Rockwool batt (k=0.033)|Y|30.303||29.4|
|Rockwool batt: R1.0|Y|30.303||29.4|
|Rockwool batt: R1.5|Y|30.303||29.4|
|Rockwool batt: R2.0|Y|30.303||29.4|
|Rockwoolbatt: R2.5|Y|30.303||29.4|
|Rockwool batt: R3.0|Y|30.303||29.4|
|Rockwool batt: R3.5|Y|30.303||29.4|
|Rockwool batt: R4.0|Y|30.303||29.4|
|Rockwool batt: R4.5|Y|30.303||29.4|
|Rockwoolbatt: R5.0|Y|30.303||29.4|
|Rockwool batt: R5.5|Y|30.303||29.4|
|Rockwool batt: R6.0|Y|30.303||29.4|
|Rockwool batt: R6.5|Y|30.303||29.4|
|Rockwool batt: R7.0|Y|30.303||29.4|
|Silica aerogel(k =0.014)|Y|71.400||142.5|
|Wool loose fill (k=0.08)|Y|12.500||14.4|
|Wool/polyesterbatt 80/20 (k =0.059 density=8kg/m3)|Y|16.949||9.6|
|Wool/polyester batt 80/20 (k=0.045 density=16 kg/m3)|Y|22.222||19.2|




|Wool/polyester batt 80/20: R1.0|Y|22.222||19.2|
|---|---|---|---|---|
|Wool/polyester batt 80/20: R1.5|Y|22.222||19.2|
|Wool/polyester batt 80/20: R2.0|Y|22.222||19.2|
|Wool/polyesterbatt 80/20: R2.5|Y|22.222||19.2|
|Wool/polyester batt 80/20: R3.0|Y|22.222||19.2|
|Wool/polyester batt 80/20: R3.5|Y|22.222||19.2|
|Wool/polyester batt 80/20: R4.0|Y|22.222||19.2|
|Wool/polyester batt 80/20: R4.5|Y|22.222||19.2|
|Wool/polyesterbatt 80/20: R5.0|Y|22.222||19.2|
|Wool/polyester batt 80/20: R5.5|Y|22.222||19.2|
|Wool/polyesterbatt 80/20: R6.0|Y|22.222||19.2|
|Wool/polyester batt 80/20: R6.5|Y|22.222||19.2|
|Wool/polyester batt 80/20: R7.0|Y|22.222||19.2|




## **Air gaps vertical, unventilated** 

The following table lists the material properties of all the vertical unventilated air gaps available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|respectively, and that the effective emissivity is 0.38.|||||
|---|---|---|---|---|
|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|Air gap vertical 90 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.161||0.0|
|Air gap vertical 90 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.213||0.0|
|Airgapvertical90mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.275||0.0|
|Air gap vertical 90 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.396||0.0|
|Air gap vertical 90 mm unventilated reflective (0.1/0.9; E=0.10)|N|0.511||0.0|
|Airgapvertical90mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.601||0.0|
|Air gap vertical 90 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.657||0.0|
|Airgapvertical90mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.685||0.0|
|Air gap vertical 40 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.163||0.0|
|Air gap vertical 40 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.216||0.0|
|Airgapvertical 40mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.280||0.0|
|Air gap vertical 40 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.406||0.0|
|Airgapvertical 40mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.529||0.0|
|Airgapvertical 40mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.625||0.0|
|Air gap vertical 40 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.686||0.0|
|Airgapvertical 40mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.716||0.0|
|Air gap vertical 20 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.161||0.0|
|Air gap vertical 20 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.212||0.0|
|Airgapvertical 20mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.274||0.0|
|Air gap vertical 20 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.394||0.0|
|Airgapvertical 20mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.508||0.0|
|Air gap vertical 20 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.596||0.0|
|Air gap vertical 20 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.652||0.0|
|Airgapvertical 20mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.679||0.0|
|Air gap vertical 13 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.147||0.0|
|Airgapvertical 13mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.189||0.0|
|Airgapvertical 13mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.237||0.0|
|Air gap vertical 13 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.321||0.0|
|Airgapvertical 13mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.393||0.0|
|Air gap vertical 13 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.444||0.0|
|Air gap vertical 13 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.474||0.0|
|Airgapvertical 13mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.488||0.0|




## **Air gaps vertical, ventilated** 

The following table lists the material properties of all the vertical ventilated air gaps available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Air gap vertical 90 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.131||0.0|
|Airgapvertical90mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.180||0.0|
|Airgapvertical90mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.237||0.0|
|Air gap vertical 90 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.350||0.0|
|Airgapvertical90mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.457||0.0|
|Air gap vertical 90 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.541||0.0|
|Air gap vertical 90 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.592||0.0|
|Airgapvertical90mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.619||0.0|
|Air gap vertical 40 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.133||0.0|
|Airgapvertical 40mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.182||0.0|
|Air gap vertical 40 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.242||0.0|
|Air gap vertical 40 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.358||0.0|
|Airgapvertical 40mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.473||0.0|
|Air gap vertical 40 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.562||0.0|
|Air gap vertical 40 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.619||0.0|
|Airgapvertical 40mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.647||0.0|
|Air gap vertical 20 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.131||0.0|
|Airgapvertical 20mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.179||0.0|
|Air gap vertical 20 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.236||0.0|
|Air gap vertical 20 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.348||0.0|
|Airgapvertical 20mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.454||0.0|
|Air gap vertical 20 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.536||0.0|
|Airgapvertical 20mm ventilatedreflective (0.05/0.05;E =0.03)|N|0.588||0.0|
|Airgapvertical 20mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.613||0.0|
|Air gap vertical 13 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.120||0.0|
|Airgapvertical 13mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.159||0.0|
|Air gap vertical 13 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.204||0.0|
|Air gap vertical 13 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.283||0.0|
|Airgapvertical 13mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.351||0.0|
|Air gap vertical 13 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.399||0.0|
|Airgapvertical 13mm ventilatedreflective (0.05/0.05;E =0.03)|N|0.427||0.0|
|Airgapvertical 13mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.441||0.0|




## **Air gaps horizontal, unventilated** 

The following table lists the material properties of all the horizontal unventilated air gaps available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Air gap horizontal 90 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.149|0.192|0.0|
|Airgaphorizontal90mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.192|0.271|0.0|
|Airgaphorizontal90mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.242|0.380|0.0|
|Air gap horizontal 90 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.330|0.656|0.0|
|Airgaphorizontal90mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.407|1.051|0.0|
|Air gap horizontal 90 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.461|1.514|0.0|
|Air gap horizontal 90 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.494|1.930|0.0|
|Airgaphorizontal90mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.509|2.190|0.0|
|Air gap horizontal 40 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.145|0.180|0.0|
|Airgaphorizontal 40mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.185|0.248|0.0|
|Air gap horizontal 40 mm unventilated reflective (0.4/0.9; E=0.38)|N|0.230|0.337|0.0|
|Air gap horizontal 40 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.309|0.537|0.0|
|Airgaphorizontal 40mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.376|0.775|0.0|
|Air gap horizontal 40 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.422|1.000|0.0|
|Air gap horizontal 40 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.449|1.166|0.0|
|Airgaphorizontal 40mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.461|1.257|0.0|
|Air gap horizontal 20 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.140|0.163|0.0|
|Airgaphorizontal 20mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.178|0.215|0.0|
|Air gap horizontal 20 mm unventilated reflective (0.4/0.9; E=0.38)|N|0.220|0.279|0.0|
|Air gap horizontal 20 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.291|0.404|0.0|
|Airgaphorizontal 20mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.349|0.526|0.0|
|Air gap horizontal 20 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.388|0.621|0.0|
|Airgaphorizontal 20mmunventilatedreflective (0.05/0.05;E =0.03)|N|0.411|0.682|0.0|
|Airgaphorizontal 20mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.523|0.711|0.0|
|Air gap horizontal 13 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.137|0.146|0.0|
|Airgaphorizontal 13mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.174|0.188|0.0|
|Air gap horizontal 13 mm unventilated reflective (0.4/0.9; E=0.38)|N|0.213|0.235|0.0|
|Air gap horizontal 13 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.278|0.318|0.0|
|Airgaphorizontal 13mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.331|0.389|0.0|
|Air gap horizontal 13 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.366|0.438|0.0|
|Airgaphorizontal 13mmunventilatedreflective (0.05/0.05;E =0.03)|N|0.387|0.467|0.0|
|Airgaphorizontal 13mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.396|0.481|0.0|




## **Air gaps horizontal, ventilated** 

The following table lists the material properties of all the horizontal ventilated air gaps available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Air gap horizontal 90 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.121|0.156|0.0|
|Airgaphorizontal90mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.162|0.228|0.0|
|Airgaphorizontal90mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.209|0.328|0.0|
|Air gap horizontal 90 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.291|0.579|0.0|
|Airgaphorizontal90mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.364|0.939|0.0|
|Air gap horizontal 90 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.415|1.362|0.0|
|Air gap horizontal 90 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.445|1.741|0.0|
|Airgaphorizontal90mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.460|1.978|0.0|
|Air gap horizontal 40 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.118|0.146|0.0|
|Airgaphorizontal 40mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.156|0.209|0.0|
|Air gap horizontal 40 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.198|0.291|0.0|
|Air gap horizontal 40 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.273|0.474|0.0|
|Airgaphorizontal 40mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.336|0.693|0.0|
|Air gap horizontal 40 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.380|0.899|0.0|
|Air gap horizontal 40 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.405|1.052|0.0|
|Airgaphorizontal 40mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.416|1.135|0.0|
|Air gap horizontal 20 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.114|0.133|0.0|
|Airgaphorizontal 20mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.150|0.181|0.0|
|Air gap horizontal 20 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.190|0.241|0.0|
|Air gap horizontal 20 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.257|0.357|0.0|
|Airgaphorizontal 20mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.312|0.470|0.0|
|Air gap horizontal 20 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.349|0.559|0.0|
|Airgaphorizontal 20mm ventilatedreflective (0.05/0.05;E =0.03)|N|0.371|0.615|0.0|
|Airgaphorizontal 20mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.472|0.642|0.0|
|Air gap horizontal 13 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.111|0.119|0.0|
|Airgaphorizontal 13mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.147|0.158|0.0|
|Air gap horizontal 13 mm ventilated reflective (0.4/0.9; E=0.38)|N|0.184|0.203|0.0|
|Air gap horizontal 13 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.245|0.281|0.0|
|Airgaphorizontal 13mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.296|0.348|0.0|
|Air gap horizontal 13 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.329|0.394|0.0|
|Airgaphorizontal 13mm ventilatedreflective (0.05/0.05;E =0.03)|N|0.349|0.421|0.0|
|Airgaphorizontal 13mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.358|0.435|0.0|




## **Air gaps inclined 45°, unventilated** 

The following table lists the material properties of all the unventilated air gaps inclined at 45 degrees available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|respectively, and that the effective emissivity is 0.38.|||||
|---|---|---|---|---|
|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|Air gap 45°90 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.154|0.171|0.0|
|Air gap 45°90 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.200|0.230|0.0|
|Airgap45°90mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.254|0.305|0.0|
|Air gap 45°90 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.354|0.461|0.0|
|Air gap 45°90 mm unventilated reflective (0.1/0.9; E=0.10)|N|0.443|0.626|0.0|
|Airgap45°90mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.509|0.766|0.0|
|Air gap 45°90 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.549|0.860|0.0|
|Airgap45°90mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.568|0.908|0.0|
|Air gap 45°40 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.151|0.173|0.0|
|Air gap 45°40 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.195|0.235|0.0|
|Airgap45° 40mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.247|0.313|0.0|
|Air gap 45°40 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.339|0.479|0.0|
|Airgap45° 40mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.421|0.660|0.0|
|Airgap45° 40mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.480|0.816|0.0|
|Air gap 45°40 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.515|0.923|0.0|
|Airgap45° 40mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.532|0.979|0.0|
|Air gap 45°20 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.150|0.162|0.0|
|Air gap 45°20 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.194|0.215|0.0|
|Airgap45° 20mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.245|0.278|0.0|
|Air gap 45°20 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.336|0.403|0.0|
|Airgap45° 20mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.416|0.523|0.0|
|Air gap 45°20 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.473|0.617|0.0|
|Air gap 45°20 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.507|0.677|0.0|
|Airgap45° 20mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.523|0.706|0.0|
|Air gap 45°13 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.144|0.146|0.0|
|Airgap45° 13mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.185|0.188|0.0|
|Airgap45° 13mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.230|0.234|0.0|
|Air gap 45°13 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.309|0.317|0.0|
|Airgap45° 13mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.375|0.387|0.0|
|Air gap 45°13 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.421|0.436|0.0|
|Air gap 45°13 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.448|0.465|0.0|
|Airgap45° 13mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.461|0.479|0.0|




## **Air gaps inclined 45°, ventilated** 

The following table lists the material properties of all the ventilated air gaps inclined at 45 degrees available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|respectively, and that the effective emissivity is 0.38.|||||
|---|---|---|---|---|
|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|Air gap 45°90 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.125|0.139|0.0|
|Air gap 45°90 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.169|0.194|0.0|
|Airgap45°90mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.219|0.263|0.0|
|Air gap 45°90 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.312|0.407|0.0|
|Air gap 45°90 mm ventilated reflective (0.1/0.9; E=0.10)|N|0.396|0.560|0.0|
|Airgap45°90mm ventilatedreflective (0.05/0.9;E =0.05)|N|0.458|0.689|0.0|
|Air gap 45°90 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.495|0.776|0.0|
|Airgap45°90mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.513|0.820|0.0|
|Air gap 45°40 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.123|0.141|0.0|
|Air gap 45°40 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.164|0.198|0.0|
|Airgap45° 40mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.213|0.270|0.0|
|Air gap 45°40 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.299|0.423|0.0|
|Airgap45° 40mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.376|0.590|0.0|
|Airgap45° 40mm ventilatedreflective (0.05/0.9;E =0.05)|N|0.432|0.734|0.0|
|Air gap 45°40 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.464|0.833|0.0|
|Airgap45° 40mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.481|0.884|0.0|
|Air gap 45°20 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.122|0.132|0.0|
|Air gap 45°20 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.163|0.181|0.0|
|Airgap45° 20mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.211|0.240|0.0|
|Air gap 45°20 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.297|0.356|0.0|
|Airgap45° 20mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.372|0.467|0.0|
|Air gap 45°20 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.425|0.555|0.0|
|Air gap 45°20 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.457|0.611|0.0|
|Airgap45° 20mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.472|0.638|0.0|
|Air gap 45°13 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.117|0.119|0.0|
|Airgap45° 13mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.156|0.158|0.0|
|Airgap45° 13mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.198|0.202|0.0|
|Air gap 45°13 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.273|0.280|0.0|
|Airgap45° 13mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.335|0.346|0.0|
|Air gap 45°13 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.379|0.392|0.0|
|Air gap 45°13 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.404|0.419|0.0|
|Airgap45° 13mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.416|0.433|0.0|




## **Air gaps inclined 22.5°, unventilated** 

The following table lists the material properties of all the unventilated air gaps inclined at 22.5 degrees available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|respectively, and that the effective emissivity is 0.38.|||||
|---|---|---|---|---|
|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|Air gap 22.5°90 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.152|0.182|0.0|
|Air gap 22.5°90 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.196|0.251|0.0|
|Airgap22.5°90mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.248|0.343|0.0|
|Air gap 22.5°90 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.342|0.559|0.0|
|Air gap 22.5°90 mm unventilated reflective (0.1/0.9; E=0.10)|N|0.425|0.839|0.0|
|Airgap22.5°90mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.485|1.140|0.0|
|Air gap 22.5°90 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.522|1.395|0.0|
|Airgap22.5°90mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.539|1.549|0.0|
|Air gap 22.5°40 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.148|0.177|0.0|
|Air gap 22.5°40 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.190|0.242|0.0|
|Airgap22.5° 40mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.239|0.325|0.0|
|Air gap 22.5°40 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.324|0.508|0.0|
|Airgap22.5° 40mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.399|0.718|0.0|
|Airgap22.5° 40mmunventilatedreflective (0.05/0.9;E =0.05)|N|0.451|0.908|0.0|
|Air gap 22.5°40 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.482|1.045|0.0|
|Airgap22.5° 40mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.497|1.118|0.0|
|Air gap 22.5°20 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.145|0.163|0.0|
|Air gap 22.5°20 mm unventilated reflective (0.6/0.9; E=0.56)|N|0.186|0.215|0.0|
|Airgap22.5° 20mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.233|0.279|0.0|
|Air gap 22.5°20 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.314|0.404|0.0|
|Airgap22.5° 20mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.383|0.525|0.0|
|Air gap 22.5°20 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.431|0.619|0.0|
|Air gap 22.5°20 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.459|0.680|0.0|
|Airgap22.5° 20mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.523|0.709|0.0|
|Air gap 22.5°13 mm unventilated non-reflective (0.9/0.9; E=0.82)|N|0.141|0.146|0.0|
|Airgap22.5° 13mmunventilatedreflective (0.6/0.9;E =0.56)|N|0.180|0.188|0.0|
|Airgap22.5° 13mmunventilatedreflective (0.4/0.9;E =0.38)|N|0.222|0.235|0.0|
|Air gap 22.5°13 mm unventilated reflective (0.2/0.9; E=0.20)|N|0.294|0.318|0.0|
|Airgap22.5° 13mmunventilatedreflective (0.1/0.9;E =0.10)|N|0.353|0.388|0.0|
|Air gap 22.5°13 mm unventilated reflective (0.05/0.9; E=0.05)|N|0.394|0.437|0.0|
|Air gap 22.5°13 mm unventilated reflective (0.05/0.05; E=0.03)|N|0.418|0.466|0.0|
|Airgap22.5° 13mmunventilatedreflective (0.03/0.03;E =0.015)|N|0.429|0.480|0.0|




## **Air gaps inclined 22.5°, ventilated** 

The following table lists the material properties of all the ventilated air gaps inclined at 22.5 degrees available from the Material Selector, which is accessed via the button in the Constructions page, details section. See Overview for air gaps below 13 mm thickness. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

Air gap names include the emissivities of the two surfaces and the effective emissivity. For example, (0.4/0.9, E = 0.38) indicates that the emissivities of the two surfaces are 0.4 and 0.9 respectively, and that the effective emissivity is 0.38. 

|respectively, and that the effective emissivity is 0.38.|||||
|---|---|---|---|---|
|Name|**Thickness**<br>**required**|**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|Air gap 22.5°90 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.123|0.148|0.0|
|Air gap 22.5°90 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.165|0.211|0.0|
|Airgap22.5°90mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.214|0.295|0.0|
|Air gap 22.5°90 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.302|0.493|0.0|
|Air gap 22.5°90 mm ventilated reflective (0.1/0.9; E=0.10)|N|0.380|0.750|0.0|
|Airgap22.5°90mm ventilatedreflective (0.05/0.9;E =0.05)|N|0.436|1.025|0.0|
|Air gap 22.5°90 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.470|1.258|0.0|
|Airgap22.5°90mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.486|1.399|0.0|
|Air gap 22.5°40 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.120|0.144|0.0|
|Air gap 22.5°40 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.160|0.204|0.0|
|Airgap22.5° 40mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.206|0.280|0.0|
|Air gap 22.5°40 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.286|0.448|0.0|
|Airgap22.5° 40mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.356|0.641|0.0|
|Airgap22.5° 40mm ventilatedreflective (0.05/0.9;E =0.05)|N|0.406|0.817|0.0|
|Air gap 22.5°40 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.435|0.942|0.0|
|Airgap22.5° 40mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.449|1.010|0.0|
|Air gap 22.5°20 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.118|0.132|0.0|
|Air gap 22.5°20 mm ventilated reflective (0.6/0.9; E=0.56)|N|0.157|0.181|0.0|
|Airgap22.5° 20mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.201|0.240|0.0|
|Air gap 22.5°20 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.277|0.356|0.0|
|Airgap22.5° 20mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.342|0.469|0.0|
|Air gap 22.5°20 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.387|0.557|0.0|
|Air gap 22.5°20 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.414|0.613|0.0|
|Airgap22.5° 20mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.472|0.640|0.0|
|Air gap 22.5°13 mm ventilated non-reflective (0.9/0.9; E=0.82)|N|0.114|0.119|0.0|
|Airgap22.5° 13mm ventilatedreflective (0.6/0.9;E =0.56)|N|0.151|0.158|0.0|
|Airgap22.5° 13mm ventilatedreflective (0.4/0.9;E =0.38)|N|0.191|0.202|0.0|
|Air gap 22.5°13 mm ventilated reflective (0.2/0.9; E=0.20)|N|0.259|0.280|0.0|
|Airgap22.5° 13mm ventilatedreflective (0.1/0.9;E =0.10)|N|0.316|0.347|0.0|
|Air gap 22.5°13 mm ventilated reflective (0.05/0.9; E=0.05)|N|0.354|0.393|0.0|
|Air gap 22.5°13 mm ventilated reflective (0.05/0.05; E=0.03)|N|0.376|0.420|0.0|
|Airgap22.5° 13mm ventilatedreflective (0.03/0.03;E =0.015)|N|0.387|0.434|0.0|




## **Air gaps, other** 

The following table lists the material properties of other types of air gaps available from the Material Selector, which is accessed via the button in the Constructions page, details section. 

A 'Y' in the 'Thickness required' column indicates that the resistances and capacitances listed are for a material thickness of 1.0 m. The actual resistance and capacitance of the material used in a construction is the product of its thickness and the value in the table. 

'N' indicates that the resistance and capacitance in the table are used directly without reference to any indicated thickness. 

A blank entry in the Resistance (heat flow down) column indicates that the resistance for heat flow down is the same as for heat flow up. 

|Name|**Thickness**<br>**required**|<br>**Resistance**<br>**(heat flow up)**<br>**(m².K/W)**|<br>**Resistance**<br>**(heat flow down)**<br>**(m².K/W)**|**Capacitance**<br>**(kJ/m³)**|
|---|---|---|---|---|
|Double cell horizontal 25 mm + 25 mm unventilated E=0.026|N|0.844|1.638|0.0|
|Double cell vertical 25mm+25mmunventilatedE =0.026|N|1.418||0.0|
|Double cell 45° 25mm+25mmunventilatedE =0.026|N|1.030|1.570|0.0|
|Double cell 22.5°25 mm + 25 mm unventilated E=0.026|N|0.937|1.604|0.0|
|Glazing airgap (generic)|N|0.110||0.0|




