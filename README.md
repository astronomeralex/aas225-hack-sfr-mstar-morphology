# aas225-hack-sfr-mstar-morphology
Looking at star forming galaxies to see if scatter in the main sequence of star 
forming galaxies is correlated with morphology.

This is from an idea from the Stellar Mass and Star Formation Rate session after talking with Louis Abramson and Dan Kelson.

###To Do
* Using [matplotlib colorbar](http://matplotlib.org/examples/pylab_examples/colorbar_tick_labelling_demo.html) to visualize effective radius, sersic, and axis ratio along sfr - stellar mass diagram
* maybe try [voronoi binning](http://www-astro.physics.ox.ac.uk/~mxc/software/#binning) or the [weighted version here](http://www.phy.ohiou.edu/~diehl/WVT/)
* compare to [Wuyts et al. 2011](http://adslabs.org/adsabs/abs/2011ApJ...742...96W/)
* try machine learning or n-d statistics to tease out relationships? PCA doesn't work too well
* how to fit main sequence line
	- medians in little bins, then fit line
	- something that removes outliers? ask feigelson?
	- some sort of sigma clipping?
	- gaussian regression, loess, etc?
	- thiel-sen!

###Data From:
* GAMA
	* http://www.gama-survey.org/dr2/
	* SFRs from http://adslabs.org/adsabs/abs/2003ApJ...599..971H/
* COSMOS and UltraVISTA Catalogs
	* http://www.strw.leidenuniv.nl/galaxyevolution/ULTRAVISTA/Ultravista/K-selected.html
	* http://irsa.ipac.caltech.edu/data/COSMOS/datasets.html
	
###Other Work
W working on 3DHST and van der wel morphology, collaborate on this to compare in the paper.

galaxy zoo looked at sdss/galaxy zoo (Willett et al.)

* SDSS Data 
	* http://www.mpa-garching.mpg.de/SDSS/DR7/
	* http://www.mpa-garching.mpg.de/SDSS/DR7/sfrs.html
	* http://home.strw.leidenuniv.nl/~jarle/SDSS/
	* http://www.mpa-garching.mpg.de/SDSS/DR7/Data/stellarmass.html
	* http://www.sdss.org/dr12/spectro/galaxy_mpajhu/
	* http://www.sdss.org/dr12/spectro/galaxy/
* Galaxy Zoo
	* http://arxiv.org/abs/1308.3496v2
	* http://data.galaxyzoo.org/
* 3DHST
	* Using data from Skelton et al. and van der wel et al. 
	* http://www.mpia-hd.mpg.de/homes/vdwel/3dhstcandels.html
	* http://3dhst.research.yale.edu/Data.php
