# Procedure training description

Started executing C1 (regular sized map with 26x26 map size - this means ~10 samples per unit)

Go to the soomtoolbox directory, and run the following:

````bash
./somtoolbox.sh GrowingSOM ../som-exercise-1/data/satimage.prop 
```
*Note*: make sure to have the paths valid in the properties file.

 
This will train the model and store the trained map in the selcted output directory. 

These trainings can be analyzed by using the SOMViewer by executing the following:

````bash
./somtoolbox.sh SOMViewer -u ../som-exercise-1/data/maps_ilir/satimage.unit.gz -w  ../som-exercise-1/data/maps_ilir/satimage.wgt.gz --dw ../som-exercise-1/data/maps_iliratimage.dwm.gz 

```


To store the activity histograms (whatever that means) as png's, do the following:


```bash
./somtoolbox.sh VisualisationImageSaver -u ../som-exercise-1/data/maps_ilir/satimage.unit.gz -w ../som-exercise-1/data/maps_ilir/satimage.wgt.gz -v ../som-exercise-1/data/satimage.vec -o ../som-exercise-1/data/maps_ilir/ActivityHistograms_Ilir/
```

