Parameters
----------

These are convenience functions for you to get to your favorite quantities faster, but might be deprecated in the future. Also, for the use with samplers, please always use the :func:`get_derived_parameters`

 .. function:: age()
  
  Get total age of the universe (in Gyrs)

 .. function:: h()
  
  Get reduced Hubble constant :math:`h = H_0/(100\mathrm{km/s/Mpc})`

 .. function:: n_s()
  
  Get primordial power spectrum tilt

 .. function:: tau_reio()
  
  Get optical depth of reionization :math:`\tau_\mathrm{reio} = \int_{\eta_*}^{\eta_0} \frac{a \sigma_T n_e}{R}

 .. function:: z_reio()
  
  Get redshift of reionization

 .. function:: T_cmb()
  
  Get CMB temperature (can be used to convert :math:`C_\ell` to `\mu K` (by a factor of T_cmb**2 * 1e6**2)

 .. function:: N_eff()
  
  Get effective number of relativistic degrees of freedom :math:`\frac{7}{8} N_\mathrm{eff} \left(\frac{4}{11}\right)^{4/3} = \rho_\nu/\rho_g`

 .. function:: Omega_Lambda()
  
  Get cosmological constant energy density fraction :math:`\Omega_\Lambda = \rho_{\Lambda,0}/\mathrm{\rho_{\mathrm{crit},0}}`

 .. function:: Omega_m()
  
  Get matter energy density fraction :math:`\Omega_m = \rho_{m,0}/\mathrm{\rho_{\mathrm{crit},0}}`

 .. function:: Omega0_m()
  
  Depracated version of :func:`Omega_m`

 .. function:: Omega_g()
  
  Get photon energy density fraction :math:`\Omega_g = \rho_{g,0}/\mathrm{\rho_{\mathrm{crit},0}}`

 .. function:: Omega_b()
  
  Get baryon energy density fraction :math:`\Omega_b = \rho_{b,0}/\mathrm{\rho_{\mathrm{crit},0}}` 

 .. function:: Omega_r()
  
  Get radiation energy density fraction :math:`\Omega_r = \rho_{r,0}/\mathrm{\rho_{\mathrm{crit},0}}`

 .. function:: omega_b()
  
  Get reducded baryon energy density fraction :math:`\Omega_b h^2 = \rho_{b,0}/\mathrm{\rho_{\mathrm{crit},0}} \cdot h^2` 

 .. function:: theta_s_100()
  
  Get sound horizon angle :math:`100 \theta_s = 100 r_s/r_A`

 .. function:: theta_star_100()
  
  Get sound horizon angle :math:`100 \theta_s = 100 r_*/r_A`

 .. function:: k_eq()
  
  Get equality wavenumbers :math:`k_\mathrm{eq} = a_\mathrm{eq} H_\mathrm{eq}`

 .. function:: z_eq()
  
  Get equality wavenumbers :math:`z_\mathrm{eq} = 1/a_\mathrm{eq} - 1`

 .. function:: rs_drag()
  
  Sound horizon :math:`r_s = \int_{z_\mathrm{drag}}^\infty c_s \mathrm{d}x/H(x)` 





