# -*- coding: utf-8 -*-
"""
Project 1

Created on Sat Sep  5 18:36:37 2015

@author: Duo Wang

1. What is our independent variable? What is our dependent variable?
2. What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.
Now it’s your chance to try out the Stroop task for yourself. Go to this link, which has a Java-based applet for performing the Stroop task. Record the times that you received on the task (you do not need to submit your times to the site.) Now, download this dataset which contains results from a number of participants in the task. Each row of the dataset contains the performance for one participant, with the first number their results on the congruent task and the second number their performance on the incongruent task.
3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.
4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.
5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?
6. Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!
"""

# Reading data locally
import pandas as pd
stroop = pd.read_csv('/Users/Wangduo/stroopdata.csv')

#Report some descriptive statistics
print stroop.describe()

#visualizations (with seaborn style)
import matplotlib.pyplot as plot
import seaborn as sns

# Do the boxplot
plot.show(sns.boxplot(stroop))

# Do the violinplot
plot.show(sns.violinplot(stroop, widths = 0.5))

"""
# Do the distribution plot
sns.distplot(stroop['Congruent'],kde=False, color= "b")
"""

from scipy.stats import levene
print levene(stroop.Congruent, stroop.Incongruent)

from scipy.stats import kstest
print 'ks_con', kstest(stroop.Congruent, 'norm')
print 'ks_inc', kstest(stroop.Incongruent, 'norm')

from scipy.stats import ks_2samp
ks_2samp(stroop.Congruent, stroop.Incongruent)
# Do the t-test
import scipy.stats as ss
print ss.ttest_ind(stroop.Congruent, stroop.Incongruent)