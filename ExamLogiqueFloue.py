#PUEL QUENTIN
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

err = ctrl.Antecedent(np.arange(-4,5,1), 'erreur')
errd = ctrl.Antecedent(np.arange(-10,11,1), 'erreurDot')
degree = ctrl.Consequent(np.arange(-100,101,1), 'degree')

err.automf(3)
errd.automf(3)

degree['cool'] = fuzz.trimf(degree.universe, [-100, -50, 0])
degree['rien'] = fuzz.trimf(degree.universe, [-50, 0, 50])
degree['chauffe'] = fuzz.trimf(degree.universe, [0, 50, 100])


err.view()
errd.view()
degree.view()

rule1 = ctrl.Rule(err['good'] | errd['good'], degree['chauffe'])
rule2 = ctrl.Rule(err['average'] | errd['good'], degree['chauffe'])
rule3 = ctrl.Rule(err['poor'] | errd['good'], degree['cool'])
rule4 = ctrl.Rule(err['good'] | errd['average'], degree['chauffe'])
rule5 = ctrl.Rule(err['average'] | errd['average'], degree['rien'])
rule6 = ctrl.Rule(err['poor'] | errd['average'], degree['cool'])
rule7 = ctrl.Rule(err['good'] | errd['poor'], degree['chauffe'])
rule8 = ctrl.Rule(err['average'] | errd['poor'], degree['cool'])
rule9 = ctrl.Rule(err['poor'] | errd['poor'], degree['cool'])

rule1.view()

degreecontrol = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
degre = ctrl.ControlSystemSimulation(degreecontrol)

degre.input['erreur'] = 1
degre.input['erreurDot'] = -2.5

degre.compute()
print(degre.output['degree'])
degree.view(sim=degre)