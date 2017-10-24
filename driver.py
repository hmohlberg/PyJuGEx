#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyjugex
import hbp_human_atlas as atlas
import nibabel as nib
import warnings

warnings.filterwarnings("ignore")
#genelist = ['ADRA2A', 'AVPR1B', 'CHRM2', 'CNR1', 'CREB1', 'CRH', 'CRHR1', 'CRHR2', 'GAD2', 'HTR1A', 'HTR1B', 'HTR1D', 'HTR2A', 'HTR3A', 'HTR5A', 'MAOA', 'PDE1A', 'SLC6A2', 'SLC6A4', 'SST', 'TAC1', 'TPH1', 'GPR50', 'CUX2', 'TPH2']
genelist = ['ADRA2A', 'AVPR1B', 'CHRM2']
roi1 = atlas.jubrain.probability_map('VIIIa_Hem', atlas.MNI152)
roi2 = atlas.jubrain.probability_map('AStr', atlas.MNI152)
jugex = pyjugex.PyJugex(cache=".pyjugex", verbose=True)
result = jugex.DifferentialAnalysis(genelist, roi1, roi2)
if len([id for id in result if result[id] < .05]) > 0:
    print('Differentially expressed genes are : ')
    print([id for id in result if result[id] < .05])
else:
    print('There are no differentially expressed genes in the given regions')

