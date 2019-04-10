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
Alias      MyD+         D+
Alias      MyD-         D-
ChargeConj MyD+         MyD-
#
Alias             MyD*0       D*0
Alias             Myanti-D*0       anti-D*0
ChargeConj        MyD*0        Myanti-D*0
#
Alias      MyD*-        D*-
Alias      MyD*+        D*+
ChargeConj MyD*-        MyD*+
#
Alias      MyD_10         D_10
Alias      MyAntiD_10     anti-D_10
ChargeConj MyD_10         MyAntiD_10
#
Alias      MyD_1+         D_1+
Alias      MyD_1-         D_1-
ChargeConj MyD_1+         MyD_1-
#
Alias      MyD_0*+         D_0*+
Alias      MyD_0*-         D_0*-
ChargeConj MyD_0*+         MyD_0*-
#
Alias      MyD_0*0         D_0*0
Alias      MyAntiD_0*0     anti-D_0*0
ChargeConj MyD_0*0         MyAntiD_0*0
#
Alias      MyD'_10         D'_10
Alias      MyAntiD'_10     anti-D'_10
ChargeConj MyD'_10         MyAntiD'_10
#
Alias      MyD'_1+         D'_1+
Alias      MyD'_1-         D'_1-
ChargeConj MyD'_1+         MyD'_1-
#
Alias      MyD_2*+         D_2*+
Alias      MyD_2*-         D_2*-
ChargeConj MyD_2*+         MyD_2*-
#
Alias      MyD_2*0         D_2*0
Alias      MyAntiD_2*0     anti-D_2*0
ChargeConj MyD_2*0         MyAntiD_2*0
#
Decay MyB0
  0.0046  MyD'_1-    mu+  nu_mu         PHOTOS  ISGW2;
  0.0042  MyD_1-     mu+  nu_mu         PHOTOS  ISGW2;
  0.0033  MyD_2*-    mu+  nu_mu         PHOTOS  ISGW2;
Enddecay
CDecay Myanti-B0
#
SetLineshapePW MyD_1+ MyD*+ pi0 2
SetLineshapePW MyD_1- MyD*- pi0 2
SetLineshapePW MyD_10 MyD*+ pi- 2
SetLineshapePW MyAntiD_10 MyD*- pi+ 2
#
SetLineshapePW MyD_2*+ MyD*+ pi0 2
SetLineshapePW MyD_2*- MyD*- pi0 2
SetLineshapePW MyD_2*0 MyD*+ pi- 2
SetLineshapePW MyAntiD_2*0 MyD*- pi+ 2
#
Decay MyD_0*+
  0.3333   MyD+  pi0                         PHSP;
  0.6667   MyD0  pi+                         PHSP;
#0.04     MyD*+ pi0 pi0                     PHOTOS PHSP;
#0.08     MyD*+ pi+ pi-                     PHOTOS PHSP;
Enddecay
CDecay MyD_0*-
#
Decay MyD_0*0
  0.3333   MyD0  pi0                         PHSP;
  0.6667   MyD+  pi-                         PHSP;
#0.08    MyD*+ pi- pi0                      PHOTOS PHSP;
Enddecay
CDecay MyAntiD_0*0
#
Decay MyD'_1+
0.6667     MyD*+ pi0                        PHOTOS VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
Enddecay
CDecay MyD'_1-
#
Decay MyD'_10
0.6667    MyD*+ pi-                         PHOTOS VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
Enddecay
CDecay MyAntiD'_10
#
Decay MyD_1+
  0.3333    MyD*+ pi0                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
  0.6667    MyD*0 pi+                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.200    MyD*+ pi0                         PHOTOS VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.0208    MyD_0*0 pi+                      PHOTOS PHSP;
#0.0156    MyD_0*+ pi0                      PHOTOS PHSP;
Enddecay
CDecay MyD_1-
#
Decay MyD_10
  0.3333    MyD*0 pi0                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
  0.6667    MyD*+ pi-                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.400    MyD*+ pi-                         PHOTOS VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.0312    MyD_0*+ pi-                      PHOTOS PHSP;
#0.0104    MyD_0*0 pi0                      PHSP;
Enddecay
CDecay MyAntiD_10
#
Decay MyD_2*+
  0.1030    MyD*+ pi0                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
  0.2090    MyD*0 pi+                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
  0.2290    MyD+  pi0                        TSS;
  0.4590    MyD0  pi+                        TSS;
#0.087    MyD*+ pi0                         PHOTOS TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
#0.0117    MyD_0*0 pi+                      PHOTOS PHSP;
#0.0088    MyD_0*+ pi0                      PHOTOS PHSP;
#0.004     MyD*+ pi0 pi0                    PHOTOS PHSP;
#0.008     MyD*+ pi+ pi-                    PHOTOS PHSP;
Enddecay
CDecay MyD_2*-
#
Decay MyD_2*0
  0.2090    MyD*+ pi-                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
  0.1030    MyD*0 pi0                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
  0.2290    MyD0  pi0                        TSS;
  0.4590    MyD+  pi-                        TSS;
#0.173    MyD*+ pi-                         PHOTOS TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
#0.0176    MyD_0*+ pi-                      PHOTOS PHSP;
#0.0059    MyD_0*0 pi0                      PHSP;
#0.008     MyD*+ pi- pi0                    PHOTOS PHSP;
Enddecay
CDecay MyAntiD_2*0
#
Decay MyD*-
1.00       MyAntiD0   pi-                  VSS;
Enddecay
CDecay MyD*+
#
Decay MyD0
1.00   K-  pi+                             PHOTOS PHSP;
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

Mufilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(13,-13),
    MinPt = cms.untracked.vdouble(3.,3.),
    MinEta = cms.untracked.vdouble(-2.5,-2.5),
    MaxEta = cms.untracked.vdouble(2.5,2.5),
    Status = cms.untracked.vint32(1,1)
)

ProductionFilterSequence = cms.Sequence(generator*Bfilter*Mufilter)
