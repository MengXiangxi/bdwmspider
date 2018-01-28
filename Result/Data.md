# User Profile of BDWM BBS

This data set is collected from BDWM BBS, a campus-based bulletin board system in Peking University, Beijing. Currently, it contains some user profile information which is available to the public without restrictions.

## Basic information

The data set `user_profile997.csv` is collected between **Jan/24/2018** and **Jan/26/2018**, during which time there are approximately **44296** registered users. Since the user registration and unregistration are dynamic processes, it is not a precise figure. However, nowadays, the rate of change is estimated to be very low. It is estimated that the coverage of the population is greater than 99.7%, and may exceed 99.9%. The entries are generally organized in an increased order of their `uid`, a random number assigned to each ID when they registered. But there are a very few exceptions (<10). The `uid` field is not provided in this data set. `user_profile995.csv` contains 44207 entries, which covers more than 99.5% registered users. We believe this is very close to a census.

The data set `user_profile_1To115000.csv` is collected on **Jan/27/2018**. The `uid` range 1-115000 was scanned, and it reflects the cross section scenario of a census. More fields are provided in this data set. `user_profile_1To115000.csv` contains 44173 entries.

This does not reflect all the registered IDs since the BBS was established, because the ID becomes invalid and the `uid` is recycled if the user stops logging in for a certain period of time. This period varies according to different `life` score. The `life` score is calculated with a certain algorithm, however some IDs that are actively involved in public affairs etc, are awarded higher `life` scores. See [this help information](https://bbs.pku.edu.cn/v2/help.php?cate=1) for more details (in Chinese). For IDs with a `life` score of 999, they never expire, unless they opt to unregister. However, this has rarely, if ever, happened.

## The definition of the fields

* `uid`, a random number assigned to each ID when they registered. Not available in `user_profile997.csv`.
* `uname`, the user name chosen by the user when they registered. The length is between 2 and 12 letters [A-Za-z], and is case insensitive.
* `gender`, 男=male, 女=female, 保密=not disclosed. This is defined by the users themselves and may not reflect their actual identity.
* `zodiac`, as defined in the code block below. similarly, 保密=not disclosed. This is automatically converted from the user's birthday provided, according to a conventional algorithm.

```json
{
    "白羊座":"Aries",
    "金牛座":"Taurus",
    "双子座":"Gemini",
    "巨蟹座":"Cancer",
    "狮子座":"Leo",
    "处女座":"Virgo",
    "天秤座":"Libra",
    "天蝎座":"Scorpio",
    "射手座":"Sagittarius",
    "摩羯座":"Capricorn",
    "水瓶座":"Aquarius",
    "双鱼座":"Pisces",
    "保密":"NA",
}
```

* `login`, number of login.
* `post`, number of posts submitted, excluding those published in certain boards which do not contribute to this figure.
* `life`, explained above.
* `uscore` A score calculated to reflect the activeness of a user. See [this help information](https://bbs.pku.edu.cn/v2/help.php?cate=1) for more details (in Chinese).  In the scripts I used a parody translation of `integral`, which has the same Chinese translations coincidentally.
* `YCF`, or "original score". When an ID posts an original post which is of great value, it may be awarded 1-3 'YCF' by the management IDs.
* `last_seen`, the last time of logging in. the format is `YYYY/MM/DD hh:mm`
* `duty`, the special management duty assigned to a certain ID. Not available in `user_profile997.csv`.
* `VIP`, the type of VIP account. There are three types of VIP accounts, and most normal accounts are labelled as 'NA'. Not available in `user_profile997.csv`.