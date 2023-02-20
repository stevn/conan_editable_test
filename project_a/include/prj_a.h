#pragma once

#ifdef _WIN32
  #define prj_a_EXPORT __declspec(dllexport)
#else
  #define prj_a_EXPORT
#endif

prj_a_EXPORT void prj_a();
