/*
 * findEnergyGame_mod_mexutil.c
 *
 * Code generation for function 'findEnergyGame_mod_mexutil'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "findEnergyGame_mod_mexutil.h"

/* Function Definitions */
void error(const emlrtStack *sp, const mxArray *b, emlrtMCInfo *location)
{
  const mxArray *pArray;
  pArray = b;
  emlrtCallMATLABR2012b(sp, 0, NULL, 1, &pArray, "error", true, location);
}

const mxArray *message(const emlrtStack *sp, const mxArray *b, emlrtMCInfo
  *location)
{
  const mxArray *pArray;
  const mxArray *m6;
  pArray = b;
  return emlrtCallMATLABR2012b(sp, 1, &m6, 1, &pArray, "message", true, location);
}

/* End of code generation (findEnergyGame_mod_mexutil.c) */
