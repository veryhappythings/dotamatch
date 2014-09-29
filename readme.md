Dotamatch
=========

Python bindings for the Dota 2 API.

Take a look in the examples for clues as to how to run it! This readme will slowly grow to become more friendly as things get more concrete.

If you need an account ID that's public, mine is 507891.

Some Design Comments
--------------------

I've decided that Valve's names for APIs (GetTeamInfoByTeamId, for example) aren't very conducive to readable code, so I've taken a few liberties with my naming.

I intend to use python native data types whenever possible, and keep things quite close to generic dicts and lists where possible. For example, I'm going to convert Valve's dates and times to Python datetime objects.

I'm going to aim to lazy-load as much as possible in future, but for now, quite a lot is eager loaded. I suggest you keep an eye on the number of API calls that you're making! As it stands, the code is very simple, so it should be pretty easy to follow and get to grips with.


The Basics
----------

You'll need a Steam API key to get started. You can get that here: <http://steamcommunity.com/dev/apikey>

So let's jump in:
```python
key = "Insert your Steam API key here!"
history = MatchHistory(key)
for match in history.matches():
    print match
```

That is enough to get you some data. Not very useful, though, is it? Well, once we have a match, we can grab a player from it and inspect them:
```python
player = match.player('Maccy')
if player:
    print player
```

So here, player is just a dictionary. You've pretty much got the JSON that Valve's API offers in python form. Right now, that is basically the limit of this API. You can attach the API's parameters to any API call though, so, say you wanted to get my 10 most recent games:

```python
key = "Insert your Steam API key here!"
history = MatchHistory(key)
for match in history.matches(account_id=507891, matches_requested=10):
    print match.match_id
```

Supported APIs
--------------

* GetMatchHistory
* GetMatchDetails
* GetHeroes
* GetPlayerSummaries
* EconomySchema
* GetMatchHistoryBySequenceNum
* GetTeamInfoByTeamId


Links
-----

* [Official API documentation](http://dev.dota2.com/showthread.php?t=47115)
* [Unofficial API documentation](http://dev.dota2.com/showthread.php?t=58317)
* [Test status on Travis](https://travis-ci.org/veryhappythings/dotamatch)
* [Cyborgmatt on game types and leaver statuses](http://dev.dota2.com/showthread.php?t=47115&page=57&p=462940&viewfull=1#post462940)
* [MatchHistoryBySequenceNum information](http://dev.dota2.com/showthread.php?t=71679&p=464233&viewfull=1#post464233)

[![Build Status](https://travis-ci.org/veryhappythings/dotamatch.png)](https://travis-ci.org/veryhappythings/dotamatch)
