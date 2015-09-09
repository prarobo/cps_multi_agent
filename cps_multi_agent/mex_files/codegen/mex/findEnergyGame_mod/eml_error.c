/*
 * eml_error.c
 *
 * Code generation for function 'eml_error'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "eml_error.h"

/* Variable Definitions */
static emlrtRTEInfo m_emlrtRTEI = { 20, 5, "eml_error",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_error.m" };

/* Function Definitions */
void eml_error(const emlrtStack *sp)
{
  emlrtErrorWithMessageIdR2012b(sp, &m_emlrtRTEI,
    "Coder:toolbox:ismember_unsortedS", 0);
}

/* End of code generation (eml_error.c) */
