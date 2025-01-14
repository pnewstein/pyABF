# pclamp11_4ch_abf1.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `2018-12-14 20:36:12.308000`
* abfDateTimeString = `2018-12-14T20:36:12.308`
* abfFileComment = `                                                        `
* abfFilePath = `C:/some/path/to/pclamp11_4ch_abf1.abf`
* abfFolderPath = `C:/some/path`
* abfID = `pclamp11_4ch_abf1`
* abfVersion = `{'major': 1, 'minor': 8, 'bugfix': 4, 'build': 0}`
* abfVersionString = `1.8.4.0`
* adcNames = `['IN 0', 'IN 1', 'IN 2', 'IN 3']`
* adcUnits = `['pA', 'pA', 'pA', 'pA']`
* channelCount = `4`
* channelList = `[0, 1, 2, 3]`
* creator = `Clampex 11.0.3.3`
* creatorVersion = `{'major': 11, 'minor': 0, 'bugfix': 3, 'build': 3}`
* creatorVersionString = `11.0.3.3`
* dacNames = `['Cmd 0', 'Cmd 1', 'Cmd 2', 'Cmd 3']`
* dacUnits = `['mV', 'mV', 'mV', 'mV']`
* data = `array (2d) with values like: -0.23987, -0.02472, -0.36377, ..., -0.02563, 0.19806, 0.38391`
* dataByteStart = `6144`
* dataLengthMin = `0.03666666666666667`
* dataLengthSec = `2.2`
* dataPointByteSize = `2`
* dataPointCount = `160000`
* dataPointsPerMs = `20`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* fileGUID = `CCAF08FC-E624-4191-AFFE-FC6C3B00D858`
* fileUUID = `2D0140FD-A045-AB19-2CCB-B8A7E7FEE92C`
* holdingCommand = `[10.0, 0.0, 0.0, ..., 0.0, 0.0, 0.0]`
* md5 = `2D0140FDA045AB192CCBB8A7E7FEE92C`
* nOperationMode = `5`
* protocol = `None`
* protocolPath = `None`
* stimulusByChannel = `[Stimulus(abf, 0), Stimulus(abf, 1), Stimulus(abf, 2), Stimulus(abf, 3)]`
* stimulusFileFolder = `C:/some/path/to/pclamp11_4ch_abf1.abf`
* sweepC = `array (1d) with values like: 10.00000, 10.00000, 10.00000, ..., 10.00000, 10.00000, 10.00000`
* sweepChannel = `0`
* sweepCount = `10`
* sweepDerivative = `array (1d) with values like: 4302.97852, -6781.00586, -4418.94531, ..., -1770.01953, -1995.84961, -1995.84961`
* sweepEpochs = `Sweep epoch waveform: Step 10.00 [0:62], Step 10.00 [62:2062], Step 10.00 [2062:4000]`
* sweepIntervalSec = `0.2`
* sweepLabelC = `Membrane Potential (mV)`
* sweepLabelD = `Digital Output (V)`
* sweepLabelX = `Time (seconds)`
* sweepLabelY = `Clamp Current (pA)`
* sweepLengthSec = `0.2`
* sweepList = `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
* sweepNumber = `0`
* sweepPointCount = `4000`
* sweepTimesMin = `array (1d) with values like: 0.00000, 0.00333, 0.00667, ..., 0.02333, 0.02667, 0.03000`
* sweepTimesSec = `array (1d) with values like: 0.00000, 0.20000, 0.40000, ..., 1.40000, 1.60000, 1.80000`
* sweepUnitsC = `mV`
* sweepUnitsX = `sec`
* sweepUnitsY = `pA`
* sweepX = `array (1d) with values like: 0.00000, 0.00005, 0.00010, ..., 0.19985, 0.19990, 0.19995`
* sweepY = `array (1d) with values like: -0.23987, -0.02472, -0.36377, ..., -0.32227, -0.41077, -0.51056`
* tagComments = `[]`
* tagSweeps = `[]`
* tagTimesMin = `[]`
* tagTimesSec = `[]`
* userList = `                `
* userListEnable = `[0, 0, 0, 0]`
* userListParamToVary = `[0, 0, 0, 0]`
* userListParamToVaryName = `['CONDITNUMPULSES', 'CONDITNUMPULSES', 'CONDITNUMPULSES', 'CONDITNUMPULSES']`
* userListRepeat = `                                                                                                                                                                                  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?                 PG PG PG PG PG PG PG PG PG PG PG PG                                                                                                                                                                                                 (untitled)                                                                                                                                                                                                                                                                                                                                                                                      $Al; X                    Clampfit                                                                                               `

## Epochs for Channel 0


```
                    EPOCH         A
                     Type      Step
              First Level     10.00
              Delta Level      0.00
  First Duration (points)      2000
  Delta Duration (points)         0
     Digital Pattern #3-0      0000
     Digital Pattern #7-4      0000
    Train Period (points)         0
     Pulse Width (points)         0
```

## Epochs for Channel 1


```

```

## Epochs for Channel 2


```

```

## Epochs for Channel 3


```

```

## ABF1 Header

> The first several bytes of an ABF1 file contain variables     located at specific byte positions from the start of the file.     All ABF1 header values are read in this single block.     Arrays which reference ADC entries are shown as read, no physical <-> logical     channel mapping and interpretation of the sampling sequence is done. 

* abfDateTime = `2018-12-14 20:36:12.308000`
* abfDateTimeString = `2018-12-14T20:36:12.308`
* abfVersionDict = `{'major': 1, 'minor': 8, 'bugfix': 4, 'build': 0}`
* abfVersionFloat = `1.84`
* abfVersionString = `1.8.4.0`
* creatorVersionDict = `{'major': 11, 'minor': 0, 'bugfix': 3, 'build': 3}`
* creatorVersionString = `11.0.3.3`
* fADCProgrammableGain = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fADCRange = `10.0`
* fADCSampleInterval = `12.5`
* fDACCalibrationFactor = `[1.0, 1.0, 1.0, 1.0]`
* fDACCalibrationOffset = `[0.0, 0.0, 0.0, 0.0]`
* fDACFileOffset = `[0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0]`
* fDACRange = `10.0`
* fEpochInitLevel = `[10.0, 0.0, 0.0, ..., 0.0, 0.0, 0.0]`
* fEpochLevelInc = `[0.0, 0.0, 0.0, ..., 0.0, 0.0, 0.0]`
* fFileVersionNumber = `1.840000033378601`
* fHeaderVersionNumber = `1.840000033378601`
* fInstrumentHoldingLevel = `[0.0, 0.0, 0.0, 0.0]`
* fInstrumentOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fInstrumentScaleFactor = `[1.0, 1.0, 1.0, 1.0, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]`
* fSignalGain = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fSignalOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fSynchTimeUnit = `3.125`
* fTelegraphAdditGain = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fTelegraphFilter = `[0.0, 0.0, 0.0, 0.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0]`
* fTelegraphMembraneCap = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* lADCResolution = `32768`
* lActualAcqLength = `160000`
* lActualEpisodes = `10`
* lDACFileEpisodeNum = `[0, 0]`
* lDACFileNumEpisodes = `[0, 0]`
* lDACFilePtr = `[0, 0]`
* lDACResolution = `32768`
* lDataSectionPtr = `12`
* lEpisodesPerRun = `10`
* lEpochDurationInc = `[0, 0, 0, ..., 0, 0, 0]`
* lEpochInitDuration = `[2000, 0, 0, ..., 0, 0, 0]`
* lFileSignature = `1072399647`
* lFileStartDate = `20181214`
* lFileStartTime = `74172`
* lNumSamplesPerEpisode = `16000`
* lNumTagEntries = `0`
* lPreTriggerSamples = `80`
* lStopwatchTime = `291`
* lSynchArrayPtr = `637`
* lSynchArraySize = `10`
* lTagSectionPtr = `0`
* lTagTime = `[]`
* nADCNumChannels = `4`
* nADCPtoLChannelMap = `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
* nADCSamplingSeq = `[0, 1, 2, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]`
* nActiveDACChannel = `0`
* nCreatorBugfixVersion = `3`
* nCreatorBuildVersion = `3`
* nCreatorMajorVersion = `11`
* nCreatorMinorVersion = `0`
* nDACFileADCNum = `[0, 0]`
* nDataFormat = `0`
* nDigitalEnable = `0`
* nDigitalHolding = `0`
* nDigitalInterEpisode = `0`
* nDigitalValue = `[15, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nEpochType = `[1, 0, 0, ..., 0, 0, 0]`
* nExperimentType = `2`
* nFileStartMillisecs = `308`
* nFileType = `1`
* nInterEpisodeLevel = `[0, 0]`
* nMSBinFormat = `0`
* nNumPointsIgnored = `0`
* nOperationMode = `5`
* nTagType = `[]`
* nTelegraphDACScaleFactorEnable = `[0, 0, 0, 0]`
* nTelegraphEnable = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nTelegraphInstrument = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nTelegraphMode = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nULEnable = `[0, 0, 0, 0]`
* nULParamToVary = `[0, 0, 0, 0]`
* nULRepeat = `                                                                                                                                                                                  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?                 PG PG PG PG PG PG PG PG PG PG PG PG                                                                                                                                                                                                 (untitled)                                                                                                                                                                                                                                                                                                                                                                                      $Al; X                    Clampfit                                                                                               `
* nWaveformEnable = `[1, 1]`
* nWaveformSource = `[1, 1]`
* sADCChannelName = `['IN 0', 'IN 1', 'IN 2', 'IN 3', 'AI #4', 'AI #5', 'AI #6', 'AI #7', 'AI #8', 'AI #9', 'AI #10', 'AI #11', 'AI #12', 'AI #13', 'AI #14', 'AI #15']`
* sADCUnits = `['pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA']`
* sCreatorInfo = `Clampex`
* sDACChannelName = `['Cmd 0', 'Cmd 1', 'Cmd 2', 'Cmd 3']`
* sDACChannelUnit = `['mV', 'mV', 'mV', 'mV']`
* sDACFilePath = `['', '']`
* sFileCommentNew = ``
* sFileCommentOld = `                                                        `
* sFileGUID = `CCAF08FC-E624-4191-AFFE-FC6C3B00D858`
* sProtocolPath = `(untitled)`
* sTagComment = `[]`
* sULParamValueList = `                `
* uFileGUID = `[252, 8, 175, 204, 36, 230, 145, 65, 175, 254, 252, 108, 59, 0, 216, 88]`
* ulFileCRC = `0`
