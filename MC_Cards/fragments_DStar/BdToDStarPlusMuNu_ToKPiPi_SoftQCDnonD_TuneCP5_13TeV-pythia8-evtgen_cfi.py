import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays = cms.vstring('MyB0', 'Myanti-B0'),
            operates_on_particles = cms.vint32(511,-511),    # we care just about our signal particles
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Alias      MyB0      B0
Alias      Myanti-B0 anti-B0
ChargeConj Myanti-B0 MyB0
#
Alias      MyD0         D0
Alias      MyAntiD0     anti-D0
ChargeConj MyD0         MyAntiD0
#
Alias      MyD*-        D*-
Alias      MyD*+        D*+
ChargeConj MyD*-        MyD*+
#
Decay MyB0
1.00   MyD*-        mu+  nu_mu         PHOTOS  HQET 1.20 1.426 0.818 0.908;
Enddecay
CDecay Myanti-B0
#
Decay MyD*-
1.00       MyAntiD0   pi-              VSS;
Enddecay
CDecay MyD*+
#
Decay MyD0
1.00   K-  pi+                         PHOTOS PHSP;
Enddecay
CDecay MyAntiD0
#
End
"""
            )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('SoftQCD:nonDiffractive = on',
					                    'PTFilter:filter = on', # this turn on the filter
                                        'PTFilter:quarkToFilter = 5', # PDG id of q quark
                                        'PTFilter:scaleToFilter = 1.0'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)

###### Filters ##########
Bfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(511,-511),
    MinPt = cms.untracked.vdouble(-1.,-1.),
    MinEta = cms.untracked.vdouble(-999.,-999.),
    MaxEta = cms.untracked.vdouble(999.,999.),
    Status = cms.untracked.vint32(2,2)
)

MuFilter = cms.EDFilter("PythiaDauVFilter",
    Status = cms.untracked.int32(1), # stable muons
    ChargeConjugation = cms.untracked.bool(True), #also the 511 decay
    MotherID = cms.untracked.int32(0), # not assigned to any particle
    ParticleID = cms.untracked.int32(-511),
    NumberDaughters = cms.untracked.int32(3), #just care about the mu
    DaughterIDs = cms.untracked.vint32(413,13,-14),
    MinPt = cms.untracked.vdouble(0.1,2.,-999.), #cut for daughterIDs
    MinEta = cms.untracked.vdouble(-2.5,-2.5,-2.5), #cut for daughterIDs
    MaxEta = cms.untracked.vdouble(2.5,2.5,2.5), #cut for daughterIDs
)



ProductionFilterSequence = cms.Sequence(generator*Bfilter*MuFilter)
