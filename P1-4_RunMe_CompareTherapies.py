import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# simululating no therapy
# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# simulating anticoagulation therapy
# create a cohort
cohort_anticoag = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_anticoag = cohort_anticoag.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_anticoag)

# print the estimates for the mean survival and number of strokes
print("Problem 1: Discounted Cost and Utility (plus prior outcomes)")
SupportMarkov.print_outcomes(simOutputs_none, "No therapy:")
SupportMarkov.print_outcomes(simOutputs_anticoag, "Anticoagulation therapy:")

# print the comparative outcomes
print("Problem 2: Change in Outcomes")
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticoag)

# report the CEA results
print("")
print("Problem 3: Cost-Utility Analysis and Problem 4: Cost-Benefit Analysis")
print("Please see graphs and the .csv file.")
print("A non-negative incremental net monetary benefit is obtained at a willingness-to-pay value of ≥$20,000 per one additional QALY.")
print("  Willingness-to-pay values below this point would not benefit from the use of anticoagulation therapy.")
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)
