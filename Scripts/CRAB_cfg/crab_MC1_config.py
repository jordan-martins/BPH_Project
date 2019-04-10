from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'GS_BdToDStarPlusMinusXc_ToMuNuX' # MC#1
#config.General.requestName = 'GS_BdToDStarPlusMuNu_ToKPiPi' # MC#2
#config.General.requestName = 'GS_BdToDStarPlusTauNu_ToKPiPiToMuNuBarNu' # MC#3
#config.General.requestName = 'GS_BdToDStarStarPlusMuNuBar' # MC#4
#config.General.requestName = 'GS_BdToDStarStarPlusTauNuBar_ToMuNuNuBar' # MC#5
#config.General.requestName = 'GS_BdToDStarStarPlusX_ToDsMinusToTauNuBar_ToMuNuNuBar' # MC#6
#config.General.requestName = 'GS_BsToDStarStarPlusMuNuBar' # MC#7
#config.General.requestName = 'GS_BuToDStarPlusMinus_ToXcToMuNuX' # MC#8
#config.General.requestName = 'GS_BuToDStarStarMuNuBar' # MC#9
#config.General.requestName = 'GS_BuToDStarStarTauNuBar_ToMuNuNuBar' # MC#10
#config.General.requestName = 'GS_BuToDStarStarX_ToDsMinusTauNu_ToMuNuNuBar' # MC#11

config.General.workArea = 'crab_BdToDStarPlusMinusXc_ToMuNuX' # MC#1
#config.General.workArea = 'crab_BdToDStarPlusMuNu_ToKPiPi' # MC#2
#config.General.workArea = 'crab_BdToDStarPlusTauNu_ToKPiPiToMuNuBarNu' # MC#3
#config.General.workArea = 'crab_BdToDStarStarPlusMuNuBar' # MC#4
#config.General.workArea = 'crab_BdToDStarStarPlusTauNuBar_ToMuNuNuBar' # MC#5
#config.General.workArea = 'crab_BdToDStarStarPlusX_ToDsMinusToTauNuBar_ToMuNuNuBar' # MC#6
#config.General.workArea = 'crab_BsToDStarStarPlusMuNuBar' # MC#7
#config.General.workArea = 'crab_BuToDStarPlusMinus_ToXcToMuNuX' # MC#8
#config.General.workArea = 'crab_BuToDStarStarMuNuBar' # MC#9
#config.General.workArea = 'crab_BuToDStarStarTauNuBar_ToMuNuNuBar' # MC#10
#config.General.workArea = 'crab_BuToDStarStarX_ToDsMinusTauNu_ToMuNuNuBar' # MC#11
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'

config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarPlusMinusXc_ToMuNuX_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#1
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarPlusMuNu_ToKPiPi_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#2
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarPlusTauNu_ToKPiPiToMuNuBarNu_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#3
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarStarPlusMuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#4
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarStarPlusTauNuBar_ToMuNuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#5
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BdToDStarStarPlusX_ToDsMinusToTauNuBar_ToMuNuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#6
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BsToDStarStarPlusMuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#7
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BuToDStarPlusMinus_ToXcToMuNuX_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#8
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BuToDStarStarMuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#9
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BuToDStarStarTauNuBar_ToMuNuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#10
#config.JobType.psetName = '/eos/user/j/jordanm/BPH/CMSSW_10_2_11_patch1/src/BuToDStarStarX_ToDsMinusTauNu_ToMuNuNuBar_cocktail_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen_cfg.py' # MC#11

config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2000
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/jordanm' # or '/store/group/<subdir>'
config.Data.publication = False

config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarPlusMinusXc_ToMuNuX' # MC#1
#config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarPlusMuNu_ToKPiPi' # MC#2
#config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarPlusTauNu_ToKPiPiToMuNuBarNu' # MC#3
#config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarStarPlusMuNuBar' # MC#4
#config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarStarPlusTauNuBar_ToMuNuNuBar' # MC#5
#config.Data.outputDatasetTag= 'GEN-SIM-BdToDStarStarPlusX_ToDsMinusToTauNuBar_ToMuNuNuBar' # MC#6
#config.Data.outputDatasetTag= 'GEN-SIM-BsToDStarStarPlusMuNuBar' # MC#7
#config.Data.outputDatasetTag= 'GEN-SIM-BuToDStarPlusMinus_ToXcToMuNuX' # MC#8
#config.Data.outputDatasetTag= 'GEN-SIM-BuToDStarStarMuNuBar' # MC#9
#config.Data.outputDatasetTag= 'GEN-SIM-BuToDStarStarTauNuBar_ToMuNuNuBar' # MC#10
#config.Data.outputDatasetTag= 'GEN-SIM-BuToDStarStarX_ToDsMinusTauNu_ToMuNuNuBar' # MC#11

config.Data.outputPrimaryDataset = 'BdToDStarPlusMinusXc_ToMuNuX' # MC#1
#config.Data.outputPrimaryDataset = 'BdToDStarPlusMuNu_ToKPiPi' # MC#2
#config.Data.outputPrimaryDataset = 'BdToDStarPlusTauNu_ToKPiPiToMuNuBarNu' # MC#3
#config.Data.outputPrimaryDataset = 'BdToDStarStarPlusMuNuBar' # MC#4
#config.Data.outputPrimaryDataset = 'BdToDStarStarPlusTauNuBar_ToMuNuNuBar' # MC#5
#config.Data.outputPrimaryDataset = 'BdToDStarStarPlusX_ToDsMinusToTauNuBar_ToMuNuNuBar' # MC#6
#config.Data.outputPrimaryDataset = 'BsToDStarStarPlusMuNuBar' # MC#7
#config.Data.outputPrimaryDataset = 'BuToDStarPlusMinus_ToXcToMuNuX' # MC#8
#config.Data.outputPrimaryDataset = 'BuToDStarStarMuNuBar' # MC#9
#config.Data.outputPrimaryDataset = 'BuToDStarStarTauNuBar_ToMuNuNuBar' # MC#10
#config.Data.outputPrimaryDataset = 'BuToDStarStarX_ToDsMinusTauNu_ToMuNuNuBar' # MC#11

config.Site.storageSite     = 'T3_US_FNALLPC'
