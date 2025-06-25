

Spectra functions
-----------------

.. function:: lensed_cl()

  | Lensed CMB power spectra (to be used for cosmological inference)
  | Can return temperature, polarization, lensing, depending on the ``'output'`` settings
  | For ``output`` including ``tCl`` has the temperature autocorrelation (TT)
  | For ``output`` including ``pCl`` has the polarization auto/cross-correlations (EE, BB, EB)
  | For ``output`` including ``lCl`` has the lensing auto-correlations (PP)
  | If multiple options are present, also their cross-correlations are included, e.g. with ``tCl, pCl`` we also have TE
  | The option ``lensing`` needs to be set to ``yes`` for this function to work correctly

  :param lmax: Define the maximum l for which the C_l will be returned
               (inclusively) -- by default this will just be the maximal l that is computed (which is given by the input parameter ``l_max_scalars``).
               This number will be checked against the maximum l
               at which they were actually computed by CLASS, and an error will
               be raised if the desired lmax is bigger than what CLASS can give.
  :type lmax: int, optional

  :param nofail: Check and enforce the computation of the C_l's to the given lmax.
  :type nofail: bool, optional

.. function:: raw_cl()
  
  | Raw un-lensed CMB power spectra
  | See documentation for :func:`lensed_cl` for more info.
  | The only differences are that ``lensing=yes`` is not required for this case

.. function:: density_cl()
  
  | Number count/Shear angular power spectra
  | See documentation for :func:`lensed_cl` for more info.
  | The only differences are that ``lensing=yes`` is not required for this case

  :return: Array that contains the list (in this order) of self correlation of
           1st bin, then successive correlations (set by non_diagonal) to the
           following bins, then self correlation of 2nd bin, etc. The array
           starts at index_ct_dd.
