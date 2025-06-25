Wrapper functions
==================

Main usage
----------

.. code::
  import classy
  cosmo = classy.Class()
  # Now work with the cosmo object!
  cosmo.set({'omega_b':0.022,'H0':71, 'output':'tCl'})
  cosmo.raw_cl()

.. function set(dictionary)
  Tell classy to use certain input parameters

Background functions
--------------------

.. function get_background()
  Get entire background dictionary available in CLASS, containing a dictionary of all background quantities that CLASS saved

.. Test
  comment:: .. attention:: -- for attention blocks
  comment:: caution, hint, tip, advice, warning, seealso, note
  comment:: .. admonition:: Example -- for examples
  comment:: .. code:: for code block
