# importing libraries
import numpy as np
import math
import scipy.stats as st
from colorama import Fore, Style

# Print Lines
def lines():
    print("-----------------------------------------------")

# Z critical region test
def z_critical(z_statistic, alpha):
    # choosing of critical region
    lines()
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    # left sided critical region
    if critical_region == 1:
        #calculation of the critical value and p-value
        critical_value = st.norm.ppf(alpha)
        p_value = st.norm.cdf(z_statistic)

        # displaying of the values
        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing to accept or reject the null hypothesis
        if z_statistic < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    # right sided critical region
    elif critical_region == 2:
        #computation for the critical value and the p-value
        critical_value = st.norm.ppf(1 - alpha)
        p_value = 1 - st.norm.cdf(z_statistic)

        #printing of the values
        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing the accept or reject the null hypothesis
        if z_statistic > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

    # two-sided crtical region  
    elif critical_region == 3:
        # calculation of the two critical values and p-value
        # the alpha is divided by 2 since there are 2 critical regions
        alpha = alpha/2
        critical_value1 = st.norm.ppf(alpha)
        critical_value2 = st.norm.ppf( 1 - alpha)
        p_value = 2 * (1 - st.norm.cdf(abs(z_statistic)))

        #printing of the values
        print("The p-value is " + str(round(p_value,10)) + ".")
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")

        # choosing the accept or reject the null hypothesis
        if z_statistic < critical_value1 or z_statistic > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

# T critical Region
def t_critical(t_stat, alpha, d_f):
    # choosing of critical region
    lines()
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    # left sided critical region
    if critical_region == 1:
        #calculation of the critical value and p-value
        critical_value = st.t.ppf(alpha, d_f)
        p_value = st.t.cdf(t_stat, d_f)

        #displaying of the values
        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Critical Value is " + str(round(critical_value, 4)) + ".")

        # choosing the accept or reject the null hypothesis
        if t_stat < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    # right sided critical region
    elif critical_region == 2:
        # calculation of the critical value and p-value
        critical_value = st.t.ppf(1 - alpha, d_f)
        p_value = 1 - st.t.cdf(t_stat, d_f)

        #printing of the values
        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Critical Value is " + str(round(critical_value, 4)) + ".")

        # choosing the accept or reject the null hypothesis
        if t_stat > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    #two sided critical value
    elif critical_region == 3:
        # calculation of the two critical values and p-value
        # the alpha is divided by 2 since there are 2 critical regions
        alpha = alpha/2
        critical_value1 = st.t.ppf(alpha, d_f)
        critical_value2 = st.t.ppf( 1 - alpha, d_f)
        p_value = (1 - st.t.cdf(abs(t_stat), d_f)) * 2

        #printing of the values
        print("The P-Value is " + str(round(p_value, 5)) + ".")
        print("The Left Critical Value is " + str(round(critical_value1, 4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2, 4)) + ".")

        # choosing the accept or reject the null hypothesis
        if t_stat < critical_value1 or t_stat > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL) 

# Case D Pooled Standard Deviation Claculation
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
    # asking for values
    print(Fore.GREEN + "You have Chosen Case A: Single Population where sigma is known or sample is large."  + Style.RESET_ALL)
    x = float(input("Enter the Sample Mean: "))
    u_0 = float(input("Enter the Population Mean: "))
    o = float(input("Enter the Population Standard Deviation: "))
    n = int(input("Enter the Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    # calculation for the z statistics
    numerator = x - u_0
    d_up = o
    d_down = np.sqrt(n)
    denominator = np.divide(d_up, d_down)
    z_statistic = np.divide(numerator, denominator)
    
    # displaying the value
    lines()
    print("The Z-Statistic Value is " + str(round(z_statistic,4)) + ".")

    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    z_critical(z_statistic, alpha)
    
# Case B: Sigma is Unknown or Sample is Small
def one_mean_case_B():
    # asking for values
    print(Fore.GREEN + "You have chosen Case B: Sigma is Unknown or Sample is Small."  + Style.RESET_ALL)
    x = float(input("Enter the Sample Mean: "))
    u_0 = float(input("Enter the Population Mean: "))
    s = float(input("Enter the Sample Standard Deviation: "))
    n = int(input("Enter the Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    # calculation for the t statistics and degree of freedom
    numerator = x - u_0
    d_up = s
    d_down = np.sqrt(n)
    denominator = np.divide(d_up, d_down)
    t_stat = np.divide(numerator, denominator)
    d_f = n - 1

    # displaying of values
    lines()
    print("The T-Statistic Value is " + str(round(t_stat, 4)) + ".")
    print("The Degree of Freedom is " + str(d_f) + ".")

    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    t_critical(t_stat, alpha, d_f)

# Test for Proportions: Single Population
# 𝑥 is the number of “successes” in the sample, the sample size is 𝑛 ≥ 30
def proportion_single():
    # asking for values
    print(Fore.GREEN + "You have Chosen Test for Proportions: Single Population."  + Style.RESET_ALL)
    x = int(input("Enter the Number of Successes: "))
    n = int(input("Enter the Sample Size: "))
    p_0 = float(input("Enter the Population Proportion: "))
    alpha = float(input("Enter the Significance Level: "))

    # calculation for the sample proportion and the z statisics
    sample_prop = np.divide(x, n)
    numerator = sample_prop - p_0
    denominator = np.sqrt(np.divide(np.multiply(p_0, 1 - p_0), n))
    z_stat = np.divide(numerator, denominator)

    #displaying of value
    lines()
    print("The Z-Statistic Value is " + str(round(z_stat, 4)) + ".")

    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    z_critical(z_stat, alpha)

# Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given
def two_means_case_C():
    # asking for values
    print(Fore.GREEN + "You have Chosen Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given."  + Style.RESET_ALL)
    x_1 = float(input("Enter the 1st Sample Mean: "))
    s_1 = float(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = float(input("Enter the 2nd Sample Mean: "))
    s_2 = float(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = float(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))

    # calculation for the z statistics
    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(np.square(s_1), n_1) + np.divide(np.square(s_2), n_2)
    denominator = np.sqrt(root_term)
    z_statistic = np.divide(numerator, denominator)

    # displaying of value
    print("The Z-Statistic Value is " + str(round(z_statistic, 4)) + ".")
    
    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    z_critical(z_statistic, alpha)

# Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal
def two_means_case_D():
    # asking for values
    print(Fore.GREEN + "You have Chosen Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal."  + Style.RESET_ALL)
    x_1 = float(input("Enter the 1st Sample Mean: "))
    s_1 = float(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = float(input("Enter the 2nd Sample Mean: "))
    s_2 = float(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = float(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))
    lines()

    # calculation of the degree of freedom, pooled standard deviation, and t-statistic
    s_p2 = math.sqrt(pooled_std(n_1, n_2, s_1, s_2))
    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(1, n_1) + np.divide(1, n_2)
    denominator = np.multiply(s_p2, np.sqrt(root_term))
    d_f = n_1 + n_2 - 2
    t_statistic = np.divide(numerator, denominator)
    
    # displaying of values
    print("The T-Statistic is " + str(round(t_statistic, 4)) + ".")
    print("The Pooled Standard Deviation is " + str(round(s_p2,4)) + '.')
    print("The Degree of Freedom is " + str(d_f) + '.')
    
    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    t_critical(t_statistic, alpha, d_f)

# Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal
def two_means_case_E():
    # asking for values
    print(Fore.GREEN + "You have Chosen Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal."  + Style.RESET_ALL)
    x_1 = float(input("Enter the 1st Sample Mean: "))
    s_1 = float(input("Enter the 1st Sample Standard Deviation: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = float(input("Enter the 2nd Sample Mean: "))
    s_2 = float(input("Enter the 2nd Sample Standard Deviation: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    d_0 = float(input("Enter the Difference Between the Population Means: "))
    alpha = float(input("Enter the Significance Level: "))
    
    # solving for the t-statistics
    numerator = (x_1 - x_2) - d_0
    root_term = np.divide(np.square(s_1), n_1) + np.divide(np.square(s_2), n_2)
    denominator = np.sqrt(root_term)
    t_statistic = np.divide(numerator, denominator)

    # calling the function to solve for the degree of freedom
    d_f = dof_case_E(n_1, n_2, s_1, s_2)
  
    # displaying of values
    lines()
    print("The T-Statistic is " + str(round(t_statistic, 4)) + ".")
    print("The Degree of Freedom is " + str(round(d_f, 4)) + '.')

    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    t_critical(t_statistic, alpha, d_f)

# Case F: Paired Observation
def paired_observation_case_F():
    # asking for values
    print(Fore.GREEN + "You have Chosen Case F: Paired Observation."  + Style.RESET_ALL)
    sample1 = np.array([float(x) for x in input("Enter the data for the 1st Sample (Separate by Spaces): ").split()])
    sample2 = np.array([float(x) for x in input("Enter the data for the 2nd Sample (Separated by Spaces): ").split()])
    d_0 = int(input("Enter the Difference Between the Samples: "))
    alpha = float(input("Enter the Significance Level: "))
    
    # solving for the difference and difference standard deviation
    differences = sample1 - sample2
    mean_difference = np.mean(differences)
    std_difference = np.std(differences, ddof=1)

    # calculation for the t-statistic and degree of freedom
    numerator = mean_difference - d_0
    denominator = np.divide(std_difference, np.sqrt(len(differences)))
    t_stat = np.divide(numerator, denominator)
    d_f = len(differences) - 1
    
    # displaying of values
    lines()
    print("The Difference is " + str(round(mean_difference, 4)) + ".")
    print("The Difference Standard Deviation is " + str(round(std_difference, 4)) + ".")
    print("The T-Statistic is " + str(round(t_stat, 4)) + ".")
    print("The Degree of Freedom is " + str(round(d_f, 4)) + '.')

    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    t_critical(t_stat, alpha, d_f)

# Test for Proportions: Two Population
# 𝑥 is the number of “successes” in the sample, the sample size is 𝑛 ≥ 30
def proportion_two():
    # asking for values
    print(Fore.GREEN + "You have Chosen Test for Proportions: Two Population."  + Style.RESET_ALL)
    x_1 = int(input("Enter the 1st Number of Successes: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    x_2 = int(input("Enter the 2nd Number of Successes: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))

    # solving for the 2 sample proportions and pooled sampled proportion
    sample1_prop = x_1 / n_1
    sample2_prop = x_2 / n_2
    pooled_sample_prop = (x_1 + x_2) / (n_1 + n_2)
    q = 1 - pooled_sample_prop

    # calculation for z-statistic Value
    numerator = sample1_prop - sample2_prop
    denominator = np.sqrt(pooled_sample_prop * q * (1/n_1 + 1/n_2))
    z_stat = np.divide(numerator, denominator)

    # displaying of values
    print("The 1st Sample Proportion is " + str(round(sample1_prop,4)) + ".")
    print("The 2nd Sample Proportion is " + str(round(sample2_prop,4)) + ".")
    print("The Pooled Sample Proportion is " + str(round(pooled_sample_prop,4)) + ".")
    print("The Z-Statistic Value is " + str(round(z_stat, 4)) + ".")
    
    # calling the function for the remaining calculations (p-value, critical value, conclusion)
    z_critical(z_stat, alpha)

# Variance For Single Population
def var_one():
    # asking for values
    print(Fore.GREEN + "You have Chosen Variance For Single Population."  + Style.RESET_ALL)
    n = int(input("Enter the Sample Size: "))
    s = float(input("Enter the Sample Variance: "))
    o_0 = float(input("Enter the Population Variance: "))
    alpha = float(input("Enter the Significance Level: "))

    # calculation for chi-square statistic and degree of freedom
    numerator = (n - 1) * np.square(s)
    denominator = np.square(o_0)
    chi_squared = np.divide(numerator, denominator)
    d_f = n - 1
    
    # displaying of values
    lines()
    print("The Chi-Square Value is " + str(round(chi_squared,4)) + ".")
    print("The Degree of Freedom is " + str(d_f) + ".")
    
    # calculating and displaying the p-value
    p_value = st.chi2.sf(chi_squared, n - 1)
    print("The P-Value is " + str(round(p_value,6)) + ".")
    lines()
    
    # choosing of critical region
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()
    
    # left sided critical region
    if critical_region == 1:
        # calculating and displaying the critical value
        critical_value = st.chi2.ppf(alpha, n - 1)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if chi_squared < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    # right sided critical region
    elif critical_region == 2:
        # calculating and displaying the critical value
        critical_value = st.chi2.ppf(1 - alpha, n - 1)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if chi_squared > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    # two sided critical region
    elif critical_region == 3:
        # calculating and displaying the two critical values
        # alpha is divided by 2 since there are 2 critical regions
        alpha = alpha/2
        critical_value1 = st.chi2.ppf(alpha, n - 1)
        critical_value2 = st.chi2.ppf(1 - alpha, n - 1)
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if chi_squared < critical_value1 or chi_squared > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

# Variance For Two Populations
def var_two():
    # asking for values
    print(Fore.GREEN + "You have Chosen Variance For Two Population."  + Style.RESET_ALL)
    s_1 = float(input("Enter the 1st Sample Variance: "))
    n_1 = int(input("Enter the 1st Sample Size: "))
    s_2 = float(input("Enter the 2nd Sample Variance: "))
    n_2 = int(input("Enter the 2nd Sample Size: "))
    alpha = float(input("Enter the Significance Level: "))
    
    # calculation for the f-statistic, 2 degree of freedom, and p-value
    f_stats = np.divide(s_1, s_2)
    v_1 = n_1 - 1
    v_2 = n_2 - 1
    p_value = st.f.sf(f_stats, v_1, v_2)
    
    # displaying of values
    lines()
    print("The F-Ratio Value is " + str(round(f_stats,4)) + ".")
    print("The 1st Degree of Freedom is " + str(v_1) + ".")
    print("The 2nd Degree of Freedom is " + str(v_2) + ".")
    print("The P-Value is " + str(round(p_value,6)) + ".")
    lines()

    # choosing of critical region
    critical_region = int(input(Fore.YELLOW + "Enter the Critical Region (1) Left, (2) Right, (3) Both: " +Style.RESET_ALL))
    lines()

    # left sided critical region
    if critical_region == 1:
        # calculating and displaying the critical value
        critical_value = st.f.ppf(alpha, v_1, v_2)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if f_stats < critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
    
    elif critical_region == 2:
        # calculating and displaying the critical value
        critical_value = st.f.ppf(1 - alpha, v_1, v_2)
        print("The Critical Value is " + str(round(critical_value,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if f_stats > critical_value:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)
            
    elif critical_region == 3:
        # calculating and displaying the critical value
        # alpha is divided by 2 since there are 2 critical regions
        alpha = alpha/2
        critical_value1 = st.f.ppf(alpha, v_1, v_2)
        critical_value2 = st.f.ppf(1 - alpha, v_1, v_2)
        print("The Left Critical Value is " + str(round(critical_value1,4)) + ".")
        print("The Right Critical Value is " + str(round(critical_value2,4)) + ".")

        # choosing whether to accept or reject the null hypothesis
        if f_stats < critical_value1 or f_stats > critical_value2:
            print(Fore.RED + "Reject The Null Hypothesis."+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Accept The Null Hypothesis." + Style.RESET_ALL)

# Main Program that will print the welcome message
# It also shows choice for different choices for the user to choose from
print(Fore.BLUE + '\nWelcome to Hippopotamus - Hypothesis Testing Calculator' + Style.RESET_ALL)
lines()
print(Fore.GREEN + "The following are the choices for Single Population:" + Style.RESET_ALL)
lines()
print("1. Case A: Single Population Where Sigma is Known or Sample is Large")
print("2. Case B: Sigma is Unknown or Sample is Small")
print("3. Test for Proportions: Single Population")
print("4. Variance For Single Population")
lines()
print(Fore.GREEN + "The following are the choices for Two Population:" + Style.RESET_ALL)
lines()
print("5. Case C: Two Mean Big Sample Size or Population Stnadard Deviation is Given")
print("6. Case D: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal")
print("7. Case E: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal")
print("8. Case F: Paired Observation")
print("9. Test for Proportions: Two Population")
print("10. Variance For Two Populations")
lines()
choice = int(input(Fore.BLUE + "Enter your choice: "  + Style.RESET_ALL))
lines()

# if-else statement to execute specified task based on choice option
# if the choice is not in the selected range then the program will display "invalid option"
if choice == 1:
    one_mean_case_A()
elif choice == 2:
    one_mean_case_B()
elif choice == 3:
    proportion_single()    
elif choice == 4:
    var_one()    
elif choice == 5:
    two_means_case_C()
elif choice == 6:
    two_means_case_D()
elif choice == 7:
    two_means_case_E()
elif choice == 8:
    paired_observation_case_F()
elif choice == 9:
    proportion_two()
elif choice == 10:
    var_two()
else:
    print(Fore.RED + "Invalid Option!" + Style.RESET_ALL)