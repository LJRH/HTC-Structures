# HTC-Structures
Structures of postulated Hydrothermal Carbon (HTC) molecular components for XANES calcs.

### To do
- [x] Generate structures in Avogadro and UFF minimise.
- [x] Orca geometry optimisation.
- [ ] Erkale C-K core calculation.

### Geometry Optomisation:
Ground state geometry optimisation performed using ORCA (4.0) software.\\
Smaller structures were performed using:
* functional set:  B3LYP
* basis set:	     ma-def2-TZVP
* aux basis set:	 def2/J
* dispersion Corr: D3
* approximations: RIJCOSX

The larger structures (bpath_HMF02 & bpath_HMF03) were performed using:
* functional set: PBE0
* basis set: def2-TZVP (triple Zeta)
* aux basis set: def2/JK
* dispersion correction: D3BJ
* approximations: RIJK

### Erkale Calculation:
<insert details of calculations>

### List of Structures:
Structure Name | Geom Optomised? | Erkale Calculation |Type | Notes
----------------|-----------|-----------|------------------------------------------------------------------------------------
5HMF		        | [x] | [x] |Reference	|Literature suggests hydroxymethylfurfural as the HTC subunit.
DHA		          | [x] | [x] |Reference	|Dihydoxyacetone - suggested to be a major linking unit
Formic Acid	    | [x] | [x] |Reference	|Formic Acid - Typically formed during HTC from HPLC measurements.
Levullinic Acid	| [x] | [x] |Reference	|Levullinic Acid - Typically formed during HTC from HPLC measurements.
apath_HMF00	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 0 - Alpha carbon bonding with no linking unit.
apath_HMF01	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 1 - Alpha carbon bonding with 01 linking unit.
apath_HMF02	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 2 - Alpha carbon bonding with 02 linking unit.
apath_HMF02_O	  | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 2 with ketone - as above with ketone O=C.
apath_HMF03	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 3 - Alpha carbon bonding with 02 linking unit.
bpath_HMF01	    | [x] | [x] |Beta-C		  |HMF binding beta-C pathway 1 - Beta carbon bonding with single linking unit.
bpath_HMF02	    | [x] | [x] |Beta-C		  |HMF binding beta-C pathway 2 - 2 alpha 1 Beta carbon bonding with 0 linking units.
bpath_HMF03     | [x] | [x] |Beta-C     |HMF binding beta-C pathway 3 - 3 Beta carbon bonding with 0 linking units.
