import numpy as np
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy.table import hstack
import astropy.units as u

def make_uvista(catfile = "UVISTA_final_v4.1.cat", 
    sfr_stellarmass_file = "UVISTA_final_colors_sfrs_v4.1.dat"):
    """
    convienance function combine and write out parts of uvista cataloge
    """
    radec = ascii.read(catfile,include_names=['ra', 'dec'])
    sfr_sm = ascii.read(sfr_stellarmass_file)
    uvista_table = hstack([sfr_sm,radec])
    ascii.write(uvista_table,"uvista_radec_sfr.tbl")
    
def read_tables(morph_file = 'cosmos_morph_zurich.tbl.txt',
    uvista_file='uvista_radec_sfr.tbl'):
    """
    convienance function to read tables
    """
    morphcat = ascii.read(morph_file)
    morphcat['ra'].unit = u.degree
    morphcat['dec'].unit = u.degree
    uvistacat = ascii.read(uvista_file)
    return morphcat, uvistacat

def cat_matching(morphcat, uvistacat, match_radius=0.5, unique_radius=2.0):
    """
    matches the catalogs using astropy's skycoord. match radius is the maximum
    matching distance and the unique radius is the radius within which the match must
    be unique. both in arcseconds
    """
    morphcoords = SkyCoord(morphcat['ra'],morphcat['dec'],unit='deg', frame='icrs')
    uvistacoords = SkyCoord(uvistacat['ra'],uvistacat['dec'],unit='deg', frame='icrs')
    idx, d2d, d3d = morphcoords.match_to_catalog_sky(uvistacoords)
    #idx is an array of length cosmos_coords that contains the index of the closest match in uvista_coords
    #d2d is the two dimensional distance between the cosmos_coords object and its best match
    matched_cat = hstack([uvistacat[idx],morphcat])
    uniq, uniq_counts = np.unique(idx[d2d.arcsec < unique_radius],return_counts=True)
    uniq1 = uniq[uniq_counts == 1]
    uniqb = np.empty_like(idx,dtype=bool)
    for i, x in enumerate(idx):
        uniqb[i] = x in uniq1 #should be able to do a numpy thing to make this fast
        if i % 5000 == 0:
            print(i)
    b = (d2d.arcsec < match_radius) & (uniqb) & (matched_cat['USE'] == 1)
    return matched_cat[b]
    