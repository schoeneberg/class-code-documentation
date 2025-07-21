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

* ``output`

  Here you can control the output of class that you'll be able to access after it computes. In the future the code might be smart enough to recompute always based on what you are actually using, but for now you explicitly have to tell it ahead of time. That means, if you want to use the :func:`get_pk_all` function, for example, you have to tell it ahead of time that you'll want the matter power spectrum (mPk) output. This is only required for the output spectra (angular or matter power spectra, spectral distortions), not for the output of intermediate modules (e.g. background/thermodynamics/perturbations/...).
  
  Examples of commonly needed output options:
    * ``'mPk'`` for :func:`get_pk_all` or :func:`sigma8` or anything else related to :math:`P(k,z)`
    * ``'tCl, pCl, lCl'`` for the :func:`lensed_cl` (coupled with ``{'lensing':'yes'}``)
    * ``'mTk, vTk'`` for the transfer functions, :func:`get_transfer`, e.g. for N-body initial conditions. These are the (gauge-transformed) perturbations **at a fixed time**

  If you want the perturbations **at a fixed wavenumber** (for multiple times), see instead ``'k_output_values'``.
