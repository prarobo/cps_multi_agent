/*
 * findEnergyGame_mod_initialize.c
 *
 * Code generation for function 'findEnergyGame_mod_initialize'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "findEnergyGame_mod_initialize.h"
#include "findEnergyGame_mod_data.h"

/* Function Definitions */
void findEnergyGame_mod_initialize(emlrtContext *aContext)
{
  emlrtStack st = { NULL, NULL, NULL };

  emlrtBreakCheckR2012bFlagVar = emlrtGetBreakCheckFlagAddressR2012b();
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, aContext, NULL, 1);
  st.tls = emlrtRootTLSGlobal;
  emlrtClearAllocCountR2012b(&st, false, 0U, 0);
  emlrtEnterRtStackR2012b(&st);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

/* End of code generation (findEnergyGame_mod_initialize.c) */
