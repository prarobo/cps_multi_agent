/*
 * dijkstraGameEff_mod.h
 *
 * Code generation for function 'dijkstraGameEff_mod'
 *
 */

#ifndef __DIJKSTRAGAMEEFF_MOD_H__
#define __DIJKSTRAGAMEEFF_MOD_H__

/* Include files */
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include "mwmathutil.h"
#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"
#include "blas.h"
#include "rtwtypes.h"
#include "findEnergyGame_mod_types.h"

/* Function Declarations */
extern void dijkstraGameEff_mod(const emlrtStack *sp, const emxArray_boolean_T
  *TM_old, const emxArray_real_T *F, const emxArray_real_T *turn,
  emxArray_real_T *dist);

#endif

/* End of code generation (dijkstraGameEff_mod.h) */
