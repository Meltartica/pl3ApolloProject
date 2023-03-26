import numpy as np
import math
import scipy.stats as st
from colorama import Fore, Back, Style

# Print Lines
def lines():
    print("-----------------------------------------------")

# Z critical Region
def z_critical(z_statistic, alpha):
    lines()
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    if critical_region == 1:
        critical_value = st.norm.ppf(alpha)
        p_value = st.norm.cdf(z_statistic)

        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        if z_statistic < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    elif critical_region == 2:
        critical_value = st.norm.ppf(1 - alpha)
        p_value = 1 - st.norm.cdf(z_statistic)

        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        if z_statistic > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    elif critical_region == 3:
        alpha = alpha/2
        critical_value1 = st.norm.ppf(alpha)
        critical_value2 = st.norm.ppf( 1 - alpha)
        p_value = 2 * (1 - st.norm.cdf(abs(z_statistic)))

        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")

        if z_statistic < critical_value1 or z_statistic > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

# T critical Region
def t_critical(t_stat, alpha, d_f):
    lines()
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    if critical_region == 1:
        critical_value = st.t.ppf(alpha, d_f)
        p_value = st.t.cdf(t_stat, d_f)

        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Critical Value is " + str(round(critical_value, 4)) + ".")

        if t_stat < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    elif critical_region == 2:
        critical_value = st.t.ppf(1 - alpha, d_f)
        p_value = 1 - st.t.cdf(t_stat, d_f)

        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Critical Value is " + str(round(critical_value, 4)) + ".")

        if t_stat > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    elif critical_region == 3:
        alpha = alpha/2
        critical_value1 = st.t.ppf(alpha, d_f)
        critical_value2 = st.t.ppf( 1 - alpha, d_f)
        p_value = (1 - st.t.cdf(abs(t_stat), d_f)) * 2

        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Left Critical Value is " + str(round(critical_value1, 4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2, 4)) + ".")

        if t_stat < critical_value1 or t_stat > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL) 

# Pooled Standard Deviation
def pooled_std(n_1, n_2, s_1, s_2):
    numerator = np.multiply(n_1 - 1, np.square(s_1)) + np.multiply(n_2 - 1, np.square(s_2))
    denominator = n_1 + n_2 - 2
    return np.divide(numerator, denominator)

# Case E Degree of Freedom
def dof_case_E(n_1, n_2, s_1, s_2):
    dof_first_term = np.divide(np.square(s_1), n_1)
    dof_second_term = np.divide(np.square(s_2), n_2)
    dof_numerator = np.square(dof_first_term + dof_second_term)
    dof_denominator = np.divide(np.square(dof_first_term), n_1 - 1) + np.divide(np.square(dof_second_term), n_2 - 1)
    
    return np.divide(dof_numerator, dof_denominator)

# Case A: Single Population where sigma is known or sample is large
def one_mean_case_A():
    print(Fore.GREEN + "You have Chosen Case A: Single Population where sigma is known or sample is large."  + Style.RESET_ALL)
    x = float(input("Enter the Sample Mean: "))
    u_0 = float(input("Enter the Population Mean: "))
    o = float(input("Enter the Population Standard Deviation: "))
    n = int(input("Enter the Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    numerator = x - u_0
    d_up = o
    d_down = np.sqrt(n)
    denominator = np.divide(d_up, d_down)
    z_statistic = np.divide(numerator, denominator)
    
    lines()
    print("The Z Score is " + str(round(z_statistic,4)) + ".")

    z_critical(z_statistic, alpha)
    
# Case B: Sigma is Unknown or Sample is Small
def one_mean_case_B():
    print(Fore.GREEN + "You have chosen Case B: Sigma is Unknown or Sample is Small."  + Style.RESET_ALL)
    x = float(input("Enter the Sample Mean: "))
    u_0 = float(input("Enter the Population Mean: "))
    s = float(input("Enter the Sample Standard Deviation: "))
    n = int(input("Enter the Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    numerator = x - u_0
    d_up = s
    d_down = np.sqrt(n)
    denominator = np.divide(d_up, d_down)
    t_stat = np.divide(numerator, denominator)
    d_f = n - 1

    lines()
    print("The T Score is " + str(round(t_stat, 4)) + ".")
    print("The Degree of Freedom is " + str(d_f) + ".")

    t_critical(t_stat, alpha, d_f)

# Test for Proportions: Single Population
# 𝑥 is the number of “successes” in the sample, the sample size is 𝑛 ≥ 30
def proportion_single():
    print(Fore.GREEN + "You have Chosen Test for Proportions: Single Population."  + Style.RESET_ALL)
    x = int(input("Enter the Number of Successes: "))
    n = int(input("Enter the Sample Size: "))
    p_0 = float(input("Enter the Population Proportion: "))
    alpha = float(input("Enter the Significance Level: "))

    sample_prop = np.divide(x, n)
    numerator = sample_prop - p_0
    denominator = np.sqrt(np.divide(np.multiply(p_0, 1 - p_0), n))
    z_stat = np.divide(numerator, denominator)

    lines()
    print("The Z-Statistic is " + str(round(z_stat, 4)) + ".")
    
    z_critical(z_stat, alpha)

# Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given
def two_means_case_C():
    print(Fore.GREEN + "You have Chosen Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given."  + Style.RESET_ALL)
    x_1 = int(input("Enter the 1st Sample Mean: "))
    s_1 = int(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = int(input("Enter the 2nd Sample Mean: "))
    s_2 = int(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = int(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))

    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(np.square(s_1), n_1) + np.divide(np.square(s_2), n_2)
    denominator = np.sqrt(root_term)
    z_statistic = np.divide(numerator, denominator)

    print("The Z-Statistic is " + str(round(z_statistic, 4)) + ".")
    
    z_critical(z_statistic, alpha)

# Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal
def two_means_case_D():
    print(Fore.GREEN + "You have Chosen Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal."  + Style.RESET_ALL)
    x_1 = int(input("Enter the 1st Sample Mean: "))
    s_1 = int(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = int(input("Enter the 2nd Sample Mean: "))
    s_2 = int(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = int(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))
    lines()

    s_p2 = math.sqrt(pooled_std(n_1, n_2, s_1, s_2))
    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(1, n_1) + np.divide(1, n_2)
    denominator = np.multiply(np.sqrt(s_p2), np.sqrt(root_term))
    d_f = n_1 + n_2 - 2
    t_statistic = np.divide(numerator, denominator)
    
    print("The T Score is " + str(round(t_statistic, 4)) + ".")
    print("The Pooled Standard Deviation is " + str(round(s_p2,4)) + '.')
    print("The Degree of Freedom is " + str(d_f) + '.')
    
    t_critical(t_statistic, alpha, d_f)

# Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal
def two_means_case_E():
    print(Fore.GREEN + "You have Chosen Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal."  + Style.RESET_ALL)
    x_1 = int(input("Enter the 1st Sample Mean: "))
    s_1 = int(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = int(input("Enter the 2nd Sample Mean: "))
    s_2 = int(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = int(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))
    
    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(np.square(s_1), n_1) + np.divide(np.square(s_2), n_2)
    denominator = np.sqrt(root_term)

    d_f = dof_case_E(n_1, n_2, s_1, s_2)
  
    t_statistic = np.divide(numerator, denominator)
    
    lines()
    print("The T Score is " + str(round(t_statistic, 4)) + ".")
    print("The Degree of Freedom is " + str(round(d_f, 4)) + '.')

    t_critical(t_statistic, alpha, d_f)

# Case F: Paired Observation
def paired_observation_case_F():
    print(Fore.GREEN + "You have Chosen Case F: Paired Observation."  + Style.RESET_ALL)
    sample1 = np.array([float(x) for x in input("Enter the data for the 1st Sample (Separate by Spaces): ").split()])
    sample2 = np.array([float(x) for x in input("Enter the data for the 2nd Sample (Separated by Spaces): ").split()])
    d_0 = int(input("Enter the Difference Between the Samples: "))
    alpha = float(input("Enter the Significance Level: "))
    
    differences = sample1 - sample2
    mean_difference = np.mean(differences)
    std_difference = np.std(differences, ddof=1)

    numerator = mean_difference - d_0
    denominator = np.divide(std_difference, np.sqrt(len(differences)))
    t_stat = np.divide(numerator, denominator)
    d_f = len(differences) - 1
    
    lines()
    print("The Difference is " + str(round(mean_difference, 4)) + ".")
    print("The Difference Standard Deviation is " + str(round(std_difference, 4)) + ".")
    print("The T Score is " + str(round(t_stat, 4)) + ".")
    print("The Degree of Freedom is " + str(round(d_f, 4)) + '.')

    t_critical(t_stat, alpha, d_f)

# Test for Proportions: Two Population
# 𝑥 is the number of “successes” in the sample, the sample size is 𝑛 ≥ 30
def proportion_two():
    print(Fore.GREEN + "You have Chosen Test for Proportions: Two Population."  + Style.RESET_ALL)
    x_1 = int(input("Enter the 1st Number of Successes: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = int(input("Enter the 2nd Number of Successes: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))

    sample1_prop = x_1 / n_1
    sample2_prop = x_2 / n_2
    pooled_sample_prop = (x_1 + x_2) / (n_1 + n_2)
    q = 1 - pooled_sample_prop

    numerator = sample1_prop - sample2_prop
    denominator = np.sqrt(pooled_sample_prop * q * (1/n_1 + 1/n_2))
    z_stat = np.divide(numerator, denominator)

    print("The 1st Sample Proportion is " + str(round(sample1_prop,4)) + ".")
    print("The 2nd Sample Proportion is " + str(round(sample2_prop,4)) + ".")
    print("The Pooled Sample Proportion is " + str(round(pooled_sample_prop,4)) + ".")
    print("The Z-Statistic is " + str(round(z_stat, 4)) + ".")
    
    z_critical(z_stat, alpha)

# Variance For Single Population
def var_one():
    print(Fore.GREEN + "You have Chosen Variance For Single Population."  + Style.RESET_ALL)
    n = int(input("Enter the Sample Size: "))
    s = float(input("Enter the Sample Variance: "))
    o_0 = float(input("Enter the Population Variance: "))
    alpha = float(input("Enter the Significance Level: "))

    numerator = (n - 1) * np.square(s)
    denominator = np.square(o_0)
    chi_squared = np.divide(numerator, denominator)
    d_f = n - 1
    
    lines()
    print("The Chi-Square Score is " + str(round(chi_squared,4)) + ".")
    print("The Degree of Freedom is " + str(d_f) + ".")
    
    p_value = st.chi2.sf(chi_squared, n - 1)
    print("The P-Value is " + str(round(p_value,6)) + ".")
    lines()
    
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()
    
    if critical_region == 1:
        critical_value = st.chi2.ppf(alpha, n - 1)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")
        if chi_squared < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    elif critical_region == 2:
        critical_value = st.chi2.ppf(1 - alpha, n - 1)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")
        if chi_squared > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    elif critical_region == 3:
        alpha = alpha/2
        critical_value1 = st.chi2.ppf(alpha, n - 1)
        critical_value2 = st.chi2.ppf(1 - alpha, n - 1)
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")
        if chi_squared < critical_value1 or chi_squared > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

# Variance For Two Populations
def var_two():
    print(Fore.GREEN + "You have Chosen Variance For Two Population."  + Style.RESET_ALL)
    s_1 = float(input("Enter the 1st Sample Variance: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    s_2 = float(input("Enter the 2nd Sample Variance: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    f_stats = np.divide(s_1, s_2)
    v_1 = n_1 - 1
    v_2 = n_2 - 1
    p_value = st.f.sf(f_stats, v_1, v_2)
    
    lines()
    print("The F-Ratio Value is " + str(round(f_stats,4)) + ".")
    print("The 1st Degree of Freedom is " + str(v_1) + ".")
    print("The 2nd Degree of Freedom is " + str(v_2) + ".")
    print("The P-Value is " + str(round(p_value,6)) + ".")
    lines()

    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    if critical_region == 1:
        critical_value = st.f.ppf(alpha, v_1, v_2)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")
        if f_stats < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    elif critical_region == 2:
        critical_value = st.f.ppf(1 - alpha, v_1, v_2)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")
        if f_stats > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    elif critical_region == 3:
        alpha = alpha/2
        critical_value1 = st.f.ppf(alpha, v_1, v_2)
        critical_value2 = st.f.ppf(1 - alpha, v_1, v_2)
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")
        if f_stats < critical_value1 or f_stats > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

print(Fore.BLUE + '\nWelcome to Hippotamus - Hypothesis Testing Calculator' + Style.RESET_ALL)
lines()
print(Fore.GREEN + "There following are the choices for Single Population:" + Style.RESET_ALL)
lines()
print("1. Case A: Single Population Where Sigma is Known or Sample is Large")
print("2. Case B: Sigma is Unknown or Sample is Small")
print("3. Test for Proportions: Single Population")
print("4. Variance For Single Population")
lines()
print(Fore.GREEN + "There following are the choices for Two Population:" + Style.RESET_ALL)
lines()
print("5. Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given")
print("6. Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal")
print("7. Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal")
print("8. Case F: Paired Observation")
print("9. Test for Proportions: Two Population")
print("10. Variance For Two Populations")
lines()
choice = int(input(Fore.BLUE +"Enter your choice: "  + Style.RESET_ALL))
lines()

if choice == 1:
    one_mean_case_A()
elif choice == 2:
    one_mean_case_B()
elif choice == 3:
    proportion_single()
elif choice == 4:
    two_means_case_C()
elif choice == 5:
    two_means_case_D()
elif choice == 6:
    two_means_case_E()
elif choice == 7:
    paired_observation_case_F()
elif choice == 8:
    proportion_two()
elif choice == 9:
    var_one()
elif choice == 10:
    var_two()
else:
    print(Fore.RED + "Invalid Option!" + Style.RESET_ALL)