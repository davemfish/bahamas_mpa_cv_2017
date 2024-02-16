### Random Notes

scripts/cv_params_nompa_habitat.py
scripts/cv_params_nompa_allhabitat.py
two python scripts that each executed the CV model for country-wide runs. All input data is referenced in those scripts and seems to mostly point to the “cv-fromjess” directory. 

While these scripts seem to represent two scenarios (one with intact habitat layers and one with all habitats removed from within MPA boundaries), it seems we did not actually use these two runs for our scenario analysis.

We used the “rank” outputs of all variables except habitat from one of these runs (doesn’t matter which, but looks like /mpa-removeall-habitat/cv-output-invest3.3.0/) and “manually” applied habitat scenarios of habitat ranks, and re-calculated the final exposure index. All that was done in scripts/cv_ModHabitats_RecalcExposure_Summarize_v2.ipynb

According to that notebook, the baseline habitat ranks at each shore point are ../mpa-removeall-habitat/habitat_ranks_baseline.shp

These data built by Jess in GIS - selecting points within the 'protective distance' of each habitat, and assigning rank then maybe some manual selection/deselection of points to account for the 'skinny island' effect. When building this shapefile, MUST start with 'coastal_exposure.shp' returned by invest so that later on habitats ranks can be merged with other exposure indices, by simply binding columns together

When re-calculating the exposure index, at first we created high-med-low categories based on the combined distribution of index values in the two scenarios (unused_scripts/cv_ModHabitats_RecalcExposure_Summarize.ipynb). 

Later we decided to make two simple categories: did exposure increase or not under the “remove habitat” scenario? And this is the method we ultimately presented.
scripts/cv_ModHabitats_RecalcExposure_Summarize_v2.ipynb

### The Workflow

cv_params_nompa_habitat.py - run the CV model to get baseline outputs for all non-habitat variables.

cv_ModHabitats_RecalcExposure_Summarize_v2.ipynb - takes some baseline CV outputs and creates habitat role & final exposure results for two scenarios (../mpa-removeall-habitat/scenario_data/cv_2scenarios_byisland_habrolecat.shp)

cv_SocialMetrics_v2.ipynb - joins final scenario data (../mpa-removeall-habitat/scenario_data/cv_2scenarios_byisland_habrolecat.shp) to population & income data by first constructing a polygon for each shore point and then using zonal stats to summarize population & income raster data.

cv_socialmetrics_table.rmd - I think this just formatted data into a nice-looking table, probably don’t want to re-use this.
