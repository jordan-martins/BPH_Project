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
Alias             MyD*-       D*-
Alias             MyD*+       D*+
ChargeConj        MyD*+       MyD*-
#
Alias      MyD+         D+
Alias      MyD-         D-
ChargeConj MyD+         MyD-
#
Alias             Myanti-D0   anti-D0
Alias             MyD0        D0
ChargeConj        MyD0        Myanti-D0
#
Alias             MyD*0       D*0
Alias             Myanti-D*0       anti-D*0
ChargeConj        MyD*0        Myanti-D*0
#
Alias             MyOtherD0        D0
Alias             MyOtheranti-D0   anti-D0
ChargeConj        MyOtherD0        MyOtheranti-D0
#
Alias             MyD_s+      D_s+
Alias             MyD_s-      D_s-
ChargeConj        MyD_s+      MyD_s-
#
Alias             MyD_s*+      D_s*+
Alias             MyD_s*-      D_s*-
ChargeConj        MyD_s*+      MyD_s*-
#
Alias      MyD_1+         D_1+
Alias      MyD_1-         D_1-
ChargeConj MyD_1+         MyD_1-
#
Alias      MyD'_1+         D'_1+
Alias      MyD'_1-         D'_1-
ChargeConj MyD'_1+         MyD'_1-
#
Alias      MyD_2*+         D_2*+
Alias      MyD_2*-         D_2*-
ChargeConj MyD_2*+         MyD_2*-
#
Alias      MyD_0*+         D_0*+
Alias      MyD_0*-         D_0*-
ChargeConj MyD_0*+         MyD_0*-
#
Alias      MyD_0*0         D_0*0
Alias      MyAntiD_0*0     anti-D_0*0
ChargeConj MyD_0*0         MyAntiD_0*0
#
Alias      Mytau+         tau+
Alias      Mytau-         tau-
ChargeConj Mytau+         Mytau-
#
Alias      MyD_s1+         D_s1+
Alias      MyD_s1-         D_s1-
ChargeConj MyD_s1-         MyD_s1+
#
Alias      MyD_s0*+         D_s0*+
Alias      MyD_s0*-         D_s0*-
ChargeConj MyD_s0*-         MyD_s0*+
#
#https://github.com/cms-data/GeneratorInterface-EvtGenInterface/blob/master/DECAY_2014_NOLONGLIFE.DEC#L1098

Decay MyB0
  0.01770  MyD*-     MyD_s*+             SVV_HELAMP 0.4904 0.0 0.7204 0.0 0.4904 0.0;
  0.00800  MyD*-     MyD_s+              SVS;
  0.0006   MyD'_1-   MyD_s+              SVS;
  0.0012   MyD'_1-   MyD_s*+             SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
  0.0012   MyD_1-    MyD_s+              SVS;
  0.0024   MyD_1-    MyD_s*+             SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
  0.0042   MyD_2*-   MyD_s+              STS;
  0.0040   MyD_2*-   MyD_s*+             PHSP;
  0.0015  MyD*-      MyD_s0*+            SVS;
  0.0093  MyD*-      MyD_s1+             SVV_HELAMP 0.4904 0.0 0.7204 0.0 0.4904 0.0;
Enddecay
CDecay Myanti-B0
#
Decay MyD*-
  1.000        Myanti-D0 pi-             VSS;
Enddecay
CDecay MyD*+
#
Decay Myanti-D0
  1.000        K+        pi-             PHSP;
Enddecay
CDecay MyD0
#
Decay MyD_s+
  1.0000 Mytau+      nu_tau              PHOTOS   SLN;
Enddecay
CDecay MyD_s-
#
Decay MyD_s*+
  0.942000000 MyD_s+    gamma            VSP_PWAVE; #[Reconstructed PDG2011]
  0.058000000 MyD_s+    pi0              VSS; #[Reconstructed PDG2011]
Enddecay
CDecay MyD_s*-
#
Decay MyD*0
  0.619000000 MyOtherD0      pi0         VSS; #[Reconstructed PDG2011]
  0.381000000 MyOtherD0      gamma       VSP_PWAVE; #[Reconstructed PDG2011]
Enddecay
CDecay Myanti-D*0
#
SetLineshapePW MyD_1+ MyD*+ pi0 2
SetLineshapePW MyD_1- MyD*- pi0 2
SetLineshapePW MyD_2*+ MyD*+ pi0 2
SetLineshapePW MyD_2*- MyD*- pi0 2
#
Decay MyD'_1+
  0.3333     MyD*+ pi0                    PHOTOS VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
Enddecay
CDecay MyD'_1-
#
Decay MyD_1+
  0.3333    MyD*+ pi0                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
  0.6667    MyD*0 pi+                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
##0.200     MyD*+ pi0                         PHOTOS VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
##0.0208    MyD_0*0 pi+                      PHOTOS PHSP;
##0.0156    MyD_0*+ pi0                      PHOTOS PHSP;
Enddecay
CDecay MyD_1-
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
Decay MyD_0*+
  0.3333   MyD+  pi0                         PHSP;
  0.6667   MyD0  pi+                         PHSP;
#0.04     MyD*+ pi0 pi0                     PHOTOS PHSP;
#0.08     MyD*+ pi+ pi-                     PHOTOS PHSP;
Enddecay
CDecay MyD_0*-
#
Decay MyD_0*0
  0.3333   D0  pi0                         PHSP;
  0.6667   D+  pi-                         PHSP;
#0.08    MyD*+ pi- pi0                      PHOTOS PHSP;
Enddecay
CDecay MyAntiD_0*0
#
Decay Mytau-
1.00      mu-  nu_tau  anti-nu_mu     PHOTOS TAULNUNU;
Enddecay
CDecay Mytau+
#
#Ds(2317)
Decay MyD_s0*+
1.000      MyD_s+ pi0                  PHSP;
Enddecay
CDecay MyD_s0*-
#
#Ds(2460)
Decay MyD_s1+
0.80000  MyD_s*+ pi0                   PARTWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.20000  MyD_s+ gamma                  VSP_PWAVE;
Enddecay
CDecay MyD_s1-
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
