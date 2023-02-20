#pragma once

#ifdef _WIN32
  #define prj_b_EXPORT __declspec(dllexport)
#else
  #define prj_b_EXPORT
#endif

prj_b_EXPORT void prj_b();
