from rasterio.merge import merge
from rasterio.plot import show
import rasterio as rio
from pathlib import Path

# 

def mosaic_list_of_rasters(list_of_raster_files, output_path_filepath):
    """
    Takes a list of rasters and mosicas them. 
    Writes them to output filepath
    Taken from this great tutorial https://medium.com/spatial-data-science/how-to-mosaic-merge-raster-data-in-python-fb18e44f3c8
    """
    # Taken from this great tutorial 
    # https://medium.com/spatial-data-science/how-to-mosaic-merge-raster-data-in-python-fb18e44f3c8
    # empty list to append to 
    raster_to_mosaic = []

    for rf in list_of_raster_files:
        raster = rio.open(rf)
        raster_to_mosaic.append(raster)
    
    mosaic, output = merge(raster_to_mosaic)

    # create metadata
    output_meta = raster.meta.copy()
    output_meta.update(
        {"driver": "GTiff",
            "height": mosaic.shape[1],
            "width": mosaic.shape[2],
            "transform": output,
        }
    )
    # save mosaic to output path
    with rio.open(output_path_filepath, "w", **output_meta) as m:
        m.write(mosaic)
    
    return(mosaic)