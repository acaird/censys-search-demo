

## Set-up

1. `pip install censys`
1. Get your API ID and Secret from https://censys.io/account/api
1. Note your API query budget at https://censys.io/account
It will look something like this:
```
       Subscription Plan: Free
            Queries Used: 0 (0.0%)
         Allowed Queries: 250
           Queries Reset: September 23, 2020
Results per search query: Up to 1,000
```

## Making Queries

The file `simply-censys.py` in this directory will make the simplest
of queries; fill in your API ID, Secret, and a website to search for.
