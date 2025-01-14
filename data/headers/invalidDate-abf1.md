# invalidDate-abf1.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `0001-01-01 00:00:00`
* abfDateTimeString = `ERROR`
* abfFileComment = `%!	`
* abfFilePath = `C:/some/path/to/invalidDate-abf1.abf`
* abfFolderPath = `C:/some/path`
* abfID = `invalidDate-abf1`
* abfVersion = `{'major': 1, 'minor': 2, 'bugfix': 9, 'build': 9}`
* abfVersionString = `1.2.9.9`
* adcNames = `['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']`
* adcUnits = `['pA']`
* channelCount = `1`
* channelList = `[0]`
* creator = `                 -4431.-4483.-4523.-4515`
* creatorVersion = `{'major': -4431, 'minor': -4483, 'bugfix': -4523, 'build': -4515}`
* creatorVersionString = `-4431.-4483.-4523.-4515`
* dacNames = `['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']`
* dacUnits = `['\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00']`
* data = `array (2d) with values like: -138.39722, -139.00757, -140.22827, ..., -137.78687, -136.81030, -136.19995`
* dataByteStart = `2048`
* dataLengthMin = `0.10200000000000001`
* dataLengthSec = `6.12`
* dataPointByteSize = `2`
* dataPointCount = `120000`
* dataPointsPerMs = `20`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* fileGUID = `EDFDEDF9-EDF9-EDE9-DDED-B5ED99EDA5ED`
* fileUUID = `C2C1EDFB-5AE2-8704-E6DF-B5471CE3685C`
* holdingCommand = `[nan, nan, nan, ..., nan, nan, nan]`
* md5 = `C2C1EDFB5AE28704E6DFB5471CE3685C`
* nOperationMode = `5`
* protocol = `None`
* protocolPath = `None`
* stimulusByChannel = `[Stimulus(abf, 0)]`
* stimulusFileFolder = `C:/some/path/to/invalidDate-abf1.abf`
* sweepC = `array (1d) with values like: nan, nan, nan, ..., nan, nan, nan`
* sweepChannel = `0`
* sweepCount = `50`
* sweepDerivative = `array (1d) with values like: -12207.03125, -24414.06250, -24414.06250, ..., 24414.06250, 21972.65625, 21972.65625`
* sweepEpochs = `Sweep epoch waveform: Step nan [0:37], Unknown nan [37:-315495106], Unknown nan [-315495106:-634660257], Unknown nan [-634660257:-958544068], Unknown nan [-958544068:-1282427935], Unknown nan [-1282427935:-1603428206], Unknown nan [-1603428206:-1921282665], Unknown nan [-1921282665:-2240709980], Unknown nan [-2240709980:-2563283087], Unknown nan [-2563283087:-2887166942], Unknown nan [-2887166942:-3210002197], Step nan [-3210002197:2400]`
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
* sweepUnitsC = `        `
* sweepUnitsX = `sec`
* sweepUnitsY = `pA`
* sweepX = `array (1d) with values like: 0.00000, 0.00005, 0.00010, ..., 0.11985, 0.11990, 0.11995`
* sweepY = `array (1d) with values like: -138.39722, -139.00757, -140.22827, ..., -138.39722, -137.17651, -136.07788`
* tagComments = `[]`
* tagSweeps = `[]`
* tagTimesMin = `[]`
* tagTimesSec = `[]`
* userList = `[]`
* userListEnable = `[]`
* userListParamToVary = `[]`
* userListParamToVaryName = `[]`
* userListRepeat = `[]`

## Epochs for Channel 0


```
unknown nWaveformSource (-4795)
```

## ABF1 Header

> The first several bytes of an ABF1 file contain variables     located at specific byte positions from the start of the file.     All ABF1 header values are read in this single block.     Arrays which reference ADC entries are shown as read, no physical <-> logical     channel mapping and interpretation of the sampling sequence is done. 

* abfDateTime = `0001-01-01 00:00:00`
* abfDateTimeString = `ERROR`
* abfVersionDict = `{'major': 1, 'minor': 2, 'bugfix': 9, 'build': 9}`
* abfVersionFloat = `1.299`
* abfVersionString = `1.2.9.9`
* creatorVersionDict = `{'major': -4431, 'minor': -4483, 'bugfix': -4523, 'build': -4515}`
* creatorVersionString = `-4431.-4483.-4523.-4515`
* fADCProgrammableGain = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fADCRange = `10.0`
* fADCSampleInterval = `50.0`
* fDACCalibrationFactor = `[-1.840902299083601e+28, -1.2219318072042625e+28, -8.430754108383055e+27, -8.58546827909483e+27]`
* fDACCalibrationOffset = `[-7.811765199274433e+27, -9.668661091103055e+27, -1.3147735322574798e+28, -1.0671817465072174e+28]`
* fDACFileOffset = `[-1.5660431265393915e+27, -1.2279000667818705e+27]`
* fDACFileScale = `[-2.455816661846431e+27, -2.3784477705743363e+27]`
* fDACRange = `0.0`
* fEpochInitLevel = `[nan, nan, nan, ..., nan, nan, nan]`
* fEpochLevelInc = `[-2.1850225909150474e+27, -1.1118449589862972e+27, -1.3725996477099815e+27, ..., -1.8755263654733055e+27, -2.2237005432971809e+27, -2.8999843016289814e+27]`
* fFileVersionNumber = `1.2999999523162842`
* fHeaderVersionNumber = `0.0`
* fInstrumentHoldingLevel = `[-7.502251855254191e+27, -8.740196616906054e+27, -8.740215506371986e+27, -1.1909724447792174e+28]`
* fInstrumentOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fInstrumentScaleFactor = `[0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582, 0.009999999776482582]`
* fSignalGain = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fSignalOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fSynchTimeUnit = `0.0`
* fTelegraphAdditGain = `[-2.5131280393523e+27, -2.8226201327233694e+27, -3.983198364286379e+27, -3.8284605817421895e+27, -3.6737204380147584e+27, -4.2926904576574485e+27, -3.054750418372068e+27, -2.7452512414512746e+27, -2.185018458844375e+27, -2.2236987724097498e+27, -3.7510798845538875e+27, -2.89999846872843e+27, -2.6678788084043176e+27, -2.745240616126688e+27, -2.3784519026450088e+27, -2.1076424840225557e+27]`
* fTelegraphFilter = `[-2.417131035618763e+27, -3.286851189230249e+27, -2.1463357840957585e+27, -2.5131221363941965e+27, -2.745248880268033e+27, -2.513131581127162e+27, -3.596333837868353e+27, -4.2926939994323107e+27, -4.9116687414414837e+27, -5.335833174672361e+27, -4.215328649935078e+27, -3.7510928710617154e+27, -3.9058330147891465e+27, -4.29269281884069e+27, -3.751094051653336e+27, -3.5963432826013186e+27]`
* fTelegraphMembraneCap = `[-2.7452595055926196e+27, -1.8755293169523573e+27, -3.9831759330455855e+27, -4.4474471296675697e+27, -3.364233067010172e+27, -3.054743334822344e+27, -1.875528726656547e+27, -3.3642094551777576e+27, -4.679554984075475e+27, -4.2153262887518366e+27, -3.1321169484609217e+27, -3.0547327094977575e+27, -3.8284558593757066e+27, -3.2868582727799735e+27, -4.215310941060767e+27, -4.756930958897294e+27]`
* lADCResolution = `32768`
* lActualAcqLength = `120000`
* lActualEpisodes = `50`
* lDACFileEpisodeNum = `[-325456751, -323883879]`
* lDACFileNumEpisodes = `[-298717715, -290328947]`
* lDACFilePtr = `[-298455479, -303698419]`
* lDACResolution = `0`
* lDataSectionPtr = `4`
* lEpisodesPerRun = `0`
* lEpochDurationInc = `[-323621679, -323359571, -318903083, ..., -318378779, -317330151, -321262339]`
* lEpochInitDuration = `[-315495143, -319165151, -323883811, ..., -321262355, -322573107, -320738099]`
* lFileSignature = `1067869798`
* lFileStartDate = `-1`
* lFileStartTime = `-1`
* lNumSamplesPerEpisode = `2400`
* lNumTagEntries = `0`
* lPreTriggerSamples = `0`
* lStopwatchTime = `0`
* lSynchArrayPtr = `0`
* lSynchArraySize = `0`
* lTagSectionPtr = `0`
* lTagTime = `[]`
* nADCNumChannels = `1`
* nADCPtoLChannelMap = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nADCSamplingSeq = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nActiveDACChannel = `0`
* nCreatorBugfixVersion = `-4523`
* nCreatorBuildVersion = `-4515`
* nCreatorMajorVersion = `-4431`
* nCreatorMinorVersion = `-4483`
* nDACFileADCNum = `[-4895, -4879]`
* nDataFormat = `0`
* nDigitalEnable = `0`
* nDigitalHolding = `0`
* nDigitalInterEpisode = `0`
* nDigitalValue = `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
* nEpochType = `[-4931, -4971, -4963, ..., -4887, -4919, -4895]`
* nExperimentType = `0`
* nFileStartMillisecs = `0`
* nFileType = `0`
* nInterEpisodeLevel = `[-4871, -4887]`
* nMSBinFormat = `0`
* nNumPointsIgnored = `0`
* nOperationMode = `5`
* nTagType = `[]`
* nTelegraphDACScaleFactorEnable = `[-4931, -4935, -4919, -4887]`
* nTelegraphEnable = `[-4967, -4939, -4891, -4891, -4903, -4911, -4959, -4971, -4959, -4919, -4823, -4787, -4795, -4783, -4787, -4803]`
* nTelegraphInstrument = `[-4815, -4839, -4851, -4875, -4911, -4911, -4903, -4919, -4931, -4947, -4963, -4915, -4863, -4827, -4827, -4847]`
* nTelegraphMode = `[-4739, -4719, -4683, -4715, -4751, -4795, -4811, -4839, -4819, -4767, -4739, -4711, -4755, -4803, -4855, -4911]`
* nULEnable = `[]`
* nULParamToVary = `[]`
* nULRepeat = `[]`
* nWaveformEnable = `[-4775, -4767]`
* nWaveformSource = `[-4795, -4847]`
* sADCChannelName = `['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']`
* sADCUnits = `['pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA', 'pA']`
* sCreatorInfo = `                `
* sDACChannelName = `['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']`
* sDACChannelUnit = `['\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00', '\x00\x00\x00\x00\x00\x00\x00\x00']`
* sDACFilePath = `['ei\x1d\x11yaeM%9y\x05\x05aUm}}qiYueQiuqY1=IQqyyieUm]A=UUIi}ymeeqM\x1d)IamQiiAUyuq}UMm]\x1d\re}Q5', '91)1A9!)A)\x11\x1dIyuI\r!UaU-\x11\r))\r\r-M=\x11\x01\r1a}a\x15\r\x11511\x05\x15=91)y\r\t-55=5=Q]i5\x15aA\r\x01\x05\x05\x01\x01\x1d=U-']`
* sFileCommentNew = `%!	`
* sFileCommentOld = `                                                        `
* sFileGUID = `EDFDEDF9-EDF9-EDE9-DDED-B5ED99EDA5ED`
* sProtocolPath = `]=%9Q}mEAEMiqQ	)uyqq}aI-Mqy5A`
* sTagComment = `[]`
* sULParamValueList = `[]`
* uFileGUID = `[249, 237, 253, 237, 249, 237, 233, 237, 221, 237, 181, 237, 153, 237, 165, 237]`
* ulFileCRC = `3992055301`
