"""
Hello, this is a comment from Jansel regarding the progress of this program
THERMOCHEMISTRY 
✅🌡 Standard Enthalpy Change 
△Hºrxn = ∑(n△Hºf products) - ∑(n△Hºf reactants)

✅🌡 Standard Entropy Change
△Sºrxn = ∑(n△Sºf products) - ∑(n△Sºf reactants)


CHEMICAL KINETICS 
🧬 FIRST ORDER REACTIONS 
- When determining the time: ln [A]t [A]0=-kt
- When determining the final concentration: ln  [A]t =-kt +ln [A]0
- When determining the half-life: m= Δm [A]0


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
"""
#initial setup
import time
import math
import sys
import os


#for loading screen
def loading_screen():
    bar = "████████████████████████████████████████████████████████████████"
    for c in bar:
        time.sleep(0.001)
        sys.stdout.write(c)
        sys.stdout.flush()
    print("")

def gatherCoefficientsABCD():
    # define the coefficients of the balanced chemical equation
    global a_coeff, b_coeff, c_coeff, d_coeff
    a_coeff = float(input("Enter the coefficient of the reactant A: "))
    b_coeff = float(input("Enter the coefficient of the reactant B: "))
    c_coeff = float(input("Enter the coefficient of the product C: "))
    d_coeff = float(input("Enter the coefficient of the product D: "))

def gatherConcentrationsABCD(typeofvar):
    global a_concentration, b_concentration, c_concentration, d_concentration
    a_concentration = float(input("Enter the "+ typeofvar +" of reactant A: "))
    b_concentration = float(input("Enter the "+ typeofvar +" of reactant B: "))
    c_concentration = float(input("Enter the "+ typeofvar + " of product C: "))
    d_concentration = float(input("Enter the "+ typeofvar + " of product D: "))
    

#SOLVE KC FROM KP
def solveKcKp1():

    # Define the function to calculate Kc from Kp
    def solveKcFromKp(Kp, temp, coeffs_reactants, coeffs_products):
    # Calculate the gas constant (R) in Joules per mole per Kelvin
        R = 8.314
    
    # Calculate the Kc value from Kp using the ideal gas law
        Kc = Kp / ((R * temp) ** (sum(coeffs_products) - sum(coeffs_reactants)))
    
        return Kc

# Get input values from user
    Kp = float(input("Enter the value of Kp: "))
    temp = float(input("Enter the value of temperature (in Kelvin): "))
    coeffs_reactants = list(map(int, input("Enter the stoichiometric coefficients of the reactants (separated by commas): ").split(',')))
    coeffs_products = list(map(int, input("Enter the stoichiometric coefficients of the products (separated by commas): ").split(',')))

# Calculate Kc using the function and print the result
    Kc = solveKcFromKp(Kp, temp, coeffs_reactants, coeffs_products)
    print("The value of Kc is:", Kc)

#finding kc
def solveKc():
    # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()

    # define the concentrations of the reactants and products
    gatherConcentrationsABCD(typeofvar="concentrations")

    # calculate the reaction quotient Qc
    Kc = (c_concentration ** c_coeff) * (d_concentration ** d_coeff) / ((a_concentration ** a_coeff) * (b_concentration ** b_coeff))

    # calculate the equilibrium constant Kc
    Kc = Kc

    # print the equilibrium constant Kc
    print("The equilibrium constant Kc is:", Kc)

#finding kP
def solveKp():

     # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()

    # Get the partial pressures of the reactants and products
    Pa = float(input("Enter the partial pressure of A: "))
    Pb = float(input("Enter the partial pressure of B: "))
    Pc = float(input("Enter the partial pressure of C: "))
    Pd = float(input("Enter the partial pressure of D: "))

    # Calculate Kp using the formula
    Kp = (Pc ** c_coeff * Pd ** d_coeff) / (Pa ** a_coeff * Pb ** b_coeff)

    # Print the result
    print("The equilibrium constant Kp is:", Kp)

#finding Qc
def solveQc():
    # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()

    # define the concentrations of the reactants and products at equilibrium
    gatherConcentrationsABCD(typeofvar="concentrations")

    # calculate the reaction quotient Qc
    Qc = (c_concentration ** c_coeff) * (d_concentration ** d_coeff) / ((a_concentration ** a_coeff) * (b_concentration ** b_coeff))

    # print the value of Qc
    print("The value of Qc is:", Qc)

#finding standard enthalpy change
def solveStandardEnthalpyChange():
    # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()

    # define the standard enthalpies of formation for the reactants and products
    hf_a = float(input("Enter the standard enthalpy of formation of reactant A (kJ/mol): "))
    hf_b = float(input("Enter the standard enthalpy of formation of reactant B (kJ/mol): "))
    hf_c = float(input("Enter the standard enthalpy of formation of product C (kJ/mol): "))
    hf_d = float(input("Enter the standard enthalpy of formation of product D (kJ/mol): "))

    # calculate the standard enthalpy change ΔH°
    delta_h = (c_coeff * hf_c + d_coeff * hf_d) - (a_coeff * hf_a + b_coeff * hf_b)

    # print the value of ΔH°
    print("The standard enthalpy change ΔH° is:", delta_h, "kJ/mol")

#finding standard entropy change
def solveStandardEntropyChange():
    # define the coefficients of the balanced chemical equation
    gatherCoefficientsABCD()

    # define the standard entropies of formation for the reactants and products
    s_a = float(input("Enter the standard entropy of reactant A (J/(mol*K)): "))
    s_b = float(input("Enter the standard entropy of reactant B (J/(mol*K)): "))
    s_c = float(input("Enter the standard entropy of product C (J/(mol*K)): "))
    s_d = float(input("Enter the standard entropy of product D (J/(mol*K)): "))

    # calculate the standard entropy change ΔS°
    delta_s = (c_coeff * s_c + d_coeff * s_d) - (a_coeff * s_a + b_coeff * s_b)

    # print the value of ΔS°
    print("The standard entropy change ΔS° is:", delta_s, "J/(mol*K)")


#Acids and Bases Section
def acids_bases():
    restartABCondition = 1

    while restartABCondition == 1:
        print("")
        loading_screen()
        print("\nWhat are you looking for?:\n")
        print("a.)Finding pH from pOH\nb.) Finding pOH from pH\nC.) Finding pH from H+\nD.) Finding H+ from pH\nE.) Finding Finding pOH from OH-\nF.) Finding OH- from pOH")
        acids_bases_selection = input()

        try:
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
            print("An error has occured with the Acids and Bases Section.\n You may have inputted something other than a number. \n Returning you now to the main program.")
       

        #Restart Condition with wait time before it
        time.sleep(0.5)
        print("")
        print("Press Y to Restart, N if you want to end\n\n")
        restartABConditionInput = input()
        if restartABConditionInput == "Y" or restartABConditionInput == "y":
                    
            restartABConditionDecision = 1
        else:
            restartABConditionDecision = 0
        restartABCondition = restartABConditionDecision

    else:
        #If it restarts, it prints BYEBYE and clears the terminal.
        print("BYEBYE")
        os.system('cls||clear')
        
        

#MAIN CODE
#MAIN CODE
#MAIN CODE

x = "true"
while (x=="true"):
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
    print("")
    print("")
    print("(g.) Acids & Bases")

    selection = input()
    os.system('cls||clear')
    match selection:
        case "a":
            print("")
            print("StandardEnthalpyChange")
            print("")
            solveStandardEnthalpyChange()
        case "b":
            print("")
            print("StandardEntropyChange")
            print("")
            solveStandardEntropyChange()
        case "c":
            print("")
            print("Solving for Kc")
            print("")
            solveKc()
        case "d":
            print("")
            print("Solving for Qc")
            print("")
            solveQc()
        case "e":
            print("")
            print("Solving for Kc from Kp")
            print("")
            solveKcKp1()
        case "f":
            print("")
            print("Solving for Kp")
            print("")
            solveKp()
        case "g":
            print("")
            print("Acids & Bases")
            print("")
            acids_bases()
        case "j":
            print("")
            print("You have accessed the easter egg")
            print("")
            acids_bases()
else:
    print("Goodbye! Thank you for using ChEmTechPythoncalculator!")