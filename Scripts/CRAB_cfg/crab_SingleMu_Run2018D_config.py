from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'Muon_Eff_Run2018D'
config.General.workArea = 'crab_Run2018D'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/eos/user/j/jordanm/MuonEff/CMSSW_10_2_3/src/MuonAnalysis/MuonFastFeedbackTools/python/AllJobsDATA2018_cfg.py'
#config.JobType.inputFiles='/eos/user/j/jordanm/MuonEff/CMSSW_10_2_3/src/MuonAnalysis'
config.JobType.outputFiles = ['Plots_SingleMu_DATA_2018.root']

config.Data.inputDBS = 'global'
#config.Data.inputDataset = '/SingleMuon/Run2018A-PromptReco-v3/MINIAOD'
#config.Data.inputDataset = '/SingleMuon/Run2018B-PromptReco-v2/MINIAOD'
#config.Data.inputDataset = '/SingleMuon/Run2018C-PromptReco-v3/MINIAOD'
config.Data.inputDataset = '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
config.Data.runRange = '314472-325175' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/jordanm' # or '/store/group/<subdir>'
config.Data.publication = False
#config.Data.outputDatasetTag= 'SingleMu_Run2018A-PromptReco-v3'
#config.Data.outputDatasetTag= 'SingleMu_Run2018B-PromptReco-v2'
#config.Data.outputDatasetTag= 'SingleMu_Run2018C-PromptReco-v3'
config.Data.outputDatasetTag= 'SingleMu_Run2018D'

#config.Site.whitelist = ['T3_US_FNALLPC']
config.Site.storageSite     = 'T3_US_FNALLPC'
