.. _wrapper-set:

Wrapper set function
====================

.. function:: set(input)

  Tell classy to use certain input parameters, described in the python dictionary ``input``.
  Can also be passed as explicit keywords

  :param input: Input parameters
  :type input: dict


General parameters
^^^^^^^^^^^^^^^^^^

* output

Here you can control the output of class that you'll be able to access after it computes. In the future the code might be smart enough to recompute always based on what you are actually using, but for now you explicitly have to tell it ahead of time. That means, if you want to use the :func:`get_pk_all` function, for example, you have to tell it ahead of time that you'll want the matter power spectrum (mPk) output. This is only required for the output spectra (angular or matter power spectra, spectral distortions), not for the output of intermediate modules (e.g. background/thermodynamics/perturbations/...).
