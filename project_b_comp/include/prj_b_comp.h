#pragma once

#ifdef _WIN32
  #define prj_b_comp_EXPORT __declspec(dllexport)
#else
  #define prj_b_comp_EXPORT
#endif

prj_b_comp_EXPORT void prj_b_comp();
