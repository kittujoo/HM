"""
File_Name: scan_wavelength_constants.py
Desc: This file contains the constants of the scan wave length test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/22
"""


class ScanWavelengthConstants:
    WelcomeFirstParagraph = "Use the Scan Wavelengths feature to qualify the instrument, use the instrument as spectrophotometer, or for as a troubleshooting tool."

    WelcomeSecondParagraph = "Scans are also performed by Waters Technical Service personnel as part of a Total Assurance with Calibration Plan."

    WelcomeThirdParagraph = "During a scan, the detector obtains an absorbance spectrum by performing two sequential scans on the flow cell:"

    WelcomeFourParagraph = 'Blank scan – Also known as "zero" scan, characterizes the baseline absorbance spectrum of a solvent.'

    WelcomeFiveParagraph = 'Sample scan – Subtracts the Blank scan. Only the sample results display.'

    WelcomeSixParagraph = 'You typically perform this test by either injecting sample directly into the flow cell, or by adding sample to a cuvette.'

    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph,
                                       WelcomeFourParagraph, WelcomeFiveParagraph, WelcomeSixParagraph]


class RecommendedMaterialsForPMTestUsingCuvettes:
    LineOne = "Two cuvettes"
    LineTwo = "Waters UV/Visible Absorbance Detector Wavelength Accuracy Calibration Solution, WAT042885"
    LineThree = "100% HPLC-grade water"
    expected_pm_test_using_cuvettes_text = [LineOne, LineTwo, LineThree]


class RecommendedMaterialsForPMTestUsingFlowcell:
    LineOne = "Syringe, 10-mL, WAT027629"
    LineTwo = "Priming syringe needle, WAT025559"
    LineThree = "Waters UV/Visible Absorbance Detector Wavelength Accuracy Calibration Solution, WAT042885"
    LineFour = "100% HPLC-grade water"
    expected_pm_test_using_flowcell_text = [LineOne, LineTwo, LineThree, LineFour]


class RecommendedMaterialsForSampleScanUsingCuvettes:
    LineOne = "Two cuvettes"
    LineTwo = "A sample diluent"
    LineThree = "The sample to scan"
    expected_sample_scan_test_using_cuvettes_text = [LineOne, LineTwo, LineThree]


class RecommendedMaterialsForSampleScanUsingFlowcell:
    LineOne = "Syringe, 10-mL, WAT027629"
    LineTwo = "Priming syringe needle, WAT025559"
    LineThree = "A sample diluent"
    LineFour = "The sample to scan"
    expected_sample_scan_test_using_flowcell_text = [LineOne, LineTwo, LineThree, LineFour]


class ScanWavelengthPreparationForPMTest:
    LineOne = "Rinse two cuvettes at least three times using HPLC-grade water."
    LineTwo = "Fill one cuvette with 3 mL of HPLC-grade water."
    LineThree = "Fill one cuvette with 3 mL of Waters UV/Visible Absorbance Detector Wavelength Accuracy Calibration Solution."

    scan_wavelength_preparation = [LineOne, LineTwo, LineThree]

class ScanWavelengthPreparationForSampleScan:
    LineOne = "Rinse two cuvettes at least three times using HPLC-grade water."
    LineTwo = "Fill one cuvette with 3 mL diluent."
    LineThree = "Fill one cuvette with your sample dissolved in 3 mL diluent."

    scan_wavelength_preparation = [LineOne, LineTwo, LineThree]
