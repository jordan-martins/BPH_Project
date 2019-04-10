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
Alias             MyD0        D0
Alias             anti-MyD0   anti-D0
ChargeConj        MyD0        anti-MyD0
#
Alias         MyD*+   D*+
Alias         MyD*- D*-
ChargeConj    MyD*+ MyD*-
#
Alias         MyTau-   tau-
Alias         MyTau+   tau+
ChargeConj    MyTau- MyTau+
#
Decay MyB0
1.000     MyD*-     MyTau+        nu_tau             ISGW2;
Enddecay
CDecay Myanti-B0
#
Decay MyD*+
1.000     MyD0      pi+                              VSS;
Enddecay
CDecay MyD*-
#
Decay MyD0
1.000     K-        pi+                              PHSP;
Enddecay
CDecay anti-MyD0
#
Decay MyTau-
1.000     mu-       anti-nu_mu    nu_tau             TAULNUNU;
Enddecay
CDecay MyTau+
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

BTauMuFilter = cms.EDFilter("PythiaMomDauFilter",
    ChargeConjugation = cms.untracked.bool(True), #also the 511 decay
    ParticleID = cms.untracked.int32(-511),
    MomMinPt = cms.untracked.double(0.2), #cut for particleID
    NumberDaughters = cms.untracked.int32(3),
    DaughterIDs = cms.untracked.vint32(413,15,-16),
    DaughterID = cms.untracked.int32(15),
    NumberDescendants = cms.untracked.int32(3),
    DescendantsIDs = cms.untracked.vint32(13,-14,16),
    MinEta = cms.untracked.double(-2.5), #cut for descendantsIDs
    MaxEta = cms.untracked.double(2.5), #cut for descendantsIDs
)

MuFilter = cms.EDFilter("PythiaDauVFilter",
    Status = cms.untracked.int32(1),
    ChargeConjugation = cms.untracked.bool(True), #also the 15 decay
    MotherID = cms.untracked.int32(15),
    ParticleID = cms.untracked.int32(13),
    MinPt = cms.untracked.vdouble(2.),
)


ProductionFilterSequence = cms.Sequence(generator*Bfilter*BTauMuFilter*MuFilter)
