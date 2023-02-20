#pragma once

#ifdef _WIN32
  #define prj_a_comp_EXPORT __declspec(dllexport)
#else
  #define prj_a_comp_EXPORT
#endif

prj_a_comp_EXPORT void prj_a_comp();
