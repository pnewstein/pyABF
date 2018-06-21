"""
Boilerplate use case scrpit.
"""

import os
import sys
sys.path.insert(0, "src/")  # for importing
sys.path.append("../../src/")  # for your IDE

import matplotlib.pyplot as plt
plt.style.use('bmh')
import numpy as np
import glob
import inspect


class Uses:
    def __init__(self):
        self.figsize = (8, 5)
        self.dpi = 75

    def saveAndClose(self):
        callingFunctionName = inspect.stack()[1][3]
        outputFolder = os.path.dirname(__file__)+"/source/"
        outputFile = os.path.abspath(outputFolder+callingFunctionName+".jpg")
        plt.savefig(outputFile, dpi=self.dpi)
        plt.close()

    def demo_01a_print_sweep_data(self):
        """
        ## Access Sweep Data

        Load an ABF and display data from a certain sweep. 
        The output will look like: 
        `[-60.08911 -60.08911 ..., -61.67602 -61.64550]`.
        Note that sweeps start at 0, so calling `setSweep(14)` really loads
        the 15th sweep.
        """
        import pyabf
        plt.figure(figsize=self.figsize)
        abf = pyabf.ABF("data/abfs/17o05028_ic_steps.abf")
        abf.setSweep(14)
        print(abf.sweepY)

    def demo_02a_plot_matplotlib_sweep(self):
        """
        ## Plot Sweep Data

        Plot a sweep of ABF data using matplotlib.
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/17o05028_ic_steps.abf")
        abf.setSweep(14)
        plt.figure(figsize=self.figsize)
        plt.plot(abf.sweepX, abf.sweepY)
        self.saveAndClose()

    def demo_03a_decorate_matplotlib_plot(self):
        """
        ## Decorate Plots with ABF Information

        Plot every 5th sweep and decorate the plot nicely.
        Note that the _displayed_ sweep number starts at 1.
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/17o05028_ic_steps.abf")

        plt.figure(figsize=self.figsize)
        for sweepNumber in range(abf.sweepCount)[::5]:
            abf.setSweep(sweepNumber)
            plt.plot(abf.sweepX, abf.sweepY, alpha=.5,
                     label=f"sweep {sweepNumber+1}")

        plt.margins(0, .1)
        plt.legend()
        plt.ylabel(abf.sweepLabelY)
        plt.xlabel(abf.sweepLabelX)
        plt.title(abf.abfID)
        plt.tight_layout()
        self.saveAndClose()

    def demo_04a_plotting_multiple_channels(self):
        """
        ## Plot Multi-Channel ABFs

        Channel selection is done by adding the `channel=` 
        argument in `setSweep()`
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/14o08011_ic_pair.abf")

        fig = plt.figure(figsize=self.figsize)

        abf.setSweep(sweepNumber=0, channel=0)
        ax1 = fig.add_subplot(211)
        ax1.set_title(f"Channel {abf.sweepChannel+1}")
        ax1.plot(abf.sweepX, abf.sweepY)
        ax1.set_ylabel(abf.sweepLabelY)

        abf.setSweep(sweepNumber=0, channel=1)
        ax2 = fig.add_subplot(212)
        ax2.set_title(f"Channel {abf.sweepChannel+1}")
        ax2.plot(abf.sweepX, abf.sweepY)
        ax2.set_xlabel(abf.sweepLabelX)
        ax2.set_ylabel(abf.sweepLabelY)

        fig.subplots_adjust(hspace=.4)  # add more space between the subplots

        self.saveAndClose()

    def demo_05a_plotting_command_waveform(self):
        """
        ## Plot the Stimulus Waveform

        Episodic ABF files can have complex protocols designed with the waveform
        editor. After calling `setSweep()` the command waveform can be accessed
        as `sweep.C`.
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/171116sh_0018.abf")
        abf.setSweep(14)

        fig = plt.figure(figsize=self.figsize)

        ax1 = fig.add_subplot(211)
        ax1.set_title("ADC (recorded waveform)")
        ax1.plot(abf.sweepX, abf.sweepY)
        ax1.set_ylabel(abf.sweepLabelY)

        ax2 = fig.add_subplot(212)
        ax2.set_title("DAC (stimulus waveform)")
        ax2.plot(abf.sweepX, abf.sweepC, color='r')
        ax2.set_xlabel(abf.sweepLabelX)
        ax2.set_ylabel(abf.sweepLabelC)

        fig.subplots_adjust(hspace=.4)  # add more space between the subplots

        self.saveAndClose()

    def demo_06a_linking_subplots_and_zooming(self):
        """
        ## Zooming Gracefully

        While you can zoom in on data by setting its matplotlib axis, when
        using subplots it helps to link them together horizontally.
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/171116sh_0018.abf")
        abf.setSweep(14)

        fig = plt.figure(figsize=self.figsize)

        ax1 = fig.add_subplot(211)
        ax1.set_title("ADC (recorded waveform)")
        ax1.plot(abf.sweepX, abf.sweepY)
        ax1.set_ylabel(abf.sweepLabelY)

        ax2 = fig.add_subplot(212, sharex=ax1)  # this links them together
        ax2.set_title("DAC (stimulus waveform)")
        ax2.plot(abf.sweepX, abf.sweepC, color='r')
        ax2.set_xlabel(abf.sweepLabelX)
        ax2.set_ylabel(abf.sweepLabelC)

        fig.subplots_adjust(hspace=.4)  # add more space between the subplots

        ax1.axes.set_xlim(0.1, 0.2)  # zoom between 100 and 200 ms

        self.saveAndClose()

    def demo_07a_stacked_sweeps(self):
        """
        ## Stacking Sweeps

        I often like to view sweeps stacked one on top of another. In ClampFit
        this is done with "distribute traces". Here we can add a bit of offset
        when plotting sweeps.

        Note also that `abf.sweepList` is the same as `range(abf.sweepCount)`
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/171116sh_0018.abf")

        plt.figure(figsize=self.figsize)

        for sweepNumber in abf.sweepList:
            abf.setSweep(sweepNumber)
            plt.plot(abf.sweepX, abf.sweepY + 140*sweepNumber, color='C0')

        plt.gca().get_yaxis().set_visible(False)  # hide Y axis
        plt.xlabel(abf.sweepLabelX)
        plt.margins(0, .02)
        plt.tight_layout()

        self.saveAndClose()

    def demo_08a_xy_offset(self):
        """
        ## XY Offset and Custom Colormap

        Plotting every sweep with a slight X and Y offset produces a cool
        3D effect. I often use this view to visually inspect drug effects.

        I also assign a color by sweep from a matplotlib colormap.
        """

        import pyabf
        abf = pyabf.ABF("data/abfs/17o05026_vc_stim.abf")

        # only plot data between this time range
        i1=int(abf.dataRate*3.0)
        i2=int(abf.dataRate*3.5)

        # use a custom colormap
        cm = plt.get_cmap("winter")
        colors = [cm(x/abf.sweepCount) for x in abf.sweepList]

        plt.figure(figsize=self.figsize)
        for sweepNumber in abf.sweepList:
            abf.setSweep(sweepNumber)
            plt.plot(
                abf.sweepX[i1:i2] + .05 * sweepNumber,
                abf.sweepY[i1:i2] + 15*sweepNumber,
                color=colors[sweepNumber],
                lw=.5, alpha=.6)

        # remove axes and use tight margins
        plt.gca().get_yaxis().set_visible(False)  # hide Y axis
        plt.gca().get_xaxis().set_visible(False)  # hide X axis
        plt.margins(.02, .02)
        plt.tight_layout()

        self.saveAndClose()


def cleanDocstrings(s):
    s = s.strip()
    s = s.replace("\n        ", "\n")
    return s


def cleanCode(s):
    uses = Uses()
    s = s.replace("\n        ", "\n")
    s = s.replace("data/abfs/", "")
    s = s.replace("self.saveAndClose()", "")
    s = s.replace("self.figsize", str(uses.figsize))
    s = s.split('"""', 2)[2].strip()
    return s


if __name__ == "__main__":

    # start by deleting the contents of the output folder
    for fname in glob.glob(os.path.dirname(__file__)+"/source/*.*"):
        os.remove(fname)

    # start the markdown output text
    md = """

# Getting Started with pyABF

This page is a collection of common tasks performed by pyABF.
They start out simple and increase in complexity.

  * All ABFs used are provided in  [the data folder](/data/)
  * These tests (and this output) are automated by [generate.py](generate.py)
  * Examples `import matplotlib.pyplot as plt`
  * Examples `import numpy as np`
  * Alternate color scheme provided with `plt.style.use('bmh')`
"""

    # then run each of the use case functions above
    uses = Uses()
    for functionName in sorted(dir(uses)):
        if not functionName.startswith("demo_"):
            continue

        #if not "08a" in functionName:
            #continue

        # run the function
        print(f"### RUNNING {functionName}()")
        func = getattr(uses, functionName)
        func()

        # use the function docstring as the markdown text
        md += "\n\n"+cleanDocstrings(func.__doc__)

        # include the source code of the function
        md += "\n\n```python\n"
        md += cleanCode(inspect.getsource(func))
        md += "\n```"

        # show the image if it exists
        imgName = functionName+".jpg"
        if os.path.exists(os.path.dirname(__file__)+"/source/"+imgName):
            md += f"\n\n![source/{imgName}](source/{imgName})"

    # save the markdown page
    with open(os.path.dirname(__file__)+"/readme.md", 'w') as f:
        f.write(md)
