# User Manual
PLCSoftRel is a web application for reliability measurement for PLC software based on Bayesian models and statistical testing. This manual describes how to use PLCSoftRel to estimate the reliability of PLC software.

## Getting Started
1. [Sign up to create a PLCSoftRel account](#sign-up-to-create-a-plcsoftrel-account)
2. [Sign in to PLCSoftRel](#sign-in-to-plcsoftrel)
3. [Submit activity evaluation results for Bayesian Method](#submit-activity-evaluation-results-for-bayesian-method)
4. [Submit test results for Statistical Method](#submit-test-results-for-statistical-method)
5. [Configure Reliability Model Parameters ](#configure-reliability-model-parameters)
6. [View reliability results](#view-reliability-results)

## Sign up to create a PLCSoftRel account
Open the **PLCSoftRel** app and click the button in the top-right corner.

![](./images/main_page_click_icon_view.png)

The sign-in page will appear. Click the **Sign Up** button.

<img src="./images/sign-in_page_click_sign-up_view.png" width=50%>

This will guide you to the sign-up page. Enter your **Email Address** and **Password** and then click the **Sign Up** button to complete the registration.

<img src="./images/sign-up_page_view.png" width=50%>

## Sign in to PLCSoftRel
Open the **PLCSoftRel** app and click the button in the top-right corner.

![](./images/main_page_click_icon_view.png)

This will guide you to the sign-in page. Enter your **Email Address** and **Password** and then click the **Sign In** button to access your account.

<img src="./images/sign-in_page_view.png" width=50%>

## Submit activity evaluation results for Bayesian Method
Click the **Bayesian Methods** tab to start entering software-specific information including the **Number of Function Points (FP)** and **Development and V&V Activity Evaluation Results**.

![](./images/main_page_click_bbn_view.png)

### Number of Function Points (FP)
The number of Function Points (FP) is a measure of the software’s size and complexity. To estimate the number of FPs, please refer to **Table 8-10 "Ratios of Source-code Statements to Function Points for Selected Programming Languages"** in the **U.S.NRC report [1]**.

1. Enter the **Number of FPs**
2. Click the **Next** button to proceed.

![](./images/main_page_FP.png)

### Development and V&V activity evaluation results
To proceed development and V&V activity evaluation, please refer to **Section 4.2.1 "Attribute Nodes"** and **Appendix B "Detailed Attributes of All Phases"** in the **U.S.NRC report [1]**.

> Activity Quality is represented by 3 states: "High", "Medium", and "Low".
1. Enter the activity qualities by drop-down list.
2. Click the **Prev** and **Next** button to go to the previous/next section.
3. After you finish entering the data, click the **Submit** button to submit your results.

![](./images/main_page_attribute_view.png)

## Submit test results for Statistical Method

1. **Click the [Statistical Methods] tab.**
2. **1. Sensitivity Analysis**  
   - Enter the values for **PFD Goal** and **Confidence Goal**.  
   - Click the **Submit** button to perform the sensitivity analysis.
3. **2. Update PFD**  
   - Enter the **Number of Tests** and **Number of Failures**.  
   - Click the **Submit** button to calculate the statistical PFD.
4. **3. Full Analysis and Save (Save JSON)**  
   - Click the **Run Full Analysis and Save** button to execute the full analysis and download the results in JSON format.
     
![](./images/sst_page_view.png)

## Configure Reliability Model Parameters

Click the **Settings** icon in the top-right corner to open the configuration panel for reliability model parameters.

You can configure parameters used in **Bayesian models** and **statistical testing methods** to influence how the reliability is estimated.

### BBN (Bayesian Belief Network) Settings

Adjust the following parameters before running the BBN model:

- **Number of Chains**: Total MCMC chains to run in parallel.
- **Number of Iterations**: Number of total sampling steps.
- **Burn-in**: Initial steps to discard to remove bias.
- **Thinning Rate**: Interval at which samples are collected.
- **Enable DIC/pD Calculation**: Option to calculate Deviance Information Criterion and effective number of parameters.

### Statistical Method Settings

Set parameters for test-based reliability analysis:

- **Prior PFD**: Prior value of Probability of Failure on Demand.
- **Confidence Level**: Confidence level used in reliability estimation (e.g., 95%).

### Save Configuration

Click the **Save** button after adjusting the parameters. The new configuration will be applied in all subsequent reliability calculations.

> ⚠️ **Note**: Changing the model parameters may affect the final reliability results. Use with caution based on your reliability assurance strategy.
> 
![](./images/settings_icon_view.png)

## View reliability results
After submitting the results, you can view the estimated reliability results, specifically the **mean** values and **Markov chain Monte Carlo (MCMC) simulation traces** of the following reliability metrics:

- You can save the reliability calculation results to a file and load the saved file to view the results as a graph.
  
- Probability of Failure on Demand (PFD): probablity that safety software failed to take action when the demand condition is satisfied
    - Demand is a plant condition that requires the actuation of safety systems.
    - Eg. demand in reactor protection system: the condition that the trip signal should be produced

- Number of remaining faults

![](./images/results_page_view.png)

<!-- ## Accounts
### Authority
- Reviewers
- Users -->

## References
1. Chu T.-L., Varuttamaseni A., Yue M., Lee S. J., Kang H. G., Cho J., & Yang S. (2018). Developing a Bayesian Belief Network Model for Quantifying the Probability of Software Failure of a Protection System (NUREG CR-7233). U.S. NRC.
