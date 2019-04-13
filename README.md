# HTC-Structures
Structures of postulated HTC components for XANES calcs.

### To do
- [x] Generate structures in Avogadro and UFF minimise.
- [ ] Orca geometry optimisation.

### Geometry Optomisation:
Ground state geometry optimisation performed using ORCA software with following:
* functional set:  B3LYP
* basis set:	     ma-def2-TZVP
* aux basis set:	 def2/J
* dispersion Corr: D3

### List of Structures:
Structure Name |Geom Optomised? |Type | Notes
----------------|-----------|-----------|------------------------------------------------------------------------------------
5HMF		        | [x] |Reference	|Literature suggests hydroxymethylfurfural as the HTC subunit.
DHA		          | [x] |Reference	|Dihydoxyacetone - suggested to be a major linking unit
Formic Acid	    | [x] |Reference	|Formic Acid - Typically formed during HTC from HPLC measurements.
Levullinic Acid	| [x] |Reference	|Levullinic Acid - Typically formed during HTC from HPLC measurements.
apath_HMF00	    | [x] |Alpha-C		|HMF binding alpha-C pathway 0 - Alpha carbon bonding with no linking unit.
apath_HMF01	    | [x] |Alpha-C		|HMF binding alpha-C pathway 1 - Alpha carbon bonding with 01 linking unit.
apath_HMF02	    | [x] |Alpha-C		|HMF binding alpha-C pathway 2 - Alpha carbon bonding with 02 linking unit.
apath_HMF02_O	  | [x] |Alpha-C		|HMF binding alpha-C pathway 2 with ketone - as above with ketone O=C.
apath_HMF03	    | [ ] |Alpha-C		|HMF binding alpha-C pathway 3 - Alpha carbon bonding with 02 linking unit.
bpath_HMF01	    | [x] |Beta-C		  |HMF binding beta-C pathway 1 - Beta carbon bonding with single linking unit.
bpath_HMF02	    | [ ] |Beta-C		  |HMF binding beta-C pathway 2 - 2 alpha 1 Beta carbon bonding with 0 linking units.
bpath_HMF03     | [ ] |Beta-C     |HMF binding beta-C pathway 3 - 3 Beta carbon bonding with 0 linking units.
