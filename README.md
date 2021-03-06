## Background
This project is inspired by a discussion of political romanticism at the graduate school ["Romanticism as a Model"](http://modellromantik.uni-jena.de/) at the Friedrich-Schiller-University of Jena (Germany). It aims to find out whether right-wing populist politicians in the Bundestag (German federal parliament) relate their political arguments to the historical German romanticism.

## Data
_**DeBAC** (**De**utsche**B**undestags**A**bgeordneten**C**orpus)_ contains Tweets by all members of the Bundestag who have verified Twitter accounts. Currently, 478 out of 709 members of the Bundestag have verified Twitter accounts. The following table shows the distribution of seats in the Bundestag, the number of Twitter accounts and the number of Tweets of different parties.

|   |[Bundestag Members](https://www.bundestag.de/abgeordnete)|Twitter Accounts|Tweets|
|---|---:|---:|---:|
|[CDU](https://www.cducsu.de/hier-stellt-die-cducsu-bundestagsfraktion-ihre-abgeordneten-vor)|200|106|173,451|
|[CSU](https://www.cducsu.de/hier-stellt-die-cducsu-bundestagsfraktion-ihre-abgeordneten-vor)|46|24|22,594|
|[SPD](https://www.spdfraktion.de/abgeordnete/alle)|152|107|214,934|
|[AfD](https://www.afdbundestag.de/abgeordnete/)|89|53|83,445|
|[FDP](https://www.fdpbt.de/fraktion/abgeordnete)|80|69|122,280|
|[LINKE](https://www.linksfraktion.de/fraktion/abgeordnete/)|69|56|153,400|
|[GRÜNE](https://www.gruene-bundestag.de/abgeordnete)|67|59|169,450|
|non-party|6|4|16,360|
|**Total**|**709**|**478**|**955,914**|

(Status: 2020-03-09)

## Availability

According to Twitter’s [Developer Policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy) we are not allowed to provide downloadable datasets of Twitter Content. Instead, we provide a complete list of Tweets IDs ([tweets-meta.tsv](tweets-meta.tsv)) and Python scripts ([download_tweets.py](download_tweets.py)) which can be used to download the content of these Tweets via Twitter API. In this way, you can reconstruct DeBAC on your local computer.

## Methods

### Collecting Accounts
We started collecting Twitter accounts of members of the Bundestag with the official website of the [Bundestag](https://www.bundestag.de/abgeordnete). Since some members did not publish their Twitter accounts there, we then examined the office websites of each party where we could identify more Twitter accounts. [MdB_list.tsv](MdB_list.tsv) provides an overview of all the collected accounts and their metadata. It is possible that there are more members of the Bundestag who have Twitter accounts. For exemple, the username "[verhartmannafd](https://twitter.com/verhartmannafd)" seems to belong to the non-party politician Verena Hartmann. But since this is not shown on any official websites, we did not included it in DeBAC.

### Getting Tweets
We used [Tweepy](https://www.tweepy.org/) to access Twitter API. With the [Get Tweet timelines Method](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline), we got the textual content as well as various metadata such like created_at, if_retweet etc.
<br/>**Note:** Due to the limitation of Twitter API, we could only get up to 3,200 of a account's most recent Tweets at the beginning of the project (Sep 2019). Since then, however, newly posted Tweets are continuously added to DeBAC. 

* Create a [Twitter Developer account](https://developer.twitter.com/).
* Create an App and generate 'Keys and tokens'
* Create the JSON ``file twitter_credentials.json`` with the following format and in the directory ``DeBAC``, paste your created values of ``API key``, ``API secret key``, ``Access token``, ``Access token secret`` into the form:
```
{
  "CONSUMER_KEY":       "... value of API key ...",
  "CONSUMER_SECRET":    "... value of API secret key ...",
  "ACCESS_TOKEN":       "... value of Access token ...",
  "ACCESS_SECRET":      "... value of Access token secret ..."
}
```
* If you run the script [download_tweets.py](download_tweets.py), it can take several hours, usually 12 hours.

## Publication

Duan, Tinghui; Buechel, Sven; Hahn, Udo (2020): "Romantik" im aktuellen parteipolitischen Diskurs auf Twitter. In: [*DHd2020. Spielräume – Digital Humanities zwischen Modellierung und Interpretation*](https://dhd2020.de/). Paderborn, Germany, March 2-6, 2020. [[Poster](https://github.com/JULIELab/DeBAC/raw/master/DHd2020/Poster_dhd2020.pdf)]

## Acknowledgment

We thank [Susanna Rücker](https://github.com/susannaruecker) for her support with the data analysis.
