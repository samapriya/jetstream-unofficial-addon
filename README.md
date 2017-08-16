# JetStream Unofficial Addon for Atmosphere VM
[![JetStream](https://img.shields.io/badge/SupportedBy%3A-JetStream-brightgreen.svg)](https://jetstream-cloud.org/)


ArcticDEM project was a joint project supported by both the National Geospatial-Intelligence Agency(NGA) and the National Science Foundation(NSF) with the idea of creating a high resolution and high quality digital surface model(DSM). The product is distributed free of cost as time-dependent DEM strips and is hosted as https links that a user can use to download each strip. As per their policy

*The seamless terrain mosaic can be distributed without restriction.*

The created product is a 2-by-2 meter elevation cells over an over of over 20 million square kilometers and uses digital globe stereo imagery to create these high resolution DSM. The method used for the 2m derivate is Surface Extraction with TIN-based Search-space Minimization(SETSM).

Based on their acknowledgements requests you can use
*Acknowledging PGC services(including data access)*

* Geospatial support for this work provided by the Polar Geospatial Center under NSF OPP awards 1043681 & 1559691.

*Acknowledging DEMS created from the ArcticDEM project*

* DEMs provided by the Polar Geospatial Center under NSF OPP awards 1043681, 1559691 and 1542736.

You can find details on the background, scope and methods among other details [here](https://www.pgc.umn.edu/guides/arcticdem/introduction-to-arcticdem/?print=pdf)
A detailed acknowledgement link can be found [here](https://www.pgc.umn.edu/guides/user-services/acknowledgement-policy/)

With this in mind and with the potential applications of using these toolsets there was a need to batch download the DEM files for your area of interest and to be able to extract, clean and process metadata. In all fairness this tool has a motive of extending this as an input to Google Earth Engine and hence the last tool which is the metadata parser is designed to create a metadata manifest in a csv file which GEE can understand and associate during asset upload. 

![CLI](http://i.imgur.com/52eJzp6.gif)

## Table of contents
* [Usage examples](#usage-examples)
	* [Subset to AOI](#subset-to-aoi)
    * [Estimate Download Size](#estimate-download-size)
    * [Download DEM](#download-dem)
    * [Extract DEM](#extract-dem)
    * [Metadata Parsing for GEE](#metadata-parsing-for-gee)


## Getting started


As usual, to print help  `arcticdem -h`:
```

```

## Subset to AOI

```

```

```

### Estimate Download Size


```

```
An example setup would be
```

```



## Download DEM


```

```
An example setup would be
```
arcticdem demdownload --subset "C:\users\master_aoi.shp" --destination "C:\users\ArcticDEM"
```
 
## Extract DEM


```

```
An example setup would be
```
arcticdem demdextract --folder "C:\users\ArcticDEM" --destination "C:\users\ArcticDEM\Extract" --action "yes"
```
