/*
 * _coder_findEnergyGame_mod_mex.c
 *
 * Code generation for function 'findEnergyGame_mod'
 *
 */

/* Include files */
#include "mex.h"
#include "_coder_findEnergyGame_mod_api.h"
#include "findEnergyGame_mod_initialize.h"
#include "findEnergyGame_mod_terminate.h"

/* Function Declarations */
static void findEnergyGame_mod_mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]);

/* Variable Definitions */
emlrtContext emlrtContextGlobal = { true, false, EMLRT_VERSION_INFO, NULL, "findEnergyGame_mod", NULL, false, {2045744189U,2170104910U,2743257031U,4284093946U}, NULL };
void *emlrtRootTLSGlobal = NULL;

/* Function Definitions */
static void findEnergyGame_mod_mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
  const mxArray *outputs[2];
  const mxArray *inputs[4];
  int n = 0;
  int nOutputs = (nlhs < 1 ? 1 : nlhs);
  int nInputs = nrhs;
  emlrtStack st = { NULL, NULL, NULL };
  /* Module initialization. */
  findEnergyGame_mod_initialize(&emlrtContextGlobal);
  st.tls = emlrtRootTLSGlobal;
  /* Check for proper number of arguments. */
  if (nrhs != 4) {
    emlrtErrMsgIdAndTxt(&st, "EMLRT:runTime:WrongNumberOfInputs", 5, mxINT32_CLASS, 4, mxCHAR_CLASS, 18, "findEnergyGame_mod");
  } else if (nlhs > 2) {
    emlrtErrMsgIdAndTxt(&st, "EMLRT:runTime:TooManyOutputArguments", 3, mxCHAR_CLASS, 18, "findEnergyGame_mod");
  }
  /* Temporary copy for mex inputs. */
  for (n = 0; n < nInputs; ++n) {
    inputs[n] = prhs[n];
  }
  /* Call the function. */
  findEnergyGame_mod_api(inputs, outputs);
  /* Copy over outputs to the caller. */
  for (n = 0; n < nOutputs; ++n) {
    plhs[n] = emlrtReturnArrayR2009a(outputs[n]);
  }
  /* Module finalization. */
  findEnergyGame_mod_terminate();
}

void findEnergyGame_mod_atexit_wrapper(void)
{
   findEnergyGame_mod_atexit();
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
  /* Initialize the memory manager. */
  mexAtExit(findEnergyGame_mod_atexit_wrapper);
  /* Dispatch the entry-point. */
  findEnergyGame_mod_mexFunction(nlhs, plhs, nrhs, prhs);
}
/* End of code generation (_coder_findEnergyGame_mod_mex.c) */
