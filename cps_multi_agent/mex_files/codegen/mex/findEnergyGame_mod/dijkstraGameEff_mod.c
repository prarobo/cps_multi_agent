/*
 * dijkstraGameEff_mod.c
 *
 * Code generation for function 'dijkstraGameEff_mod'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "findEnergyGame_mod.h"
#include "dijkstraGameEff_mod.h"
#include "findEnergyGame_mod_emxutil.h"
#include "eml_error.h"
#include "eml_int_forloop_overflow_check.h"
#include "findEnergyGame_mod_mexutil.h"
#include "findEnergyGame_mod_data.h"

/* Variable Definitions */
static emlrtRSInfo g_emlrtRSI = { 45, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRSInfo h_emlrtRSI = { 44, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRSInfo i_emlrtRSI = { 36, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRSInfo j_emlrtRSI = { 26, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRSInfo k_emlrtRSI = { 19, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRSInfo l_emlrtRSI = { 21, "colon",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/colon.m" };

static emlrtRSInfo m_emlrtRSI = { 79, "colon",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/colon.m" };

static emlrtRSInfo n_emlrtRSI = { 283, "colon",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/colon.m" };

static emlrtRSInfo o_emlrtRSI = { 291, "colon",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/colon.m" };

static emlrtRSInfo q_emlrtRSI = { 18, "min",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/min.m" };

static emlrtRSInfo r_emlrtRSI = { 15, "eml_min_or_max",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/eml/eml_min_or_max.m" };

static emlrtRSInfo u_emlrtRSI = { 41, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

static emlrtRSInfo v_emlrtRSI = { 230, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

static emlrtRSInfo w_emlrtRSI = { 33, "ismember",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/ismember.m" };

static emlrtRSInfo x_emlrtRSI = { 108, "ismember",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/ismember.m" };

static emlrtRSInfo y_emlrtRSI = { 109, "ismember",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/ismember.m" };

static emlrtRSInfo ab_emlrtRSI = { 22, "issorted",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/issorted.m" };

static emlrtRSInfo eb_emlrtRSI = { 16, "max",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/datafun/max.m" };

static emlrtMCInfo e_emlrtMCI = { 239, 9, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

static emlrtRTEInfo d_emlrtRTEI = { 1, 19, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRTEInfo e_emlrtRTEI = { 284, 1, "colon",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/ops/colon.m" };

static emlrtRTEInfo f_emlrtRTEI = { 127, 5, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

static emlrtRTEInfo g_emlrtRTEI = { 9, 1, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRTEInfo h_emlrtRTEI = { 19, 1, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRTEInfo i_emlrtRTEI = { 36, 5, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtRTEInfo j_emlrtRTEI = { 33, 6, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

static emlrtECInfo d_emlrtECI = { -1, 51, 8, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtBCInfo m_emlrtBCI = { -1, -1, 51, 8, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtECInfo e_emlrtECI = { -1, 45, 31, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtBCInfo n_emlrtBCI = { -1, -1, 45, 39, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo o_emlrtBCI = { -1, -1, 44, 33, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo p_emlrtBCI = { -1, -1, 38, 13, "ind", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo q_emlrtBCI = { -1, -1, 36, 22, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtECInfo f_emlrtECI = { -1, 31, 5, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtBCInfo r_emlrtBCI = { -1, -1, 31, 5, "Q", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo s_emlrtBCI = { -1, -1, 31, 19, "Q", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo t_emlrtBCI = { -1, -1, 28, 15, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtDCInfo c_emlrtDCI = { 28, 15, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  1 };

static emlrtECInfo g_emlrtECI = { -1, 26, 21, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtBCInfo u_emlrtBCI = { -1, -1, 26, 26, "Q", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo v_emlrtBCI = { -1, -1, 13, 6, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtECInfo h_emlrtECI = { -1, 10, 1, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m"
};

static emlrtBCInfo w_emlrtBCI = { -1, -1, 10, 12, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo x_emlrtBCI = { -1, -1, 10, 4, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo y_emlrtBCI = { -1, -1, 13, 4, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtDCInfo d_emlrtDCI = { 13, 4, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  1 };

static emlrtBCInfo ab_emlrtBCI = { -1, -1, 17, 1, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo bb_emlrtBCI = { -1, -1, 18, 1, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo cb_emlrtBCI = { -1, -1, 26, 21, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtDCInfo e_emlrtDCI = { 26, 21, "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  1 };

static emlrtBCInfo db_emlrtBCI = { -1, -1, 27, 9, "Q", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo eb_emlrtBCI = { -1, -1, 32, 5, "Q", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo fb_emlrtBCI = { -1, -1, 39, 12, "turn", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo gb_emlrtBCI = { -1, -1, 45, 31, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo hb_emlrtBCI = { -1, -1, 45, 17, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo ib_emlrtBCI = { -1, -1, 40, 16, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo jb_emlrtBCI = { -1, -1, 40, 36, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo kb_emlrtBCI = { -1, -1, 40, 39, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo lb_emlrtBCI = { -1, -1, 41, 17, "dist", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo mb_emlrtBCI = { -1, -1, 41, 36, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtBCInfo nb_emlrtBCI = { -1, -1, 41, 39, "TM", "dijkstraGameEff_mod",
  "/home/prasanna/Linux_Workspaces/eclipse_workspace_kepler/cps_multi_agent/mex_files/dijkstraGameEff_mod.m",
  0 };

static emlrtRSInfo mb_emlrtRSI = { 239, "find",
  "/usr/local/MATLAB/R2014a/toolbox/eml/lib/matlab/elmat/find.m" };

/* Function Definitions */
void dijkstraGameEff_mod(const emlrtStack *sp, const emxArray_boolean_T *TM_old,
  const emxArray_real_T *F, const emxArray_real_T *turn, emxArray_real_T *dist)
{
  uint32_T b_TM_old[2];
  uint32_T uv0[2];
  int32_T i2;
  emxArray_real_T *TM;
  int32_T absb;
  int32_T i3;
  int32_T cdiff;
  emxArray_int32_T *ii;
  emxArray_int32_T *r10;
  int32_T b_ii[2];
  real_T absxk;
  int32_T apnd;
  int32_T ndbl;
  int32_T n;
  emxArray_int32_T *r11;
  emxArray_real_T *Q;
  int32_T qInd;
  emxArray_real_T *ind;
  emxArray_boolean_T *x;
  emxArray_boolean_T *b_x;
  emxArray_boolean_T *b_TM;
  emxArray_int32_T *b_Q;
  emxArray_int32_T *c_Q;
  emxArray_int32_T *d_Q;
  emxArray_real_T *e_Q;
  emxArray_int32_T *c_ii;
  emxArray_int32_T *r12;
  emxArray_int32_T *r13;
  emxArray_int32_T *r14;
  emxArray_int32_T *r15;
  emxArray_int32_T *r16;
  emxArray_int32_T *r17;
  emxArray_int32_T *r18;
  emxArray_int32_T *r19;
  boolean_T exitg1;
  real_T mtmp;
  int32_T exitg9;
  real_T u;
  boolean_T overflow;
  boolean_T exitg8;
  boolean_T guard1 = false;
  const mxArray *y;
  const mxArray *m1;
  int32_T j;
  int32_T exitg2;
  int8_T ii_size[2];
  boolean_T exitg7;
  int32_T exitg6;
  boolean_T p;
  boolean_T exitg5;
  int32_T b_ndbl;
  int32_T b_cdiff;
  int32_T exponent;
  boolean_T exitg4;
  int32_T b_exponent;
  boolean_T b_guard1 = false;
  const mxArray *b_y;
  static const int32_T iv4[2] = { 1, 36 };

  char_T cv6[36];
  static const char_T cv7[36] = { 'C', 'o', 'd', 'e', 'r', ':', 't', 'o', 'o',
    'l', 'b', 'o', 'x', ':', 'a', 'u', 't', 'o', 'D', 'i', 'm', 'I', 'n', 'c',
    'o', 'm', 'p', 'a', 't', 'i', 'b', 'i', 'l', 'i', 't', 'y' };

  const mxArray *c_y;
  static const int32_T iv5[2] = { 1, 39 };

  char_T cv8[39];
  static const char_T cv9[39] = { 'C', 'o', 'd', 'e', 'r', ':', 't', 'o', 'o',
    'l', 'b', 'o', 'x', ':', 'e', 'm', 'l', '_', 'm', 'i', 'n', '_', 'o', 'r',
    '_', 'm', 'a', 'x', '_', 'v', 'a', 'r', 'D', 'i', 'm', 'Z', 'e', 'r', 'o' };

  int32_T exitg3;
  emxArray_real_T *b_dist;
  emlrtStack st;
  emlrtStack b_st;
  emlrtStack c_st;
  emlrtStack d_st;
  emlrtStack e_st;
  emlrtStack f_st;
  emlrtStack g_st;
  st.prev = sp;
  st.tls = sp->tls;
  b_st.prev = &st;
  b_st.tls = st.tls;
  c_st.prev = &b_st;
  c_st.tls = b_st.tls;
  d_st.prev = &c_st;
  d_st.tls = c_st.tls;
  e_st.prev = &d_st;
  e_st.tls = d_st.tls;
  f_st.prev = &c_st;
  f_st.tls = c_st.tls;
  g_st.prev = &e_st;
  g_st.tls = e_st.tls;
  emlrtHeapReferenceStackEnterFcnR2012b(sp);

  /* Modified dijkstra's algorithm for a game transition system */
  /*  */
  /* Inputs are a transition matrix (can be sparse), destination node, and */
  /* whose turn it is (1 is robot's turn, 0 is adversary's turn) */
  /*  */
  /* Written by Kevin Leahy March 2015 */
  b_TM_old[0] = (uint32_T)TM_old->size[0];
  b_TM_old[1] = (uint32_T)TM_old->size[1];
  for (i2 = 0; i2 < 2; i2++) {
    uv0[i2] = b_TM_old[i2] + 1U;
  }

  b_emxInit_real_T(sp, &TM, 2, &g_emlrtRTEI, true);
  i2 = TM->size[0] * TM->size[1];
  TM->size[0] = (int32_T)uv0[0];
  emxEnsureCapacity(sp, (emxArray__common *)TM, i2, (int32_T)sizeof(real_T),
                    &d_emlrtRTEI);
  i2 = TM->size[0] * TM->size[1];
  TM->size[1] = (int32_T)uv0[1];
  emxEnsureCapacity(sp, (emxArray__common *)TM, i2, (int32_T)sizeof(real_T),
                    &d_emlrtRTEI);
  absb = (int32_T)uv0[0] * (int32_T)uv0[1];
  for (i2 = 0; i2 < absb; i2++) {
    TM->data[i2] = 0.0;
  }

  if (1 > (int32_T)uv0[0] - 1) {
    absb = 0;
  } else {
    i2 = (int32_T)uv0[0];
    i3 = (int32_T)uv0[0] - 1;
    absb = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &x_emlrtBCI, sp);
  }

  if (1 > (int32_T)uv0[1] - 1) {
    cdiff = 0;
  } else {
    i2 = (int32_T)uv0[1];
    i3 = (int32_T)uv0[1] - 1;
    cdiff = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &w_emlrtBCI, sp);
  }

  b_emxInit_int32_T(sp, &ii, 1, &j_emlrtRTEI, true);
  i2 = ii->size[0];
  ii->size[0] = absb;
  emxEnsureCapacity(sp, (emxArray__common *)ii, i2, (int32_T)sizeof(int32_T),
                    &d_emlrtRTEI);
  for (i2 = 0; i2 < absb; i2++) {
    ii->data[i2] = i2;
  }

  b_emxInit_int32_T(sp, &r10, 1, &d_emlrtRTEI, true);
  i2 = r10->size[0];
  r10->size[0] = cdiff;
  emxEnsureCapacity(sp, (emxArray__common *)r10, i2, (int32_T)sizeof(int32_T),
                    &d_emlrtRTEI);
  for (i2 = 0; i2 < cdiff; i2++) {
    r10->data[i2] = i2;
  }

  b_ii[0] = ii->size[0];
  b_ii[1] = r10->size[0];
  emlrtSubAssignSizeCheckR2012b(b_ii, 2, *(int32_T (*)[2])TM_old->size, 2,
    &h_emlrtECI, sp);
  absb = TM_old->size[1];
  for (i2 = 0; i2 < absb; i2++) {
    cdiff = TM_old->size[0];
    for (i3 = 0; i3 < cdiff; i3++) {
      TM->data[ii->data[i3] + TM->size[0] * r10->data[i2]] = TM_old->data[i3 +
        TM_old->size[0] * i2];
    }
  }

  emxFree_int32_T(&r10);

  /*  TM(end+1,:) = zeros(1,length(TM));%add row and column of zeros to add virtual end node */
  /*  TM(:,end+1) = zeros(length(TM),1); */
  i2 = ii->size[0];
  ii->size[0] = F->size[1];
  emxEnsureCapacity(sp, (emxArray__common *)ii, i2, (int32_T)sizeof(int32_T),
                    &d_emlrtRTEI);
  absb = F->size[1];
  for (i2 = 0; i2 < absb; i2++) {
    i3 = TM->size[0];
    absxk = F->data[F->size[0] * i2];
    apnd = (int32_T)emlrtIntegerCheckFastR2012b(absxk, &d_emlrtDCI, sp);
    ii->data[i2] = emlrtDynamicBoundsCheckFastR2012b(apnd, 1, i3, &y_emlrtBCI,
      sp);
  }

  ndbl = TM->size[1];
  cdiff = TM->size[1];
  emlrtDynamicBoundsCheckFastR2012b(ndbl, 1, cdiff, &v_emlrtBCI, sp);
  cdiff = ii->size[0];
  for (i2 = 0; i2 < cdiff; i2++) {
    TM->data[(ii->data[i2] + TM->size[0] * (ndbl - 1)) - 1] = 1.0;
  }

  /* add transitions to virtual node */
  n = muIntScalarMax_sint32(TM->size[0], TM->size[1]);
  i2 = dist->size[0];
  dist->size[0] = n;
  emxEnsureCapacity(sp, (emxArray__common *)dist, i2, (int32_T)sizeof(real_T),
                    &d_emlrtRTEI);
  for (i2 = 0; i2 < n; i2++) {
    dist->data[i2] = rtInf;
  }

  emxInit_int32_T(sp, &r11, 2, &d_emlrtRTEI, true);

  /* make virtual node destination */
  i2 = dist->size[0];
  dist->data[emlrtDynamicBoundsCheckFastR2012b(n, 1, i2, &ab_emlrtBCI, sp) - 1] =
    0.0;

  /* set dist to virtual node as 0 */
  i2 = r11->size[0] * r11->size[1];
  r11->size[0] = 1;
  r11->size[1] = F->size[1];
  emxEnsureCapacity(sp, (emxArray__common *)r11, i2, (int32_T)sizeof(int32_T),
                    &d_emlrtRTEI);
  absb = F->size[0] * F->size[1];
  for (i2 = 0; i2 < absb; i2++) {
    i3 = dist->size[0];
    apnd = (int32_T)F->data[i2];
    r11->data[i2] = emlrtDynamicBoundsCheckFastR2012b(apnd, 1, i3, &bb_emlrtBCI,
      sp);
  }

  absb = r11->size[0] * r11->size[1];
  for (i2 = 0; i2 < absb; i2++) {
    dist->data[r11->data[i2] - 1] = 0.0;
  }

  /* set dist to final states as 0 */
  st.site = &k_emlrtRSI;
  b_st.site = &l_emlrtRSI;
  c_st.site = &m_emlrtRSI;
  if (n - 1 < 1) {
    ndbl = -1;
    apnd = n - 1;
  } else {
    ndbl = (int32_T)muDoubleScalarFloor((((real_T)n - 1.0) - 1.0) + 0.5);
    apnd = ndbl + 1;
    cdiff = (ndbl - n) + 2;
    absb = (int32_T)muDoubleScalarAbs((real_T)n - 1.0);
    if (muDoubleScalarAbs(cdiff) < 4.4408920985006262E-16 * (real_T)
        muIntScalarMax_sint32(1, absb)) {
      ndbl++;
      apnd = n - 1;
    } else if (cdiff > 0) {
      apnd = ndbl;
    } else {
      ndbl++;
    }

    ndbl--;
  }

  b_emxInit_real_T(&c_st, &Q, 2, &h_emlrtRTEI, true);
  d_st.site = &n_emlrtRSI;
  i2 = Q->size[0] * Q->size[1];
  Q->size[0] = 1;
  Q->size[1] = ndbl + 1;
  emxEnsureCapacity(&c_st, (emxArray__common *)Q, i2, (int32_T)sizeof(real_T),
                    &e_emlrtRTEI);
  if (ndbl + 1 > 0) {
    Q->data[0] = 1.0;
    if (ndbl + 1 > 1) {
      Q->data[ndbl] = apnd;
      i2 = ndbl + (ndbl < 0);
      if (i2 >= 0) {
        cdiff = (int32_T)((uint32_T)i2 >> 1);
      } else {
        cdiff = ~(int32_T)((uint32_T)~i2 >> 1);
      }

      d_st.site = &o_emlrtRSI;
      for (absb = 1; absb < cdiff; absb++) {
        Q->data[absb] = 1.0 + (real_T)absb;
        Q->data[ndbl - absb] = apnd - absb;
      }

      if (cdiff << 1 == ndbl) {
        Q->data[cdiff] = (1.0 + (real_T)apnd) / 2.0;
      } else {
        Q->data[cdiff] = 1.0 + (real_T)cdiff;
        Q->data[cdiff + 1] = apnd - cdiff;
      }
    }
  }

  /* consider all but final node */
  qInd = Q->size[1];

  /*  Q = setdiff(Q,F); %remove final states from Q */
  /*  turnD = turn(dest); %is destination node robot turn? */
  b_emxInit_real_T(sp, &ind, 2, &i_emlrtRTEI, true);
  b_emxInit_boolean_T(sp, &x, 1, &d_emlrtRTEI, true);
  emxInit_boolean_T(sp, &b_x, 2, &d_emlrtRTEI, true);
  emxInit_boolean_T(sp, &b_TM, 2, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &b_Q, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &c_Q, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &d_Q, 1, &d_emlrtRTEI, true);
  b_emxInit_real_T(sp, &e_Q, 2, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &c_ii, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r12, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r13, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r14, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r15, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r16, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r17, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r18, 1, &d_emlrtRTEI, true);
  b_emxInit_int32_T(sp, &r19, 1, &d_emlrtRTEI, true);
  exitg1 = false;
  while ((!exitg1) && (qInd != 0)) {
    /* begin dijkstra */
    i2 = Q->size[1];
    emlrtDynamicBoundsCheckFastR2012b(1, 1, i2, &u_emlrtBCI, sp);
    i2 = Q->size[1];
    emlrtDynamicBoundsCheckFastR2012b(qInd, 1, i2, &u_emlrtBCI, sp);
    i2 = ind->size[0] * ind->size[1];
    ind->size[0] = 1;
    ind->size[1] = qInd;
    emxEnsureCapacity(sp, (emxArray__common *)ind, i2, (int32_T)sizeof(real_T),
                      &d_emlrtRTEI);
    for (i2 = 0; i2 < qInd; i2++) {
      ind->data[ind->size[0] * i2] = Q->data[i2];
    }

    emlrtVectorVectorIndexCheckR2012b(dist->size[0], 1, 1, qInd, &g_emlrtECI, sp);
    st.site = &j_emlrtRSI;
    absb = ind->size[0] * ind->size[1];
    for (i2 = 0; i2 < absb; i2++) {
      i3 = dist->size[0];
      absxk = ind->data[i2];
      apnd = (int32_T)emlrtIntegerCheckFastR2012b(absxk, &e_emlrtDCI, &st);
      emlrtDynamicBoundsCheckFastR2012b(apnd, 1, i3, &cb_emlrtBCI, &st);
    }

    b_st.site = &q_emlrtRSI;
    c_st.site = &r_emlrtRSI;
    d_st.site = &s_emlrtRSI;
    mtmp = dist->data[(int32_T)ind->data[0] - 1];
    ndbl = 0;
    i2 = b_Q->size[0];
    b_Q->size[0] = qInd;
    emxEnsureCapacity(&d_st, (emxArray__common *)b_Q, i2, (int32_T)sizeof
                      (int32_T), &d_emlrtRTEI);
    for (i2 = 0; i2 < qInd; i2++) {
      b_Q->data[i2] = (int32_T)Q->data[i2];
    }

    if (b_Q->size[0] > 1) {
      i2 = c_Q->size[0];
      c_Q->size[0] = qInd;
      emxEnsureCapacity(&d_st, (emxArray__common *)c_Q, i2, (int32_T)sizeof
                        (int32_T), &d_emlrtRTEI);
      for (i2 = 0; i2 < qInd; i2++) {
        c_Q->data[i2] = (int32_T)Q->data[i2];
      }

      if (1 < c_Q->size[0]) {
        e_st.site = &t_emlrtRSI;
        cdiff = 1;
        do {
          exitg9 = 0;
          i2 = d_Q->size[0];
          d_Q->size[0] = qInd;
          emxEnsureCapacity(&d_st, (emxArray__common *)d_Q, i2, (int32_T)sizeof
                            (int32_T), &d_emlrtRTEI);
          for (i2 = 0; i2 < qInd; i2++) {
            d_Q->data[i2] = (int32_T)Q->data[i2];
          }

          if (cdiff + 1 <= d_Q->size[0]) {
            if (dist->data[(int32_T)ind->data[ind->size[0] * cdiff] - 1] < mtmp)
            {
              mtmp = dist->data[(int32_T)ind->data[ind->size[0] * cdiff] - 1];
              ndbl = cdiff;
            }

            cdiff++;
          } else {
            exitg9 = 1;
          }
        } while (exitg9 == 0);
      }
    }

    i2 = Q->size[1];
    u = Q->data[emlrtDynamicBoundsCheckFastR2012b(ndbl + 1, 1, i2, &db_emlrtBCI,
      sp) - 1];

    /*  index of the vertex */
    i2 = dist->size[0];
    absxk = Q->data[ndbl];
    i3 = (int32_T)emlrtIntegerCheckFastR2012b(absxk, &c_emlrtDCI, sp);
    emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &t_emlrtBCI, sp);
    if (muDoubleScalarIsInf(dist->data[(int32_T)Q->data[ndbl] - 1])) {
      exitg1 = true;
    } else {
      if (ndbl + 2 > Q->size[1]) {
        i2 = 0;
        i3 = 0;
      } else {
        i2 = Q->size[1];
        i2 = emlrtDynamicBoundsCheckFastR2012b(ndbl + 2, 1, i2, &s_emlrtBCI, sp)
          - 1;
        i3 = Q->size[1];
        apnd = Q->size[1];
        i3 = emlrtDynamicBoundsCheckFastR2012b(apnd, 1, i3, &s_emlrtBCI, sp);
      }

      if (ndbl + 1 > Q->size[1] - 1) {
        apnd = 0;
        ndbl = 0;
      } else {
        apnd = Q->size[1];
        apnd = emlrtDynamicBoundsCheckFastR2012b(ndbl + 1, 1, apnd, &r_emlrtBCI,
          sp) - 1;
        ndbl = Q->size[1];
        cdiff = Q->size[1] - 1;
        ndbl = emlrtDynamicBoundsCheckFastR2012b(cdiff, 1, ndbl, &r_emlrtBCI, sp);
      }

      ndbl -= apnd;
      cdiff = i3 - i2;
      emlrtSizeEqCheck1DFastR2012b(ndbl, cdiff, &f_emlrtECI, sp);
      ndbl = e_Q->size[0] * e_Q->size[1];
      e_Q->size[0] = 1;
      e_Q->size[1] = i3 - i2;
      emxEnsureCapacity(sp, (emxArray__common *)e_Q, ndbl, (int32_T)sizeof
                        (real_T), &d_emlrtRTEI);
      absb = i3 - i2;
      for (i3 = 0; i3 < absb; i3++) {
        e_Q->data[e_Q->size[0] * i3] = Q->data[i2 + i3];
      }

      absb = e_Q->size[1];
      for (i2 = 0; i2 < absb; i2++) {
        Q->data[apnd + i2] = e_Q->data[e_Q->size[0] * i2];
      }

      i2 = Q->size[1];
      i3 = Q->size[1];
      Q->data[emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &eb_emlrtBCI, sp) - 1]
        = rtInf;
      qInd--;

      /*  Q = setdiff(Q, u); */
      /*  all transitions to u TM(:,u); */
      st.site = &i_emlrtRSI;
      absb = TM->size[0];
      i2 = TM->size[1];
      i3 = (int32_T)u;
      ndbl = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &q_emlrtBCI, &st);
      i2 = x->size[0];
      x->size[0] = absb;
      emxEnsureCapacity(&st, (emxArray__common *)x, i2, (int32_T)sizeof
                        (boolean_T), &d_emlrtRTEI);
      for (i2 = 0; i2 < absb; i2++) {
        x->data[i2] = (TM->data[i2 + TM->size[0] * (ndbl - 1)] == 1.0);
      }

      b_st.site = &u_emlrtRSI;
      cdiff = 0;
      i2 = ii->size[0];
      ii->size[0] = x->size[0];
      emxEnsureCapacity(&b_st, (emxArray__common *)ii, i2, (int32_T)sizeof
                        (int32_T), &f_emlrtRTEI);
      c_st.site = &v_emlrtRSI;
      if (1 > x->size[0]) {
        overflow = false;
      } else {
        overflow = (x->size[0] > 2147483646);
      }

      if (overflow) {
        d_st.site = &p_emlrtRSI;
        check_forloop_overflow_error(&d_st);
      }

      ndbl = 1;
      exitg8 = false;
      while ((!exitg8) && (ndbl <= x->size[0])) {
        guard1 = false;
        if (x->data[ndbl - 1]) {
          cdiff++;
          ii->data[cdiff - 1] = ndbl;
          if (cdiff >= x->size[0]) {
            exitg8 = true;
          } else {
            guard1 = true;
          }
        } else {
          guard1 = true;
        }

        if (guard1) {
          ndbl++;
        }
      }

      if (cdiff <= x->size[0]) {
      } else {
        y = NULL;
        m1 = emlrtCreateString("Assertion failed.");
        emlrtAssign(&y, m1);
        c_st.site = &mb_emlrtRSI;
        error(&c_st, y, &e_emlrtMCI);
      }

      if (x->size[0] == 1) {
        if (cdiff == 0) {
          i2 = ii->size[0];
          ii->size[0] = 0;
          emxEnsureCapacity(&b_st, (emxArray__common *)ii, i2, (int32_T)sizeof
                            (int32_T), &d_emlrtRTEI);
        }
      } else {
        if (1 > cdiff) {
          absb = 0;
        } else {
          absb = cdiff;
        }

        i2 = c_ii->size[0];
        c_ii->size[0] = absb;
        emxEnsureCapacity(&b_st, (emxArray__common *)c_ii, i2, (int32_T)sizeof
                          (int32_T), &d_emlrtRTEI);
        for (i2 = 0; i2 < absb; i2++) {
          c_ii->data[i2] = ii->data[i2];
        }

        i2 = ii->size[0];
        ii->size[0] = c_ii->size[0];
        emxEnsureCapacity(&b_st, (emxArray__common *)ii, i2, (int32_T)sizeof
                          (int32_T), &d_emlrtRTEI);
        absb = c_ii->size[0];
        for (i2 = 0; i2 < absb; i2++) {
          ii->data[i2] = c_ii->data[i2];
        }
      }

      i2 = ind->size[0] * ind->size[1];
      ind->size[0] = 1;
      ind->size[1] = ii->size[0];
      emxEnsureCapacity(sp, (emxArray__common *)ind, i2, (int32_T)sizeof(real_T),
                        &d_emlrtRTEI);
      absb = ii->size[0];
      for (i2 = 0; i2 < absb; i2++) {
        ind->data[ind->size[0] * i2] = ii->data[i2];
      }

      j = 0;
      do {
        exitg2 = 0;
        emlrtBreakCheckFastR2012b(emlrtBreakCheckR2012bFlagVar, sp);
        if (j <= ind->size[1] - 1) {
          i2 = ind->size[1];
          i3 = j + 1;
          emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &p_emlrtBCI, sp);
          i2 = turn->size[0];
          i3 = (int32_T)ind->data[j];
          if (turn->data[emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2,
               &fb_emlrtBCI, sp) - 1] == 1.0) {
            /* robot's turn -- use regular dijkstra */
            i2 = dist->size[0];
            i3 = (int32_T)ind->data[j];
            apnd = TM->size[0];
            ndbl = (int32_T)ind->data[j];
            cdiff = TM->size[1];
            absb = (int32_T)u;
            if (dist->data[emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2,
                 &ib_emlrtBCI, sp) - 1] > mtmp + TM->data
                [(emlrtDynamicBoundsCheckFastR2012b(ndbl, 1, apnd, &jb_emlrtBCI,
                  sp) + TM->size[0] * (emlrtDynamicBoundsCheckFastR2012b(absb, 1,
                   cdiff, &kb_emlrtBCI, sp) - 1)) - 1]) {
              /* && (TM(i,u)~=0) */
              i2 = dist->size[0];
              i3 = (int32_T)ind->data[j];
              apnd = TM->size[0];
              ndbl = (int32_T)ind->data[j];
              cdiff = TM->size[1];
              absb = (int32_T)u;
              dist->data[emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2,
                &lb_emlrtBCI, sp) - 1] = mtmp + TM->data
                [(emlrtDynamicBoundsCheckFastR2012b(ndbl, 1, apnd, &mb_emlrtBCI,
                   sp) + TM->size[0] * (emlrtDynamicBoundsCheckFastR2012b(absb,
                    1, cdiff, &nb_emlrtBCI, sp) - 1)) - 1];
            }
          } else {
            /* environment's turn */
            st.site = &h_emlrtRSI;
            absb = TM->size[1];
            i2 = TM->size[0];
            i3 = (int32_T)ind->data[j];
            ndbl = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &o_emlrtBCI, &st);
            i2 = b_x->size[0] * b_x->size[1];
            b_x->size[0] = 1;
            b_x->size[1] = absb;
            emxEnsureCapacity(&st, (emxArray__common *)b_x, i2, (int32_T)sizeof
                              (boolean_T), &d_emlrtRTEI);
            for (i2 = 0; i2 < absb; i2++) {
              b_x->data[b_x->size[0] * i2] = (TM->data[(ndbl + TM->size[0] * i2)
                - 1] == 1.0);
            }

            b_st.site = &u_emlrtRSI;
            cdiff = 0;
            for (i2 = 0; i2 < 2; i2++) {
              ii_size[i2] = 1;
            }

            c_st.site = &v_emlrtRSI;
            if (1 > b_x->size[1]) {
              overflow = false;
            } else {
              overflow = (b_x->size[1] > 2147483646);
            }

            if (overflow) {
              d_st.site = &p_emlrtRSI;
              check_forloop_overflow_error(&d_st);
            }

            ndbl = 1;
            exitg7 = false;
            while ((!exitg7) && (ndbl <= b_x->size[1])) {
              if (b_x->data[ndbl - 1]) {
                cdiff = 1;
                exitg7 = true;
              } else {
                ndbl++;
              }
            }

            if (cdiff == 0) {
              ii_size[1] = 0;
            }

            if (!(ii_size[1] == 0)) {
              st.site = &h_emlrtRSI;
              b_st.site = &w_emlrtRSI;
              c_st.site = &x_emlrtRSI;
              overflow = true;
              ndbl = F->size[1];
              if (ndbl == 0) {
              } else {
                d_st.site = &ab_emlrtRSI;
                absb = 1;
                do {
                  exitg6 = 0;
                  ndbl = F->size[1];
                  if (absb <= ndbl - 1) {
                    p = (F->data[absb - 1] <= F->data[absb]);
                    if (!p) {
                      overflow = false;
                      exitg6 = 1;
                    } else {
                      absb++;
                    }
                  } else {
                    exitg6 = 1;
                  }
                } while (exitg6 == 0);
              }

              if (!overflow) {
                c_st.site = &y_emlrtRSI;
                eml_error(&c_st);
              }

              overflow = false;
              n = 0;
              ndbl = 1;
              cdiff = F->size[1];
              exitg5 = false;
              while ((!exitg5) && (cdiff >= ndbl)) {
                if (ndbl >= 0) {
                  b_ndbl = (int32_T)((uint32_T)ndbl >> 1);
                } else {
                  b_ndbl = ~(int32_T)((uint32_T)~ndbl >> 1);
                }

                if (cdiff >= 0) {
                  b_cdiff = (int32_T)((uint32_T)cdiff >> 1);
                } else {
                  b_cdiff = ~(int32_T)((uint32_T)~cdiff >> 1);
                }

                absb = (b_ndbl + b_cdiff) - 1;
                if (((ndbl & 1) == 1) && ((cdiff & 1) == 1)) {
                  absb++;
                }

                absxk = F->data[absb] / 2.0;
                if (absxk <= 2.2250738585072014E-308) {
                  absxk = 4.94065645841247E-324;
                } else {
                  frexp(absxk, &exponent);
                  absxk = ldexp(1.0, exponent - 53);
                }

                p = (muDoubleScalarAbs(F->data[absb] - ind->data[j]) < absxk);
                if (p) {
                  n = absb + 1;
                  exitg5 = true;
                } else {
                  p = (ind->data[j] < F->data[absb]);
                  if (p) {
                    cdiff = absb;
                  } else {
                    ndbl = absb + 2;
                  }
                }
              }

              if (n > 0) {
                exitg4 = false;
                while ((!exitg4) && (n - 1 > 0)) {
                  absxk = F->data[n - 2] / 2.0;
                  if (absxk <= 2.2250738585072014E-308) {
                    absxk = 4.94065645841247E-324;
                  } else {
                    frexp(absxk, &b_exponent);
                    absxk = ldexp(1.0, b_exponent - 53);
                  }

                  p = (muDoubleScalarAbs(F->data[n - 2] - ind->data[j]) < absxk);
                  if (p) {
                    n--;
                  } else {
                    exitg4 = true;
                  }
                }
              }

              if (n > 0) {
                overflow = true;
              }

              if (!overflow) {
                absb = TM->size[1];
                i2 = TM->size[0];
                i3 = (int32_T)ind->data[j];
                ndbl = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &n_emlrtBCI,
                  sp);
                i2 = b_TM->size[0] * b_TM->size[1];
                b_TM->size[0] = 1;
                b_TM->size[1] = absb;
                emxEnsureCapacity(sp, (emxArray__common *)b_TM, i2, (int32_T)
                                  sizeof(boolean_T), &d_emlrtRTEI);
                for (i2 = 0; i2 < absb; i2++) {
                  b_TM->data[b_TM->size[0] * i2] = (TM->data[(ndbl + TM->size[0]
                    * i2) - 1] == 1.0);
                }

                st.site = &g_emlrtRSI;
                eml_li_find(&st, b_TM, r11);
                emlrtVectorVectorIndexCheckR2012b(dist->size[0], 1, 1, r11->
                  size[1], &e_emlrtECI, sp);
                st.site = &g_emlrtRSI;
                absb = r11->size[0] * r11->size[1];
                for (i2 = 0; i2 < absb; i2++) {
                  i3 = dist->size[0];
                  apnd = r11->data[i2];
                  emlrtDynamicBoundsCheckFastR2012b(apnd, 1, i3, &gb_emlrtBCI,
                    &st);
                }

                b_st.site = &eb_emlrtRSI;
                c_st.site = &fb_emlrtRSI;
                i2 = r12->size[0];
                r12->size[0] = r11->size[1];
                emxEnsureCapacity(&c_st, (emxArray__common *)r12, i2, (int32_T)
                                  sizeof(int32_T), &d_emlrtRTEI);
                absb = r11->size[1];
                for (i2 = 0; i2 < absb; i2++) {
                  r12->data[i2] = r11->data[r11->size[0] * i2];
                }

                b_guard1 = false;
                if (r12->size[0] == 1) {
                  b_guard1 = true;
                } else {
                  i2 = r13->size[0];
                  r13->size[0] = r11->size[1];
                  emxEnsureCapacity(&c_st, (emxArray__common *)r13, i2, (int32_T)
                                    sizeof(int32_T), &d_emlrtRTEI);
                  absb = r11->size[1];
                  for (i2 = 0; i2 < absb; i2++) {
                    r13->data[i2] = r11->data[r11->size[0] * i2];
                  }

                  if (r13->size[0] != 1) {
                    b_guard1 = true;
                  } else {
                    overflow = false;
                  }
                }

                if (b_guard1) {
                  overflow = true;
                }

                if (overflow) {
                } else {
                  b_y = NULL;
                  m1 = emlrtCreateCharArray(2, iv4);
                  for (cdiff = 0; cdiff < 36; cdiff++) {
                    cv6[cdiff] = cv7[cdiff];
                  }

                  emlrtInitCharArrayR2013a(&c_st, 36, m1, cv6);
                  emlrtAssign(&b_y, m1);
                  d_st.site = &lb_emlrtRSI;
                  f_st.site = &rb_emlrtRSI;
                  error(&d_st, message(&f_st, b_y, &c_emlrtMCI), &d_emlrtMCI);
                }

                i2 = r14->size[0];
                r14->size[0] = r11->size[1];
                emxEnsureCapacity(&c_st, (emxArray__common *)r14, i2, (int32_T)
                                  sizeof(int32_T), &d_emlrtRTEI);
                absb = r11->size[1];
                for (i2 = 0; i2 < absb; i2++) {
                  r14->data[i2] = r11->data[r11->size[0] * i2];
                }

                if (r14->size[0] > 0) {
                } else {
                  c_y = NULL;
                  m1 = emlrtCreateCharArray(2, iv5);
                  for (cdiff = 0; cdiff < 39; cdiff++) {
                    cv8[cdiff] = cv9[cdiff];
                  }

                  emlrtInitCharArrayR2013a(&c_st, 39, m1, cv8);
                  emlrtAssign(&c_y, m1);
                  d_st.site = &kb_emlrtRSI;
                  f_st.site = &qb_emlrtRSI;
                  error(&d_st, message(&f_st, c_y, &g_emlrtMCI), &h_emlrtMCI);
                }

                d_st.site = &s_emlrtRSI;
                absxk = dist->data[r11->data[0] - 1];
                i2 = r15->size[0];
                r15->size[0] = r11->size[1];
                emxEnsureCapacity(&d_st, (emxArray__common *)r15, i2, (int32_T)
                                  sizeof(int32_T), &d_emlrtRTEI);
                absb = r11->size[1];
                for (i2 = 0; i2 < absb; i2++) {
                  r15->data[i2] = r11->data[r11->size[0] * i2];
                }

                if (r15->size[0] > 1) {
                  i2 = r16->size[0];
                  r16->size[0] = r11->size[1];
                  emxEnsureCapacity(&d_st, (emxArray__common *)r16, i2, (int32_T)
                                    sizeof(int32_T), &d_emlrtRTEI);
                  absb = r11->size[1];
                  for (i2 = 0; i2 < absb; i2++) {
                    r16->data[i2] = r11->data[r11->size[0] * i2];
                  }

                  if (1 < r16->size[0]) {
                    e_st.site = &t_emlrtRSI;
                    i2 = r17->size[0];
                    r17->size[0] = r11->size[1];
                    emxEnsureCapacity(&e_st, (emxArray__common *)r17, i2,
                                      (int32_T)sizeof(int32_T), &d_emlrtRTEI);
                    absb = r11->size[1];
                    for (i2 = 0; i2 < absb; i2++) {
                      r17->data[i2] = r11->data[r11->size[0] * i2];
                    }

                    if (2 > r17->size[0]) {
                      overflow = false;
                    } else {
                      i2 = r18->size[0];
                      r18->size[0] = r11->size[1];
                      emxEnsureCapacity(&e_st, (emxArray__common *)r18, i2,
                                        (int32_T)sizeof(int32_T), &d_emlrtRTEI);
                      absb = r11->size[1];
                      for (i2 = 0; i2 < absb; i2++) {
                        r18->data[i2] = r11->data[r11->size[0] * i2];
                      }

                      overflow = (r18->size[0] > 2147483646);
                    }

                    if (overflow) {
                      g_st.site = &p_emlrtRSI;
                      check_forloop_overflow_error(&g_st);
                    }

                    cdiff = 1;
                    do {
                      exitg3 = 0;
                      i2 = r19->size[0];
                      r19->size[0] = r11->size[1];
                      emxEnsureCapacity(&d_st, (emxArray__common *)r19, i2,
                                        (int32_T)sizeof(int32_T), &d_emlrtRTEI);
                      absb = r11->size[1];
                      for (i2 = 0; i2 < absb; i2++) {
                        r19->data[i2] = r11->data[r11->size[0] * i2];
                      }

                      if (cdiff + 1 <= r19->size[0]) {
                        if (dist->data[r11->data[r11->size[0] * cdiff] - 1] >
                            absxk) {
                          absxk = dist->data[r11->data[r11->size[0] * cdiff] - 1];
                        }

                        cdiff++;
                      } else {
                        exitg3 = 1;
                      }
                    } while (exitg3 == 0);
                  }
                }

                i2 = dist->size[0];
                i3 = (int32_T)ind->data[j];
                dist->data[emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2,
                  &hb_emlrtBCI, sp) - 1] = absxk + 1.0;

                /* maximum energy for next states */
              }
            }
          }

          j++;
          emlrtBreakCheckFastR2012b(emlrtBreakCheckR2012bFlagVar, sp);
        } else {
          exitg2 = 1;
        }
      } while (exitg2 == 0);
    }
  }

  emxFree_int32_T(&r19);
  emxFree_int32_T(&r18);
  emxFree_int32_T(&r17);
  emxFree_int32_T(&r16);
  emxFree_int32_T(&r15);
  emxFree_int32_T(&r14);
  emxFree_int32_T(&r13);
  emxFree_int32_T(&r12);
  emxFree_int32_T(&c_ii);
  emxFree_real_T(&e_Q);
  emxFree_int32_T(&d_Q);
  emxFree_int32_T(&c_Q);
  emxFree_int32_T(&b_Q);
  emxFree_boolean_T(&b_TM);
  emxFree_int32_T(&ii);
  emxFree_boolean_T(&b_x);
  emxFree_boolean_T(&x);
  emxFree_int32_T(&r11);
  emxFree_real_T(&ind);
  emxFree_real_T(&Q);
  emxFree_real_T(&TM);

  /*  dist(dest) = 0; %manually make distance to this state 0 */
  if (1 > dist->size[0] - 1) {
    absb = 0;
  } else {
    i2 = dist->size[0];
    emlrtDynamicBoundsCheckFastR2012b(1, 1, i2, &m_emlrtBCI, sp);
    i2 = dist->size[0];
    i3 = dist->size[0] - 1;
    absb = emlrtDynamicBoundsCheckFastR2012b(i3, 1, i2, &m_emlrtBCI, sp);
  }

  emxInit_real_T(sp, &b_dist, 1, &d_emlrtRTEI, true);
  emlrtVectorVectorIndexCheckR2012b(dist->size[0], 1, 1, absb, &d_emlrtECI, sp);
  i2 = b_dist->size[0];
  b_dist->size[0] = absb;
  emxEnsureCapacity(sp, (emxArray__common *)b_dist, i2, (int32_T)sizeof(real_T),
                    &d_emlrtRTEI);
  for (i2 = 0; i2 < absb; i2++) {
    b_dist->data[i2] = dist->data[i2];
  }

  i2 = dist->size[0];
  dist->size[0] = b_dist->size[0];
  emxEnsureCapacity(sp, (emxArray__common *)dist, i2, (int32_T)sizeof(real_T),
                    &d_emlrtRTEI);
  absb = b_dist->size[0];
  for (i2 = 0; i2 < absb; i2++) {
    dist->data[i2] = b_dist->data[i2];
  }

  emxFree_real_T(&b_dist);

  /*  dist = dist - 1; %remove distance to virtual node, and keep distance to real nodes */
  emlrtHeapReferenceStackLeaveFcnR2012b(sp);
}

/* End of code generation (dijkstraGameEff_mod.c) */
