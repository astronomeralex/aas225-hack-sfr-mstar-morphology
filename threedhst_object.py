#reads in data files and makes an object for each entry

import numpy as np

class ThreeDHST_Catalog(object):
    """
    class for the 3dhst catalog
    """
    def __init__(self):
        self.morph125_file = "vanderwel_morphology/cosmos_3dhst.v4.1_f125w.galfit"
        self.morph125_cols = ['id125', 'ra125', 'dec125', 'flag125', 'mag125', 'dmag125',
        're125', 'dre125', 'n125', 'dn125', 'q125', 'dq125', 'pa125', 'dpa125', 'sn125']
        self.morph160_file = "vanderwel_morphology/cosmos_3dhst.v4.1_f160w.galfit"
        self.morph160_cols = ['id160', 'ra160', 'dec160', 'flag160', 'mag160', 'dmag160',
        're160', 'dre160', 'n160', 'dn160', 'q160', 'dq160', 'pa160', 'dpa160', 'sn160']
        self.threedhst_restframe_file = "3dhst_data/cosmos_3dhst.v4.1.master.RF"
        self.threedhst_restframe_cols = ['idrf','zrf','DM','L153','n_153','L154','n_154',
        'L155','n_155', 'L161','n_161','L162','n_162','L163','n_163','L156','n_156',
        'L157','n_157','L158','n_158','L159','n_159','L160','n_160','L135','n_135','L136',
        'n_136','L137','n_137','L138','n_138','L139','n_139','L270','n_270','L271',
        'n_271','L272','n_272','L273','n_273','L274','n_274','L275','n_275']
        self.threedhst_fast_file = "3dhst_data/cosmos_3dhst.v4.1.fout"
        self.threedhst_fast_cols = ['idfast','z','ltau','metal','lage','Av','lmass',
        'lsfr','lssfr','la2t','chi2']
        self._catalog = None
        
    @property
    def catalog(self):
        if self._catalog is None:
            self.morph125 = np.loadtxt(self.morph125_file)
            self.morph160 = np.loadtxt(self.morph160_file)
            self.threedhst_restframe = np.loadtxt(self.threedhst_restframe_file)
            self.threedhst_fast = np.loadtxt(self.threedhst_fast_file)
            self._catalog = []
            self.stackeddata = np.hstack((self.threedhst_fast, self.threedhst_restframe, 
                             self.morph125, self.morph160))
            self.stackedcols = self.threedhst_fast_cols + self.threedhst_restframe_cols +\
                             self.morph125_cols + self.morph160_cols
            for i in self.stackeddata:
                newobj = ThreeDHST_Object()
                for colname, value in zip(self.stackedcols, i):
                    if 'id' in colname or 'flag' in colname:
                        setattr(newobj, colname, int(value))
                    else:
                        setattr(newobj, colname, value)
                self._catalog.append(newobj)
                
        return self._catalog
    
    def zrange(self,zmin,zmax):
        """
        returns a catalog with objects with a redshift of zmin to zmax
        """
        newcat = []
        for i in self.catalog:
            if i.z >= zmin and i.z <=zmax:
                newcat.append(i)
        return newcat
            
class ThreeDHST_Object(object):
    """
    class for 3dhst objects
    """
    def __init__(self):
        self._uvsfr = None
    
    @property
    def uvsfr(self):
        if self._uvsfr is None:
            #using rest frame uv, not corrected for dust
            #self.L270 is fnu at 1400 Angstroms with AB zeropoint of 25
            relative_abmag = 25.0 - 2.5*np.log10(self.L270)
            absolute_abmag = relative_abmag - self.DM
            Lnu = 10**(-0.4 * (absolute_abmag + 48.6)) * 1.196e40 # in erg/s/Hz
            self._uvsfr = 1.4e-28 * Lnu #in solar masses per year
            
        return self._uvsfr
    
        
