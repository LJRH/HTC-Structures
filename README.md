# HTC-Structures
Structures of postulated Hydrothermal Carbon (HTC) molecular components for XANES calcs.

### To do

[x] Calculate Structures and corresponding CK XRSS spectra for relevant subuntits in hydrothermal carbon.
[x] Collect LA and FDCA standards at 20ID APS (March 2020)
[ ] Calculate CK XRSS spectra for FDCA and compare to collected standard.
[ ] Adjust broadening for calculated XRSS to match collected standard.

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
https://github.com/susilehtola/erkale/wiki/ERKALE
* scf: gga, double-zeta basis set
* xrs: half core-hole TPA calculation, dipole and q=0.01, 0.2, 0.4, 0.6, 0.8, 1.0 a.u. available, averages done for dipole
* xch: full core-hole calculation for delta-Kohn-Sham energy correction
calculations of the bigger molecules are still missing, will come as soon as the cluster is less busy

### List of Structures:
Structure Name | Geom Optomised? | Erkale Calculation |Type | Notes
----------------|-----------|-----------|-----------|------------------------------------------------------------------------------------
5HMF		        | [x] | [x] |Reference	|Literature suggests hydroxymethylfurfural as the HTC subunit.
FDCA            | [x] | [ ] |Standard   |XRSS data collected for FDCA in March at 20ID APS (attached).
DHA		          | [x] | [x] |Reference	|Dihydoxyacetone - suggested to be a major linking unit
Formic Acid	    | [x] | [x] |Reference	|Formic Acid - Typically formed during HTC from HPLC measurements.
Levullinic Acid	(LA)| [x] | [x] |Reference/Standard	|Levullinic Acid - Typically formed during HTC from HPLC measurements and collected as a standard at 20ID APS (attached).
apath_HMF00	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 0 - Alpha carbon bonding with no linking unit.
apath_HMF01	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 1 - Alpha carbon bonding with 01 linking unit.
apath_HMF02	    | [x] | [x] |Alpha-C		|HMF binding alpha-C pathway 2 - Alpha carbon bonding with 02 linking unit.
apath_HMF02_O	  | [x] | [ ] |Alpha-C		|HMF binding alpha-C pathway 2 with ketone - as above with ketone O=C.
apath_HMF03	    | [x] | [ ] |Alpha-C		|HMF binding alpha-C pathway 3 - Alpha carbon bonding with 02 linking unit.
bpath_HMF01	    | [x] | [x] |Beta-C		  |HMF binding beta-C pathway 1 - Beta carbon bonding with single linking unit.
bpath_HMF02	    | [x] | [ ] |Beta-C		  |HMF binding beta-C pathway 2 - 2 alpha 1 Beta carbon bonding with 0 linking units.
bpath_HMF03     | [x] | [ ] |Beta-C     |HMF binding beta-C pathway 3 - 3 Beta carbon bonding with 0 linking units.
