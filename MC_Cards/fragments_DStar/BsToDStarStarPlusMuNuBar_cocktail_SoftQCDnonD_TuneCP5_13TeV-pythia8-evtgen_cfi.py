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
            list_forced_decays = cms.vstring('MyB_s0', 'Myanti-B_s0'),
            operates_on_particles = cms.vint32(531,-531),    # we care just about our signal particles
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Alias      MyB_s0        B_s0
Alias      Myanti-B_s0   anti-B_s0
ChargeConj Myanti-B_s0   MyB_s0
#
Alias      Mytau+         tau+
Alias      Mytau-         tau-
ChargeConj Mytau+         Mytau-
#
Alias      MyD0         D0
Alias      MyAntiD0     anti-D0
ChargeConj MyD0         MyAntiD0
#
Alias      MyD*-        D*-
Alias      MyD*+        D*+
ChargeConj MyD*-        MyD*+
#
Alias      MyD_s1+         D_s1+
Alias      MyD_s1-         D_s1-
ChargeConj MyD_s1+         MyD_s1-
#
Alias      MyD_s0*+         D_s0*+
Alias      MyD_s0*-         D_s0*-
ChargeConj MyD_s0*+         MyD_s0*-
#
Alias      MyD'_s1+         D'_s1+
Alias      MyD'_s1-         D'_s1-
ChargeConj MyD'_s1+         MyD'_s1-
#
Alias      MyD_s2*+         D_s2*+
Alias      MyD_s2*-         D_s2*-
ChargeConj MyD_s2*+         MyD_s2*-
#
Decay MyB_s0
  0.0070   MyD'_s1-   mu+    nu_mu        PHOTOS  ISGW2;
  0.0070   MyD_s2*-   mu+    nu_mu        PHOTOS  ISGW2;
Enddecay
CDecay Myanti-B_s0
#
Decay MyD'_s1-
0.5000   MyD*- anti-K0                      VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
Enddecay
CDecay MyD'_s1+
#
Decay MyD_s2*+
0.0500    MyD*+ K0                         TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
Enddecay
CDecay MyD_s2*-
#
Decay MyD*-
1.0       MyAntiD0   pi-                   VSS;
Enddecay
CDecay MyD*+
#
Decay MyD0
1.00   K-  pi+                              PHOTOS PHSP;
Enddecay
CDecay MyAntiD0
#
Decay Mytau-
1.00      mu-  nu_tau  anti-nu_mu        PHOTOS TAULNUNU;
Enddecay
CDecay Mytau+
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
    ParticleID = cms.untracked.vint32(531,-531),
    MinPt = cms.untracked.vdouble(-1.,-1.),
    MinEta = cms.untracked.vdouble(-999.,-999.),
    MaxEta = cms.untracked.vdouble(999.,999.),
    Status = cms.untracked.vint32(2,2)
)

Mufilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(13,-13),
    MinPt = cms.untracked.vdouble(3.,3.),
    MinEta = cms.untracked.vdouble(-2.5,-2.5),
    MaxEta = cms.untracked.vdouble(2.5,2.5),
    Status = cms.untracked.vint32(1,1)
)

ProductionFilterSequence = cms.Sequence(generator*Bfilter*Mufilter)
