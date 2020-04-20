Train the regular SOM (26X26 map, basically 10 input vectors per unit)

For the small radius we have used a sigma of 4, and for large radius a sigma of
0.1 (there was no specific reason for choosing any of them, just a guess)

My somtoolbox directory is in the same folder with som-exercise-1,
so in order to train the SOM, the following is run:

```bash
./somtoolbox.sh GrowingSOM ../som-exercise-1/data/4.Different_initial_neighborhood/1.Regular_SOM/1.\ Small\ Radius/satimage.prop
```

satimage.prop should be configured in that way that it stores the maps data within
that directory, not somewhere else


Open the SOM Viewer:


```bash
./somtoolbox.sh SOMViewer -u ../som-exercise-1/data/4.Different_initial_neighborhood/1.Regular_SOM/1.\ Small\ Radius/satimage_regsom_smallrad.unit.gz -w  ../som-exercise-1/data/4.Different_initial_neighborhood/1.Regular_SOM/1.\ Small\ Radius/satimage_regsom_smallrad.wgt.gz --dw ../som-exercise-1/data/4.Different_initial_neighborhood/1.Regular_SOM/1.\ Small\ Radius/satimage_regsom_smallrad.dwm.gz
```
