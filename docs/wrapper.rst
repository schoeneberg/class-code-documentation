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

.. function:: set(dic)

  Tell classy to use certain input parameters, described in the python dictionary :code:`dic`.
  Can also be passed as explicit keywords

  :param dic: Input parameters
  :type dic: dict

.. note::

  :code:`cosmo.set({'omega_b':0.02})`
  is equivalent to
  :code:`cosmo.set(omega_b=0.02)`

.. caution::

  It is impossible to do the same for
  :code:`cosmo.set({'100*theta_s':1.04})`
  In this case, we would use instead the equivalent parameter name
  :code:`cosmo.set({'theta_s_100':1.04})`
  and convert it into
  :code:`cosmo.set(theta_s_100=1.04)`

.. function:: set_baseline(baseline_name):

  Set input parameters to one of the available baseline cosmologies.

  * |:code:`planck2018_lensing_bao` or :code:`p18lb`:
    |Best-fitting cosmology to Planck 2018 + lensing + BAO (SDSS)

  * |:code:`planck2018_lensing` or :code:`p18l`:
    |Best-fitting cosmology to Planck 2018 + lensing

  * |:code:`planck2018` or :code:`p18`:
    |Best-fitting cosmology to Planck 2018

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

.. function:: get_background()

  Get entire background dictionary available in CLASS, containing a dictionary of all background quantities that CLASS saved

Spectra functions
-----------------

.. function:: lensed_cl()

  Lensed CMB power spectra (to be used for cosmological inference)
  Can return temperature, polarization, lensing, depending on the `'output'` settings
  For `output` including `tCl` has the temperature autocorrelation (TT)
  For `output` including `pCl` has the polarization auto/cross-correlations (EE, BB, EB)
  For `output` including `lCl` has the lensing auto-correlations (PP)
  If multiple options are present, also their cross-correlations are included, e.g. with `tCl, pCl` we also have TE

.. function:: raw_cl()
  
  .. | 
     | Raw un-lensed CMB power spectra
     | See documentation for :func:`lensed_cl` for more info.
     | The only differences are that `lensing=yes` is not required for this case

.. Test
  comment:: .. attention:: -- for attention blocks
  comment:: caution, hint, tip, advice, warning, seealso, note
  comment:: .. admonition:: Example -- for examples
  comment:: .. code:: for code block
