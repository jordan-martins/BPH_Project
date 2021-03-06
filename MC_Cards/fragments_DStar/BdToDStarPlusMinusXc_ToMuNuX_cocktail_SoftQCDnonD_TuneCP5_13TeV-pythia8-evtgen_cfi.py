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
Alias             MyOtherD*-       D*-
Alias             MyOtherD*+       D*+
ChargeConj        MyOtherD*+       MyOtherD*-
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
Alias      MyD+         D+
Alias      MyD-         D-
ChargeConj MyD+         MyD-
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
Alias      MyD_s1+         D_s1+
Alias      MyD_s1-         D_s1-
ChargeConj MyD_s1-         MyD_s1+
#
Alias      MyD'_s1+         D'_s1+
Alias      MyD'_s1-         D'_s1-
ChargeConj MyD'_s1-         MyD'_s1+
#
Alias      MyOtherD'_s1+         D'_s1+
Alias      MyOtherD'_s1-         D'_s1-
ChargeConj MyOtherD'_s1-         MyOtherD'_s1+
#
Alias      MyD_s0*+         D_s0*+
Alias      MyD_s0*-         D_s0*-
ChargeConj MyD_s0*-         MyD_s0*+
#
Decay MyB0
  0.017700000 MyD*-     MyD_s*+             SVV_HELAMP 0.4904 0.0 0.7204 0.0 0.4904 0.0;
  0.008000000 MyD*-     MyD_s+              SVS;
  0.003100000 MyD*-     MyOtherD0 K+        PHSP;
  0.011800000 MyD*-     MyD*0 K+            PHSP;
  0.0047   MyD*- MyD+  anti-K0              PHSP;
  0.0025   MyD*- MyOtherD0  K*+             PHSP;
  0.0050   MyD*- MyD*0  K*+                 PHSP;
  0.0025   MyD*- MyD+  anti-K*0             PHSP;
  0.0050   MyD*- MyOtherD*+  anti-K*0       PHSP;
  0.00061    MyD*+  MyD-                    SVS;
  0.000820000 MyD*-     MyOtherD*+          SVV_HELAMP 0.56 0.0 0.96 0.0 0.47 0.0;
  0.0006   MyD'_1-  MyD_s+                  SVS;
  0.0012   MyD'_1-  MyD_s*+                 SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
  0.0012   MyD_1-  MyD_s+                   SVS;
  0.0024   MyD_1-  MyD_s*+                  SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
  0.0042   MyD_2*-  MyD_s+                  STS;
  0.0040   MyD_2*-  MyD_s*+                 PHSP;
  0.0015  MyD*-    MyD_s0*+                 SVS;
  0.0093  MyD*-    MyD_s1+                  SVV_HELAMP 0.4904 0.0 0.7204 0.0 0.4904 0.0;
  0.00083  MyD*-    MyD'_s1+                PHSP;
  0.00043  MyOtherD'_s1+ MyD-               PHSP;
  0.0018  MyD*+     MyD- K0                 PHSP;
  0.0078  MyD*+ MyOtherD*-  K0              PHSP;
Enddecay
CDecay Myanti-B0
#
Decay MyD*-
1.000        Myanti-D0 pi-                    VSS;
Enddecay
CDecay MyD*+
#
Decay Myanti-D0
1.000        K+        pi-                    PHSP;
Enddecay
CDecay MyD0
#
Decay MyD_s+
 0.018309605 phi      mu+     nu_mu                      PHOTOS  ISGW2;
 0.022845082 eta      mu+     nu_mu                      PHOTOS  ISGW2;
 0.008186726 eta'     mu+     nu_mu                      PHOTOS  ISGW2;
 0.002058115 K0       mu+     nu_mu                      PHOTOS  ISGW2;
 0.000762265 K*0      mu+     nu_mu                      PHOTOS  ISGW2;
 ###???0.0020 f_0      mu+     nu_mu                      PHOTOS  ISGW2;
 0.005800000 mu+      nu_mu                              PHOTOS   SLN;
Enddecay
CDecay MyD_s-
#
Decay MyOtherD*-
  0.6770    MyOtheranti-D0 pi-                        VSS;
  0.3070    MyD-      pi0                             VSS;
  0.0160    MyD-      gamma                           VSP_PWAVE;
Enddecay
CDecay MyOtherD*+
#
Decay MyD-
  0.052800000 K*0     mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.092000000 K0      mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.002773020 K_10    mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.002927076 K_2*0   mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.004050000 pi0     mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.001140000 eta     mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.002200000 eta'    mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.002400000 rho0    mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.001820000 omega   mu-     anti-nu_mu                      PHOTOS  ISGW2; #[Reconstructed PDG2011]
  0.002921725 K+      pi-     mu-     anti-nu_mu              PHOTOS   PHSP; #[Reconstructed PDG2011]
  0.001200122 K0      pi0     mu-     anti-nu_mu              PHOTOS   PHSP; #[Reconstructed PDG2011]
  0.000382000 mu-     anti-nu_mu                              PHOTOS   SLN;
Enddecay
CDecay MyD+
#
Decay MyOtherD0
  0.021000000 K*-     mu+     nu_mu                           PHOTOS  ISGW2; # 1.1 * PDG2014
  0.034700000 K-      mu+     nu_mu                           PHOTOS  ISGW2; # 1.05 * PDG2014
  0.000076000 K_1-    mu+     nu_mu                           PHOTOS  ISGW2; # PDG2014 for electron
  0.001100000 K_2*-   mu+     nu_mu                           PHOTOS  ISGW2; # copy from electron
  0.002370000 pi-     mu+     nu_mu                           PHOTOS  ISGW2; # PDG2014
  0.002015940 rho-    mu+     nu_mu                           PHOTOS  ISGW2; # PDG2014 for electron
  0.001080000 anti-K0 pi-     mu+     nu_mu                   PHOTOS   PHSP; # copy electron
  0.000400000 K-      pi0     mu+     nu_mu                   PHOTOS   PHSP; # copy electron
Enddecay
CDecay MyOtheranti-D0
#
Decay MyD_s*+
  0.942000000 MyD_s+    gamma                                   VSP_PWAVE; #[Reconstructed PDG2011]
  0.058000000 MyD_s+    pi0                                     VSS; #[Reconstructed PDG2011]
Enddecay
CDecay MyD_s*-
#
Decay MyD*0
  0.619000000 MyOtherD0      pi0                                 VSS; #[Reconstructed PDG2011]
  0.381000000 MyOtherD0      gamma                               VSP_PWAVE; #[Reconstructed PDG2011]
Enddecay
CDecay Myanti-D*0
#
SetLineshapePW MyD_1+ MyD*+ pi0 2
SetLineshapePW MyD_1- MyD*- pi0 2
SetLineshapePW MyD_2*+ MyD*+ pi0 2
SetLineshapePW MyD_2*- MyD*- pi0 2
#
Decay MyD'_1+
  0.3333    MyD*+ pi0                        VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
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
  0.3333   MyD0  pi0                         PHSP;
  0.6667   MyD+  pi-                         PHSP;
#0.08    MyD*+ pi- pi0                      PHOTOS PHSP;
Enddecay
CDecay MyAntiD_0*0
#
#Ds(2317)
Decay MyD_s0*+
#0.5000   MyD+ K0                           PHSP;
#0.5000   MyD0 K+                           PHSP;
  1.000      MyD_s+ pi0                        PHSP;
Enddecay
CDecay MyD_s0*-
#
#Ds(2460)
Decay MyD_s1+
0.80000  MyD_s*+ pi0                       PARTWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.20000  MyD_s+ gamma                      VSP_PWAVE;
Enddecay
CDecay MyD_s1-
#
#Ds(2536)
Decay MyD'_s1+
0.5000   MyOtherD*+ K0                      VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.5000   MyD*0 K+                           VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.0000   gamma MyD_s*+                      PHSP;
0.0000   gamma MyD_s+                       PHSP;
Enddecay
CDecay MyD'_s1-
#
Decay MyOtherD'_s1+
0.5000   MyD*+ K0                           VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.5000   MyD*0 K+                          VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
#0.0000   gamma MyD_s*+                     PHSP;
#0.0000   gamma MyD_s+                      PHSP;
Enddecay
CDecay MyOtherD'_s1-
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
