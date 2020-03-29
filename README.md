# Question

Is the proportion of female characters in Marvel and DC Comics different between the three scrape dates and between the publishers?
- Is there a difference in the proportion of female characters between the original scrape in 2015, when I first scraped it in 2017, and when I scraped it for the project?
- Is the proportion of female characters in Marvel Comics different from the proportion in DC Comics for each of the above time periods?


## Design

- Why were you interested in this question?

I was inspired by a [FiveThirtyEight article](https://fivethirtyeight.com/features/women-in-comic-books/) I found when I was first starting out in data science a few years ago that analyzed diversity in characters in Marvel and DC Comics. I found the article and the data it used particularly interesting at the time but did not know how to conduct my own research on the topic so I was unable to do much with the additional data I collected. Now that I have a better understanding of statistics, however, I have decided to perform my own analysis on the topic for this project.

- How did you collect the data?

Each scrape collected data on all characters on the respective wiki pages on the given date. The first scrape, on August 24, 2014, was [linked to the article](https://github.com/fivethirtyeight/data/tree/master/comic-characters) and I performed the additional scrapes December 27, 2018 and March 26, 2020. Once this data was collected, I took a sample of all characters with more than five appearances. This is to reduce bias resulting from characters with multiple entries due to their presence in multiple universes. The alternate versions of these characters are more likely to have appeared in special series or one-offs and would therefore be not as likely to be in the sample. Also, since the wiki pages are user-submitted less popular characters with fewer appearances may not have accurate data. From these samples, the number of female characters was recorded.

- What are the explanatory and response variables?

The explanatory variables are the date of the scrape and the comic publisher, while the response variable is the proportion of female characters in the sample.

- What kind of study is it?

Since the study period does not extend into the future and there are no experimental groups, this is a retrospective observational study.

- What are possible limitations in your design and how could you address these?

Since the samples were not randomly sampled, it may not be truly possible to infer the study's results to the population. However, random sampling cannot be used in this case, as many of the samples would have overlapping data. This also means that the individuals in the dataset from the same publisher are not independent. Therefore, we must merely assume that each sample of characters with more than 5 appearances is representative of all chararacters in their respective population.

## Data

| | Prop | Num. Fem. | Num. Not | Total >5| Total|
|-----|-----|-----|-----|-----|-----|
|dc14|0.301437908496732|1153|2672|3825|6896|
|dc18|0.30852698290762437|3213|7201|10414|24818|
|dc20|0.3098817041714845|3484|7759|11243|27071|
|m14|0.28758503401360547|1691|4189|5880|16376|
|m18|0.2886446886446886|3546|8739|12285|60276|
|m20|0.29224605232147066|3720|9009|12729|67022|

![frequency bargraph](https://raw.githubusercontent.com/FrostForth/Comics/master/images/freqbar.png)
- All three Marvel groups have a higher total frequency of characters with more than five appearances
- Although the frequency of nonfemale characters  in groups m18 and m20 are greater than the those in groups dc18 and dc20, the frequency of female characters is roughly similar across all four groups
- For both publishers, the frequency of nonfemales increases more between each scrape than the proportion of females

![percentage bargraph](https://raw.githubusercontent.com/FrostForth/Comics/master/images/percentbar.png)
- All groups seem to have proportions close to .3
- For both publishers, the proportions seem to increase slightly over time
- The proportions in all three Marvel groups seem to be lower than the proportion in dc14

![lineplot](https://raw.githubusercontent.com/FrostForth/Comics/master/images/scatter.png)

First scrape date: 10/13/2014

Second scrape date: 12/27/2018

Third scrape date: 3/26/2020

- The increase between the 2014 scrape and the 2018 scrapes are greater than the increase between the 2018 and 2020 scrapes for both publishers
- The amount of time between the first and second scrapes is about 3.5 times longer than between the second and third scrapes
- The increase in frequency between the first and third scrapes may not be linear but we do not have enough data to make a conclusion

### Based on the graphs,is it likely that the significance test will find statistically significant evidence for the alternative hypothesis?

There seems to be initial evidence that the proportion of female characters varies between each sample, as well as between each publisher and scrape.

## Significance Test

- Hypotheses:

Parameter: pi = the true proportion of female characters from scrape i

H0: There is no difference in proportions between the six populations

HA: At least one proportion is significantly different between the six populations

<details>
<summary> Follow-up Testing </summary>
If we find evidence for the alternative hypothesis, follow-up analysis will be conducted. First, I will conduct a chi-squared test for homogeneity on the three samples from each publishers. If either of those tests succeed, I will perform follow-up z tests for differences in proportions. Additionally, I will conduct a z test for differences in proportions for each scrape date.
</details>

- Initial Evidence

The raw data and graphs suggest differences between the groups.

- Two possible explanations

1. The observed differences in proportions over time and between publishers is a result of random chance

2. There really is a difference in at least one proportion

- Type of Significance Test:

Initially a chi-squared test for homogeneity will be used, but follow up z interval tests for proportions will be used if necessary.

- Is a confidence interval appropriate?

No. Since the study involves more than two samples, it would not be appropriate to use an interval to approximate the difference in population proportions.

Data:

| |dc14|dc18|dc20|m14|m18|m20|
|---|---|---|---|---|---|---|
|Fem|1153|3213|3484|1691|3546|3720|
|Not|2672|7201|7759|4189|8739|9009|

Exp:
| |dc14|dc18|dc20|m14|m18|m20|
|---|---|---|---|---|---|---|
|Fem|1140.3|3104.7|3351.8|1753.0|3662.4|3794.8|
|Not|2684.7|7309.3|7891.2|4127.0|8622.6|8934.2|


Conditions:

alpha = 0.05

1. We assume each sample is representative of its respective population
2. All expected counts are >5
3. We assume each observation is independent of other observations in each sample

![Chi-Squared Test](https://raw.githubusercontent.com/FrostForth/Comics/master/images/chisquare.png)

chi-squared = [(1153 - 1140)^2]/ + [(2672 - 2685)^2]/ + ... = 23.513

p-value = 0.0002692

Assuming there is no difference in proportions between the six populations, there is a 0.00027 chance that the observed chi-squared value of 23.513 would occure by random chance.

Since 0 < .05, we reject the null hypothesis and conclude that we have evidence that there is a significant difference in the proportion of female characters in at least one population.

## Simulation

![simulation distribution](https://raw.githubusercontent.com/FrostForth/Comics/master/images/sim.png)

p = 0

## Follow-Up Analysis

Assuming all conditions are met for all tests

Cont:
| |dc14|dc18|dc20|m14|m18|m20|
|---|---|---|---|---|---|---|
|Fem|0.141|3.781|5.214|2.190|3.702|1.475|
|Not|0.060|1.606|2.215|0.930|1.572|0.626|

The three cells with the highest contributions are:
1. dc2020 female
2. dc18 female
3. m18 female

This suggests that the most successful tests will be the DC chi-squared test and the z tests for 2018 and 2020.

### Additional chi-squared by publisher:

- DC

![Chi-square test DC](https://raw.githubusercontent.com/FrostForth/Comics/master/images/chidc.png)

chi-squared = 0.9726

p = 0.615

Since 0.615 > .05, we fail to reject the null hypothesis and conclude that we do not have evidence that the proportion of female characters in DC Comics has changed significantly between the scrapes.

- Marvel

![Chi-square test Marvel](https://raw.githubusercontent.com/FrostForth/Comics/master/images/chimarvel.png)

chi-squared = 0.587

p = 0.7455

Since 0.7455 > .05, we fail to reject the null hypothesis and conclude that we do not have evidence that the proportion of female characters in Marvel Comics has changed significantly between the scrapes.

### Z tests by scrape

- 2014

![z test 2014](https://raw.githubusercontent.com/FrostForth/Comics/master/images/z2014.png)

z = 1.465

p = 0.1429

Since .143 > .05, we fail to reject the null hypothesis and conclude that we do not have evidence that the true proportion of female characters was significantly different between the two publishers in the 2014 scrape.

- 2018

![z test 2018](https://raw.githubusercontent.com/FrostForth/Comics/master/images/z2018.png)

z = 3.264

p = 0.0011

Since .0011 < .05, we reject the null hypothesis and conclude that we have evidence that there is a significant difference in the true proportion of female characters between the publishers in the 2018 scrape.

- 2020

![z test 2020](https://raw.githubusercontent.com/FrostForth/Comics/master/images/z2020.png)

z = 2.972

p = 0.003

Since .003 < .05, we reject the null hypothesis and conclude that we have evidence that there is a significant difference in the true proportion of female characters between the publishers in the 2020 scrape.

## Conclusion

- Conclusion of tests

The initial test found evidence of at least one sample's proportion of female characters being statistically significantly different from the six populations. Upon further analysis, we discovered that there was not statistically significant evidence that the proportion had changed over time for either publisher. However, there is statistically significant evidence that the proportion of female characters is different between the publishers in both 2018 and 2020, but not in 2014.

- Possible error (in initial test only)

A type I error may have occurred in this test. This would mean that we found evidence that at least one proportion is significantly different when in reality, the proportions were not significantly different. This would lead to unnecessary follow-up analysis.

- Population

We should be able to generalize the results to all characters recorded in the Marvel and DC wikis.

- Cause and Effect?

Since this is an observational study and not an experiment, we cannot infer a cause-and-effect relationship.

- Advice

1. Set up a schedule and pace the steps of the project appropriately
2. Do research on what needs to be built beforehand, such as programs to collect the data and perform the simulation
3. Choose data that is independent

- Improvements / Further Study

Since most of the data is cumulative over time, using the proportions between scrapes may have impacted the data and contributed to the lack of evidence in both additional chi-squared tests. A better test of the proportion of female characters over time for each publisher may be using the first appearance dates for each characters to create a regression line. By plotting the number or proportion of female characters in each month or release cycle, a clearer association between the proportion of female characters and time may emerge. However, this data is the most commonly incomplete section on the wiki pages and the most difficult to scrape, I did not use this method in this study.
