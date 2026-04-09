---
title: 'thermoprofiler?'
tags:
  - Python
  - thermal properties
  - petrophysics
  - well logs
  - sedimentary rocks
authors:
  - name: 
    orcid: 
    affiliation: ""
    corresponding:
  - name: 
    orcid:
    affiliation: GFZ 
  - name:
    orcid: 
    affiliation: GFZ
date: 2026
bibliography: paper.bib
---

# Summary
FROM ABSTRACT
Thermal conductivity, heat capacity, and thermal diffusivity control subsurface temperature and heat-flow estimates and are key inputs for geothermal exploration and basin-scale thermal modelling. In practice, these properties are rarely available as continuous depth profiles because laboratory measurements require core material and are typically sparse. We present an extended thermo-profiler workflow that predicts continuous thermal property profiles directly from standard wireline logs and provides uncertainty-aware outputs for downstream geothermal and heat-flow applications. Thermo-profiler uses multivariate statistics on physically modelled synthetic datasets representing realistic mineralogical and porosity variations in common sedimentary lithologies. The workflow learns relationships between thermal properties and routinely available logs (e.g., sonic velocity, density, neutron porosity, gamma ray). Multiple prediction models and log combinations are evaluated, enabling robust predictions even when only a subset of logs is available and allowing automated model choice based on the input data of a given borehole. Validation with independent laboratory core measurements shows that prediction performance improves with log coverage and with formation-scale averaging. For thermal conductivity, uncertainties are commonly within the ~10–30% range at sample scale, while interval means can be constrained substantially better for larger stratigraphic units. Heat capacity is predicted with higher accuracy in the best-performing models, and thermal diffusivity uncertainties follow are derived  from the combined conductivity and heat-capacity predictions. We illustrate application examples where thermo-profiler outputs are used to generate thermal property profiles for wells in sedimentary settings and to provide consistent inputs for conductive 1D temperature and heat-flow modelling, including geothermal screening in data-limited settings. The workflow is implemented as an automated, FOSS  Python package (thermo-profiler) to support reproducible thermal characterization from legacy and modern wireline datasets.




## Statement of need


## State of the field


## Key functions


## Package Design

## Other resources


## Availability



# Acknowledgements


# References
