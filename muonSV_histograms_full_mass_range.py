import ROOT
from ROOT import TFile
from array import array
from ROOT import TChain
from ROOT import gStyle
from ROOT import TStyle

import numpy as np
import matplotlib.pyplot as plt
#import mplhep as hep

signal = TChain()
background1 = TChain()
background2 = TChain()
background3 = TChain()
background4 = TChain()
background5 = TChain()
background6 = TChain()
background7 = TChain()
background8 = TChain()
background9 = TChain()
background10 = TChain()
background11 = TChain()
background12 = TChain()

background5_ext = TChain()
background6_ext = TChain()
background8_ext = TChain()
background9_ext = TChain()

signal_bdt = TChain()
background1_bdt = TChain()
background2_bdt = TChain()
background3_bdt = TChain()
background4_bdt = TChain()
background5_bdt = TChain()
background6_bdt = TChain()
background7_bdt = TChain()
background8_bdt = TChain()
background9_bdt = TChain()
background10_bdt = TChain()
background11_bdt = TChain()
background12_bdt = TChain()

background5_bdt_ext = TChain()
background6_bdt_ext = TChain()
background8_bdt_ext = TChain()
background9_bdt_ext = TChain()


signal_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/HiddenValley_vector_m_2_ctau_10_xiO_1_xiL_1_privateMC_11X_NANOAODSIM_v1p0_generationSync/*.root/Events")
background1_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Events");
background2_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4_MINIAODSIM_v1p0_generationSync/*.root/Events");
background3_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Events");
background4_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Events");
background5_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");
background6_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");

background7_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Events");
background8_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Events");
background9_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");
background10_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");
background11_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2_MINIAODSIM_v1p0_generationSync/*.root/Events");
background12_bdt.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");

background5_bdt_ext.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Events");
background6_bdt_ext.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Events");
background8_bdt_ext.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v1_MINIAODSIM_v1p0_generationSync/*.root/Events");
background9_bdt_ext.Add("/vols/cms/mmieskol/icenet/output/dqcd/deploy/modeltag__vector_all/vols/cms/mc3909/bparkProductionAll_V1p0/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Events");

background5_bdt.Add(background5_bdt_ext);
background6_bdt.Add(background6_bdt_ext);
background8_bdt.Add(background8_bdt_ext);
background9_bdt.Add(background9_bdt_ext);



signal.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/HiddenValley_vector_m_2_ctau_10_xiO_1_xiL_1_privateMC_11X_NANOAODSIM_v1p0_generationSync/*.root/Friends")
background1.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background2.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background3.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background4.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background5.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background6.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")

background7.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background8.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background9.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background10.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background11.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background12.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")

background5_ext.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background6_ext.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background8_ext.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v1_MINIAODSIM_v1p0_generationSync/*.root/Friends")
background9_ext.Add("/vols/cms/khl216/nano_out/nanotron_v3_bdt_0_fixed/bparkProductionAll_V1p0/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_MINIAODSIM_v1p0_generationSync/*.root/Friends")

background5.Add(background5_ext)
background6.Add(background6_ext)
background8.Add(background8_ext)
background9.Add(background9_ext)


df = ROOT.RDataFrame(signal)
df1 = ROOT.RDataFrame(background1)
df2 = ROOT.RDataFrame(background2)
df3 = ROOT.RDataFrame(background3)
df4 = ROOT.RDataFrame(background4)
df5 = ROOT.RDataFrame(background5)
df6 = ROOT.RDataFrame(background6)
df7 = ROOT.RDataFrame(background7)
df8 = ROOT.RDataFrame(background8)
df9 = ROOT.RDataFrame(background9)
df10 = ROOT.RDataFrame(background10)
df11 = ROOT.RDataFrame(background11)
df12 = ROOT.RDataFrame(background12)

df_bdt = ROOT.RDataFrame(signal_bdt)
df1_bdt = ROOT.RDataFrame(background1_bdt)
df2_bdt = ROOT.RDataFrame(background2_bdt)
df3_bdt = ROOT.RDataFrame(background3_bdt)
df4_bdt = ROOT.RDataFrame(background4_bdt)
df5_bdt = ROOT.RDataFrame(background5_bdt)
df6_bdt = ROOT.RDataFrame(background6_bdt)
df7_bdt = ROOT.RDataFrame(background7_bdt)
df8_bdt = ROOT.RDataFrame(background8_bdt)
df9_bdt = ROOT.RDataFrame(background9_bdt)
df10_bdt = ROOT.RDataFrame(background10_bdt)
df11_bdt = ROOT.RDataFrame(background11_bdt)
df12_bdt = ROOT.RDataFrame(background12_bdt)

print("RDataFrame done")
#For BDT
no_of_entries_original = 80000.0
no_of_entries1_original = 4159734.0
no_of_entries2_original = 30100864.0
no_of_entries3_original = 29327371.0
no_of_entries4_original = 19814379.0
no_of_entries5_original = 24759617.0
no_of_entries6_original = 20454047.0
no_of_entries7_original = 35664362.0
no_of_entries8_original = 28899863.0
no_of_entries9_original = 19939641.0
no_of_entries10_original = 16125220.0
no_of_entries11_original = 16464596.0
no_of_entries12_original = 10377764.0


print("Number of entries in background 1 =", no_of_entries1_original)
print("Number of entries in background 2 =", no_of_entries2_original)
print("Number of entries in background 3 =", no_of_entries3_original)
print("Number of entries in background 4 =", no_of_entries4_original)
print("Number of entries in background 5 =", no_of_entries5_original)
print("Number of entries in background 6 =", no_of_entries6_original)
print("Number of entries in background 7 =", no_of_entries7_original)
print("Number of entries in background 8 =", no_of_entries8_original)
print("Number of entries in background 9 =", no_of_entries9_original)
print("Number of entries in background 10 =", no_of_entries10_original)
print("Number of entries in background 11 =", no_of_entries11_original)
print("Number of entries in background 12 =", no_of_entries12_original)

print("Counting done")
'''
h_svmass = df.Histo1D(("hist_svmass_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass1 = df1.Histo1D(("hist_svmass1_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass2 = df2.Histo1D(("hist_svmass2_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass3 = df3.Histo1D(("hist_svmass3_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass4 = df4.Histo1D(("hist_svmass4_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass5 = df5.Histo1D(("hist_svmass5_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass6 = df6.Histo1D(("hist_svmass6_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass7 = df7.Histo1D(("hist_svmass7_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass8 = df8.Histo1D(("hist_svmass8_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass9 = df9.Histo1D(("hist_svmass9_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass10 = df10.Histo1D(("hist_svmass10_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass11 = df11.Histo1D(("hist_svmass11_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
h_svmass12 = df12.Histo1D(("hist_svmass12_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 40, 4.8, 5.2), "svAdapted_mass")
'''
cut = "xgb0__m_2p0_ctau_10p0_xiO_1p0_xiL_1p0 > 0.9994"

h_svmass = df.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass1 = df1.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass1_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass2 = df2.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass2_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass3 = df3.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass3_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass4 = df4.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass4_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass5 = df5.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass5_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass6 = df6.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass6_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass7 = df7.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass7_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass8 = df8.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass8_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass9 = df9.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass9_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass10 = df10.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass10_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass11 = df11.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass11_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")
h_svmass12 = df12.Filter("nmuonSV > 0").Define("muonSV_deltaR", "sqrt(pow(muonSV_mu1phi-muonSV_mu2phi, 2) + pow(muonSV_mu1eta-muonSV_mu2eta, 2))").Define("MuonSV_deltaR", "muonSV_deltaR[ArgMin(muonSV_chi2)]").Define("MuonSV_dxySig", "muonSV_dxySig[ArgMin(muonSV_chi2)]").Define("MuonSV_pAngle","muonSV_pAngle[ArgMin(muonSV_chi2)]").Define("MuonSV_chi2", "muonSV_chi2[ArgMin(muonSV_chi2)]").Define("MuonSV_mass", "muonSV_mass[ArgMin(muonSV_chi2)]").Filter(cut).Histo1D(("hist_svmass12_nano", "Mass distribution; Mass (GeV); Number of secondary vertices", 100, 0.0, 21.5), "MuonSV_mass")



print("TH1D done")

branching_ratio = 0.01
xs = 43.9

xs1 = 2799000.0
xs2 = 2526000.0
xs3 = 1362000.0
xs4 = 376600.0
xs5 = 88930.0
xs6 = 21230.0

xs7 = 7055.0
xs8 = 619.3
xs9 = 59.24
xs10 = 18.21
xs11 = 3.275
xs12 = 1.078

lumi = 33.6*1000

h_svmass.Scale(lumi*xs*branching_ratio/no_of_entries_original)
h_svmass1.Scale(lumi*xs1/no_of_entries1_original)
h_svmass2.Scale(lumi*xs2/no_of_entries2_original)
h_svmass3.Scale(lumi*xs3/no_of_entries3_original)
h_svmass4.Scale(lumi*xs4/no_of_entries4_original)
h_svmass5.Scale(lumi*xs5/no_of_entries5_original)
h_svmass6.Scale(lumi*xs6/no_of_entries6_original)
h_svmass7.Scale(lumi*xs7/no_of_entries7_original)
h_svmass8.Scale(lumi*xs8/no_of_entries8_original)
h_svmass9.Scale(lumi*xs9/no_of_entries9_original)
h_svmass10.Scale(lumi*xs10/no_of_entries10_original)
h_svmass11.Scale(lumi*xs11/no_of_entries11_original)
h_svmass12.Scale(lumi*xs12/no_of_entries12_original)

h_svmass1.Add(h_svmass2.GetPtr())
h_svmass1.Add(h_svmass3.GetPtr())
h_svmass1.Add(h_svmass4.GetPtr())
h_svmass1.Add(h_svmass5.GetPtr())
h_svmass1.Add(h_svmass6.GetPtr())
h_svmass1.Add(h_svmass7.GetPtr())
h_svmass1.Add(h_svmass8.GetPtr())
h_svmass1.Add(h_svmass9.GetPtr())
h_svmass1.Add(h_svmass10.GetPtr())
h_svmass1.Add(h_svmass11.GetPtr())
h_svmass1.Add(h_svmass12.GetPtr())

'''
myFile = TFile("/vols/cms/khl216/muonSV_BDT_background_fixed.root", "UPDATE")
print("TFile created")

myFile.WriteObject(h_svmass1.GetPtr(), "BDT > 0.9994")
'''
gStyle.SetOptStat(0) 
gStyle.SetTextFont(42);

c2 = ROOT.TCanvas("", "", 800, 700)
c2.SetLogy()
h_svmass1.SetLineColor(ROOT.kRed)
h_svmass.SetLineColor(ROOT.kBlue+1)

h_svmass1.SetMaximum(1E9);
h_svmass1.SetMinimum(1E-1);

h_svmass1.SetTitle("Muon SV mass (nmuonSV > 1, muonSV[0] in increasing chi2)")
h_svmass1.DrawClone("hist e1")
h_svmass.DrawClone("hist e1 Same")

out_legend2 = ROOT.TLegend(0.68, 0.795, 0.88, 0.875)
out_legend2.AddEntry(h_svmass1.GetPtr(), "Background (BDT > 0.9994)", "l")
out_legend2.AddEntry(h_svmass.GetPtr(), "Signal (BDT > 0.9994)", "l")
out_legend2.Draw("Same")

c2.Print("muonSV_mass_full_range_BDT>0p9994_nmuonSV>0.pdf")
