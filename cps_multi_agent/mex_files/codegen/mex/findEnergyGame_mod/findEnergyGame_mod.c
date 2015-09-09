/*
 * findEnergyGame_mod.c
 *
 * Code generation for function 'findEnergyGame_mod'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "findEnergyGame_mod_emxutil.h"
#include "eml_int_forloop_overflow_check.h"
#include "dijkstraGameEff_mod.h"
#include "findEnergyGame_mod_mexutil.h"
#include "findEnergyGame_mod_data.h"

/* Variable Definitions */
static emlrtRSInfo emlrtRSI = { 7, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo b_emlrtRSI = { 13, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo c_emlrtRSI = { 14, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo d_emlrtRSI = { 17, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo e_emlrtRSI = { 18, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo f_emlrtRSI = { 25, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRSInfo bb_emlrtRSI = { 11, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtRSInfo cb_emlrtRSI = { 26, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtRSInfo db_emlrtRSI = { 39, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtRSInfo gb_emlrtRSI = { 16, "min",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/min.m" };

static emlrtRSInfo hb_emlrtRSI = { 61, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtMCInfo f_emlrtMCI = { 14, 5, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtMCInfo i_emlrtMCI = { 18, 9, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtMCInfo j_emlrtMCI = { 17, 19, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtMCInfo k_emlrtMCI = { 23, 9, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtMCInfo l_emlrtMCI = { 20, 19, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtRTEInfo emlrtRTEI = { 1, 26, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRTEInfo b_emlrtRTEI = { 7, 1, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRTEInfo c_emlrtRTEI = { 16, 13, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtRTEInfo k_emlrtRTEI = { 17, 9, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtDCInfo emlrtDCI = { 13, 25, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  1 };

static emlrtBCInfo emlrtBCI = { -1, -1, 13, 25, "trans", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtECInfo emlrtECI = { -1, 13, 17, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtDCInfo b_emlrtDCI = { 14, 28, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  1 };

static emlrtBCInfo b_emlrtBCI = { -1, -1, 14, 28, "trans", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtECInfo b_emlrtECI = { -1, 14, 20, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtBCInfo c_emlrtBCI = { -1, -1, 16, 21, "FStar", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo d_emlrtBCI = { -1, -1, 18, 13, "FStar", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtECInfo c_emlrtECI = { -1, 18, 13, "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m"
};

static emlrtBCInfo e_emlrtBCI = { -1, -1, 19, 13, "FStar", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo f_emlrtBCI = { -1, -1, 25, 34, "FStar", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo g_emlrtBCI = { -1, -1, 13, 25, "F", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo h_emlrtBCI = { -1, -1, 13, 17, "d", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo i_emlrtBCI = { -1, -1, 14, 28, "F", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo j_emlrtBCI = { -1, -1, 14, 20, "d", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo k_emlrtBCI = { -1, -1, 16, 38, "F", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtBCInfo l_emlrtBCI = { -1, -1, 18, 31, "FStar", "findEnergyGame_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/findEnergyGame_mod.m",
  0 };

static emlrtDCInfo f_emlrtDCI = { 17, 37, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m", 4 };

static emlrtRSInfo ib_emlrtRSI = { 14, "eml_li_find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_li_find.m" };

static emlrtRSInfo nb_emlrtRSI = { 20, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtRSInfo ob_emlrtRSI = { 17, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtRSInfo sb_emlrtRSI = { 23, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

static emlrtRSInfo tb_emlrtRSI = { 18, "sum",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/sum.m" };

/* Function Definitions */
void eml_li_find(const emlrtStack *sp, const emxArray_boolean_T *x,
                 emxArray_int32_T *y)
{
  int32_T k;
  boolean_T overflow;
  int32_T i;
  const mxArray *b_y;
  const mxArray *m3;
  int32_T j;
  emlrtStack st;
  emlrtStack b_st;
  emlrtStack c_st;
  st.prev = sp;
  st.tls = sp->tls;
  st.site = &bb_emlrtRSI;
  b_st.prev = &st;
  b_st.tls = st.tls;
  c_st.prev = &b_st;
  c_st.tls = b_st.tls;
  k = 0;
  b_st.site = &db_emlrtRSI;
  if (1 > x->size[1]) {
    overflow = false;
  } else {
    overflow = (x->size[1] > 2147483646);
  }

  if (overflow) {
    c_st.site = &p_emlrtRSI;
    check_forloop_overflow_error(&c_st);
  }

  for (i = 1; i <= x->size[1]; i++) {
    if (x->data[i - 1]) {
      k++;
    }
  }

  if (k <= x->size[1]) {
  } else {
    b_y = NULL;
    m3 = emlrtCreateString("Assertion failed.");
    emlrtAssign(&b_y, m3);
    st.site = &ib_emlrtRSI;
    error(&st, b_y, &f_emlrtMCI);
  }

  emlrtNonNegativeCheckFastR2012b(k, &f_emlrtDCI, sp);
  j = y->size[0] * y->size[1];
  y->size[0] = 1;
  y->size[1] = k;
  emxEnsureCapacity(sp, (emxArray__common *)y, j, (int32_T)sizeof(int32_T),
                    &k_emlrtRTEI);
  j = 0;
  st.site = &cb_emlrtRSI;
  for (i = 1; i <= x->size[1]; i++) {
    if (x->data[i - 1]) {
      y->data[j] = i;
      j++;
    }
  }
}

void findEnergyGame_mod(const emlrtStack *sp, const emxArray_boolean_T *trans,
  const emxArray_real_T *F, const emxArray_real_T *S, const emxArray_real_T
  *turn, emxArray_real_T *dist, emxArray_real_T *FStar)
{
  emxArray_real_T *d;
  int32_T i0;
  int32_T loop_ub;
  real_T numInd;
  int32_T i;
  emxArray_boolean_T *ind;
  emxArray_int32_T *r0;
  emxArray_real_T *r1;
  emxArray_boolean_T *b_trans;
  emxArray_boolean_T *c_trans;
  emxArray_int32_T *r2;
  emxArray_int32_T *r3;
  emxArray_int32_T *r4;
  emxArray_int32_T *r5;
  emxArray_int32_T *r6;
  emxArray_int32_T *r7;
  emxArray_int32_T *r8;
  emxArray_int32_T *r9;
  real_T mtmp;
  int32_T b_i;
  int32_T ind_idx_0;
  boolean_T guard2 = false;
  boolean_T overflow;
  const mxArray *y;
  static const int32_T iv0[2] = { 1, 36 };

  const mxArray *m0;
  char_T cv0[36];
  static const char_T cv1[36] = { 'C', 'o', 'd', 'e', 'r', ':', 't', 'o', 'o',
    'l', 'b', 'o', 'x', ':', 'a', 'u', 't', 'o', 'D', 'i', 'm', 'I', 'n', 'c',
    'o', 'm', 'p', 'a', 't', 'i', 'b', 'i', 'l', 'i', 't', 'y' };

  const mxArray *b_y;
  static const int32_T iv1[2] = { 1, 39 };

  char_T cv2[39];
  static const char_T cv3[39] = { 'C', 'o', 'd', 'e', 'r', ':', 't', 'o', 'o',
    'l', 'b', 'o', 'x', ':', 'e', 'm', 'l', '_', 'm', 'i', 'n', '_', 'o', 'r',
    '_', 'm', 'a', 'x', '_', 'v', 'a', 'r', 'D', 'i', 'm', 'Z', 'e', 'r', 'o' };

  int32_T exitg3;
  boolean_T p;
  int32_T exitg2;
  const mxArray *c_y;
  static const int32_T iv2[2] = { 1, 30 };

  char_T cv4[30];
  static const char_T cv5[30] = { 'C', 'o', 'd', 'e', 'r', ':', 't', 'o', 'o',
    'l', 'b', 'o', 'x', ':', 's', 'u', 'm', '_', 's', 'p', 'e', 'c', 'i', 'a',
    'l', 'E', 'm', 'p', 't', 'y' };

  boolean_T guard1 = false;
  const mxArray *d_y;
  static const int32_T iv3[2] = { 1, 36 };

  int32_T exitg1;
  int32_T i1;
  emxArray_real_T *b_FStar;
  emlrtStack st;
  emlrtStack b_st;
  emlrtStack c_st;
  emlrtStack d_st;
  emlrtStack e_st;
  emlrtStack f_st;
  emlrtStack g_st;
  emlrtStack h_st;
  (void)S;
  st.prev = sp;
  st.tls = sp->tls;
  b_st.prev = &st;
  b_st.tls = st.tls;
  c_st.prev = &b_st;
  c_st.tls = b_st.tls;
  d_st.prev = &c_st;
  d_st.tls = c_st.tls;
  e_st.prev = &c_st;
  e_st.tls = c_st.tls;
  f_st.prev = &d_st;
  f_st.tls = d_st.tls;
  g_st.prev = &f_st;
  g_st.tls = f_st.tls;
  h_st.prev = &st;
  h_st.tls = st.tls;
  emlrtHeapReferenceStackEnterFcnR2012b(sp);
  emxInit_real_T(sp, &d, 1, &b_emlrtRTEI, true);

  /* function takes transition relation, accepting states, and states and returns a vector */
  /* of distance to acceptance */
  /* cardinality of F */
  st.site = &emlrtRSI;
  dijkstraGameEff_mod(&st, trans, F, turn, d);

  /* call djikstra for each final state */
  i0 = FStar->size[0] * FStar->size[1];
  FStar->size[0] = 1;
  FStar->size[1] = F->size[1];
  emxEnsureCapacity(sp, (emxArray__common *)FStar, i0, (int32_T)sizeof(real_T),
                    &emlrtRTEI);
  loop_ub = F->size[0] * F->size[1];
  for (i0 = 0; i0 < loop_ub; i0++) {
    FStar->data[i0] = F->data[i0];
  }

  /* set FStar to F then prune */
  numInd = F->size[1];
  i = 1;
  emxInit_boolean_T(sp, &ind, 2, &c_emlrtRTEI, true);
  emxInit_int32_T(sp, &r0, 2, &emlrtRTEI, true);
  b_emxInit_real_T(sp, &r1, 2, &emlrtRTEI, true);
  emxInit_boolean_T(sp, &b_trans, 2, &emlrtRTEI, true);
  emxInit_boolean_T(sp, &c_trans, 2, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r2, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r3, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r4, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r5, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r6, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r7, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r8, 1, &emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r9, 1, &emlrtRTEI, true);
  while (i - 1 <= F->size[1] - 1) {
    loop_ub = trans->size[1];
    i0 = F->size[1];
    mtmp = F->data[emlrtDynamicBoundsCheckFastR2012b(i, 1, i0, &g_emlrtBCI, sp)
      - 1];
    i0 = trans->size[0];
    b_i = (int32_T)emlrtIntegerCheckFastR2012b(mtmp, &emlrtDCI, sp);
    b_i = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &emlrtBCI, sp);
    i0 = c_trans->size[0] * c_trans->size[1];
    c_trans->size[0] = 1;
    c_trans->size[1] = loop_ub;
    emxEnsureCapacity(sp, (emxArray__common *)c_trans, i0, (int32_T)sizeof
                      (boolean_T), &emlrtRTEI);
    for (i0 = 0; i0 < loop_ub; i0++) {
      c_trans->data[c_trans->size[0] * i0] = (trans->data[(b_i + trans->size[0] *
        i0) - 1] == 1);
    }

    st.site = &b_emlrtRSI;
    eml_li_find(&st, c_trans, r0);
    emlrtVectorVectorIndexCheckR2012b(d->size[0], 1, 1, r0->size[1], &emlrtECI,
      sp);
    loop_ub = r0->size[0] * r0->size[1];
    for (i0 = 0; i0 < loop_ub; i0++) {
      b_i = d->size[0];
      ind_idx_0 = r0->data[i0];
      emlrtDynamicBoundsCheckFastR2012b(ind_idx_0, 1, b_i, &h_emlrtBCI, sp);
    }

    if (!(r0->size[1] == 0)) {
      loop_ub = trans->size[1];
      i0 = F->size[1];
      mtmp = F->data[emlrtDynamicBoundsCheckFastR2012b(i, 1, i0, &i_emlrtBCI, sp)
        - 1];
      i0 = trans->size[0];
      b_i = (int32_T)emlrtIntegerCheckFastR2012b(mtmp, &b_emlrtDCI, sp);
      b_i = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &b_emlrtBCI, sp);
      i0 = b_trans->size[0] * b_trans->size[1];
      b_trans->size[0] = 1;
      b_trans->size[1] = loop_ub;
      emxEnsureCapacity(sp, (emxArray__common *)b_trans, i0, (int32_T)sizeof
                        (boolean_T), &emlrtRTEI);
      for (i0 = 0; i0 < loop_ub; i0++) {
        b_trans->data[b_trans->size[0] * i0] = (trans->data[(b_i + trans->size[0]
          * i0) - 1] == 1);
      }

      st.site = &c_emlrtRSI;
      eml_li_find(&st, b_trans, r0);
      emlrtVectorVectorIndexCheckR2012b(d->size[0], 1, 1, r0->size[1],
        &b_emlrtECI, sp);
      st.site = &c_emlrtRSI;
      loop_ub = r0->size[0] * r0->size[1];
      for (i0 = 0; i0 < loop_ub; i0++) {
        b_i = d->size[0];
        ind_idx_0 = r0->data[i0];
        emlrtDynamicBoundsCheckFastR2012b(ind_idx_0, 1, b_i, &j_emlrtBCI, &st);
      }

      b_st.site = &gb_emlrtRSI;
      c_st.site = &fb_emlrtRSI;
      i0 = r2->size[0];
      r2->size[0] = r0->size[1];
      emxEnsureCapacity(&c_st, (emxArray__common *)r2, i0, (int32_T)sizeof
                        (int32_T), &emlrtRTEI);
      loop_ub = r0->size[1];
      for (i0 = 0; i0 < loop_ub; i0++) {
        r2->data[i0] = r0->data[r0->size[0] * i0];
      }

      guard2 = false;
      if (r2->size[0] == 1) {
        guard2 = true;
      } else {
        i0 = r3->size[0];
        r3->size[0] = r0->size[1];
        emxEnsureCapacity(&c_st, (emxArray__common *)r3, i0, (int32_T)sizeof
                          (int32_T), &emlrtRTEI);
        loop_ub = r0->size[1];
        for (i0 = 0; i0 < loop_ub; i0++) {
          r3->data[i0] = r0->data[r0->size[0] * i0];
        }

        if (r3->size[0] != 1) {
          guard2 = true;
        } else {
          overflow = false;
        }
      }

      if (guard2) {
        overflow = true;
      }

      if (overflow) {
      } else {
        y = NULL;
        m0 = emlrtCreateCharArray(2, iv0);
        for (b_i = 0; b_i < 36; b_i++) {
          cv0[b_i] = cv1[b_i];
        }

        emlrtInitCharArrayR2013a(&c_st, 36, m0, cv0);
        emlrtAssign(&y, m0);
        d_st.site = &lb_emlrtRSI;
        e_st.site = &rb_emlrtRSI;
        error(&d_st, message(&e_st, y, &c_emlrtMCI), &d_emlrtMCI);
      }

      i0 = r4->size[0];
      r4->size[0] = r0->size[1];
      emxEnsureCapacity(&c_st, (emxArray__common *)r4, i0, (int32_T)sizeof
                        (int32_T), &emlrtRTEI);
      loop_ub = r0->size[1];
      for (i0 = 0; i0 < loop_ub; i0++) {
        r4->data[i0] = r0->data[r0->size[0] * i0];
      }

      if (r4->size[0] > 0) {
      } else {
        b_y = NULL;
        m0 = emlrtCreateCharArray(2, iv1);
        for (b_i = 0; b_i < 39; b_i++) {
          cv2[b_i] = cv3[b_i];
        }

        emlrtInitCharArrayR2013a(&c_st, 39, m0, cv2);
        emlrtAssign(&b_y, m0);
        d_st.site = &kb_emlrtRSI;
        e_st.site = &qb_emlrtRSI;
        error(&d_st, message(&e_st, b_y, &g_emlrtMCI), &h_emlrtMCI);
      }

      d_st.site = &s_emlrtRSI;
      mtmp = d->data[r0->data[0] - 1];
      i0 = r5->size[0];
      r5->size[0] = r0->size[1];
      emxEnsureCapacity(&d_st, (emxArray__common *)r5, i0, (int32_T)sizeof
                        (int32_T), &emlrtRTEI);
      loop_ub = r0->size[1];
      for (i0 = 0; i0 < loop_ub; i0++) {
        r5->data[i0] = r0->data[r0->size[0] * i0];
      }

      if (r5->size[0] > 1) {
        i0 = r6->size[0];
        r6->size[0] = r0->size[1];
        emxEnsureCapacity(&d_st, (emxArray__common *)r6, i0, (int32_T)sizeof
                          (int32_T), &emlrtRTEI);
        loop_ub = r0->size[1];
        for (i0 = 0; i0 < loop_ub; i0++) {
          r6->data[i0] = r0->data[r0->size[0] * i0];
        }

        if (1 < r6->size[0]) {
          f_st.site = &t_emlrtRSI;
          i0 = r7->size[0];
          r7->size[0] = r0->size[1];
          emxEnsureCapacity(&f_st, (emxArray__common *)r7, i0, (int32_T)sizeof
                            (int32_T), &emlrtRTEI);
          loop_ub = r0->size[1];
          for (i0 = 0; i0 < loop_ub; i0++) {
            r7->data[i0] = r0->data[r0->size[0] * i0];
          }

          if (2 > r7->size[0]) {
            overflow = false;
          } else {
            i0 = r8->size[0];
            r8->size[0] = r0->size[1];
            emxEnsureCapacity(&f_st, (emxArray__common *)r8, i0, (int32_T)sizeof
                              (int32_T), &emlrtRTEI);
            loop_ub = r0->size[1];
            for (i0 = 0; i0 < loop_ub; i0++) {
              r8->data[i0] = r0->data[r0->size[0] * i0];
            }

            overflow = (r8->size[0] > 2147483646);
          }

          if (overflow) {
            g_st.site = &p_emlrtRSI;
            check_forloop_overflow_error(&g_st);
          }

          b_i = 1;
          do {
            exitg3 = 0;
            i0 = r9->size[0];
            r9->size[0] = r0->size[1];
            emxEnsureCapacity(&d_st, (emxArray__common *)r9, i0, (int32_T)sizeof
                              (int32_T), &emlrtRTEI);
            loop_ub = r0->size[1];
            for (i0 = 0; i0 < loop_ub; i0++) {
              r9->data[i0] = r0->data[r0->size[0] * i0];
            }

            if (b_i + 1 <= r9->size[0]) {
              if (d->data[r0->data[r0->size[0] * b_i] - 1] < mtmp) {
                mtmp = d->data[r0->data[r0->size[0] * b_i] - 1];
              }

              b_i++;
            } else {
              exitg3 = 1;
            }
          } while (exitg3 == 0);
        }
      }

      if (mtmp == rtInf) {
        if (1.0 > numInd) {
          loop_ub = 0;
        } else {
          i0 = FStar->size[1];
          emlrtDynamicBoundsCheckFastR2012b(1, 1, i0, &c_emlrtBCI, sp);
          i0 = FStar->size[1];
          b_i = (int32_T)numInd;
          loop_ub = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &c_emlrtBCI,
            sp);
        }

        i0 = F->size[1];
        mtmp = F->data[emlrtDynamicBoundsCheckFastR2012b(i, 1, i0, &k_emlrtBCI,
          sp) - 1];
        i0 = ind->size[0] * ind->size[1];
        ind->size[0] = 1;
        ind->size[1] = loop_ub;
        emxEnsureCapacity(sp, (emxArray__common *)ind, i0, (int32_T)sizeof
                          (boolean_T), &emlrtRTEI);
        for (i0 = 0; i0 < loop_ub; i0++) {
          ind->data[ind->size[0] * i0] = !(FStar->data[i0] == mtmp);
        }

        st.site = &d_emlrtRSI;
        overflow = false;
        p = false;
        b_i = 0;
        do {
          exitg2 = 0;
          if (b_i < 2) {
            if (b_i + 1 <= 1) {
              ind_idx_0 = ind->size[1];
            } else {
              ind_idx_0 = 1;
            }

            if (ind_idx_0 != 0) {
              exitg2 = 1;
            } else {
              b_i++;
            }
          } else {
            p = true;
            exitg2 = 1;
          }
        } while (exitg2 == 0);

        if (!p) {
        } else {
          overflow = true;
        }

        if (!overflow) {
        } else {
          c_y = NULL;
          m0 = emlrtCreateCharArray(2, iv2);
          for (b_i = 0; b_i < 30; b_i++) {
            cv4[b_i] = cv5[b_i];
          }

          emlrtInitCharArrayR2013a(&st, 30, m0, cv4);
          emlrtAssign(&c_y, m0);
          b_st.site = &ob_emlrtRSI;
          h_st.site = &tb_emlrtRSI;
          error(&b_st, message(&h_st, c_y, &i_emlrtMCI), &j_emlrtMCI);
        }

        ind_idx_0 = ind->size[1];
        guard1 = false;
        if (ind_idx_0 == 1) {
          guard1 = true;
        } else {
          ind_idx_0 = ind->size[1];
          if (ind_idx_0 != 1) {
            guard1 = true;
          } else {
            overflow = false;
          }
        }

        if (guard1) {
          overflow = true;
        }

        if (overflow) {
        } else {
          d_y = NULL;
          m0 = emlrtCreateCharArray(2, iv3);
          for (b_i = 0; b_i < 36; b_i++) {
            cv0[b_i] = cv1[b_i];
          }

          emlrtInitCharArrayR2013a(&st, 36, m0, cv0);
          emlrtAssign(&d_y, m0);
          b_st.site = &nb_emlrtRSI;
          h_st.site = &sb_emlrtRSI;
          error(&b_st, message(&h_st, d_y, &k_emlrtMCI), &l_emlrtMCI);
        }

        ind_idx_0 = ind->size[1];
        if (ind_idx_0 == 0) {
          numInd = 0.0;
        } else {
          numInd = ind->data[0];
          b_st.site = &hb_emlrtRSI;
          ind_idx_0 = ind->size[1];
          if (2 > ind_idx_0) {
            overflow = false;
          } else {
            ind_idx_0 = ind->size[1];
            overflow = (ind_idx_0 > 2147483646);
          }

          if (overflow) {
            c_st.site = &p_emlrtRSI;
            check_forloop_overflow_error(&c_st);
          }

          b_i = 2;
          do {
            exitg1 = 0;
            ind_idx_0 = ind->size[1];
            if (b_i <= ind_idx_0) {
              numInd += (real_T)ind->data[b_i - 1];
              b_i++;
            } else {
              exitg1 = 1;
            }
          } while (exitg1 == 0);
        }

        if (1.0 > numInd) {
          i0 = 0;
        } else {
          i0 = FStar->size[1];
          emlrtDynamicBoundsCheckFastR2012b(1, 1, i0, &d_emlrtBCI, sp);
          i0 = FStar->size[1];
          b_i = (int32_T)numInd;
          i0 = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &d_emlrtBCI, sp);
        }

        st.site = &e_emlrtRSI;
        eml_li_find(&st, ind, r0);
        b_i = r1->size[0] * r1->size[1];
        r1->size[0] = 1;
        r1->size[1] = r0->size[1];
        emxEnsureCapacity(sp, (emxArray__common *)r1, b_i, (int32_T)sizeof
                          (real_T), &emlrtRTEI);
        loop_ub = r0->size[0] * r0->size[1];
        for (b_i = 0; b_i < loop_ub; b_i++) {
          ind_idx_0 = FStar->size[1];
          i1 = r0->data[b_i];
          r1->data[b_i] = FStar->data[emlrtDynamicBoundsCheckFastR2012b(i1, 1,
            ind_idx_0, &l_emlrtBCI, sp) - 1];
        }

        b_i = r1->size[1];
        emlrtSizeEqCheck1DFastR2012b(i0, b_i, &c_emlrtECI, sp);
        loop_ub = r1->size[1];
        for (i0 = 0; i0 < loop_ub; i0++) {
          FStar->data[i0] = r1->data[r1->size[0] * i0];
        }

        if ((uint32_T)numInd + 1U > (uint32_T)FStar->size[1]) {
          i0 = 0;
          b_i = 0;
        } else {
          i0 = FStar->size[1];
          b_i = (int32_T)((uint32_T)numInd + 1U);
          i0 = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &e_emlrtBCI, sp) -
            1;
          b_i = FStar->size[1];
          ind_idx_0 = FStar->size[1];
          b_i = emlrtDynamicBoundsCheckFastR2012b(ind_idx_0, 1, b_i, &e_emlrtBCI,
            sp);
        }

        ind_idx_0 = r0->size[0] * r0->size[1];
        r0->size[0] = 1;
        r0->size[1] = b_i - i0;
        emxEnsureCapacity(sp, (emxArray__common *)r0, ind_idx_0, (int32_T)sizeof
                          (int32_T), &emlrtRTEI);
        loop_ub = b_i - i0;
        for (b_i = 0; b_i < loop_ub; b_i++) {
          r0->data[r0->size[0] * b_i] = i0 + b_i;
        }

        loop_ub = r0->size[0] * r0->size[1];
        for (i0 = 0; i0 < loop_ub; i0++) {
          FStar->data[r0->data[i0]] = rtInf;
        }

        /* FStar = setdiff(FStar,F(i)); */
      }
    }

    i++;
    emlrtBreakCheckFastR2012b(emlrtBreakCheckR2012bFlagVar, sp);
  }

  emxFree_int32_T(&r9);
  emxFree_int32_T(&r8);
  emxFree_int32_T(&r7);
  emxFree_int32_T(&r6);
  emxFree_int32_T(&r5);
  emxFree_int32_T(&r4);
  emxFree_int32_T(&r3);
  emxFree_int32_T(&r2);
  emxFree_boolean_T(&c_trans);
  emxFree_boolean_T(&b_trans);
  emxFree_real_T(&r1);
  emxFree_int32_T(&r0);
  emxFree_boolean_T(&ind);
  emxFree_real_T(&d);
  if (1.0 > numInd) {
    loop_ub = 0;
  } else {
    i0 = FStar->size[1];
    emlrtDynamicBoundsCheckFastR2012b(1, 1, i0, &f_emlrtBCI, sp);
    i0 = FStar->size[1];
    b_i = (int32_T)numInd;
    loop_ub = emlrtDynamicBoundsCheckFastR2012b(b_i, 1, i0, &f_emlrtBCI, sp);
  }

  b_emxInit_real_T(sp, &b_FStar, 2, &emlrtRTEI, true);
  i0 = b_FStar->size[0] * b_FStar->size[1];
  b_FStar->size[0] = 1;
  b_FStar->size[1] = loop_ub;
  emxEnsureCapacity(sp, (emxArray__common *)b_FStar, i0, (int32_T)sizeof(real_T),
                    &emlrtRTEI);
  for (i0 = 0; i0 < loop_ub; i0++) {
    b_FStar->data[b_FStar->size[0] * i0] = FStar->data[i0];
  }

  st.site = &f_emlrtRSI;
  dijkstraGameEff_mod(&st, trans, b_FStar, turn, dist);
  emxFree_real_T(&b_FStar);
  emlrtHeapReferenceStackLeaveFcnR2012b(sp);
}

/* End of code generation (findEnergyGame_mod.c) */
