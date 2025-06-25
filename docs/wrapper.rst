Wrapper functions
==================

Main usage
----------

.. code:: python

  import classy
  cosmo = classy.Class()
  # Now work with the cosmo object!
  cosmo.set({'omega_b':0.022,'H0':71, 'output':'tCl'})
  cosmo.raw_cl()

.. function:: set(input)

  Tell classy to use certain input parameters, described in the python dictionary ``input``.
  Can also be passed as explicit keywords

  :param input: Input parameters
  :type input: dict

.. note::

  ``cosmo.set({'omega_b':0.02})``
  is equivalent to
  ``cosmo.set(omega_b=0.02)``

.. caution::

  It is impossible to do the same for
  ``cosmo.set({'100*theta_s':1.04})``
  In this case, we would use instead the equivalent parameter name
  ``cosmo.set({'theta_s_100':1.04})``
  and convert it into
  ``cosmo.set(theta_s_100=1.04)``

.. function:: set_baseline(baseline_name):

  Set input parameters to one of the available baseline cosmologies.

  * | ``planck2018_lensing_bao`` or ``p18lb``:
    | Best-fitting cosmology to Planck 2018 + lensing + BAO (SDSS)

  * | ``planck2018_lensing`` or ``p18l``:
    | Best-fitting cosmology to Planck 2018 + lensing

  * | ``planck2018`` or ``p18``:
    | Best-fitting cosmology to Planck 2018

Conversion factors
------------------

Class works internally in units of Mpc^n, therefore we want to use conversion factors to SI units. These are available as properties of each cosmo object

* ``density_factor``
  Converting from class density units to kg/m^3

* ``kg_to_eV``
  Converting from kg to eV (useful also to convrt kg/m^3 to eV/m^3, see example)

* ``Mpc_to_m``
  Converting from Mpc to m

* ``kg_to_Msol``
  Converting from kg to solar mass ($2 \times 10^{30}$kg)

* ``kgm3_to_MsolMpc3``
  Converting from kg/m^3 to Msol/Mpc^3

.. admonition:: Example

  If we want the CDM density in SI units or in astrophysical units, we can do it like that:

  .. code:: python

    bg = cosmo.get_background()
    rho_cdm = bg['(.)rho_cdm']
    rho_cdm_SI = rho_cdm * cosmo.density_factor
    rho_cdm_astro = rho_cdm_SI * cosmo.kgm3_to_MsolMpc3
    print(f"The current CDM density is {rho_cdm_SI[-1]*1e27:.3f} * 10^(-27) kg/m^3")
    print(f"The current CDM density is {rho_cdm_SI[-1]*(cosmo.Mpc_to_m/1e6)**3*1e-22:.3f} * 10^22 kg/pc^3")
    print(f"The current CDM density is {rho_cdm_astro[-1]*1e-10:.3f} * 10^10 Msol/Mpc^3")


Background functions
--------------------

Cosmic distances are defined as usual, i.e.

.. math::
   D_c(z) = \int_0^z \frac{\mathrm{d}x}{H(x)} \\
   D_M(z) = \left\{\begin{array}{lr} D_c(z), & \text{for } K=0\\
        \sin(\sqrt{K}D_c(z))/\sqrt{K}, & \text{for } K>0\\
        \sinh(\sqrt{-K}D_c(z))/\sqrt{-K}, & \text{for } K<0
        \end{array}\right. \\
   D_A(z) = D_M(z) / (1+z) \\
   D_L(z) = D_M(z) \cdot (1+z) \\
   D_A(z1,z2) = D_M(z)/(1+z2) \text{ with $D_M(z)$ computed with} D_c(z) \to D_c(z2)-D_c(z1)

.. function:: get_background()

  Get entire background dictionary available in CLASS, containing a dictionary of all background quantities that CLASS saved

 .. function:: z_of_r(z)
  Get conformal/comoving distance D_M(z) and Hubble parameter H(z) for the redshift z
  :param z: Redshift (value or list)

 .. function:: comoving_distance(z)
  Get conformal/comoving distance D_M(z) for the redshift z
  :param z: Redshift (value or list)

 .. function:: luminosity_distance(z)
  Get luminosity distance D_L(z) for the redshift z
  :param z: Redshift (value or list)

 .. function:: angular_distance(z)
  Get luminosity distance D_A(z) for the redshift z
  :param z: Redshift (value or list)

 .. function:: angular_distance_from_to(z1,t2)
  Get luminosity distance D_A(z1,z2) for the redshift pair (z1,z2)
  :param z1: Redshift (value only)
  :param z2: Redshift (value only)

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
  :type lmax: int (, optional)

  :param nofail: Check and enforce the computation of the C_l's to the given lmax.
  :type nofail: bool (, optional)

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
  :rtype: array of numpy arrays

.. Test
  comment:: .. attention:: -- for attention blocks
  comment:: caution, hint, tip, advice, warning, seealso, note
  comment:: .. admonition:: Example -- for examples
  comment:: .. code:: for code block
