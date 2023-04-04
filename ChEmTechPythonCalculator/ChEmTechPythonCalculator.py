"""
Hello, this is a comment from Jansel regarding the progress of this program
These are the following topics tackled by the program successfully:

THERMOCHEMISTRY 
✅🌡 Standard Enthalpy Change 
✅🌡 Standard Entropy Change

CHEMICAL KINETICS 
🧬 FIRST ORDER REACTIONS 
✅- When determining the time: ln [A]t [A]0=-kt
✅- When determining the final concentration: ln  [A]t =-kt +ln [A]0
✅- When determining the half-life: m= Δm [A]0

Chemical Equilibrium 
✅🧪 Kc = [products] / [reactants] 
✅🧪 Qc = [products] / [reactants] 
✅🧪 Kp = [P products] / [P reactants]
✅ 🧪 Kc from Kp 

ACIDS & BASES 
✅⚗️ pH  = 14 - pOH 
✅⚗️ pOH = 14 - pH 
✅⚗️ pH  =-log[H+]
✅⚗️ [H+] = 10^-pH
✅⚗️ pH  =-log[OH-]
✅⚗️ [H+] = 10^-pOH
✅⚗️ pH + pOH = 14 [should auto calculate from the pH and pOH]

If you discover any errors in the program, create an issue on our github page at: https://github.com/Jansel80/ChEmTechPythonCalculator
"""
#initial setup
from email.policy import default
import time
import math
import sys
import os
import webbrowser
from turtle import goto

#Initial Comment
'''
    The program contains general try and except that assumes that you have inputted something other than an integer. 
    Assuming you have, it will warn the user about this and restart the whole program meaning it returns to the main menu.
'''


#for fancy bar. It is there for readability to separate the title from the choices.
def loading_screen():
    bar = "████████████████████████████████████████████████████████████████"
    for c in bar:
        time.sleep(0.0001)
        sys.stdout.write(c)
        sys.stdout.flush()
    print("")


def gatherCoefficientsABCD():
    try:
        # define the coefficients of the balanced chemical equation
        global a_coeff, b_coeff, c_coeff, d_coeff
        a_coeff = float(input("Enter the coefficient of the reactant A: "))
        b_coeff = float(input("Enter the coefficient of the reactant B: "))
        c_coeff = float(input("Enter the coefficient of the product C: "))
        d_coeff = float(input("Enter the coefficient of the product D: "))
    except:
     os.system('cls||clear')
     print("There was an error in gathering a coefficient. Please input a numeric value only.")
     time.sleep(1.5)
     pass

 #typeofvar refers to the label it receives which is specific to the calculating function that will call this function.
def gatherConcentrationsABCD(typeofvar):
    try:
        #Gathers the concentration values for a 2 reactants and products.
        global a_concentration, b_concentration, c_concentration, d_concentration
        a_concentration = float(input("Enter the "+ typeofvar +" of reactant A: "))
        b_concentration = float(input("Enter the "+ typeofvar +" of reactant B: "))
        c_concentration = float(input("Enter the "+ typeofvar + " of product C: "))
        d_concentration = float(input("Enter the "+ typeofvar + " of product D: "))
    except:
     os.system('cls||clear')
     print("There was an error in gathering a concentration. Please input a numeric value only.")
     time.sleep(1.5)
     pass


#SOLVE KC FROM KP
def solveKcKp1():
  #Restarts the equation when the user inputs Y or N in the end.
  os.system('cls||clear')
  chemEqRestarter="yes"
  while chemEqRestarter=="ya" or chemEqRestarter=="Y" or chemEqRestarter=="yes" or chemEqRestarter=="y" or chemEqRestarter=="Yes": 
        try:
            # Define the function to calculate Kc from Kp
            def solveKcFromKp(Kp, temp, coeffs_reactants, coeffs_products):
            # Calculate the gas constant (R) in Joules per mole per Kelvin
                R = 8.314
    
            # Calculate the Kc value from Kp using the ideal gas law
                Kc = Kp / ((R * temp) ** (sum(coeffs_products) - sum(coeffs_reactants)))
    
                return Kc

        # Get input values from user for Kp and temperature as well as the coefficients of reactants and products.
            Kp = float(input("Enter the value of Kp: "))
            temp = float(input("Enter the value of temperature (in Kelvin): "))
            coeffs_reactants = list(map(int, input("Enter the stoichiometric coefficients of the reactants (separated by commas): ").split(',')))
            coeffs_products = list(map(int, input("Enter the stoichiometric coefficients of the products (separated by commas): ").split(',')))

        # Calculate Kc using the function and print the result
            Kc = solveKcFromKp(Kp, temp, coeffs_reactants, coeffs_products)
            print("The value of Kc is:", Kc)
            time.sleep(1)
        except:
             os.system('cls||clear')
             print("There was an error in gathering a value.\n Please input a numeric value only.")
             time.sleep(1.5)
             pass
        chemEqRestarter=input("\nWould you like to restart the calculator? Y or N?\n") 



#finding kc
def solveKc():
  #Restarts kP Code when Y. Works the same as the above 
  os.system('cls||clear')
  chemEqRestarter="yes"
  while chemEqRestarter=="ya" or chemEqRestarter=="Y" or chemEqRestarter=="yes" or chemEqRestarter=="y" or chemEqRestarter=="Yes":  
      try:
        # define the coefficients of the balanced chemical equation
        gatherCoefficientsABCD()

        # define the concentrations of the reactants and products
        gatherConcentrationsABCD(typeofvar="concentrations")
 
        # calculate the reaction quotient Qc
        Kc = (c_concentration ** c_coeff) * (d_concentration ** d_coeff) / ((a_concentration ** a_coeff) * (b_concentration ** b_coeff))

        # print the equilibrium constant Kc
        print("The equilibrium constant Kc is:", Kc)
        time.sleep(1)
      except:
         break
      chemEqRestarter=input("\nWould you like to restart the calculator? Y or N?\n")   

#finding kP
def solveKp():
  #Restarts kP Code when Y. Works the same as the above 
  os.system('cls||clear')
  chemEqRestarter="yes"
  while chemEqRestarter=="ya" or chemEqRestarter=="Y" or chemEqRestarter=="yes" or chemEqRestarter=="y" or chemEqRestarter=="Yes":    
     # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()
    try:
        # Get the partial pressures of the reactants and products
        Pa = float(input("Enter the partial pressure of A: "))
        Pb = float(input("Enter the partial pressure of B: "))
        Pc = float(input("Enter the partial pressure of C: "))
        Pd = float(input("Enter the partial pressure of D: "))

        # Calculate Kp using the formula
        Kp = (Pc ** c_coeff * Pd ** d_coeff) / (Pa ** a_coeff * Pb ** b_coeff)

        # Print the result
        print("The equilibrium constant Kp is:", Kp)
        time.sleep(1)
    except:
         os.system('cls||clear')
         print("There was an error in gathering partial pressure resulting in an error of calculation.")
         time.sleep(1.5)
         pass
    chemEqRestarter=input("\nWould you like to restart the calculator? Y or N?")

#finding Qc
def solveQc():
    #Restarts QC Code when Y. Works the same as the above 
    os.system('cls||clear')
    chemEqRestarter="yes"
    while chemEqRestarter=="ya" or chemEqRestarter=="Y" or chemEqRestarter=="yes" or chemEqRestarter=="y" or chemEqRestarter=="Yes":    
        try:
            # define the coefficients of the balanced chemical equation
            gatherCoefficientsABCD()

            # define the concentrations of the reactants and products at equilibrium
            gatherConcentrationsABCD(typeofvar="concentrations")

            # calculate the reaction quotient Qc
            Qc = (c_concentration ** c_coeff) * (d_concentration ** d_coeff) / ((a_concentration ** a_coeff) * (b_concentration ** b_coeff))

            # print the value of Qc
            print("The value of Qc is:", Qc)
            time.sleep(1)
        except:
         os.system('cls||clear')
         print("There was an error. Please type a numeric value")
         time.sleep(2)
        chemEqRestarter=input("\nWould you like to restart the calculator? Y or N?\n")


#finding standard enthalpy change
def solveStandardEnthalpyChange():
#Restarts Enthalpy Code when Y. Works the same as the above 

        chemEnthalpyRestarter="yes"
        while chemEnthalpyRestarter=="ya" or chemEnthalpyRestarter=="Y" or chemEnthalpyRestarter=="yes" or chemEnthalpyRestarter=="y" or chemEnthalpyRestarter=="Yes":    
            os.system('cls||clear')
            # define the coefficients of the balanced chemical equation
            gatherCoefficientsABCD()
            try:
            # define the standard enthalpies of formation for the reactants and products
                hf_a = float(input("Enter the standard enthalpy of formation of reactant A (kJ/mol): "))
                hf_b = float(input("Enter the standard enthalpy of formation of reactant B (kJ/mol): "))
                hf_c = float(input("Enter the standard enthalpy of formation of product C (kJ/mol): "))
                hf_d = float(input("Enter the standard enthalpy of formation of product D (kJ/mol): "))
            

                # calculate the standard enthalpy change ΔH°
                delta_h = (c_coeff * hf_c + d_coeff * hf_d) - (a_coeff * hf_a + b_coeff * hf_b)
            except: 
                os.system('cls||clear')
                print("There was an error. Please type a numeric value")
                time.sleep(2)
                break
            # print the value of ΔH°
            print("The standard enthalpy change ΔH° is:", delta_h, "kJ/mol")
            time.sleep(1)
            chemEnthalpyRestarter=input("\nWould you like to restart the calculator? Y or N?\n")

#finding standard entropy change
def solveStandardEntropyChange():
    #Restarts Entropy Code when Y. Works the same as the above 
    chemEntropyRestarter="yes"
    while chemEntropyRestarter=="ya" or chemEntropyRestarter=="Y" or chemEntropyRestarter=="yes" or chemEntropyRestarter=="y" or chemEntropyRestarter=="Yes":    
        # define the coefficients of the balanced chemical equation
        gatherCoefficientsABCD()

        # define the standard entropies of formation for the reactants and products
        try:
            s_a = float(input("Enter the standard entropy of reactant A (J/(mol*K)): "))
            s_b = float(input("Enter the standard entropy of reactant B (J/(mol*K)): "))
            s_c = float(input("Enter the standard entropy of product C (J/(mol*K)): "))
            s_d = float(input("Enter the standard entropy of product D (J/(mol*K)): "))

            # calculate the standard entropy change ΔS°
            delta_s = (c_coeff * s_c + d_coeff * s_d) - (a_coeff * s_a + b_coeff * s_b)
        except: 
                os.system('cls||clear')
                print("There was an error. Please type a numeric value")
                time.sleep(2)
                break
        # print the value of ΔS°
        print("The standard entropy change ΔS° is:", delta_s, "J/(mol*K)")
        time.sleep(1)
        chemEntropyRestarter=input("\nWould you like to restart the calculator? Y or N?\n")


#Acids and Bases Section
def acids_bases():
    #Restart condition for acids and bases
    restartABCondition = 1

    #This section will only loop while restartABCondition equals 1.
    while restartABCondition == 1:
        os.system('cls||clear')
        print("")
        loading_screen()
        print("\nWhat are you looking for?:\n")
        print("a.)Finding pH from pOH\nb.) Finding pOH from pH\nC.) Finding pH from H+\nD.) Finding H+ from pH\nE.) Finding Finding pOH from OH-\nF.) Finding OH- from pOH")
        acids_bases_selection = input()
        try:
            #match case wherein the user inputs a letter and whatever calculator corresponds to that letter will be utilized.
            match acids_bases_selection:
                case "a":
                    print("")
                    print("Find pH from pOH")
                    print("")
                    pOHInput = float(input("Enter the value of pOH\n"))
                    pOHInputRound = round(pOHInput)
                    pH = 14-pOHInputRound
                    print("\n Your PH is " , pH, "\n")
                    print("The total value of pH + pOH then should be 14 =", int(pH+pOHInput))
            
                case "b":
                    print("")
                    print("Find pOH from pH")
                    print("")
                    pHInput = float(input("Enter the value of pOH\n"))
                    pHInputRound = round(pHInput)
                    pOH = 14-pHInputRound
                    print("\n Your PH is " , pH, "\n")
                    print("The total value of pH + pOH then should be 14 =", int(pOH+pHInput))

                case "c":
                    print("")
                    print("Finding pH from H+")
                    print("")
                    HInput = float(input("Enter the numerical value of H+\n"))
                    pH = -math.log10(HInput)
                    print("\n Your pH is " , round(pH), "\n")

                case "d":
                    print("")
                    print("Finding H+ from pH")
                    print("")
                    pHInput = float(input("Enter the numerical value of pH\n"))
                    H = 10**-(pHInput)
                    print("\n Your H+ is " , '{:.5e}'.format(H), "M \n")

                case "e":
                    print("")
                    print("Find pOH from OH-")
                    print("")
                    OHInput = float(input("Enter the numerical value of OH-\n"))
                    pOH = -math.log10(OHInput)
                    print("\n Your pOH is " , round(pOH), "\n")

                case "f":
                    print("")
                    print("Finding OH- from pOH")
                    print("")
                    pOHInput = float(input("Enter the numerical value of pOH\n"))
                    OH = 10**-(pOHInput)
                    print("\n Your OH- is " , '{:.5e}'.format(OH), "M \n")

        except:
            os.system('cls||clear')
            print("An error has occured with the Acids and Bases Section.\n You may have inputted something other than a number. \n Restart prompt incoming.")
            time.sleep(1)
            os.system('cls||clear')
            pass

        #Restart Condition with a short wait time before.

        time.sleep(0.5)
        print("")
        print("Press Y to Restart, N if you want to end\n\n")
        restartABConditionInput = input()
        #If the user types Y, it will restart. Otherwise, any other input will return to the main menu
        if restartABConditionInput == "Y" or restartABConditionInput == "y":
                    
            restartABConditionDecision = 1
        else:
            restartABConditionDecision = 0
        restartABCondition = restartABConditionDecision

    else:
        #If it restarts, it prints BYEBYE and clears the terminal.
        print("BYEBYE")
        os.system('cls||clear')


#Solves for Time in Chemical Kinetics
def chemicalKineticsTime():
            #asks for init. conc and final conc.
        try:
            IC=float(input("Please input Initial Concentration:\n"))
            FC=float(input("\nPlease input Final Concentration:\n"))
            k=float(input("Input the rate constant replacing x10^ with e. (i.e 4.10e-2 for 4.10x10^-2)\n"))
            #asks for the unit of both rate constant and the required answer
            unitTimeK=input("Is the rate constant in Minutes(m) or Seconds(s)\n")
            unitTimeRequired=input("Is Required Time in Minutes (m) or Seconds (s)?\n")

            #solves for time
            cKTime = math.log(FC/IC)/(-k)

            #If the unit of both rate constant and required is the same, it will simply just continue
            if unitTimeRequired.casefold()==unitTimeK.casefold():
                print(cKTime,"",unitTimeRequired)
                time.sleep(2)

            #If the unit of rate constant is in minutes and the required is in seconds, it will multiply by 60 to turn it into seconds.
            elif unitTimeRequired.casefold()=="s" and unitTimeK.casefold()=="m":
                finaltime = cKTime*60
                print(finaltime,"",unitTimeRequired)
                time.sleep(2)

            #If the unit of rate constant is in seconds and the required is in minutes, it will multiply by 60 to turn it into minutes.

            elif unitTimeRequired=="m" and unitTimeK =="s":
                finaltime = cKTime/60
                print(finaltime,"",unitTimeRequired)
                time.sleep(2)
        except:
          os.system('cls||clear')
          print("Please type a numeric value")
          time.sleep(1.5)
          pass

#To find final concentration.
def chemicalKineticsFC():
        try:
            #asks for init. conc, time elapsed, k, as well as the units for time and rate.
            IC=float(input("Please input Initial Concentration:\n"))
            cKTime=float(input("\nPlease input Time:\n"))
            unitTimeGiven=input("Is Given Time in Minutes (m) or Seconds (s)?\n")
            k=float(input("Input the rate constant replacing x10^ with e. (i.e 4.10e-2 for 4.10x10^-2)\n"))
            unitTimeK=input("Is Rate Constant in Minutes (m) or Seconds (s)?\n")
        

            #lnA = -k*cKTime + math.log(IC)
            #FC= math.e**lnA

            #all the same, proceed as normal.
            if unitTimeGiven.casefold()==unitTimeK.casefold():
                    lnA = -k*cKTime + math.log(IC)
                    FC= math.e**lnA
                    print("\nThe Final Concentration is ", FC, " M after ", cKTime, unitTimeGiven, " of reaction." )
                    time.sleep(2)


                #if k is in minutes we need to find the rate per second which means we divide by 60. (There is less rate per second)
            elif unitTimeGiven.casefold()=="s" and unitTimeK.casefold()=="m":
                    Nk = k/60
                    lnA = -k*cKTime + math.log(IC)
                    FC= math.e**lnA
                    print("\nThe Final Concentration is ", FC, " M after ", cKTime, unitTimeGiven, " of reaction." )
                    time.sleep(2)


                #rate constant is in second while given time is in minute, we can convert either of these.
                #I just chose to convert rate to keep it interesting. It still provides us the same result.
            elif unitTimeGiven.casefold()=="m" and unitTimeK.casefold()=="s":
                    Nk = k*60
                    lnA = -Nk*cKTime + math.log(IC)
                    FC= math.e**lnA
                    print("\nThe Final Concentration is ", FC, " M after ", cKTime, unitTimeGiven, " of reaction." )
                    time.sleep(2)
        except:
          os.system('cls||clear')
          print("Please type a numeric value")
          time.sleep(1.5)
          pass



#Finds Half Life. Since Half Life only relies on constant, we can find Half Life using only the k value.
def chemicalKineticsHL():
        try:
            k=float(input("Input the rate constant replacing x10^ with e. (i.e 4.10e-2 for 4.10x10^-2)\n"))
            HL=math.log(2)/k
            print("The Half Life is ", HL)
        except:
          os.system('cls||clear')
          print("Please type a numeric value")
          time.sleep(1.5)
          pass


#Chemical Kinetics section. The restart condition works similarly to the acids_bases subsection. 
def chemicalKinetics():
        os.system('cls||clear')
        print("Chemical Kinetics Section Active\n\nAt this time, only first order reactions can be solved for concentrations, time, and HL.\n")
        loading_screen()
        time.sleep(0.75)
        chemicalKineticsProceed = 1
        while chemicalKineticsProceed == 1  and not chemicalKineticsProceed==-1:
            #The user is asked whether any of the values are given. The calculator will automatically choose which 
            #formula to use depending on what is given and what isn't. 
            os.system('cls||clear')
            isICGiven = input("Is Initial Concentration Given? Y or N?\n")
            isFCGiven = input("Is Final Concentration Given? Y or N?\n")
            isTGiven = input("Is Time Given? Y or N?\n")
            iskGiven = input("Is rate constant given? Y or N?\n")

            if isICGiven=="Y" or isICGiven=="y" or isICGiven=="yes" or isICGiven=="Yes" or isICGiven=="YES":
                ICGValue=1
            else:
                ICGValue=0

            if isFCGiven=="Y" or isFCGiven=="y" or isFCGiven=="yes" or isFCGiven=="Yes" or isFCGiven=="YES":
                FCGValue=1
            else:
                FCGValue=0
            if isTGiven=="Y" or isTGiven=="y" or isTGiven=="yes" or isTGiven=="Yes" or isTGiven=="YES":
                TGValue=1
            else:
                TGValue=0

            if iskGiven=="Y" or iskGiven=="y" or iskGiven=="yes" or iskGiven=="Yes" or iskGiven=="YES":
                kconstGValue=1
            else:
                kconstGValue=0

            #Proceeds with finding time
            if ICGValue==1 and FCGValue==1 and kconstGValue==1 and TGValue==0:
                os.system('cls||clear')
                print("\nWe will solve Time using initial concentration, final concentration, and rate constant\n\n")
                chemicalKineticsProceed==0
                chemicalKineticsTime()
                pass

            #Proceeds with Finding Concentration
            if ICGValue==1 and FCGValue==0 and kconstGValue==1 and TGValue==1:
                os.system('cls||clear')
                print("\nWe will solve Final Concentration using initial concentration, time, and rate constant\n\n")
                chemicalKineticsProceed==0
                chemicalKineticsFC()
                pass
        
            #Proceeds with Half Live
            if ICGValue==0 and FCGValue==0 and kconstGValue==1 and TGValue==0:
                os.system('cls||clear')
                proceedHalfLife=input("Are you finding half life? Y or N \n")
                if proceedHalfLife=="y" or proceedHalfLife=="Y" or proceedHalfLife=="Yes" or proceedHalfLife=="YES":
                    print("\nWe will now proceed with finding half life!\n Half life relies on rate alone which means all we need is rate constant! \n")
                    os.system('cls||clear')
                    chemicalKineticsHL()
                else:
                    os.system('cls||clear')                   
                    break



            print("")
            print("Press Y to Restart, N if you want to end\n\n")
            restartCKConditionInput = input()
            if restartCKConditionInput == "Y" or restartCKConditionInput == "y":
                    restartCKConditionDecision = 1
            else:
                    restartCKConditionDecision = 0

            chemicalKineticsProceed = restartCKConditionDecision

#Credits Section For Group 1
def CreditsToGrp1():
    creditsRestart="Y"
    while creditsRestart=="Y":
        os.system('cls||clear')
        print("This Project was done by Group 1 of 12D Batch 2023\n\nArriola, Bea\nCinco, Erika\nCipriano, JT\nDoctor, Phoebe\nLegaspi, Gavin\nPetalio, Spencer\nSantamaria, Alia\nTolentino, Jansel\n")
        print("Thank You Sir Neil for overseeing our EmpTech Subject!\nThank You Sir Maui for overseeing our Chemistry SUbject!")
        print("\nThe Group would like to express gratitude to those who supported us.\nTo our teachers and classmates. THANK YOU!!!\nBatch 2023 Signing Off")
        creditsRestart2=input("\n\nIf You Would Like To Visit The Github Page, type g or github.\n\nOtherwise, Go Back to Main Menu? Y or N?\n")
        
        if creditsRestart2.casefold()=="y":
            break
        elif creditsRestart2.casefold()=="n":
            creditsRestart=="Y"
        #Opens the webpage when g is typed.
        elif creditsRestart2.casefold()=="github" or creditsRestart2.casefold()=="g":
            os.system('cls||clear')
            webbrowser.open("https://github.com/Jansel80/ChEmTechPythonCalculator")
            print("WebPage Opened on your Default Browser!")
            time.sleep(3)
            creditsRestart=="Y"

        elif creditsRestart2.casefold() =="turtle80":     
            creditsRestart=="Turtle80"
            os.system('cls||clear')
            print ("You found this easter egg!\nBy: \n JONSOL80\n TURTLE80:DDD\n\nThank you for everything, DLSZ Vermosa!\n\n")
            time.sleep(3)
            print(f"Signed By {creditsRestart}")
            time.sleep(8)

#MAIN CODE
#MAIN CODE
#MAIN CODE

#While x is true, the main menu loops when it is returned to.
x = "true"
while (x=="true"):
    os.system('cls||clear')

    print("Good Day, This is 12D Group 1's Chemistry 2 Calculator!\n\n")
    print("This will cover a section of all topics of Chemistry 2. \n\n")
    time.sleep(0.05)
    print("")

    loading_screen()

    print("")

    print("Please Select a Subtopic:")
    print("")
    print("(a.) Solve Standard Enthalpy Change")
    print("(b.) Solve Standard Entropy Change")
    print("(c.) Solve Kc with 2 reactans and 2 products")
    print("(d.) Solve Qc with 2 reactans and 2 products")
    print("(e.) Solve for Kc from Kp")
    print("(f.) Solve Kp with 2 reactans and 2 products")
    print("//The topics below have their own subsections!//")
    print("(g.) Acids & Bases")
    print("(h.) Chemical Kinetics")
    print("\n//Miscellaneous//")
    print("(j.) Credits and Message")
    print("(u.) Check the Github Page for Updates")
    print("\n(CLOSE) Type anything else to close the calculator\n")

    #Input selection for which calculator the user will choose
    #match case wherein the user inputs a letter and whatever calculator corresponds to that letter will be utilized.
    selection = input()
    match selection:
    #The following calculators that talk about enthalpy, entropy, and Chemical Equilibrium
        case "a":
            print("\nStandardEnthalpyChange\n")
            solveStandardEnthalpyChange()
        case "b":
            print("\nStandardEntropyChange\n")
            solveStandardEntropyChange()
        case "c":
            print("\nSolving for Kc\n")
            solveKc()
        case "d":
            print("\nSolving for Qc\n")
            solveQc()
        case "e":
            print("\nSolving for Kc from Kp\n")
            solveKcKp1()
        case "f":
            print("\nSolving for Kp\n")
            solveKp()
    #Acids and bases have their own option!
        case "g":
            print("\nAcids & Bases\n")
            acids_bases()
        case "h":
            print("\nFirst Order Chemical Kinetics\n")
            chemicalKinetics()
    #Easter Egg that shows credits. 
        case "j":
            print("\nYou have accessed The Credits Section\n")
            CreditsToGrp1()
    #Close Condition. If the user inputs anything other than a-j, it defaults to this case
    #which sets x="untrue" ending the loop.
        case "u":
            print("\nYou have accessed The Updates Section\n")
            webbrowser.open("https://github.com/Jansel80/ChEmTechPythonCalculator/releases")
            time.sleep(3)
        case _:
            os.system('cls||clear')
            print("The calculator will now close.\n")
            time.sleep(1)
            x="untrue"
            

else:
    #The calculator closes since the loop is broken.
    print("\n\nGoodbye! Thank you for using ChEmTechPythoncalculator!")
    time.sleep(1)