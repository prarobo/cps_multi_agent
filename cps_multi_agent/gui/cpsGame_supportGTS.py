#! /usr/bin/env python
#
# Support module generated by PAGE version 4.3.2
# In conjunction with Tcl version 8.6
#    Nov 19, 2014 12:43:36 PM
# Author: Prasanna Kannappan

import sys
sys.path.append("../src")
sys.path.append("../fsa") 
sys.path.append("../matlab_integ") 
sys.path.append("../matlab_files") 

from cpsFsmIndividual import fsmIndiv
from cpsFsmTurnProduct import fsmTurnProduct
import numpy as np
from cpsFsmLabelFunctions import *
import colorsys
import cPickle as pickle
import random
from scipy import io
import matlab.engine
import matlab
import StringIO
import os
import scipy
import time
from matlabLinker import matlabLinker
from copy import deepcopy
from operator import itemgetter
import platform

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global spinbox
    spinbox = StringVar()
    return

def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    return

def destroy_window ():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    return

class guiState(object):
    def __init__(self, arenaDimensions = [2,2]):
        '''Constructor'''
        global w
        self.xSqSide = 0
        self.ySqSide = 0
        self.arenaDimensions = arenaDimensions
        self.canvasWidth = 0
        self.canvasHeight = 0
        self.currMove = 0
        self.machineID = None
        self.stateLabels = None
        self.numLabels = None
        self.labelColor = None
        self.labelIndex = {}
        self.envAutoPlay = 0
        self.initState = None    
        self.gameStates = []
        self.numRobots = 2
        self.numEnv = 1 
        self.numAgents = self.numRobots + self.numEnv
        self.envPos = [None]
        self.robotPos = [None]*self.numRobots
        self.agentDot = [None]*self.numAgents
        self.agentColor = [None]*self.numAgents
        self.numRobotsEntered = 0
        self.useMatlab = False
        self.envIndex = 0
        self.labelDisplayExcl = ['p4']
        self.usePolicy = 1
        self.currProdState = None
        self.stateNonGrammarInd = 1
        
        self.stateLog = []
        self.actionLog = []
        self.policyLog = []
        self.initLog = {}
        self.sysLog = self.getSystemInformation()
        self.gameStateLabels = {}
        
        self.robotLabelInit = {}
        
        self.agentsLabelInitList = [{}] + [self.robotLabelInit]*self.numRobots  
        self.agentColor = self.getColors(self.numAgents)
        
        assert self.numRobots < 10, "Number of robots need to be less than 10 (code design restriction)"
        
        return
    
    def createMatlabObj(self):
        self.matlabObj = matlabLinker(self.useMatlab)
        
        # Initializing matlab engine
        wsDir = os.path.dirname(os.path.realpath(__file__))
        parentDir = os.path.dirname(wsDir)  
        matlabPaths = [str(parentDir+'/matlab_files'), str(parentDir+'/matlab_integ'), str(parentDir+'/mex_files')]
        self.matlabObj.initializeMatlab(parentDir, matlabPaths)
    
        return
    
    def createGame(self, arenaDimensions=[5,5], robotInit=[0,0], envInit=[1,1]):
        '''
        Creates turn based product
        '''

        robotList = []
        for i in xrange(self.numRobots):
            robotList.append( fsmIndiv(arenaDimensions, robotLabelFuction,
                                       agentName='R'+str(i),
                                       agentAlphabetInput=[['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1],
                                                           ['oo',0,0],['ne',1,1],['nw',1,1],['se',1,1],['sw',1,1]], 
                                       drawTransitionGraph = False,
                                       grammarType = 'SP_2',
                                       agentType = 'KNOWN'))

        env = fsmIndiv(arenaDimensions, envLabelFuction, 
                        agentName='E0',
                       agentAlphabetInput=[['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1],
                                           ['oo',0,0],['ne',1,1],['nw',1,1],['se',1,1],['sw',1,1]], 
                        drawTransitionGraph = False,
                        grammarType = 'SP_2',
                        agentType = 'UNKNOWN',
                        defaultAction = 'oo0')
    
        self.turnProduct = fsmTurnProduct([env]+robotList, arenaDimensions)
                
        self.gameStateLabels = {}
        for stateID in self.turnProduct.gameStates.keys(): 
            currLabel = self.turnProduct.generateStateLabels(stateID, self.agentsLabelInitList)
            self.gameStateLabels[stateID] = currLabel.propositionList

        return

    def resetCallback(self):
        ''' Callback function when reset button is pressed'''
        global w
        print "reset pressed"
        w.spinRows.configure(state=NORMAL)
        w.spinCols.configure(state=NORMAL)
        w.spinNumRobots.configure(state=NORMAL)
        w.btnRobotPosInit.configure(state=NORMAL)
        w.btnEnvPosInit.configure(state=NORMAL)
        w.radioRobotMove.configure(state=NORMAL)
        w.radioEnvMove.configure(state=NORMAL)
        w.btnSaveAutomaton.configure(state=DISABLED)
        w.btnPlayRobot.configure(state=DISABLED)
        w.chkUsePolicy.configure(state=NORMAL)

        w.txtOutput.delete(1.0, END)
 
        w.btnRobotPosInit.configure(relief=RAISED)
        w.btnEnvPosInit.configure(relief=RAISED)
        w.btnStart.configure(relief=RAISED)

        self.numAgents = self.numRobots + 1
        
        self.agentColor = self.getColors(self.numAgents)
        
        assert self.numRobots < 10, "Number of robots need to be less than 10 (code design restriction)"
        
        self.robotPos = [None]*self.numRobots
        self.envPos = [None]
        self.numRobotsEntered = 0
        
        w.canvasBoard.delete(ALL)
        self.drawGrid()
        
        w.radioRobotMove.deselect()
        w.radioEnvMove.select()
        
        w.radioEnvAutoPlay.deselect()
        w.radioEnvManualPlay.select()
        
        if hasattr(self, "robotPolicy"):
            delattr(self, "robotPolicy")
            
        self.stateLog = []
        self.actionLog = []
        self.policyLog = []
        self.gameStates = []
        self.gameStateLabels = {}
        self.initState = None

        return

    def startCallback(self):
        ''' Callback function when start button is pressed'''
        print "start pressed"
        
        global w, root
        
        if self.numRobotsEntered == self.numRobots and self.envPos != [None]:
            w.btnStart.configure(relief=SUNKEN)
            w.spinRows.configure(state=DISABLED)
            w.spinCols.configure(state=DISABLED)
            w.spinNumRobots.configure(state=DISABLED)
            w.btnRobotPosInit.configure(state=DISABLED)
            w.btnEnvPosInit.configure(state=DISABLED)
            w.radioRobotMove.configure(state=DISABLED)
            w.radioEnvMove.configure(state=DISABLED)
            w.btnSaveAutomaton.configure(state=NORMAL)
            w.btnPlayRobot.configure(state=DISABLED)
            w.chkUsePolicy.configure(state=DISABLED)
            
            w.txtOutput.insert(END,'Initializing game, please wait ...')
            w.txtOutput.see(END)
            root.update_idletasks()
            
            # Setting state labels in corners
            self.robotLabelInit['condLabels'] = {}
            self.robotLabelInit['condLabels']['p1'] = [[0,0],[self.arenaDimensions[0]-1,self.arenaDimensions[1]-1]]
            self.robotLabelInit['condLabels']['p2'] = [[self.arenaDimensions[0]-1,0],[0,self.arenaDimensions[1]-1]]        
            self.agentsLabelInitList = [{}] + [self.robotLabelInit]*self.numRobots  

            #Initializing game
            self.createGame(self.arenaDimensions, self.robotPos, self.envPos)
            self.getStateLabels()
            self.initializeDots()
            self.redrawDots()
            self.redrawLabelDots()
            self.generateLegend()
            
            if (not hasattr(self, 'matlabObj')) and self.usePolicy:
                self.createMatlabObj()
                            
            w.txtOutput.insert(END,'done\n')
            w.txtOutput.insert(END,'Grammar=%s\n' % str(self.turnProduct.agents[self.envIndex].grammarObj.grammar))
            w.txtOutput.see(END)
            root.update_idletasks()
            
            self.moveCallback()
            
            if self.currMove != 0:                
                w.txtOutput.insert(END,'First move has to be env move, setting as env move\n')
                
                self.currMove = 0
                w.radioRobotMove.deselect()
                w.radioEnvMove.select()
                
            self.envPlayCallback()
            
            self.usePolicyCallback()
            
            self.stateLog.append(self.getMachineID())
            self.initState = self.getMachineID()   
            if self.usePolicy:
                self.generateRobotPolicy()
            
            w.txtOutput.insert(END,'Env move, waiting for user input ...\n')    
            w.txtOutput.see(END)
            self.beeper()
        else:
            w.txtOutput.insert(END,'Robot or env starting position not set or all robot positions not entered (%d robots)\n' % self.numRobots)
            w.txtOutput.see(END)
            
        return
        
    def spinRowColCallback(self):
        '''Callback function when the row/col spin boxes are changed'''
        
        print "row col changed"
        
        global w
        self.arenaDimensions[0]=int(w.spinCols.get())
        self.arenaDimensions[1]=int(w.spinRows.get())
        
        self.resetCallback()

        return
    
    def spinNumRobotsCallback(self):
        '''Callback function when the robots spin box is changed'''
        
        print "Number of robots changed"
        
        global w
        self.numRobots = int(w.spinNumRobots.get())        
        self.resetCallback()

        return 
              
    def drawGrid(self):
        '''Draw arena grid'''
        global w, root
        w.canvasBoard.delete(ALL)
        
        self.canvasWidth = float(root.winfo_width())*0.52
        self.canvasHeight = float(root.winfo_height())*0.91
        
        self.xSqSide = self.canvasWidth/self.arenaDimensions[0]
        self.ySqSide = self.canvasHeight/self.arenaDimensions[1] 
        
        
        lineXCoord = np.linspace(0, self.canvasWidth, self.arenaDimensions[0]+1)
        lineYCoord = np.linspace(0, self.canvasHeight, self.arenaDimensions[1]+1)
                        
        for i in lineXCoord:
            w.canvasBoard.create_line(i,0,i,self.canvasHeight)

        for i in lineYCoord:
            w.canvasBoard.create_line(0,i,self.canvasWidth,i)
        return
    
    def agentPlaceCallback(self, event):
        '''Callback when mouse click in game arena'''
        global w
        
        print "clicked at", event.x, event.y
        
        gridX = int(np.floor(event.x/self.xSqSide))
        gridY = int(np.floor(event.y/self.ySqSide))
        print "grid square", gridX, gridY       
        
        remapX, remapY = self.remapCoord(gridX, gridY)
        
        if w.btnRobotPosInit.cget("relief")==SUNKEN:
            w.btnRobotPosInit.configure(relief=RAISED)                      
            self.robotPos[self.numRobotsEntered] = [remapX, remapY]
            self.numRobotsEntered += 1
            
        elif w.btnEnvPosInit.cget("relief")==SUNKEN:
            w.btnEnvPosInit.configure(relief=RAISED)
            self.envPos[0] = [remapX, remapY]

        elif w.btnStart.cget("relief")==SUNKEN:
            if(self.currMove >= self.numEnv):
                for currRobotPos in self.robotPos:
                    if self.turnProduct.addActionToAgent(self.turnProduct.agentNames[self.currMove],
                                                          currRobotPos,
                                                          [remapX, remapY],
                                                          addAction=False):
                        self.robotPlay(remapX, remapY)
                        
                        if self.envAutoPlay == 1:
                            self.redrawDots()
                            self.getStateLabels()
                            self.redrawLabelDots() 
                            
                            self.envAutoPlayFunc()
    
                        else:
                            pass
                            #w.txtOutput.insert(END,'Waiting for user input ...\n')      
                            #w.txtOutput.see(END) 
                            #self.beeper()                       
                        break
                           
                    else:
                        w.txtOutput.insert(END,'Invalid robot move\n')
                        w.txtOutput.see(END)
            else:
                if self.envAutoPlay == 0:
                    if self.turnProduct.addActionToAgent(self.turnProduct.agentNames[self.currMove],
                                                          self.envPos[0][:],
                                                          [remapX, remapY],
                                                          addAction=True):     
                        
                        w.txtOutput.insert(END,'Grammar=%s\n' % str(self.turnProduct.agents[self.envIndex].grammarObj.grammar))
                        self.envPlay([remapX, remapY])                                       
                        
                        #self.turnProduct.testFSA()
                    else:
                        w.txtOutput.insert(END,'Invalid env move\n')
                        w.txtOutput.see(END)
                else:
                    w.txtOutput.insert(END,'Auto-play for env is on, cannot make env move\n') 
                    w.txtOutput.see(END)   
        else:
            pass
        
        self.redrawDots()
        if w.btnStart.cget("relief")==SUNKEN:
            self.getStateLabels()
            self.redrawLabelDots() 
                            
        return
            
    def robotInitPosCallback(self):
        global w
        
        if self.numRobotsEntered != self.numRobots:
            print "Setting robot initial position"
            w.btnRobotPosInit.configure(relief=SUNKEN)
            w.btnEnvPosInit.configure(relief=RAISED)
        return

    def envInitPosCallback(self):
        global w
        
        if self.envPos == [None]:
            print "Setting env initial position"
            w.btnEnvPosInit.configure(relief=SUNKEN)
            w.btnRobotPosInit.configure(relief=RAISED)
        return
    
    def moveCallback(self):
        print "Setting player move"
        
        global w
        print "move ", w.moveRadio.get()
        self.currMove = w.moveRadio.get()
        return
    
    def remapCoord(self,x,y):
        remapX = x
        remapY = self.arenaDimensions[1]-1-y
        return remapX, remapY
    
    def getAgentBoundingBox(self,x,y):      
        bbX1 = (x+0.1)*self.xSqSide
        bbY1 = (y+0.25)*self.ySqSide
        bbX2 = bbX1+0.5*self.xSqSide
        bbY2 = bbY1+0.5*self.ySqSide
        return [bbX1,bbY1,bbX2,bbY2]

    def getLabelBoundingBox(self,x,y,labelI):  
        labelInc = np.minimum(0.2,(0.9/self.numLabels))    
        bbX1 = (x+0.7)*self.xSqSide
        bbY1 = (y+0.05+labelInc*labelI)*self.ySqSide
        bbX2 = bbX1+labelInc*self.xSqSide
        bbY2 = bbY1+labelInc*self.ySqSide
        return [bbX1,bbY1,bbX2,bbY2]
    
    def redrawDots(self):
        global w
        
        w.canvasBoard.delete(ALL)
        self.drawGrid()
        
        agentColor = deepcopy(self.agentColor)
        agentPos = self.envPos[:] + deepcopy(self.robotPos)
        
        while len(agentPos) != 0:
            if agentPos[0] != None:
                ind = [i for i, x in enumerate(agentPos) if x == agentPos[0]]
                agX, agY = self.remapCoord(agentPos[0][0], agentPos[0][1])
                agBB = self.getAgentBoundingBox(agX, agY)
                
                for i in xrange(len(ind)):
                    if len(ind) == 1:
                        w.canvasBoard.create_oval(agBB, fill=agentColor[i])
                    else:                        
                        w.canvasBoard.create_arc(agBB, start=(360/len(ind))*i, extent=360/len(ind), fill=agentColor[ind[i]]) 
                    
                agentColor = [i for j, i in enumerate(agentColor) if j not in ind]
                agentPos = [i for j, i in enumerate(agentPos) if j not in ind]
                
            else:
                del agentPos[0]
                del agentColor[0]
                           
        return
    
    def redrawLabelDots(self):
        for prop in self.stateLabels.keys():
            if prop not in self.labelDisplayExcl:
                propIndex = self.labelIndex[prop]
                propColor = self.labelColor[propIndex]
                
                for lpos in self.stateLabels[prop]:
                    pos = np.unravel_index(lpos,self.arenaDimensions)
                    x, y = self.remapCoord(pos[0], pos[1])
                    BB = self.getLabelBoundingBox(x, y, propIndex)
                    w.canvasBoard.create_oval(BB,fill=propColor)
    
    def getStateLabels(self):                             
        self.machineID = self.getMachineID()
        #self.stateLabels = self.turnProduct.generateStateLabels(self.machineID)
        self.stateLabels = self.gameStateLabels[self.machineID]
        return    
    
    def getMachineID(self):
        userID = []
        agentPos = deepcopy(self.envPos) + deepcopy(self.robotPos)
        for ag in xrange(self.numAgents):            
            agPosStr = ''.join(map(str,agentPos[ag]))
            userID.extend([self.turnProduct.agentNames[ag], agPosStr])
            
        userID.extend(['T', self.turnProduct.agentNames[self.currMove]])
                     
        return self.turnProduct.generateMachineID(userID)            
        
    def getColors(self, numColors):
        colors=[]
        for i in np.arange(0., 360., 360. / numColors):
            hue = i/360.
            lightness = (50 + np.random.rand() * 10)/100.
            saturation = (90 + np.random.rand() * 10)/100.
            rgbColor = colorsys.hls_to_rgb(hue, lightness, saturation)
            rgbColor = np.round(np.array(rgbColor)*255)
            hexColor = '#%02x%02x%02x' % (rgbColor[0], rgbColor[1], rgbColor[2])
            colors.append(hexColor)
        return colors

    def initializeDots(self):
        self.numLabels = len(self.stateLabels.keys())
        self.labelColor = self.getColors(self.numLabels)
        
        tempKeys = self.stateLabels.keys()
        for i in range(len(tempKeys)):
            self.labelIndex[tempKeys[i]] = i
            
        return    
    
    def generateLegend(self):
        global w

        startX = 20
        startY = 30
        circDia = 20
        lineGap = 20
        
        for i in xrange(self.numAgents):
            x = startX
            y = startY+i*(circDia+lineGap)  
            w.canvasLegend.create_oval([x,y,x+circDia,y+circDia],fill=self.agentColor[i])
            w.canvasLegend.create_text([x+circDia+5,y-2], anchor=NW, text=self.turnProduct.agentNames[i])
                
        startX = 100
        startY = 30
        circDia = 10
        lineGap = 10
        
        for i in self.labelIndex.keys():
            x = startX
            y = startY+self.labelIndex[i]*(circDia+lineGap)  
            w.canvasLegend.create_oval([x,y,x+circDia,y+circDia],fill=self.labelColor[self.labelIndex[i]])
            w.canvasLegend.create_text([x+circDia+5,y-2], anchor=NW, text=i)
        return

    def windowResizeCallback(self, event):
        print "Window dimensions : ", event.width, event.height
        self.redrawDots()
        
        global w
        if w.btnStart.cget("relief")==SUNKEN:
            self.redrawLabelDots()            
        return
    
    def saveAutomatonCallback(self):
        global w
        print "Saving file to disk"      
        #         pickle.dump(self.turnProduct, open("../gameAutomaton.p","wb"))
        #         w.txtOutput.insert(END,"Game automaton saved to file ../gameAutomaton.p\n")
        #         
        #         # Getting labels of all states
        #         gameStateLabels = {}
        #         for stateID in self.turnProduct.gameStates.keys():
        #             gameStateLabels[stateID] = self.turnProduct.generateStateLabels(stateID, self.agentsLabelInitList)
        #         
        #         # Saving labels of all states to disk    
        #         pickle.dump(self.turnProduct, open("../gameLabels.p","wb"))
        #         w.txtOutput.insert(END,"Game state labels saved to file ../gameLabels.p\n")
        #         
        #         # Saving state and action logs of game
        #         pickle.dump(self.stateLog, open("../stateLog.p","wb"))
        #         pickle.dump(self.actionLog, open("../actionLog.p","wb"))
        #         w.txtOutput.insert(END,"State log saved to file ../stateLog.p\n")
        #         w.txtOutput.insert(END,"Action log saved to file ../actionLog.p\n")
        #         
        #         # Saving policy log of the game
        #         pickle.dump(self.policyLog, open("../policyLog.p","wb"))
        #         w.txtOutput.insert(END,"Policy log saved to file ../policyLog.p\n")
        #         
        #         # Saving system log of the game
        #         pickle.dump(self.sysLog, open("../sysLog.p","wb"))
        #         w.txtOutput.insert(END,"System log saved to file ../sysLog.p\n")
        #         
        #         # Saving init log of the game 
        #         pickle.dump(self.initLog, open("../initLog.p","wb"))
        #         w.txtOutput.insert(END,"Init log saved to file ../initLog.p\n")
        
        # Saving game log to reload game later
        gameLog = {'actionLog': self.actionLog,
                   'stateLog': self.stateLog,
                   'stateLabels': self.gameStateLabels,
                   'initState': self.initState,
                   'arenaDimensions': self.arenaDimensions,
                   'agentColor': self.agentColor,
                   'labelDisplayExcl': self.labelDisplayExcl,
                   'labelColor': self.labelColor,
                   'labelIndex': self.labelIndex,
                   'numLabels': self.numLabels}
        
        pickle.dump(gameLog, open("../game_runs/gameLog.p","wb"))
        w.txtOutput.insert(END,"Game log saved to file ../game_runs/gameLog.p\n")
        return
    
    def getSystemInformation(self):
        return platform.uname()
        
    def envPlayCallback(self):
        print "Setting env move mode"
        global w
        print "Env auto-play ", w.moveEnvPlay.get()
        if w.btnStart.cget("relief")==SUNKEN:
            if not self.turnProduct.agents[self.envIndex].alphabetList:
                if w.moveEnvPlay.get() == 1:
                    w.txtOutput.insert(END,'No actions available for env, cannot set auto-play reverting to manual-play\n')
                    w.txtOutput.see(END)
                w.moveEnvPlay.set(0)
                w.radioEnvAutoPlay.deselect()
                w.radioEnvManualPlay.select()                  
                self.envAutoPlay = 0          
            else:    
                self.envAutoPlay = w.moveEnvPlay.get()
            
            if self.envAutoPlay == 1 and self.currMove == self.envIndex:
                self.envAutoPlayFunc()
                
                self.redrawDots()
                self.getStateLabels()
                self.redrawLabelDots() 
                
        else:
            self.envAutoPlay = w.moveEnvPlay.get()
        return
    
    def envAutoPlayFunc(self):
        global w
        envAction, envPos = self.chooseEnvMove(list(self.turnProduct.agents[self.envIndex].alphabetList))
        
        w.txtOutput.insert(END,'Env auto-play move=%s\n' % envAction)
        self.envPlay(envPos)
        return
    
    def envPlay(self, envPos):
        global w, root
        
        self.actionLog.append(self.turnProduct.agents[self.envIndex].actionObj.getActionID(self.envPos[self.envIndex][:],envPos))
        self.envPos = [envPos[:]]    
        self.currMove = (self.currMove + 1) % self.numAgents
        
        self.redrawDots()
        self.getStateLabels()
        self.redrawLabelDots()
        root.update_idletasks()
        
        self.stateLog.append(self.getMachineID()) 
        # for state in self.matlabObj.P.currentStates:
        #     print "state:",state
        #     print 'Dist:',self.matlabObj.dist[state]
        #if self.turnProduct.getCurrentAlphabet():

        if self.usePolicy:
            self.generateRobotPolicy()
        # self.matlabObj.P.input(self.actionLog[-1])   
        # print "currProdState:",
        # for state in self.matlabObj.P.currentStates:
        #     print "state:",state
        #     print 'Dist:',self.matlabObj.dist[state]
        if hasattr(self, 'robotPolicy') and self.usePolicy:
            if self.useMatlab:
                if not self.robotPolicy[self.getMachineID()]==0:
                    w.btnPlayRobot.configure(state=NORMAL)
                else:
                    w.btnPlayRobot.configure(state=DISABLED)
                    w.txtOutput.insert(END,'waiting for user input ...\n')
                    w.txtOutput.see(END)  
                    
            else:
#                 for state in self.matlabObj.P.currentStates:
#                     self.policyAction = self.matlabObj.P.getAction(self.matlabObj.dist, state)
#                 if self.policyAction:                                                    
#                     w.btnPlayRobot.configure(state=NORMAL)
                if self.robotPolicy[self.currProdState]:
                    w.btnPlayRobot.configure(state=NORMAL)
                    act = self.getFuturePolicyActions()
                    w.txtOutput.insert(END,'Policy actions available  '+str(act)+'\n')
  
                else:
                    w.btnPlayRobot.configure(state=DISABLED)
                    w.txtOutput.insert(END,'Policy actions available not available)...\n')
           
                w.txtOutput.insert(END,'Robot move, waiting for user input ...\n')
                w.txtOutput.see(END) 
                    
        else:
            w.btnPlayRobot.configure(state=DISABLED)
            w.txtOutput.insert(END,'Robot move, waiting for user input ...\n')
            w.txtOutput.see(END) 
            
            # Beep to indicate user action        
            self.beeper()
        return
    
    def getFuturePolicyActions(self):
        '''Returns the sequence of actions available from policy'''
        
        currState = self.currProdState
        currMove = self.currMove
        
        act = [None]*(self.numAgents-currMove)
        
        for i in xrange(self.numAgents-currMove):
            
            resultState = self.robotPolicy[currState]
            
            # Exit if bad transition state is found
            if not resultState:
                break
            
            act[i] = self.turnProduct.getTransitionAction(currState[self.stateNonGrammarInd], 
                                                          resultState[self.stateNonGrammarInd])
            currState = resultState
            
        return act
    
    def chooseEnvMove(self, actionList):
        '''Choose env move randomly'''
        if not actionList:
            return 'oo0', self.envPos
            
        numActions = len(actionList)    
        
        # Choose random action
        actionNum = random.randrange(0,numActions)
        actionID = actionList[actionNum]
        
        # checking if the action is feasible
        resultPos = self.turnProduct.agents[self.envIndex].actionObj.actionResultPos(actionID, self.envPos[0][:])
        if  resultPos == None:
            actionList.remove(actionID)
            actionID, resultPos = self.chooseEnvMove(actionList)

        return actionID, resultPos  
    
    def playRobotCallback(self):
        endState = self.robotPolicy[self.currProdState]
        if endState:
            endGridSq = map(int, list(endState[self.stateNonGrammarInd][self.currMove*6+3:self.currMove*6+5]))
            robotIndex = self.currMove-self.numEnv
            actionID = self.turnProduct.agents[self.currMove].actionObj.getActionID(self.robotPos[robotIndex][:], endGridSq)
             
            if actionID in self.turnProduct.agents[self.currMove].alphabetList:
                if self.turnProduct.addActionToAgent( self.turnProduct.agentNames[self.currMove],
                                                      self.robotPos[robotIndex][:],
                                                      endGridSq[:],
                                                      addAction=False):
                    w.txtOutput.insert(END,'Robot move from policy, %s\n' % actionID)      
                    w.txtOutput.see(END)
                    self.robotPlay(endGridSq[0], endGridSq[1])
                    w.btnPlayRobot.configure(state=DISABLED)
                else:
                    print 'Invalid robot move, policy is incorrect'
                     
            else:
                print 'Policy action is incorrect'
        else:
            print 'Policy not available'
        return
    
    def robotPlay(self, remapX, remapY):
        global root
        robotInd = self.currMove-self.numEnv
        currAction = self.turnProduct.agents[self.currMove].actionObj.getActionID(self.robotPos[robotInd][:], [remapX, remapY])
        self.actionLog.append(currAction)

        self.robotPos[robotInd] = [remapX, remapY]
        self.currMove = (self.currMove + 1) % self.numAgents
        self.currProdState = self.robotPolicy[self.currProdState]   


        if self.usePolicy and (not self.useMatlab):
            self.matlabObj.P.input(currAction, self.matlabObj.dist)   
                
        self.redrawDots()
        self.getStateLabels()
        self.redrawLabelDots()
        root.update_idletasks()
        
        self.stateLog.append(self.getMachineID())
        if self.currMove > self.numEnv-1 and self.usePolicy:
            if not self.useMatlab:
                if self.robotPolicy[self.currProdState]:                                                   
                    w.btnPlayRobot.configure(state=NORMAL)
                    self.playRobotCallback()
                else:
                    w.btnPlayRobot.configure(state=DISABLED)
                    w.txtOutput.insert(END,'waiting for user input ...\n')
                    w.txtOutput.see(END) 
                    self.beeper()         
            else:
                print "Code not designed for multi-agent matlab-use"
        else:
            w.txtOutput.insert(END,'Env move, waiting for user input ...\n')      
            w.txtOutput.see(END)
            self.beeper()
            
        # If env auto-play is on
        if self.envAutoPlay == 1:
            self.envPlayCallback()
            
        return
    
    def generateRobotPolicy(self):
        '''Getting robot policy'''
        global w, root
        
        startTime = time.time()
        # gameStates, gameAlphabet, gameTransitions, newTransitions = self.turnProduct.getFSA()
        
        if not hasattr(self, "robotPolicy"):
            w.txtOutput.insert(END,'Generating robot policy ...')
            root.update_idletasks()
            w.txtOutput.see(END)
            self.robotPolicy, self.currProdState = self.matlabObj.gtsPolicyGenerator(self.turnProduct, self.gameStateLabels,
                                                                                     self.initState,
                                                                                     self.numEnv)
            #self.initLog['turnProduct'] = deepcopy(self.turnProduct)
            #self.initLog['gameStateLabels'] = deepcopy(self.gameStateLabels)
            #self.initLog['initState'] = deepcopy(self.initState)
            #self.initLog['numAgents'] = deepcopy(self.numAgents)
            #self.initLog['numEnv'] = deepcopy(self.numEnv)
            #self.initLog['matlabObj'] = deepcopy(self.matlabObj)
        else:
            w.txtOutput.insert(END,'Updating robot policy ...')
            root.update_idletasks()
            w.txtOutput.see(END)
            lastAction = self.actionLog[-1]
            currState = self.stateLog[-1]
            self.robotPolicy, self.currProdState = self.matlabObj.gtsPolicyUpdater(self.turnProduct, self.gameStateLabels, self.robotPolicy, 
                                                                                   self.stateLog, self.numEnv,
                                                                                   lastAction, currState, self.initState)         

        endTime = time.time()
        self.policyLog.append(deepcopy(self.robotPolicy))
                    
        w.txtOutput.insert(END,'done (%s minutes)\n' % str((endTime-startTime)/60))
        root.update_idletasks()
        w.txtOutput.see(END)
        return

    def usePolicyCallback(self):
        print "Setting policy computation on/off"
        
        global w
        print "Policy compute ", w.usePolicy.get()
        self.usePolicy = w.usePolicy.get()
        return
        
    def beeper(self):
        if platform.system() == 'Linux':
            soundFile = "/usr/share/sounds/KDE-Im-Message-In.ogg"
            if os.path.isfile(soundFile):
                print "Beep"
                os.system('paplay %s' % (soundFile))
        return
    
    def destroyObjects(self):
        self.matlabObj.destructor()
        return
        
        
if __name__=="__main__":
    pass
    