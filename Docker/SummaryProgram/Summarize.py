#import pandas as pd
import os
import csv

# Output - RQ1 - Table 3
#     | Flows                       | Specification               | 
# CRN | Org % | Test # | % Detected | Org % | Test # | % Detected | Inv Only | Spec Only |
# Min |
# S   |
# AM  |
# Mod |
# Max |
# AL1 |
# H1  |
# H2  |
# MWT |
def generateTable3(cData):
    # 
    print(", Without Reaction Counting ,,,,,,,,, With Reaction Counting,,,,,,,,,,,,,,")
    print(" , Flows,,, Ineq,,, Flows+Ineq,,, Ineq,,, Irred,,, Ineq+Irred,,, Flow+Ineq+Irred,,, Specification,,,")
    print("CRN, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, No. Inv, % Det,  % Fkly, ")
    # This determines order in paper
    # Grab MIN
    for k in cData:
        if 'Min' in k:
            # Grab Data
            data = cData[k]
            
            #print(data)
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("Min", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")


    # # Grab S
    for k in cData:
        if 'Sub' in k:
            #Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("S", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")   
    # # Grab AM
    for k in cData:
        if 'ApproximateMajority' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("AM", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
    # # Grab Mod
    for k in cData:
        if 'Mod' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("Mod", end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
            
    # Grab Max
    for k in cData:
        if 'Max' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("Max", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
            
    # Grab AL1
    for k in cData:
        if 'AtLeast1' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("AL1", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
            
    # Grab H1
    for k in cData:
        if 'Hailstone1' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("H1", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
    # Grab H2
    for k in cData:
        if 'Hailstone2' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("H2", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
    # # Grab MWT
    for k in cData:
        if 'Molecular' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("MWT", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("{:.1f}".format(spec['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(spec['flakeOnly']*100)     , end=" , ")
            print("")  
    # # Grab PP
    for k in cData:
        if 'PredatorPrey' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("PP", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print("")  
    # Grab ECG
    for k in cData:
        if 'EcoliGly' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("ECG", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print(0   , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print("")  
    # # Grab H4
    for k in cData:
        if 'Hailstone4' in k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("H4", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print("")  
    # # Grab EC
    for k in cData:
        if 'Ecoli' == k:
            # Grab Data
            data = cData[k]
            flows = data['F']
            ineq  = data['IN']
            fin   = data['FIN']
            eq    = data['EQ']
            irr   = data['U']
            equ   = data['EQU']
            fequ  = data['FEQU']
            spec  = data['M']
            print("EC", end=" , ")
            print("{:.1f}".format(flows['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(flows['flakeOnly']*100)     , end=" , ")
            print(flows['AT']            , end=" , ")
            print("{:.1f}".format(ineq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(ineq['flakeOnly']*100)     , end=" , ")
            print(ineq['AT']            , end=" , ")
            print("{:.1f}".format(fin['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fin['flakeOnly']*100)     , end=" , ")
            print(fin['AT']            , end=" , ")
            print("{:.1f}".format(eq['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(eq['flakeOnly']*100)     , end=" , ")
            print(eq['AT']            , end=" , ")
            print("{:.1f}".format(irr['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(irr['flakeOnly']*100)     , end=" , ")
            print(irr['AT']            , end=" , ")
            print("{:.1f}".format(equ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(equ['flakeOnly']*100)     , end=" , ")
            print(equ['AT']            , end=" , ")
            print("{:.1f}".format(fequ['mutantPercent']*100) , end=" , ")
            print("{:.1f}".format(fequ['flakeOnly']*100)     , end=" , ")
            print(fequ['AT']            , end=" , ")
            print("-" , end=" , ")
            print("-" , end=" , ")
            print("")  



# Each Summary File is a column in the old Results.csv file
# Handle each subject indepenantly
def loadSummaryFile(sumPath):
    val = {}
    try:
        #print(sumPath)
        with open(sumPath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            # Create Dictionaries
            abstractTests = {}
            countCT        = 0
            countCTFail    = 0
            countCTFailDet = 0
            countRun       = 0
            countRunNP     = 0
            
            for row in spamreader:
                #print(', '.join(row)) # DEBUG
                if row[0]== 'Test':
                    # Skip 1st row : Header
                    #print("Skipped Header")
                    pass
                else:
                    # Grab 1st value (AT)
                    # Grab 2nd value (Input)
                    # Grab 3rd value (Runs)
                    # Grab last value (NP)
                    abstractTest  = row[0]
                    inputName     = row[1]
                    runNumber     = int(row[2])
                    notPassNumber = int(row[-1])
                    # Check if AT exists in dictionary
                    keys = abstractTests.keys()
                    exists = False
                    for x in keys:
                        if abstractTest in x:
                            exists = True
                            break                            
                    #
                    if exists:
                        # Number of Inputs for AT
                        tmpDict = abstractTests[abstractTest];
                        testCount = tmpDict["testCount"]
                        tmpDict["testCount"] = testCount + 1
                        # Runs
                        runCount   = tmpDict["runCount"]
                        tmpDict["runCount"] = runCount + runNumber
                        # Failures
                        npCount   = tmpDict["npCount"]
                        tmpDict["npCount"] = npCount + notPassNumber
                        # Count Concrete Tests
                        if notPassNumber > 0:
                            countCTFail = countCTFail + 1;
                            countRunNP  = countRunNP + notPassNumber;
                            # Falky Failure
                            fail = tmpDict["fail"]
                            tmpDict["fail"] = fail + 1
                            # Count Deterministic Failures
                            if runNumber == notPassNumber:
                                countCTFailDet = countCTFailDet + 1;
                                # Deterministic Failure
                                detFail = tmpDict["detFail"]
                                tmpDict["detFail"] = detFail + 1                          
                    else:
                        # First Row case to initialize dictionaries
                        # Number of Inputs for AT
                        tmpDict = {}
                        tmpDict["testCount"] = 1
                        # Runs
                        tmpDict["runCount"] = runNumber
                        
                        # Failures
                        tmpDict["npCount"] = notPassNumber
                        # Count Concrete Tests
                        if notPassNumber > 0:
                            countCTFail = countCTFail + 1;
                            # Falky Failure
                            tmpDict["fail"] = 1
                            # Count Deterministic Failures
                            if runNumber == notPassNumber:
                                countCTFailDet = countCTFailDet + 1;
                                countRunNP  = countRunNP + notPassNumber;
                                # Deterministic Failure
                                tmpDict["detFail"] = 1  
                            else:
                                # If first test was flakey
                                tmpDict["detFail"] = 0
                        else:
                            # If 1st test passes
                            tmpDict["fail"] = 0
                            tmpDict["detFail"] = 0
                    # Store Info from this row
                    abstractTests[abstractTest] = tmpDict
                    countCT = countCT + 1        
                    countRun = countRun + runNumber
            # Handle data for full summary file  
            # Count unique AT
            uniqueAT = len(abstractTests)
            # Global Counts are now done
            lis = sumPath.split("-")
            testSuite = lis[-3]
            modelName = lis[-2]
            # Need to store to persistant object: based on 
            # Dictionary : Subject Model Name : Dict (variables : values)
            values = {}
            # Total # of AT
            values["AT"]          = uniqueAT
            # Total # of CT
            values["CT"]          = countCT
            # Total # of Runs 
            values["Run"]         = countRun
            # Total # of Runs Failing
            values["RunFailed"]   = countRunNP
            # Total # of CT Failing (At least once) - Flakily
            values["CTFailed"]    = countCTFail
            # Total # of CT Failing - Deterministcially
            values["CTFailedDet"] = countCTFailDet
            name = testSuite + '-' + modelName
            val = [name, values]
    except:
        #print(sumPath + " Is missing summary file")
        # Error catching code for Table generation
        lis = sumPath.split("-")
        testSuite = lis[-3]
        modelName = lis[-2]
        name = testSuite + '-' + modelName
        values = {}
        values["AT"]          = 0
        values["CT"]          = 0
        values["Run"]         = 0
        values["RunFailed"]   = 0
        values["CTFailed"]    = 0
        values["CTFailedDet"] = 0
        val = [name, values]   
    
    return val

def processSubject(subject):
    #print(subject)
    # Load Summaries
    # Change Directory into subject
    os.chdir(subject)
    ##print("Current working directory: {0}".format(os.getcwd()))
    # Get all Simulation folder
    simFolders = getSubjects()
    dataList = {}
    for sim in simFolders:
        os.chdir(sim)
        # Parse folder name
        lis = sim.split("-")
        subject = lis[0]
        testSuite = lis[1]
        mutation = lis[2]
        # Load *-Summary.csv from each directory        
        head = os.getcwd() + "/" + subject + "-" + testSuite + "-" + mutation + "-"
        tail = "summary.csv"
        sumPath = head + tail
        # Load SummaryFile from Folder
        [name, summaryData] = loadSummaryFile(sumPath)
        if '00' in name:
            # Skip OO and 100 - golden models
            pass
        else:
            if summaryData['AT'] == 0:
                pass
                # Skip bad models
            else:
                # Add Data to List
                dataList[name] = summaryData
        # Return to Subject Directory
        os.chdir('..')
        
    ## Notes for Data inport ##
    # Counting NPs only  
    # Data to current naming conversions
    #   EQ = IN w/ RC
    #   U  = IR
    #   M  = S
    ## At this point have loaded and summed all required data
    
    # Process Test Suites
    
    # Base invariants
    dataF   = {}
    dataIN  = {}
    dataEQ  = {}
    dataU    = {}
    # Combos
    dataFIN  = {}
    dataEQU  = {}
    dataFEQU = {}
    # Base specifications
    dataM    = {}
    #for testSuite in ['F','IN','EQ','U','M']
    # F
    for k in dataList:
        if 'F' in k:
            # Grab all Data related to test suite
            lis = k.split("-")
            modelName = lis[-1]
            values = dataList[k]
            
            # F
            dataF[modelName]    = values
            # FIN
            dataFIN[modelName]  = values
            # FEQU
            dataFEQU[modelName] = values
       
    # IN
    for k in dataList:
        if 'IN' in k:
            # Grab all Data related to test suite
            lis = k.split("-")
            modelName = lis[-1]
            values = dataList[k]
               
            # IN
            dataIN[modelName]    = values
            # FIN
            try:
                tmpVal = dataFIN[modelName] 
                tmp2 = {}
                tmp2['AT'] = tmpVal['AT'] + values['AT']
                tmp2['CT'] = tmpVal['CT'] + values['CT']
                tmp2['CTFailed'] = tmpVal['CTFailed'] + values['CTFailed']
                tmp2['CTFailedDet'] = tmpVal['CTFailedDet'] + values['CTFailedDet']
                tmp2['Run'] = tmpVal['Run'] + values['Run']
                tmp2['RunFailed'] = tmpVal['RunFailed'] + values['RunFailed']
                dataFIN[modelName]  = tmp2
            except:
                dataFIN[modelName]  = values  
    # EQ
    for k in dataList:
        if 'EQ' in k:
            # Grab all Data related to test suite
            lis = k.split("-")
            modelName = lis[-1]
            values = dataList[k]
                
            # U
            dataEQ[modelName]    = values
            # EQU
            dataEQU[modelName]   = values
            # FEQU
            try:
                tmpVal = dataFEQU[modelName] 
                tmp2 = {}
                tmp2['AT']           = tmpVal['AT'] + values['AT']
                tmp2['CT']           = tmpVal['CT'] + values['CT']
                tmp2['CTFailed']     = tmpVal['CTFailed'] + values['CTFailed']
                tmp2['CTFailedDet']  = tmpVal['CTFailedDet'] + values['CTFailedDet']
                tmp2['Run']          = tmpVal['Run'] + values['Run']
                tmp2['RunFailed']    = tmpVal['RunFailed'] + values['RunFailed']
                dataFEQU[modelName]  = tmp2
            except:
                dataFEQU[modelName]  = values
    # U
    for k in dataList:
        if 'U' in k:
            # Grab all Data related to test suite
            lis = k.split("-")
            modelName = lis[-1]
            values = dataList[k]
                
            # U
            dataU[modelName]     = values
            # EQU
            try:                
                tmpVal = dataEQU[modelName] 
                tmp2 = {}
                tmp2['AT']           = tmpVal['AT'] + values['AT']
                tmp2['CT']           = tmpVal['CT'] + values['CT']
                tmp2['CTFailed']     = tmpVal['CTFailed'] + values['CTFailed']
                tmp2['CTFailedDet']  = tmpVal['CTFailedDet'] + values['CTFailedDet']
                tmp2['Run']          = tmpVal['Run'] + values['Run']
                tmp2['RunFailed']    = tmpVal['RunFailed'] + values['RunFailed']
                dataEQU[modelName]  = tmp2
            except:
                dataEQU[modelName] = values            
            
            # FEQU
            try: 
                tmpVal = dataFEQU[modelName] 
                tmp2 = {}
                tmp2['AT']           = tmpVal['AT'] + values['AT']
                tmp2['CT']           = tmpVal['CT'] + values['CT']
                tmp2['CTFailed']     = tmpVal['CTFailed'] + values['CTFailed']
                tmp2['CTFailedDet']  = tmpVal['CTFailedDet'] + values['CTFailedDet']
                tmp2['Run']          = tmpVal['Run'] + values['Run']
                tmp2['RunFailed']    = tmpVal['RunFailed'] + values['RunFailed']
                dataFEQU[modelName]  = tmp2    
            except:
                dataFEQU[modelName]  = values 
    # M
    for k in dataList:
        if 'M' in k:
            # Grab all Data related to test suite
            lis = k.split("-")
            modelName = lis[-1]
            values = dataList[k]
            # M       
            dataM[modelName]    = values
    ##############################
    ##############################
    ##############################
    ## F ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataF:
        values = dataF[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataF[k] = values
    try:
        dataF['AT']           = values['AT']
    except:
        dataF['AT'] = 0    
    dataF['sumCT']        = sumCT
    dataF['sumNP']        = sumNP
    dataF['sumNPdet']     = sumNPdet
    dataF['sumRunFailed'] = sumRunFailed
    dataF['sumRun']       = sumRun
    
    if dataF['sumCT']  > 0:
        dataF['PercentNP']    = dataF['sumNP']          / dataF['sumCT'] 
        dataF['PercentNPdet'] = dataF['sumNPdet']       / dataF['sumCT']
        dataF['PercentRun']   = dataF['sumRunFailed']   / dataF['sumRun'] 
        dataF['mutantPercent'] = mutantsFound / mutants
        dataF['flakeOnly']     = flakeOnly / mutants
    else:
        dataF['PercentNP']    = 0
        dataF['PercentNPdet'] = 0
        dataF['PercentRun']   = 0
    ## IN ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataIN:
        values = dataIN[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataIN[k] = values
    try:
        dataIN['AT']           = values['AT']
    except:
        dataIN['AT'] = 0   
    dataIN['sumCT']        = sumCT
    dataIN['sumNP']        = sumNP
    dataIN['sumNPdet']     = sumNPdet
    dataIN['sumRunFailed'] = sumRunFailed
    dataIN['sumRun']       = sumRun
    
    if dataIN['sumCT']  > 0:
        dataIN['PercentNP']    = dataIN['sumNP']          / dataIN['sumCT'] 
        dataIN['PercentNPdet'] = dataIN['sumNPdet']       / dataIN['sumCT']
        dataIN['PercentRun']   = dataIN['sumRunFailed']   / dataIN['sumRun'] 
        dataIN['mutantPercent'] = mutantsFound / mutants
        dataIN['flakeOnly']     = flakeOnly / mutants
    else:
        dataIN['PercentNP']    = 0
        dataIN['PercentNPdet'] = 0
        dataIN['PercentRun']   = 0
     ## EQ ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataEQ:
        values = dataEQ[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0 
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataEQ[k] = values 
    try:
        dataEQ['AT']           = values['AT']
    except:
        dataEQ['AT'] = 0   
    dataEQ['sumCT']        = sumCT
    dataEQ['sumNP']        = sumNP
    dataEQ['sumNPdet']     = sumNPdet
    dataEQ['sumRunFailed'] = sumRunFailed
    dataEQ['sumRun']       = sumRun
    
    if dataEQ['sumCT']  > 0:
        dataEQ['PercentNP']    = dataEQ['sumNP']          / dataEQ['sumCT'] 
        dataEQ['PercentNPdet'] = dataEQ['sumNPdet']       / dataEQ['sumCT']
        dataEQ['PercentRun']   = dataEQ['sumRunFailed']   / dataEQ['sumRun'] 
        dataEQ['mutantPercent'] = mutantsFound / mutants
        dataEQ['flakeOnly']     = flakeOnly / mutants
    else:
        dataEQ['PercentNP']    = 0
        dataEQ['PercentNPdet'] = 0
        dataEQ['PercentRun']   = 0
    ## U ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataU:
        values = dataU[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataU[k] = values
    try:
        dataU['AT']           = values['AT']
    except:
        dataU['AT'] = 0  
    dataU['sumCT']        = sumCT
    dataU['sumNP']        = sumNP
    dataU['sumNPdet']     = sumNPdet
    dataU['sumRunFailed'] = sumRunFailed
    dataU['sumRun']       = sumRun
    

    if dataU['sumCT']  > 0:
        dataU['PercentNP']    = dataU['sumNP']          / dataU['sumCT'] 
        dataU['PercentNPdet'] = dataU['sumNPdet']       / dataU['sumCT']
        dataU['PercentRun']   = dataU['sumRunFailed']   / dataU['sumRun'] 
        dataU['mutantPercent'] = mutantsFound / mutants
        dataU['flakeOnly']     = flakeOnly / mutants
    else:
        dataU['PercentNP']    = 0
        dataU['PercentNPdet'] = 0
        dataU['PercentRun']   = 0
    
    ## FIN ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataFIN:
        values = dataFIN[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataFIN[k] = values
    try:
        dataFIN['AT']           = values['AT']
    except:
        dataFIN['AT'] = 0 
    dataFIN['sumCT']        = sumCT
    dataFIN['sumNP']        = sumNP
    dataFIN['sumNPdet']     = sumNPdet
    dataFIN['sumRunFailed'] = sumRunFailed
    dataFIN['sumRun']       = sumRun
    
    if dataFIN['sumCT']  > 0:
        dataFIN['PercentNP']    = dataFIN['sumNP']          / dataFIN['sumCT'] 
        dataFIN['PercentNPdet'] = dataFIN['sumNPdet']       / dataFIN['sumCT']
        dataFIN['PercentRun']   = dataFIN['sumRunFailed']   / dataFIN['sumRun']
        dataFIN['mutantPercent'] = mutantsFound / mutants
        dataFIN['flakeOnly']     = flakeOnly / mutants
    else:
        dataFIN['PercentNP']    = 0
        dataFIN['PercentNPdet'] = 0
        dataFIN['PercentRun']   = 0
    ## EQU ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataEQU:
        values = dataEQU[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataEQU[k] = values
    try:
        dataEQU['AT']           = values['AT']
    except:
        dataEQU['AT'] = 0  
    dataEQU['sumCT']        = sumCT
    dataEQU['sumNP']        = sumNP
    dataEQU['sumNPdet']     = sumNPdet
    dataEQU['sumRunFailed'] = sumRunFailed
    dataEQU['sumRun']       = sumRun
    
    if dataEQU['sumCT']  > 0:
        dataEQU['PercentNP']    = dataEQU['sumNP']          / dataEQU['sumCT'] 
        dataEQU['PercentNPdet'] = dataEQU['sumNPdet']       / dataEQU['sumCT']
        dataEQU['PercentRun']   = dataEQU['sumRunFailed']   / dataEQU['sumRun']
        dataEQU['mutantPercent'] = mutantsFound / mutants
        dataEQU['flakeOnly']     = flakeOnly / mutants
    else:
        dataEQU['PercentNP']    = 0
        dataEQU['PercentNPdet'] = 0
        dataEQU['PercentRun']   = 0
    ## FEQU ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataFEQU:
        values = dataFEQU[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
        dataFEQU[k] = values
    try:
        dataFEQU['AT']           = values['AT']
    except:
        dataFEQU['AT'] = 0  
    dataFEQU['sumCT']        = sumCT
    dataFEQU['sumNP']        = sumNP
    dataFEQU['sumNPdet']     = sumNPdet
    dataFEQU['sumRunFailed'] = sumRunFailed
    dataFEQU['sumRun']       = sumRun
    
    if dataFEQU['sumCT']  > 0:
        dataFEQU['PercentNP']    = dataFEQU['sumNP']          / dataFEQU['sumCT'] 
        dataFEQU['PercentNPdet'] = dataFEQU['sumNPdet']       / dataFEQU['sumCT']
        dataFEQU['PercentRun']   = dataFEQU['sumRunFailed']   / dataFEQU['sumRun'] 
        dataFEQU['mutantPercent'] = mutantsFound / mutants
        dataFEQU['flakeOnly']     = flakeOnly / mutants
    else:
        dataFEQU['PercentNP']    = 0
        dataFEQU['PercentNPdet'] = 0
        dataFEQU['PercentRun']   = 0
    ## M ##
    sumCT          = 0
    sumNP          = 0
    sumNPdet       = 0
    sumRunFailed   = 0
    sumRun         = 0
    mutants        = 0
    mutantsFound   = 0
    flakeOnly      = 0
    # Generate Percentages, for each mutant
    for k in dataM:
        values = dataM[k]
        sumCT        = sumCT          + values['CT']
        sumNP        = sumNP          + values['CTFailed']
        sumNPdet     = sumNPdet       + values['CTFailedDet']
        sumRunFailed = sumRunFailed   + values['RunFailed'] 
        sumRun       = sumRun         + values['Run']
        # Do math
        if values['CT']  > 0:
            values['PercentNP']    = values['CTFailed']    / values['CT'] 
            values['PercentNPdet'] = values['CTFailedDet'] / values['CT']
            values['PercentRun']   = values['RunFailed']   / values['Run'] 
        else:
            values['PercentNP']    = 0
            values['PercentNPdet'] = 0
            values['PercentRun']   = 0
        # Count Mutants Detected
        mutants = mutants + 1    
        if values['CTFailed'] > 0:
            mutantsFound = mutantsFound + 1
        if values['CTFailedDet'] == 0 and values['CTFailed'] > 0:
            flakeOnly      = flakeOnly + 1
            
     
        dataM[k] = values
    try:
        dataM['AT']           = values['AT']
    except:
        dataM['AT'] = 0   
    dataM['sumCT']        = sumCT
    dataM['sumNP']        = sumNP
    dataM['sumNPdet']     = sumNPdet
    dataM['sumRunFailed'] = sumRunFailed
    dataM['sumRun']       = sumRun
    if dataM['sumCT']  > 0:
        dataM['PercentNP']    = dataM['sumNP']          / dataM['sumCT'] 
        dataM['PercentNPdet'] = dataM['sumNPdet']       / dataM['sumCT']
        dataM['PercentRun']   = dataM['sumRunFailed']   / dataM['sumRun']
        dataM['mutantPercent'] = mutantsFound / mutants
        dataM['flakeOnly']     = flakeOnly / mutants
    else:
        dataM['PercentNP']    = 0
        dataM['PercentNPdet'] = 0
        dataM['PercentRun']   = 0
    # Return to Top level
    os.chdir('..')
    ## 
    data = {}
    data['F']    = dataF
    data['IN']   = dataIN
    data['FIN']  = dataFIN
    data['EQ']   = dataEQ
    data['EQU']  = dataEQU
    data['FEQU'] = dataFEQU
    data['U']    = dataU
    data['M']    = dataM
    
    
    # Percent of Mutants Found
    
    
    return data

def getSubjects():
    cats = []
    # For each Dir in SimulationData    
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        # Grab only Top-Level Directories
        if dirpath == os.getcwd():
            cats = dirnames
            break
    # subcats = list(set(subcats)) # uncomment this if you want 'subcats' to be unique
    return (cats)

# This file will take a directory
# Return 2 files summerizing full test suite results


# Parse SimuationData Directory






# Output - RQ2 - Table 4
#     | Without RC                                                                     | With Reaction Counting                                                         |                |
#     | Flows                    | Ineq                     | Flows+Ineq               | Ineq                     | Irred                    | Ineq + Irred             | Specification  |
# CRN | % Det | % Flky | No. Inv | % Det | % Flky | No. Inv | % Det | % Flky | No. Inv | % Det | % Flky | No. Inv | % Det | % Flky | No. Inv | % Det | % Flky | No. Inv | % Det | % Flky | 
# Min |
# S   |
# AM  |
# Mod |
# Max |
# AL1 |
# H1  |
# H2  |
# MWT |
# ___
# PP  |
# ECG |
# H4  |
# EC  |


# Output - RQ2 - Table 6 - IF have time
# Test ID | Inv Type | % Faults Detected | % SpCv | % ReCv
# 1       |
# 2       |
# 3       |
# 4       |
# 5       |
# 6       |
# 7       |
# 8       |
# 9       |
# 10      |
# 11      |


## EXECUTION CODE ##
def main():
    #print("Current working directory: {0}".format(os.getcwd()))
    os.chdir('../SimulationData')
    #print("Current working directory: {0}".format(os.getcwd()))
    listOfSubjects = getSubjects()
    completeData = {}
    # For each subject
    for subject in listOfSubjects:
        # Load Data
        data = processSubject(subject)
        # Save to object
        completeData[subject] = data
    # Build Tables with full data set
    generateTable3(completeData)

if __name__ == "__main__":
    main()