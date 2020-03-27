# Question

Has the proportion of female characters changed since the original data was gathered and when I first scraped it for each Marvel and DC Comics, and is the proportion for each respective set of data different for each company?

## Design

- Why were you interested in this question?

I was inspired by a 528 article I found when I was first starting out in data science a few years ago that analyzed [diversity in characters in Marvel and DC Comics]. I found the article and the data it used particularly interesting at the time but did not know how to conduct my own research on the topic so I was unable to do much with the additional data I collected. Now that I have a better understanding of statistics, however, I will perform my own analysis on the topic for this project.

- How did you collect the data?

- The original data was [linked to the article]
- I painstakingly scraped the same wikis and half-deleted all my work like a dumbass bitch and didn't write any sort of documentation so all the bullshit code that "i guess works so its fine" is impossible to fix
- I then rewrote some of the code from the spider so that it works again and it took like 8 fuckin hours and i want to die and i cant go to bed until the last of it finishes scraping

For each date, data for all characters on the Marvel and Dc wikis were scraped, resulting in six datasets and populations. For each of these populations a sample of all characters with more than five appearances were selected and the proportion of female characters was recorded.

[add dropdown of specific process? idk man the code is p janky so i dont think thats a great idea]

- What are the explanatory and response variables?

The explanatory variables are the date of the scrape and the comic publisher, while the response variable is the proportion of female characters in the sample.

- What kind of study is it?

Since all the data is representative of past events and the study does not make any predictions for future observations, it is a retrospective observational study.

- What are possible limitations in your design and how could you address these?

Since the samples were not randomly sampled, it may not be truly possible to infer the study's results to the population. However, random sampling cannot be used in this case, as many of the samples would have overlapping data. This also means that the individuals in the dataset from the same publisher are not independent. Therefore, we must merely assume that the samples of characters with more than 5 appearances are representative of all chararacters in their respective set.

## Data

| | Prop | Num. Fem. | Num. Not | Total >5| Total|
|-----|-----|-----|-----|-----|-----|
|dc14|0.301437908496732|1153|2672|3825|6896|
|dc18|0.30852698290762437|3213|7201|10414|24818|
|dc20|0.3098817041714845|3484|7759|11243|27071|
|m14|0.28758503401360547|1691|4189|5880|16376|
|m18|0.2886446886446886|3546|8739|12285|60276|
|m20|0.29224605232147066|3720|9009|12729|67022|

idk man it doesnt wanna work :(

On the bar graph, the frequencies look similar across all groups

## Significance Test

## Simulation

## Conclusion