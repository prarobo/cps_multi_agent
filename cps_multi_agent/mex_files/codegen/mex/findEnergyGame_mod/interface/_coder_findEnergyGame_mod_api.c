/*
 * _coder_findEnergyGame_mod_api.c
 *
 * Code generation for function '_coder_findEnergyGame_mod_api'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "_coder_findEnergyGame_mod_api.h"
#include "findEnergyGame_mod_emxutil.h"

/* Variable Definitions */
static emlrtRTEInfo l_emlrtRTEI = { 1, 1, "_coder_findEnergyGame_mod_api", "" };

/* Function Declarations */
static void b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_boolean_T *y);
static const mxArray *b_emlrt_marshallOut(const emxArray_real_T *u);
static void c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *F, const
  char_T *identifier, emxArray_real_T *y);
static void d_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y);
static void e_emlrt_marshallIn(const emlrtStack *sp, const mxArray *S, const
  char_T *identifier, emxArray_real_T *y);
static void emlrt_marshallIn(const emlrtStack *sp, const mxArray *trans, const
  char_T *identifier, emxArray_boolean_T *y);
static const mxArray *emlrt_marshallOut(const emxArray_real_T *u);
static void f_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y);
static void g_emlrt_marshallIn(const emlrtStack *sp, const mxArray *turn, const
  char_T *identifier, emxArray_real_T *y);
static void h_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y);
static void i_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_boolean_T *ret);
static void j_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret);
static void k_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret);
static void l_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret);

/* Function Definitions */
static void b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_boolean_T *y)
{
  i_emlrt_marshallIn(sp, emlrtAlias(u), parentId, y);
  emlrtDestroyArray(&u);
}

static const mxArray *b_emlrt_marshallOut(const emxArray_real_T *u)
{
  const mxArray *y;
  static const int32_T iv9[2] = { 0, 0 };

  const mxArray *m5;
  y = NULL;
  m5 = emlrtCreateNumericArray(2, iv9, mxDOUBLE_CLASS, mxREAL);
  mxSetData((mxArray *)m5, (void *)u->data);
  emlrtSetDimensions((mxArray *)m5, u->size, 2);
  emlrtAssign(&y, m5);
  return y;
}

static void c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *F, const
  char_T *identifier, emxArray_real_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  d_emlrt_marshallIn(sp, emlrtAlias(F), &thisId, y);
  emlrtDestroyArray(&F);
}

static void d_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y)
{
  j_emlrt_marshallIn(sp, emlrtAlias(u), parentId, y);
  emlrtDestroyArray(&u);
}

static void e_emlrt_marshallIn(const emlrtStack *sp, const mxArray *S, const
  char_T *identifier, emxArray_real_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  f_emlrt_marshallIn(sp, emlrtAlias(S), &thisId, y);
  emlrtDestroyArray(&S);
}

static void emlrt_marshallIn(const emlrtStack *sp, const mxArray *trans, const
  char_T *identifier, emxArray_boolean_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  b_emlrt_marshallIn(sp, emlrtAlias(trans), &thisId, y);
  emlrtDestroyArray(&trans);
}

static const mxArray *emlrt_marshallOut(const emxArray_real_T *u)
{
  const mxArray *y;
  static const int32_T iv8[1] = { 0 };

  const mxArray *m4;
  y = NULL;
  m4 = emlrtCreateNumericArray(1, iv8, mxDOUBLE_CLASS, mxREAL);
  mxSetData((mxArray *)m4, (void *)u->data);
  emlrtSetDimensions((mxArray *)m4, u->size, 1);
  emlrtAssign(&y, m4);
  return y;
}

static void f_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y)
{
  k_emlrt_marshallIn(sp, emlrtAlias(u), parentId, y);
  emlrtDestroyArray(&u);
}

static void g_emlrt_marshallIn(const emlrtStack *sp, const mxArray *turn, const
  char_T *identifier, emxArray_real_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  h_emlrt_marshallIn(sp, emlrtAlias(turn), &thisId, y);
  emlrtDestroyArray(&turn);
}

static void h_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId, emxArray_real_T *y)
{
  l_emlrt_marshallIn(sp, emlrtAlias(u), parentId, y);
  emlrtDestroyArray(&u);
}

static void i_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_boolean_T *ret)
{
  int32_T iv10[2];
  boolean_T bv0[2];
  int32_T i;
  int32_T iv11[2];
  for (i = 0; i < 2; i++) {
    iv10[i] = -1;
    bv0[i] = true;
  }

  emlrtCheckVsBuiltInR2012b(sp, msgId, src, "logical", false, 2U, iv10, bv0,
    iv11);
  ret->size[0] = iv11[0];
  ret->size[1] = iv11[1];
  ret->allocatedSize = ret->size[0] * ret->size[1];
  ret->data = (boolean_T *)mxGetData(src);
  ret->canFreeData = false;
  emlrtDestroyArray(&src);
}

static void j_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret)
{
  int32_T iv12[2];
  boolean_T bv1[2];
  int32_T i4;
  static const boolean_T bv2[2] = { false, true };

  int32_T iv13[2];
  for (i4 = 0; i4 < 2; i4++) {
    iv12[i4] = 1 + -2 * i4;
    bv1[i4] = bv2[i4];
  }

  emlrtCheckVsBuiltInR2012b(sp, msgId, src, "double", false, 2U, iv12, bv1, iv13);
  ret->size[0] = iv13[0];
  ret->size[1] = iv13[1];
  ret->allocatedSize = ret->size[0] * ret->size[1];
  ret->data = (real_T *)mxGetData(src);
  ret->canFreeData = false;
  emlrtDestroyArray(&src);
}

static void k_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret)
{
  int32_T iv14[2];
  boolean_T bv3[2];
  int32_T i5;
  static const boolean_T bv4[2] = { true, false };

  int32_T iv15[2];
  for (i5 = 0; i5 < 2; i5++) {
    iv14[i5] = 3 * i5 - 1;
    bv3[i5] = bv4[i5];
  }

  emlrtCheckVsBuiltInR2012b(sp, msgId, src, "double", false, 2U, iv14, bv3, iv15);
  ret->size[0] = iv15[0];
  ret->size[1] = iv15[1];
  ret->allocatedSize = ret->size[0] * ret->size[1];
  ret->data = (real_T *)mxGetData(src);
  ret->canFreeData = false;
  emlrtDestroyArray(&src);
}

static void l_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src, const
  emlrtMsgIdentifier *msgId, emxArray_real_T *ret)
{
  int32_T iv16[1];
  boolean_T bv5[1];
  int32_T iv17[1];
  iv16[0] = -1;
  bv5[0] = true;
  emlrtCheckVsBuiltInR2012b(sp, msgId, src, "double", false, 1U, iv16, bv5, iv17);
  ret->size[0] = iv17[0];
  ret->allocatedSize = ret->size[0];
  ret->data = (real_T *)mxGetData(src);
  ret->canFreeData = false;
  emlrtDestroyArray(&src);
}

void findEnergyGame_mod_api(const mxArray * const prhs[4], const mxArray *plhs[2])
{
  emxArray_boolean_T *trans;
  emxArray_real_T *F;
  emxArray_real_T *S;
  emxArray_real_T *turn;
  emxArray_real_T *dist;
  emxArray_real_T *FStar;
  emlrtStack st = { NULL, NULL, NULL };

  st.tls = emlrtRootTLSGlobal;
  emlrtHeapReferenceStackEnterFcnR2012b(&st);
  emxInit_boolean_T(&st, &trans, 2, &l_emlrtRTEI, true);
  b_emxInit_real_T(&st, &F, 2, &l_emlrtRTEI, true);
  b_emxInit_real_T(&st, &S, 2, &l_emlrtRTEI, true);
  emxInit_real_T(&st, &turn, 1, &l_emlrtRTEI, true);
  emxInit_real_T(&st, &dist, 1, &l_emlrtRTEI, true);
  b_emxInit_real_T(&st, &FStar, 2, &l_emlrtRTEI, true);

  /* Marshall function inputs */
  emlrt_marshallIn(&st, emlrtAlias(prhs[0]), "trans", trans);
  c_emlrt_marshallIn(&st, emlrtAlias(prhs[1]), "F", F);
  e_emlrt_marshallIn(&st, emlrtAlias(prhs[2]), "S", S);
  g_emlrt_marshallIn(&st, emlrtAlias(prhs[3]), "turn", turn);

  /* Invoke the target function */
  findEnergyGame_mod(&st, trans, F, S, turn, dist, FStar);

  /* Marshall function outputs */
  plhs[0] = emlrt_marshallOut(dist);
  plhs[1] = b_emlrt_marshallOut(FStar);
  FStar->canFreeData = false;
  emxFree_real_T(&FStar);
  dist->canFreeData = false;
  emxFree_real_T(&dist);
  turn->canFreeData = false;
  emxFree_real_T(&turn);
  S->canFreeData = false;
  emxFree_real_T(&S);
  F->canFreeData = false;
  emxFree_real_T(&F);
  trans->canFreeData = false;
  emxFree_boolean_T(&trans);
  emlrtHeapReferenceStackLeaveFcnR2012b(&st);
}

/* End of code generation (_coder_findEnergyGame_mod_api.c) */
