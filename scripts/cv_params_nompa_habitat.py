""""
This is a saved model run from natcap.invest.coastal_vulnerability.coastal_vulnerability.
Generated: Thu 16 Jun 2016 02:17:05 PM 
InVEST version: 3.3.1b1.post10+nff1c8fdca089
"""

## param values from Jess's logfile in:
## bahamas-mpa/cv/cv-fromjess/Bahamas_regionalCV_Inputs

import natcap.invest
print(natcap.invest.__version__)
import natcap.invest.coastal_vulnerability.coastal_vulnerability
print(natcap.invest.coastal_vulnerability.coastal_vulnerability)
import os

args = {
        u'aoi_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/AOI_Bahamas_IslandGroup/AOI_CV_Bahamaswide.shp',
        u'area_computed': u'both',
        u'bathymetry_uri': u'/home/dmf/invest-sample-data/Base_Data/Marine/DEMs/global_dem/hdr.adf',
        u'cell_size': 250,
        u'climatic_forcing_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/Bahamas_WW3_UTM18N.shp',
        u'continental_shelf_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/Bahamas_continentalshelf_UTM18N.shp',
        u'depth_contour': 150,
        u'depth_threshold': 0,
        u'elevation_averaging_radius': 2000,
        u'exposure_proportion': 0.4,
        u'habitats_csv_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/NaturalHabitat_Bahamaswide.csv',
        u'habitats_directory_uri': u'../mpa-removeall-habitat/habitat',
        u'landmass_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/LandPoly_Bahamas_08112017.shp',
        u'max_fetch': 12000,
        u'mean_sea_level_datum': 0,
        u'population_radius': 1000,
        u'population_uri': u'/home/dmf/invest-sample-data/Base_Data/Marine/Population/global_pop/w001001.adf',
        u'rays_per_sector': 1,
        u'relief_uri': u'../cv-fromjess/Bahamas_regionalCV_Inputs/Bahamas_SRTM11.tif',
        u'spread_radius': 250,
        u'urban_center_threshold': 500,
        u'geomorphology_uri':u'../cv-fromjess/Bahamas_regionalCV_Inputs/Bahamas_Geomorphology_Final.shp',
        u'workspace_dir': '../mpa-removeall-habitat/cv-output-invest3.3.0',
}

if __name__ == '__main__':
    natcap.invest.coastal_vulnerability.coastal_vulnerability.execute(args)
    
    in_tif_dir = os.path.join(args['workspace_dir'], 'intermediate/1_d_natural_habitats')
    out_csv_dir = os.path.join(args['workspace_dir'], 'outputs/natural_habitats')
    masktif = os.path.join(args['workspace_dir'], 'intermediate/00_preprocessing/00_PRE_shore.tif')

    from build_habitatrank_csv import habitat_tifs2csv
    habitat_tifs2csv(in_tif_dir, out_csv_dir, masktif)
    