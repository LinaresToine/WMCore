'''
Created on Dec 16, 2016

'''
from __future__ import (division, print_function)

import unittest
import xml.etree.ElementTree as ElementTree

from WMCore.Services.TagCollector.TagCollector import TagCollector


class TagCollectorTest(unittest.TestCase):
    def setUp(self):
        """
        _setUp_

        """
        # using the default production server
        self.tagCollecor = TagCollector()
        self.testReleasesMap = "/tmp/testReleases.map"
        self.testReleasesXML = "/tmp/testReleasesXML"

        releasesMap = (
                        "architecture=el9_amd64_gcc12;label=CMSSW_15_0_15_patch3;type=Production;state=Announced;prodarch=0;default_micro_arch=x86-64-v3;\n"
                        "architecture=el8_amd64_gcc12;label=CMSSW_15_0_15_patch3;type=Production;state=Announced;prodarch=1;default_micro_arch=x86-64-v3;\n"
                        "architecture=el8_amd64_gcc13;label=CMSSW_16_0_0_pre1_FASTPU;type=Development;state=Announced;prodarch=1;default_micro_arch=x86-64-v3;\n"
                        "architecture=el9_amd64_gcc12;label=CMSSW_15_0_15_patch4;type=Production;state=Announced;prodarch=0;default_micro_arch=x86-64-v3;\n"
                        "architecture=el8_amd64_gcc12;label=CMSSW_15_0_15_patch4;type=Production;state=Announced;prodarch=1;default_micro_arch=x86-64-v3;\n"
                    )
        with open(self.testReleasesMap, "w", encoding="utf-8") as f:
            f.write(releasesMap)

        return

    def testTagCollecorMethods(self):
        """
        _testTagCollecorMethods_
        """

        self.tagCollecor.parseCvmfsReleasesXML(self.testReleasesMap, self.testReleasesXML)
        releasesXML = self.testReleasesXML.read_text(encoding="utf-8")
        try:
            ElementTree.parse(releasesXML)
        except ElementTree.ParseError as e:
            self.fail(f"Output file is not valid XML: {e}")

        releases = self.tagCollecor.releases()
        architectures = self.tagCollecor.architectures()
        realsese_by_arch = self.tagCollecor.releases_by_architecture()
        microarch_by_release = self.tagCollecor.defaultMicroArchVersionNumberByRelease()
        microarch_testCMSSW_15 = self.tagCollecor.getGreaterMicroarchVersionNumber("CMSSW_15_0_0_pre3")
        microarch_testCMSSW_12_15 = self.tagCollecor.getGreaterMicroarchVersionNumber("CMSSW_12_4_0_pre2,CMSSW_15_0_0_pre3")
        microarch_testCMSSW_7_12 = self.tagCollecor.getGreaterMicroarchVersionNumber("CMSSW_7_1_10_patch2,CMSSW_12_4_0_pre2", rel_microarchs=microarch_by_release)
        self.assertIn('CMSSW_7_1_10_patch2', releases)
        self.assertIn('slc6_amd64_gcc493', architectures)
        self.assertIn('slc7_amd64_gcc620', architectures)
        self.assertEqual(len(architectures), len(realsese_by_arch))
        self.assertEqual(sorted(self.tagCollecor.releases('slc6_amd64_gcc493')),
                         sorted(realsese_by_arch.get('slc6_amd64_gcc493')))
        self.assertEqual(0, microarch_by_release['CMSSW_7_1_10_patch2'])
        self.assertEqual(3, microarch_by_release['CMSSW_15_0_0_pre3'])
        self.assertEqual(3, microarch_testCMSSW_12_15)
        self.assertEqual(3, microarch_testCMSSW_15)
        self.assertEqual(0, microarch_testCMSSW_7_12)

        return


if __name__ == '__main__':
    unittest.main()
