#!/usr/bin/env python
"""
This data structure is consumed by the setup_build.py script, in order to add
the required packages to each of the WMCore systems.

It contains the name of the systems that can be built out of the WMCore
repository, and their list of dependencies, which can be:
 * bin: list with the name of executable scripts available in the root bin/ area
 * packages: list with the name of a WMCore python packages (i.e. a directory
   containing an __init__.py file)
     * note that if it's suffixed with the '+' sign, subpackages will also be
     recursively searched and added to the final system
 * modules: list with the name of specific modules (a .py file) to be added.
 * statics: list with the name of files classified as statics, e.g. css, templates,
   javascript, etc.
 * systems: list with WMCore system aliases (i.e., like a meta-package that can
   be used by multiple WMCore systems).
"""
dependencies = {
    'wmcrest': {
        'bin': ['wmc-dist-patch', 'wmc-dist-unpatch', 'wmc-httpd'],
        'packages': ['WMCore.REST'],
        'modules': ['WMCore.Configuration'],
        'systems': ['wmcbase']
    },
    'wmcbase': {
        'bin': ['wmc-dist-patch', 'wmc-dist-unpatch'],
        'packages': ['Utils', 'WMCore.DataStructs', 'WMCore.Cache'],
        'modules': ['WMCore.WMFactory', 'WMCore.WMException', 'WMCore.Configuration',
                    'WMCore.WMExceptions', 'WMCore.WMFactory', 'WMCore.Lexicon',
                    'WMCore.WMBase', 'WMCore.WMLogging', 'WMCore.Algorithms.Permissions'],
    },
    'wmccomponent': {
        'packages': ['WMCore.MsgService', 'WMCore.WorkerThreads', 'WMCore.ThreadPool'],
        'modules': ['WMComponent.__init__'],
        'systems': ['wmcbase']
    },
    'wmcdatabase': {
        'packages': ['WMCore.Wrappers+', 'WMCore.GroupUser', 'WMCore.DataStructs+', 'WMCore.Database+',
                     'WMCore.Algorithms', 'WMCore.Services'],
        'modules': ['WMCore.WMConnectionBase', 'WMCore.DAOFactory', 'WMCore.WMInit'],
        'systems': ['wmcbase']
    },
    'wmcruntime': {
        'packages': ['WMCore.WMRuntime+', 'WMCore.WMSpec+', 'PSetTweaks',
                     'WMCore.FwkJobReport', 'WMCore.Storage+', 'WMCore.Services.HTTPS'],
        'modules': ['WMCore.Algorithms.ParseXMLFile'],
        'systems': ['wmcbase']
    },
    'wmcweb': {
        'packages': ['WMCore.WebTools', 'WMCore.Agent+', 'WMCore.WorkerThreads'],
        'systems': ['wmcdatabase', 'wmcbase'],
        'statics': ['src/javascript/WMCore/WebTools',
                    'src/javascript/external/yui',
                    'src/css/WMCore/WebTools',
                    'src/css/WMCore/WebTools/Masthead',
                    'src/css/external/yui',
                    'src/templates/WMCore/WebTools',
                    'src/templates/WMCore/WebTools/Masthead', ]
    },
    'wmcore': {
        'packages': ['WMCore+',
                     'WMComponent+',
                     'WMQuality+',
                     'PSetTweaks+',
                     'Utils+'],
        'modules': [],
        'systems': [],
        'statics': ['src/couchapps+',
                    'src/css+',
                    'src/html+',
                    'src/javascript+',
                    'src/templates+',
                    'etc+',
                    'bin+'
                    ],
    },
    'wmagentdev': {
        'packages': ['WMCore+',
                     'WMComponent+',
                     'WMQuality+',
                     'PSetTweaks+',
                     'Utils+'],
        'modules': [],
        'systems': [],
        'statics': ['src/couchapps+',
                    'src/css+',
                    'src/html+',
                    'src/javascript+',
                    'src/templates+',
                    'bin+',
                    'deploy+',
                    'doc+',
                    'etc+',
                    'test+',
                    'standards+'
                    'tools+'
                    ],
    },
    'reqmgr2': {
        'packages': ['WMCore.ReqMgr+',
                     'WMCore.Services+',
                     'WMCore.ACDC',
                     'Utils'],
        'modules': ['WMCore.WorkQueue.__init__',
                    'WMCore.WorkQueue.DataStructs.__init__',
                    'WMCore.WorkQueue.DataStructs.CouchWorkQueueElement',
                    'WMCore.WorkQueue.DataStructs.WorkQueueElement'],
        'systems': ['wmcrest', 'wmcruntime', 'wmcdatabase'],
        'statics': ['src/couchapps/ReqMgr+',
                    'src/couchapps/ReqMgrAux+',
                    'src/couchapps/ConfigCache+',
                    'src/couchapps/WMStats+',
                    'src/html/ReqMgr+'
                    ],
    },
    'reqmgr2ms': {
        'packages': ['Utils', 'WMCore.MicroService+', 'WMCore.Services+'],
        'modules': ['WMCore.Wrappers.__init__',
                    'WMCore.Wrappers.JsonWrapper.__init__',
                    'WMCore.Wrappers.JsonWrapper.JSONThunker',
                    'WMCore.ReqMgr.__init__', 'WMCore.ReqMgr.DataStructs.__init__',
                    'WMCore.ReqMgr.DataStructs.RequestStatus',
                    'WMCore.ReqMgr.DataStructs.RequestType'
                    ],
        'systems': ['wmcrest', 'wmcdatabase'],
        'statics': [],
    },
    'mscore': {
        'packages': ['WMCore.MicroService.MSCore', 'WMCore.MicroService.DataStructs',
                     'WMCore.MicroService.Tools', 'WMCore.MicroService.CherryPyThreads',
                     'WMCore.MicroService.Service', 'WMCore.MicroService.WebGui',
                     'Utils', 'WMCore.Services+'],
        'modules': ['WMCore.Wrappers.__init__',
                    'WMCore.Wrappers.JsonWrapper.__init__',
                    'WMCore.Wrappers.JsonWrapper.JSONThunker',
                    'WMCore.ReqMgr.__init__', 'WMCore.ReqMgr.DataStructs.__init__',
                    'WMCore.ReqMgr.DataStructs.RequestStatus',
                    'WMCore.ReqMgr.DataStructs.RequestType'
                    ],
        'systems': ['wmcrest', 'wmcdatabase'],
        'statics': [],
    },
    'msunmerged': {
        'packages': ['WMCore.MicroService.MSUnmerged+'],
        'systems': ['mscore'],
    },
    'msoutput': {
        'packages': ['WMCore.MicroService.MSOutput+'],
        'systems': ['mscore'],
    },
    'mspileup': {
        'packages': ['WMCore.MicroService.MSPileup+'],
        'systems': ['mscore'],
    },
    'mstransferor': {
        'packages': ['WMCore.MicroService.MSTransferor+'],
        'systems': ['mscore'],
    },
    'msmonitor': {
        'packages': ['WMCore.MicroService.MSMonitor+'],
        'systems': ['mscore'],
    },
    'msrulecleaner': {
        'packages': ['WMCore.MicroService.MSRuleCleaner+'],
        'systems': ['mscore'],
    },
    'wmglobalqueue': {
        'packages': ['WMCore.GlobalWorkQueue+', 'WMCore.WorkQueue+',
                     'WMCore.Wrappers+', 'WMCore.Services+',
                     'WMCore.WMSpec', 'WMCore.WMSpec.Steps', 'WMCore.WMSpec.Steps.Templates',
                     'WMCore.ACDC', 'WMCore.GroupUser'],
        'modules': ['WMCore.Algorithms.__init__', 'WMCore.Algorithms.Permissions',
                    'WMCore.Algorithms.MiscAlgos', 'WMCore.Algorithms.ParseXMLFile',
                    'WMCore.Database.__init__', 'WMCore.Database.CMSCouch',
                    'WMCore.Database.CouchUtils',
                    'WMCore.ReqMgr.__init__', 'WMCore.ReqMgr.DataStructs.__init__',
                    'WMCore.ReqMgr.DataStructs.RequestStatus',
                    'WMCore.ReqMgr.DataStructs.RequestType'],
        'systems': ['wmcrest', 'wmcdatabase'],
        'statics': ['src/couchapps/WorkQueue+'],
    },
    'wmagent': {
        'packages': ['WMCore.Agent+', 'WMCore.Algorithms+',
                     'WMCore.JobStateMachine', 'WMComponent+',
                     'WMCore.ThreadPool',
                     'WMCore.BossAir+', 'WMCore.Credential',
                     'WMCore.JobSplitting+', 'WMCore.ProcessPool',
                     'WMCore.Services+', 'WMCore.WMSpec+',
                     'WMCore.ReqMgr.DataStructs+', 'WMCore.ReqMgr.Tools+',
                     'WMCore.WMBS+', 'WMCore.ResourceControl+'],
        'systems': ['wmcweb', 'wmcdatabase', 'wmglobalqueue', 'wmcruntime'],
        'statics': ['bin+',
                    'deploy+',
                    'etc+',
                    'src/couchapps/SummaryStats+',
                    'src/couchapps/FWJRDump+',
                    'src/couchapps/JobDump+',
                    'src/couchapps/WMStatsAgent+',
                    'src/couchapps/WorkQueue+',
                    'src/couchapps/T0Request+',
                    'src/couchapps/WMStats+',
                    'src/couchapps/LogDB+',
                    'src/couchapps/UserMonitoring+',
                    'src/javascript/WMCore/WebTools/Agent',
                    'src/javascript/WMCore/WebTools/WMBS',
                    'src/javascript/external/graphael',
                    'src/templates/WMCore/WebTools/WMBS'],
    },
    'crabcache': {
        'packages': ['WMCore.Wrappers+', 'WMCore.Services.UserFileCache+'],
        'systems': ['wmcrest'],
        'modules': ['WMCore.Services.Requests', 'WMCore.Services.Service',
                    'WMCore.Services.pycurl_manager', ],
    },
    'crabserver': {
        'packages': ['WMCore.Credential', 'WMCore.Services+', 'WMCore.WMSpec+'],
        'modules': ['WMCore.DataStructs.LumiList'],
        'systems': ['wmcrest', 'wmcdatabase'],
    },
    'crabclient': {
        'packages': ['WMCore.Wrappers+', 'WMCore.Credential', 'PSetTweaks',
                     'WMCore.Services.UserFileCache+', 'WMCore.Services.DBS+'],
        'systems': ['wmcbase'],
        'modules': ['WMCore.FwkJobReport.FileInfo', 'WMCore.Services.Requests', 'WMCore.DataStructs.LumiList',
                    'WMCore.Services.Service', 'WMCore.Services.pycurl_manager', ],
    },
    'crabtaskworker': {
        'packages': ['WMCore.Credential', 'WMCore.Algorithms+', 'WMCore.WMSpec+',
                     'WMCore.JobSplitting', 'WMCore.Services+', 'Utils+'],
        'systems': ['wmcdatabase', 'wmcruntime'],
        'modules': ['WMCore.WMBS.File', 'WMCore.WMBS.WMBSBase', 'WMCore.WMBS.__init__',
                    'WMCore.BossAir.Plugins.BasePlugin', 'WMCore.BossAir.Plugins.__init__'],
    },
    'wmclient': {
        'systems': ['wmcruntime', 'wmcdatabase']
    },
    'reqmon': {
        'packages': ['WMCore.WMStats+', 'WMCore.Services+', 'WMCore.Wrappers+',
                     'WMCore.ReqMgr.DataStructs+'
                     ],
        'modules': ['WMCore.Database.__init__', 'WMCore.Database.CMSCouch',
                    'WMCore.Database.CouchUtils', 'WMCore.ReqMgr.__init__'],
        'systems': ['wmcbase', 'wmcrest'],
        'statics': ['src/couchapps/WMStats+',
                    'src/couchapps/WMStatsErl+',
                    'src/couchapps/WMStatsErl1+',
                    'src/couchapps/WMStatsErl2+',
                    'src/couchapps/WMStatsErl3+',
                    'src/couchapps/WMStatsErl4+',
                    'src/couchapps/WMStatsErl5+',
                    'src/couchapps/WMStatsErl6+',
                    'src/couchapps/WMStatsErl7+',
                    'src/couchapps/WorkloadSummary+',
                    'src/couchapps/T0Request+',
                    'src/couchapps/LogDB+',
                    'src/html/WMStats+'],
    },
    'acdcserver': {
        'packages': ['WMCore.ACDC', 'WMCore.GroupUser', 'WMCore.DataStructs',
                     'WMCore.Wrappers+', 'WMCore.Database'],
        'modules': ['WMCore.Configuration',
                    'WMCore.Algorithms.ParseXMLFile', 'WMCore.Algorithms.Permissions',
                    'WMCore.Lexicon', 'WMCore.WMException', 'WMCore.Services.Requests',
                    'WMCore.Services.pycurl_manager'],
        'statics': ['src/couchapps/ACDC+',
                    'src/couchapps/GroupUser+']
    },
    't0agent': {
        'packages': ['WMCore.Agent+', 'WMCore.Algorithms+',
                     'WMCore.JobStateMachine', 'WMComponent+',
                     'WMCore.ThreadPool', 'WMCore.WorkerThreads',
                     'WMCore.BossAir+', 'WMCore.Credential',
                     'WMCore.JobSplitting+', 'WMCore.ProcessPool',
                     'WMCore.Services+', 'WMCore.WMSpec+',
                     'WMCore.WMBS+', 'WMCore.ResourceControl+',
                     'WMCore.DataStructs+', 'WMCore.ReqMgr+',
                     'Controllers+', 'WMQuality.Emulators+',
                     'Utils'],
        'modules': ['WMCore.Configuration',
                    'WMCore.DAOFactory',
                    'WMCore.WMException',
                    'WMCore.Lexicon',
                    'WMCore.WMBS.File'],
        'systems': ['wmcweb', 'wmcdatabase', 'wmcruntime', 'wmglobalqueue'],
        'statics': ['src/javascript/external/graphael',
                    'src/couchapps/FWJRDump+',
                    'src/couchapps/T0Request+',
                    'src/couchapps/WMStats+',
                    'src/couchapps/LogDB+',
                    'src/couchapps/UserMonitoring+',
                    'src/couchapps/JobDump+',
                    'src/couchapps/WMStatsAgent+',
                    'src/couchapps/SummaryStats+'
                    ]
    }
}
