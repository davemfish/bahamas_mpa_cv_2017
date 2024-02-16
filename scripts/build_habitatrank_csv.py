# build a csv with the individual habitat rank values for each shore point
# this facilitates manually adjusting habitat contributions at certain points
# e.g. Jess's process of preventing coral on one side of a skinny island from 
# influencing shore points on the far side of the island.

# This ought to be moved to the main invest-calling script, which already has 
# args['workspace_dir'] defined.

import natcap.invest.coastal_vulnerability.coastal_vulnerability_core as cv
import os

# args = {}
# args['workspace_dir'] = '../mpa-removeall-habitat/cv-output-invest3.3.0'

def habitat_tifs2csv(in_tif_dir, out_csv_dir, masktif):

	tiflist = []
	for f in os.listdir(in_tif_dir):
		if f.endswith('influence_on_shore.tif'):
			tiflist.append(os.path.join(in_tif_dir, f))

	print(tiflist)


	if not os.path.isdir(out_csv_dir):
	        os.makedirs(out_csv_dir)

	cv.aggregate_tifs_from_list(uri_list = tiflist, path = out_csv_dir, mask = masktif)


