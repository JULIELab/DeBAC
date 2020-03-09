# Background
This project goes back to a workshop on political romanticism in summer 2020 (in planing) which is organized by the graduate school ["Romanticism as a Model"](http://modellromantik.uni-jena.de/) at the Friedrich-Schiller-University of Jena (Germany). It aims to find out whether right-wing populist politicians in the Bundestag (German federal parliament) relate their political arguments to the historical german romanticism.

# Data
**DeBAC** (/dɪˈbeɪk/, **De**utsche**B**undestags**A**bgeordneten**C**orpus) contains tweets of all members of the Bundestag who have a verified twitter account. Currently, 478 of 709 members of the Bundestag have a verified twitter account. The following table shows the distribution of seats, the number of twitter accounts and the number of tweets of different parties.

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

# Method

1. Collecting Accounts

  We started collecting Twitter accounts of members of the Bundestag with the official website of the [Bundestag](https://www.bundestag.de/abgeordnete). Since some members didn't publish their Twitter accounts there, we than inspected the office websites of each party where we could collect more Twitter accounts. The MdB_list.tsv provides an overview of all collected accounts and their metadata. Probably there are more members of the Bundestag who have a Twitter account, for exemple the non-party politician [Verena Hartmann](https://twitter.com/verhartmannafd). But since we couldn't verify its authenticity, it's not included in DeBAC.

2. Getting Tweets

  Note: Due to the limitation of Twitter API ([Get Tweet timelines](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline)), we could only get up to 3,200 of a account's most recent Tweets at the beginning of the project (Sept. 2019). Since then, newly posted Tweets are continuously added to DeBAC. 

# Availability

# Publikations

# 
