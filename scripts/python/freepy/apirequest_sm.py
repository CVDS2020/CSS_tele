# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : apirequest.sm

import statemap


class ApiRequestState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def ApiResponse(self, fsm):
        self.Default(fsm)

    def BlankLine(self, fsm):
        self.Default(fsm)

    def ContentFinished(self, fsm):
        self.Default(fsm)

    def ContentLength(self, fsm):
        self.Default(fsm)

    def ProcessLine(self, fsm, line):
        self.Default(fsm)

    def Default(self, fsm):
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write('TRANSITION   : Default\n')
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException, msg

class MainMap_Default(ApiRequestState):

    def BlankLine(self, fsm):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Default.BlankLine()\n")

        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.setRequestFinished()
            ctxt.errbackDeferred("Protocol failure - was not expecting blank line")
        finally:
            fsm.setState(endState)

    def ContentFinished(self, fsm):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Default.ContentFinished()\n")

        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.setRequestFinished()
            ctxt.errbackDeferred("Protocol failure - was not expecting content to be finished")
        finally:
            fsm.setState(endState)

    def ContentLength(self, fsm):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Default.ContentLength()\n")

        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.setRequestFinished()
            ctxt.errbackDeferred("Protocol failure - was not expecting content-length header")
        finally:
            fsm.setState(endState)

    def ApiResponse(self, fsm):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Default.ApiResponse()\n")

        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.setRequestFinished()
            ctxt.errbackDeferred("Protocol failure - was not expecting api response")
        finally:
            fsm.setState(endState)

    def ProcessLine(self, fsm, line):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Default.ProcessLine(line)\n")

        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.setRequestFinished()
            ctxt.errbackDeferred("Protocol failure - was not expecting needing to process a line")
        finally:
            fsm.setState(endState)

class MainMap_Startup(MainMap_Default):

    def ApiResponse(self, fsm):
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.Startup.ApiResponse()\n")

        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.ApiResponseStarted)
        fsm.getState().Entry(fsm)

class MainMap_ApiResponseStarted(MainMap_Default):

    def ContentLength(self, fsm):
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.ApiResponseStarted.ContentLength()\n")

        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.ContentPreStarted)
        fsm.getState().Entry(fsm)

class MainMap_ContentPreStarted(MainMap_Default):

    def BlankLine(self, fsm):
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.ContentPreStarted.BlankLine()\n")

        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.ContentStarted)
        fsm.getState().Entry(fsm)

class MainMap_ContentStarted(MainMap_Default):

    def ProcessLine(self, fsm, line):
        ctxt = fsm.getOwner()
        if fsm.getDebugFlag() == True:
            fsm.getDebugStream().write("TRANSITION   : MainMap.ContentStarted.ProcessLine(line)\n")

        if ctxt.add_content(line) == True :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.setRequestFinished()
                ctxt.callbackDeferred(ctxt.getResponse())
            finally:
                fsm.setState(MainMap.Startup)
                fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.doNothing()
            finally:
                fsm.setState(endState)


class MainMap:

    Startup = MainMap_Startup('MainMap.Startup', 0)
    ApiResponseStarted = MainMap_ApiResponseStarted('MainMap.ApiResponseStarted', 1)
    ContentPreStarted = MainMap_ContentPreStarted('MainMap.ContentPreStarted', 2)
    ContentStarted = MainMap_ContentStarted('MainMap.ContentStarted', 3)
    Default = MainMap_Default('MainMap.Default', -1)

class ApiRequest_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self)
        self._owner = owner
        self.setState(MainMap.Startup)
        MainMap.Startup.Entry(self)

    def ApiResponse(self):
        self._transition = 'ApiResponse'
        self.getState().ApiResponse(self)
        self._transition = None

    def BlankLine(self):
        self._transition = 'BlankLine'
        self.getState().BlankLine(self)
        self._transition = None

    def ContentFinished(self):
        self._transition = 'ContentFinished'
        self.getState().ContentFinished(self)
        self._transition = None

    def ContentLength(self):
        self._transition = 'ContentLength'
        self.getState().ContentLength(self)
        self._transition = None

    def ProcessLine(self, *arglist):
        self._transition = 'ProcessLine'
        self.getState().ProcessLine(self, *arglist)
        self._transition = None

    def getState(self):
        if self._state == None:
            raise statemap.StateUndefinedException
        return self._state

    def getOwner(self):
        return self._owner

