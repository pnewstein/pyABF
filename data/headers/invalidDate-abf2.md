# invalidDate-abf2.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `0001-01-01 00:00:00`
* abfDateTimeString = `ERROR`
* abfFileComment = ``
* abfFilePath = `C:/some/path/to/invalidDate-abf2.abf`
* abfFolderPath = `C:/some/path`
* abfID = `invalidDate-abf2`
* abfVersion = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionString = `2.6.0.0`
* adcNames = `['IN 0']`
* adcUnits = `['pA']`
* channelCount = `1`
* channelList = `[0]`
* creator = `Clampex 10.7.0.3`
* creatorVersion = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionString = `10.7.0.3`
* dacNames = `['Cmd 0']`
* dacUnits = `['mV']`
* data = `array (2d) with values like: -138.42772, -139.03807, -140.25877, ..., -137.81737, -136.84081, -136.23045`
* dataByteStart = `6656`
* dataLengthMin = `0.10200000000000001`
* dataLengthSec = `6.12`
* dataPointByteSize = `2`
* dataPointCount = `120000`
* dataPointsPerMs = `20`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* fileGUID = `3529074B-C6D9-4B5E-AB13-C9A9B4F09065`
* fileUUID = `A9F9A479-A3C5-AFA2-FE61-2A7F0C18BACC`
* holdingCommand = `[-70.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* md5 = `A9F9A479A3C5AFA2FE612A7F0C18BACC`
* nOperationMode = `5`
* protocol = `0204 Cm ramp`
* protocolPath = `C:\Users\swharden\Desktop\permanent\0204 Cm ramp.pro`
* stimulusByChannel = `[Stimulus(abf, 0)]`
* stimulusFileFolder = `C:/some/path/to/invalidDate-abf2.abf`
* sweepC = `array (1d) with values like: -70.00000, -70.00000, -70.00000, ..., -70.00000, -70.00000, -70.00000`
* sweepChannel = `0`
* sweepCount = `50`
* sweepDerivative = `array (1d) with values like: -12207.03125, -24414.06250, -24414.06250, ..., 24414.06250, 21972.65625, 21972.65625`
* sweepEpochs = `Sweep epoch waveform: Step -70.00 [0:37], Ramp -80.00 [37:1037], Ramp -70.00 [1037:2037], Step -70.00 [2037:2400]`
* sweepIntervalSec = `0.12`
* sweepLabelC = `Membrane Potential (mV)`
* sweepLabelD = `Digital Output (V)`
* sweepLabelX = `Time (seconds)`
* sweepLabelY = `Clamp Current (pA)`
* sweepLengthSec = `0.12`
* sweepList = `[0, 1, 2, ..., 47, 48, 49]`
* sweepNumber = `0`
* sweepPointCount = `2400`
* sweepTimesMin = `array (1d) with values like: 0.00000, 0.00200, 0.00400, ..., 0.09400, 0.09600, 0.09800`
* sweepTimesSec = `array (1d) with values like: 0.00000, 0.12000, 0.24000, ..., 5.64000, 5.76000, 5.88000`
* sweepUnitsC = `mV`
* sweepUnitsX = `sec`
* sweepUnitsY = `pA`
* sweepX = `array (1d) with values like: 0.00000, 0.00005, 0.00010, ..., 0.11985, 0.11990, 0.11995`
* sweepY = `array (1d) with values like: -138.42772, -139.03807, -140.25877, ..., -138.42772, -137.20702, -136.10838`
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
                    EPOCH         A         B
                     Type      Ramp      Ramp
              First Level    -80.00    -70.00
              Delta Level      0.00      0.00
  First Duration (points)      1000      1000
  Delta Duration (points)         0         0
     Digital Pattern #3-0      0000      0000
     Digital Pattern #7-4      0000      0000
    Train Period (points)         0         0
     Pulse Width (points)         0         0
```

## ABF2 Header

> The first several bytes of an ABF2 file contain variables     located at specific byte positions from the start of the file. 

* abfDateTime = `0001-01-01 00:00:00`
* abfDateTimeString = `ERROR`
* abfVersionDict = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionFloat = `2.6`
* abfVersionString = `2.6.0.0`
* creatorVersionDict = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionFloat = `10.703`
* creatorVersionString = `10.7.0.3`
* fFileVersionNumber = `[0, 0, 6, 2]`
* lActualEpisodes = `50`
* nCRCEnable = `0`
* nDataFormat = `0`
* nFileType = `1`
* nSimultaneousScan = `1`
* sFileGUID = `3529074B-C6D9-4B5E-AB13-C9A9B4F09065`
* sFileSignature = `ABF2`
* uCreatorNameIndex = `1`
* uCreatorVersion = `[3, 0, 7, 10]`
* uFileCRC = `0`
* uFileGUID = `[75, 7, 41, 53, 217, 198, 94, 75, 171, 19, 201, 169, 180, 240, 144, 101]`
* uFileInfoSize = `512`
* uFileStartDate = `4294967295`
* uFileStartTimeMS = `4294967295`
* uModifierNameIndex = `0`
* uModifierVersion = `0`
* uProtocolPathIndex = `2`
* uStopwatchTime = `359`

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
* lEpisodesPerRun = `50`
* lFileCommentIndex = `0`
* lFinishDisplayNum = `2400`
* lNumSamplesPerEpisode = `2400`
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
* fADCDisplayAmplification = `[25.47731590270996]`
* fADCDisplayOffset = `[-7.0]`
* fADCProgrammableGain = `[1.0]`
* fInstrumentOffset = `[0.0]`
* fInstrumentScaleFactor = `[0.0005000000237487257]`
* fPostProcessLowpassFilter = `[100000.0]`
* fSignalGain = `[1.0]`
* fSignalHighpassFilter = `[1.0]`
* fSignalLowpassFilter = `[5000.0]`
* fSignalOffset = `[0.0]`
* fTelegraphAccessResistance = `[0.0]`
* fTelegraphAdditGain = `[5.0]`
* fTelegraphFilter = `[2000.0]`
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
* nTelegraphMode = `[0]`
* sTelegraphInstrument = `['MultiClamp 700']`

## DACSection

> Information about the DAC (what gets clamped).     There is 1 item per DAC. 

* fBaselineDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fBaselineLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACCalibrationFactor = `[1.001173496246338, 1.0012290477752686, 1.001173496246338, 1.001173496246338, 1.0, 1.0, 1.0, 1.0]`
* fDACCalibrationOffset = `[-4.0, -4.0, -7.0, -6.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fDACHoldingLevel = `[-70.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACScaleFactor = `[20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]`
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

* fEpochInitLevel = `[-80.0, -70.0]`
* fEpochLevelInc = `[0.0, 0.0]`
* lEpochDurationInc = `[0, 0]`
* lEpochInitDuration = `[1000, 1000]`
* lEpochPulsePeriod = `[0, 0]`
* lEpochPulseWidth = `[0, 0]`
* nDACNum = `[0, 0]`
* nEpochNum = `[0, 1]`
* nEpochType = `[2, 2]`

## EpochSection

> This section contains the digital output signals for each epoch. This     section has been overlooked by some previous open-source ABF-reading     projects. Note that the digital output is a single byte, but represents     8 bits corresponding to 8 outputs (7->0). When working with these bits,     I convert it to a string like "10011101" for easy eyeballing. 

* nEpochDigitalOutput = `[0, 0]`
* nEpochNum = `[0, 1]`

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

* lLength = `[2400, 2400, 2400, ..., 2400, 2400, 2400]`
* lStart = `[0, 9600, 19200, ..., 451200, 460800, 470400]`

## StringsSection

> Part of the ABF file contains long strings. Some of these can be broken     apart into indexed strings.      The first string is the only one which seems to contain useful information.     This contains information like channel names, channel units, and abf     protocol path and comments. The other strings are very large and I do not     know what they do.      Strings which contain indexed substrings are separated by \x00 characters. 

* strings = `not shown due to non-ASCII characters`
