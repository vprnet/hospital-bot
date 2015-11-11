#!/usr/local/bin/python2.7

import csv

def new_tweet():
    with open('./reports.csv', 'r') as f:
        reader = csv.reader(f)
        new_tweets = []

        for row in reader:
            new_tweets.append(row)

        return new_tweets




# foundation_url = "http://www.dlp.vermont.gov/standard-surveys-hospitals"
# slug = {'Brattleboro Memorial Hospital': '/brattleboro-acc-poc-folder/', 'Brattleboro Retreat': '/brattleboro-retreat-acc-poc-folder/', 'Central Vermont Medical Center': '/central-vermont-acc-poc-folder/', 'Copley Hospital': '/copley-acc-poc-folder/', 'Fletcher Allen Health Care': '/fletcher-allen-acc-poc-folder/', 'Gifford Memorial Hospital': '/gifford-acc-poc-folder/', 'Grace Cottage Hospital': '/grace-acc-poc-folder/', 'Vermont Psychiatric Care Hospital': '/green-mountain-psychiatric-care-center/', 'Mt. Ascutney Hospital & Health Center': '/mt-ascutney-acc-poc-folder/', 'North Country Hospital & Health Center': '/north-country-acc-poc-folder/', 'Northeastern Vermont Regional Hospital': '/northeastern-acc-poc-folder/', 'Northwestern Medical Center': '/northwestern-acc-poc-folder/', 'Porter Hospital': '/porter-acc-poc-folder/', 'Rutland Regional Medical Center': '/rutland-acc-poc-folder/', 'Southwestern Vermont Medical Center': '/southwestern-acc-poc-folder/', 'Springfield Hospital': '/springfield-acc-poc-folder/', 'Navigation': 'portlet-navigation-tree'}
#
# print foundation_url + slug['Brattleboro Memorial Hospital']
