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

.. function:: get_pk_all(k, z, nonlinear = True, cdmbar = False, z_axis_in_k_arr = 0, interpolation_kind='cubic')

  | Optimized function to get the power spectrum for wavenumber(s) k in 1/Mpc and redshift(s) z
  | Supports various options, such as the total nonlinear power spectrum or just the linear power spectrum, using the ``nonlinear`` flag
  | Can also return just CDM+baryons with the ``cdmbar`` flag
  | Supports inputs of single wavenumbers and redshifts, or lists thereof
  | The general rule is that as long as the k and z arrays are broadcastable (in the numpy sense) the function should work

  :param k: List or value for the wavenumber in 1/Mpc
  :param z: List or value of the redshift(s)

  :param nonlinear: Whether to return the non-linear power spectrum (if computed)
  :type nonlinear: bool, optional
  :param cdmbar: Whether to return only the CDM+baryon power spectrum or the total matter power spectrum (only different when neutrinos are present)
  :type cdmbar: bool, optional
  :param z_axis_in_k_arr: If ``k`` is a multi-dimensional array, this integer tells which of the axes in the ``k`` array correspond to redshift variations. Typically the first axis (0).
  :type nonlinear: int, optional
  :param interpolation_kind: How to interpolate from CLASS-computed k-values to user-provided k-values? Typically done via cubic splines ('cubic')
  :type interpolation_kind: str, optional

.. hint::
  If ``k`` is a multi-dimensional array of equal shapes, we assume it is a function of k=k_obs(z, ...), like e.g. k=k_obs(z, k, mu). This order can be changed using ``z_axis_in_k_arr``. 
  If ``k`` is a multi-dimensional list of arrays, each with different lengths, we assume/hope that each index of this list corresponds to a single redshift
  If ``k`` is a single-dimensional array, assume that we should evaluate P(k,z) with the same ``k`` array for each z
  Finally, if ``k`` is a single value, assume that we should evalute P(k,z) with that value for each z.

.. function:: get_pk_and_k_and_z(nonlinear=True, only_clustering_species = False, h_units=False)

  | Returns the power spectrum AND the k and z arrays used internally in CLASS, so that you can build your own interpolator on top of it
  | Supports various options, such as the total nonlinear power spectrum or just the linear power spectrum, using the ``nonlinear`` flag
  | Can also return just CDM+baryons with the ``only_clustering_species`` flag
  | The output wavenumbers can be converted into h/Mpc with the ``h_units`` flag 

  :return:
      pk : grid of power spectrum values, pk[index_k,index_z]
      k : vector of k values, k[index_k] (in units of 1/Mpc by default, or h/Mpc when setting h_units to True)
      z : vector of z values, z[index_z]

Less used functions
^^^^^^^^^^^^^^^^^^^

.. function:: pk_numerical_nw(k,z)
  Function to get the numerically de-wiggled power spectrum of total matter

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: pk_analytic_nw(k,z)
  Function to get the analytically de-wiggled power spectrum of total matter

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: pk(k,z)
  Old/Depracated function to get the (non-linear) power spectrum of total matter, see :func:`get_pk_all` for the recommended functionality

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: pk_cb(k,z)
  Old/Depracated function to get the (non-linear) power spectrum of CDM+baryons, see :func:`get_pk_all` for the recommended functionality

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: pk_lin(k,z)
  Old/Depracated function to get the linear power spectrum of total matter, see :func:`get_pk_all` for the recommended functionality

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: pk_cb_lin(k,z)
  Old/Depracated function to get the linear power spectrum of CDM+baryons, see :func:`get_pk_all` for the recommended functionality

  :param k: Single wavenumber in 1/Mpc
  :type k: float

  :param z: Single redshift
  :type z: float

.. function:: get_pk(k,z, k_size, z_size, mu_size)

   Speciality function to get the (non-linear) power spectrum of total matter for a grid of ``k`` and ``z`` values, where the ``k`` grid is expected to be acessed as ``k[index_k,index_z,index_mu]``, and the ``z`` grid as ``z[index_z]``

  :param k: Input wavenumbers k_obs(k, z, mu)
  :type k: Three-dimensional numpy array

  :param z: Input redshifts
  :type z: One-dimensional numpy array

.. function:: get_pk_cb(k,z, k_size, z_size, mu_size)

  See :func:`get_pk`, but specifically for CDM+baryons only

.. function:: get_pk_lin(k,z, k_size, z_size, mu_size)

  See :func:`get_pk`, but specifically linearly

.. function:: get_pk_cb_lin(k,z, k_size, z_size, mu_size)

  See :func:`get_pk`, but specifically linearly
  
