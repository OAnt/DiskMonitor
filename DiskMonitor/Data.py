"""This file contains varioues dictionaries used in the program
"""

HelpContext = [
"""
Main architecture of DiskMonitor, type of analysis and
discrimination factors are selected here
""",

"""
arguments: RootPath, Analysis, Discrimination, Factor (if needed)
""",
    
"""
Type of analysis
- DirectorySizeOrdering: return sub-directories relevant with
discrimination factor
In this analysis directories are considered independently from
their sub-directories
Input: DirectorySizeOrdering
""",
   
"""
Type of discrimination
- Pareto: relevant directories are the ones representing 80% of the
total size.
Input: Pareto
""",
    
"""
- LimitSize: a directory is considered relevant if its size is
bigger than specified size.
Input: LimitSize, Size (considered MB if nothing specified)
""",

"""
- Biggest Files: Not yet
"""

"""
Please note that DiskMonitor specifies the type of analysis e.g.
choose which sub-module will be use and provides its with inputs:
Root directory and discrimination factor
""",

"""
DiskMonitor asks
the sub-module to run a first initialization procedure which will be
used to calculate discrimination factor if needed
""",
    
"""
the sub-module to run its main operations using inputs given by
DiskMonitor
"""
]


import DirectorySizeOrdering as DSO
import GeneralFunctions as GF

AnalysisDict = {"directorysizeordering": DSO.DirectorySizeOrdering}

DiscFuncDict = {
                "pareto": GF.pareto_discrimination,
                "limitsize": GF.size_discrimination
                }

UnitDict = {
            'b': 1,
            'kb': 1000,
            'mb': 1000000,
            'gb': 1000000000,
            'tb': 1000000000000,
            'pb': 1000000000000000
            }