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

  * :code:`planck2018_lensing_bao` or :code:`p18lb`
    Best-fitting cosmology to Planck 2018 + lensing + BAO (SDSS)

  * :code:`planck2018_lensing` or :code:`p18l`
    Best-fitting cosmology to Planck 2018 + lensing

  * :code:`planck2018` or :code:`p18`
    Best-fitting cosmology to Planck 2018

Background functions
--------------------

.. function:: get_background()

  Get entire background dictionary available in CLASS, containing a dictionary of all background quantities that CLASS saved

.. Test
  comment:: .. attention:: -- for attention blocks
  comment:: caution, hint, tip, advice, warning, seealso, note
  comment:: .. admonition:: Example -- for examples
  comment:: .. code:: for code block
