# 17o05028_ic_steps.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `2017-10-05 14:42:46.899000`
* abfDateTimeString = `2017-10-05T14:42:46.899`
* abfFileComment = ``
* abfFilePath = `C:/some/path/to/17o05028_ic_steps.abf`
* abfFolderPath = `C:/some/path`
* abfID = `17o05028_ic_steps`
* abfVersion = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionString = `2.6.0.0`
* adcNames = `['IN 0']`
* adcUnits = `['mV']`
* channelCount = `1`
* channelList = `[0]`
* creator = `Clampex 10.7.0.3`
* creatorVersion = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionString = `10.7.0.3`
* dacNames = `['Cmd 0']`
* dacUnits = `['pA']`
* data = `array (2d) with values like: -47.08862, -47.14966, -47.11914, ..., -62.37793, -62.40845, -62.37793`
* dataByteStart = `6656`
* dataLengthMin = `0.85`
* dataLengthSec = `51.0`
* dataPointByteSize = `2`
* dataPointCount = `960000`
* dataPointsPerMs = `20`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* fileGUID = `307EE462-8A84-41AE-8188-4AB5B73AAAE3`
* fileUUID = `FF17D4CA-749C-BA69-77E3-9DE6FC81E90D`
* holdingCommand = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* md5 = `FF17D4CA749CBA6977E39DE6FC81E90D`
* nOperationMode = `5`
* protocol = `0112 steps dual -50 to 150 step 10`
* protocolPath = `S:\Protocols\permanent\0112 steps dual -50 to 150 step 10.pro`
* stimulusByChannel = `[Stimulus(abf, 0)]`
* stimulusFileFolder = `C:/some/path/to/17o05028_ic_steps.abf`
* sweepC = `array (1d) with values like: 0.00000, 0.00000, 0.00000, ..., 0.00000, 0.00000, 0.00000`
* sweepChannel = `0`
* sweepCount = `16`
* sweepDerivative = `array (1d) with values like: -1220.70312, 610.35156, 610.35156, ..., 0.00000, 610.35156, 610.35156`
* sweepEpochs = `Sweep epoch waveform: Step 0.00 [0:937], Step 0.00 [937:2937], Step -50.00 [2937:12937], Step 0.00 [12937:22937], Step -50.00 [22937:32937], Step -50.00 [32937:42937], Step 0.00 [42937:60000]`
* sweepIntervalSec = `3.0`
* sweepLabelC = `Applied Current (pA)`
* sweepLabelD = `Digital Output (V)`
* sweepLabelX = `Time (seconds)`
* sweepLabelY = `Membrane Potential (mV)`
* sweepLengthSec = `3.0`
* sweepList = `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
* sweepNumber = `0`
* sweepPointCount = `60000`
* sweepTimesMin = `array (1d) with values like: 0.00000, 0.05000, 0.10000, ..., 0.65000, 0.70000, 0.75000`
* sweepTimesSec = `array (1d) with values like: 0.00000, 3.00000, 6.00000, ..., 39.00000, 42.00000, 45.00000`
* sweepUnitsC = `pA`
* sweepUnitsX = `sec`
* sweepUnitsY = `mV`
* sweepX = `array (1d) with values like: 0.00000, 0.00005, 0.00010, ..., 2.99985, 2.99990, 2.99995`
* sweepY = `array (1d) with values like: -47.08862, -47.14966, -47.11914, ..., -44.64722, -44.64722, -44.61670`
* tagComments = `[]`
* tagSweeps = `[]`
* tagTimesMin = `[]`
* tagTimesSec = `[]`
* userList = `None`
* userListEnable = `[]`
* userListParamToVary = `[]`
* userListParamToVaryName = `[]`
* userListRepeat = `[]`

## Epochs for Channel 0


```
                    EPOCH         A         B         C         D         E
                     Type      Step      Step      Step      Step      Step
              First Level      0.00    -50.00      0.00    -50.00    -50.00
              Delta Level      0.00     10.00      0.00      0.00     10.00
  First Duration (points)      2000     10000     10000     10000     10000
  Delta Duration (points)         0         0         0         0         0
     Digital Pattern #3-0      0000      0000      0000      0000      0000
     Digital Pattern #7-4      0000      0000      0000      0000      0000
    Train Period (points)         0         0         0         0         0
     Pulse Width (points)         0         0         0         0         0
```

## ABF2 Header

> The first several bytes of an ABF2 file contain variables     located at specific byte positions from the start of the file. 

* abfDateTime = `2017-10-05 14:42:46.899000`
* abfDateTimeString = `2017-10-05T14:42:46.899`
* abfVersionDict = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionFloat = `2.6`
* abfVersionString = `2.6.0.0`
* creatorVersionDict = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionFloat = `10.703`
* creatorVersionString = `10.7.0.3`
* fFileVersionNumber = `[0, 0, 6, 2]`
* lActualEpisodes = `16`
* nCRCEnable = `0`
* nDataFormat = `0`
* nFileType = `1`
* nSimultaneousScan = `1`
* sFileGUID = `307EE462-8A84-41AE-8188-4AB5B73AAAE3`
* sFileSignature = `ABF2`
* uCreatorNameIndex = `1`
* uCreatorVersion = `[3, 0, 7, 10]`
* uFileCRC = `0`
* uFileGUID = `[98, 228, 126, 48, 132, 138, 174, 65, 129, 136, 74, 181, 183, 58, 170, 227]`
* uFileInfoSize = `512`
* uFileStartDate = `20171005`
* uFileStartTimeMS = `52966899`
* uModifierNameIndex = `0`
* uModifierVersion = `0`
* uProtocolPathIndex = `2`
* uStopwatchTime = `8379`

## ProtocolSection

> This section contains information about the recording settings.     This is useful for determining things like sample rate and     channel scaling factors. 

* bEnableFileCompression = `0`
* fADCRange = `10.0`
* fADCSequenceInterval = `50.0`
* fAverageWeighting = `0.10000000149011612`
* fCellID = `[0.0, 0.0, 0.0]`
* fDACRange = `10.0`
* fEpisodeStartToStart = `0.0`
* fFirstRunDelayS = `0.0`
* fRunStartToStart = `0.0`
* fScopeOutputInterval = `0.0`
* fSecondsPerRun = `7200.0`
* fStatisticsPeriod = `1.0`
* fSynchTimeUnit = `12.5`
* fTrialStartToStart = `0.0`
* fTriggerThreshold = `0.0`
* lADCResolution = `32768`
* lAverageCount = `1`
* lDACResolution = `32768`
* lEpisodesPerRun = `21`
* lFileCommentIndex = `0`
* lFinishDisplayNum = `60000`
* lNumSamplesPerEpisode = `60000`
* lNumberOfTrials = `1`
* lPreTriggerSamples = `20`
* lRunsPerTrial = `1`
* lSamplesPerTrace = `40000`
* lStartDisplayNum = `0`
* lStatisticsMeasurements = `5`
* lTimeHysteresis = `1`
* nActiveDACChannel = `0`
* nAllowExternalTags = `0`
* nAlternateDACOutputState = `0`
* nAlternateDigitalOutputState = `0`
* nAutoAnalyseEnable = `1`
* nAutoTriggerStrategy = `1`
* nAverageAlgorithm = `0`
* nAveragingMode = `0`
* nChannelStatsStrategy = `0`
* nCommentsEnable = `0`
* nDigitalDACChannel = `0`
* nDigitalEnable = `0`
* nDigitalHolding = `0`
* nDigitalInterEpisode = `0`
* nDigitalTrainActiveLogic = `1`
* nDigitizerADCs = `16`
* nDigitizerDACs = `4`
* nDigitizerSynchDigitalOuts = `8`
* nDigitizerTotalDigitalOuts = `16`
* nDigitizerType = `6`
* nExperimentType = `2`
* nExternalTagType = `2`
* nFirstEpisodeInRun = `0`
* nLTPType = `0`
* nLevelHysteresis = `64`
* nManualInfoStrategy = `1`
* nOperationMode = `5`
* nScopeTriggerOut = `0`
* nShowPNRawData = `0`
* nSignalType = `0`
* nStatisticsClearStrategy = `1`
* nStatisticsDisplayStrategy = `0`
* nStatisticsSaveStrategy = `0`
* nStatsEnable = `1`
* nTrialTriggerSource = `-1`
* nTriggerAction = `0`
* nTriggerPolarity = `0`
* nTriggerSource = `-3`
* nUndoPromptStrategy = `0`
* nUndoRunCount = `0`
* sDigitizerType = `Digidata 1440`
* uFileCompressionRatio = `1`

## ADCSection

> Information about the ADC (what gets recorded).     There is 1 item per ADC. 

* bEnabledDuringPN = `[0]`
* fADCDisplayAmplification = `[12.307504653930664]`
* fADCDisplayOffset = `[-21.75]`
* fADCProgrammableGain = `[1.0]`
* fInstrumentOffset = `[0.0]`
* fInstrumentScaleFactor = `[0.009999999776482582]`
* fPostProcessLowpassFilter = `[100000.0]`
* fSignalGain = `[1.0]`
* fSignalHighpassFilter = `[1.0]`
* fSignalLowpassFilter = `[5000.0]`
* fSignalOffset = `[0.0]`
* fTelegraphAccessResistance = `[0.0]`
* fTelegraphAdditGain = `[1.0]`
* fTelegraphFilter = `[10000.0]`
* fTelegraphMembraneCap = `[0.0]`
* lADCChannelNameIndex = `[3]`
* lADCUnitsIndex = `[4]`
* nADCNum = `[0]`
* nADCPtoLChannelMap = `[0]`
* nADCSamplingSeq = `[0]`
* nHighpassFilterType = `[0]`
* nLowpassFilterType = `[0]`
* nPostProcessLowpassFilterType = `['\x00']`
* nStatsChannelPolarity = `[1]`
* nTelegraphEnable = `[1]`
* nTelegraphInstrument = `[24]`
* nTelegraphMode = `[1]`
* sTelegraphInstrument = `['MultiClamp 700']`

## DACSection

> Information about the DAC (what gets clamped).     There is 1 item per DAC. 

* fBaselineDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fBaselineLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACCalibrationFactor = `[1.0008957386016846, 1.0010067224502563, 1.000895619392395, 1.0008400678634644, 1.0, 1.0, 1.0, 1.0]`
* fDACCalibrationOffset = `[0.0, -2.0, -3.0, 2.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fDACHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACScaleFactor = `[400.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]`
* fInstrumentHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fMembTestPostSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fMembTestPreSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPNHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNInterpulse = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNSettlingTime = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPostTrainLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPostTrainPeriod = `[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]`
* fStepDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fStepLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* lConditNumPulses = `[1, 0, 0, 0, 0, 0, 0, 0]`
* lDACChannelNameIndex = `[5, 7, 9, 11, 13, 15, 17, 19]`
* lDACChannelUnitsIndex = `[6, 8, 10, 12, 14, 16, 18, 20]`
* lDACFileEpisodeNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFileNumEpisodes = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePathIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePtr = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nConditEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACFileADCNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACNum = `[0, 1, 2, 3, 4, 5, 6, 7]`
* nInterEpisodeLevel = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPPresynapticPulses = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPUsageOfDAC = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractADCIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractType = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nMembTestEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumADCChannels = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumPulses = `[4, 4, 4, 4, 4, 4, 4, 4]`
* nPNPolarity = `[1, 1, 1, 1, 1, 1, 1, 1]`
* nPNPosition = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nTelegraphDACScaleFactorEnable = `[1, 0, 0, 0, 0, 0, 0, 0]`
* nWaveformEnable = `[1, 0, 0, 0, 0, 0, 0, 0]`
* nWaveformSource = `[1, 1, 1, 1, 0, 0, 0, 0]`

## EpochPerDACSection

> This section contains waveform protocol information. These are most of     the values set when using the epoch the waveform editor. Note that digital     output signals are not stored here, but are in EpochSection. 

* fEpochInitLevel = `[0.0, -50.0, 0.0, -50.0, -50.0]`
* fEpochLevelInc = `[0.0, 10.0, 0.0, 0.0, 10.0]`
* lEpochDurationInc = `[0, 0, 0, 0, 0]`
* lEpochInitDuration = `[2000, 10000, 10000, 10000, 10000]`
* lEpochPulsePeriod = `[0, 0, 0, 0, 0]`
* lEpochPulseWidth = `[0, 0, 0, 0, 0]`
* nDACNum = `[0, 0, 0, 0, 0]`
* nEpochNum = `[0, 1, 2, 3, 4]`
* nEpochType = `[1, 1, 1, 1, 1]`

## EpochSection

> This section contains the digital output signals for each epoch. This     section has been overlooked by some previous open-source ABF-reading     projects. Note that the digital output is a single byte, but represents     8 bits corresponding to 8 outputs (7->0). When working with these bits,     I convert it to a string like "10011101" for easy eyeballing. 

* nEpochDigitalOutput = `[0, 0, 0, 0, 0]`
* nEpochNum = `[0, 1, 2, 3, 4]`

## TagSection

> Tags are comments placed in ABF files during the recording. Physically     they are located at the end of the file (after the data).      Later we will populate the times and sweeps (human-understandable units)     by multiplying the lTagTime by fSynchTimeUnit from the protocol section. 

* lTagTime = `[]`
* nTagType = `[]`
* nVoiceTagNumberorAnnotationIndex = `[]`
* sComment = `[]`
* sweeps = `[]`
* timesMin = `[]`
* timesSec = `[]`

## SynchArraySection

> Contains start time (in fSynchTimeUnit units) and length (in      multiplexed samples) of each portion of the data if the data      are not part of a continuous gap-free acquisition. 

* lLength = `[60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000]`
* lStart = `[0, 240000, 480000, 720000, 960000, 1200000, 1440000, 1680000, 1920000, 2160000, 2400000, 2640000, 2880000, 3120000, 3360000, 3600000]`

## StringsSection

> Part of the ABF file contains long strings. Some of these can be broken     apart into indexed strings.      The first string is the only one which seems to contain useful information.     This contains information like channel names, channel units, and abf     protocol path and comments. The other strings are very large and I do not     know what they do.      Strings which contain indexed substrings are separated by \x00 characters. 

* strings = `not shown due to non-ASCII characters`
