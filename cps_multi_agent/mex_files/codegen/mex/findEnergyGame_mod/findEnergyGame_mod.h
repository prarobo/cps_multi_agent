/*
 * findEnergyGame_mod.h
 *
 * Code generation for function 'findEnergyGame_mod'
 *
 */

#ifndef __FINDENERGYGAME_MOD_H__
#define __FINDENERGYGAME_MOD_H__

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
extern void eml_li_find(const emlrtStack *sp, const emxArray_boolean_T *x,
  emxArray_int32_T *y);
extern void findEnergyGame_mod(const emlrtStack *sp, const emxArray_boolean_T
  *trans, const emxArray_real_T *F, const emxArray_real_T *S, const
  emxArray_real_T *turn, emxArray_real_T *dist, emxArray_real_T *FStar);

#endif

/* End of code generation (findEnergyGame_mod.h) */
