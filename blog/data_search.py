#!/usr/bin/env python
import sys
import os
import csv
import re

state_codes = {}
state_codes['AL'] = 'Alabama'
state_codes['AK'] = 'Alaska '
state_codes['AS'] = 'American Samoa '
state_codes['AZ'] = 'Arizona'
state_codes['AR'] = 'Arkansas '
state_codes['CA'] = 'California '
state_codes['CO'] = 'Colorado '
state_codes['CT'] = 'Connecticut'
state_codes['DE'] = 'Delaware '
state_codes['DC'] = 'Dist. of Columbia'
state_codes['FL'] = 'Florida'
state_codes['GA'] = 'Georgia'
state_codes['GU'] = 'Guam '
state_codes['HI'] = 'Hawaii '
state_codes['ID'] = 'Idaho'
state_codes['IL'] = 'Illinois '
state_codes['IN'] = 'Indiana'
state_codes['IA'] = 'Iowa '
state_codes['KS'] = 'Kansas '
state_codes['KY'] = 'Kentucky '
state_codes['LA'] = 'Louisiana'
state_codes['ME'] = 'Maine'
state_codes['MD'] = 'Maryland '
state_codes['MH'] = 'Marshall Islands '
state_codes['MA'] = 'Massachusetts'
state_codes['MI'] = 'Michigan '
state_codes['FM'] = 'Micronesia '
state_codes['MN'] = 'Minnesota'
state_codes['MS'] = 'Mississippi'
state_codes['MO'] = 'Missouri '
state_codes['MT'] = 'Montana'
state_codes['NE'] = 'Nebraska '
state_codes['NV'] = 'Nevada '
state_codes['NH'] = 'New Hampshire'
state_codes['NJ'] = 'New Jersey '
state_codes['NM'] = 'New Mexico '
state_codes['NY'] = 'New York '
state_codes['NC'] = 'North Carolina '
state_codes['ND'] = 'North Dakota '
state_codes['MP'] = 'Northern Marianas'
state_codes['OH'] = 'Ohio '
state_codes['OK'] = 'Oklahoma '
state_codes['OR'] = 'Oregon '
state_codes['PW'] = 'Palau'
state_codes['PA'] = 'Pennsylvania '
state_codes['PR'] = 'Puerto Rico'
state_codes['RI'] = 'Rhode Island '
state_codes['SC'] = 'South Carolina '
state_codes['SD'] = 'South Dakota '
state_codes['TN'] = 'Tennessee'
state_codes['TX'] = 'Texas'
state_codes['UT'] = 'Utah '
state_codes['VT'] = 'Vermont'
state_codes['VA'] = 'Virginia '
state_codes['VI'] = 'Virgin Islands '
state_codes['WA'] = 'Washington '
state_codes['WV'] = 'West Virginia'
state_codes['WI'] = 'Wisconsin'
state_codes['WY'] = 'Wyoming'


def find_pol(name, state):
    print ("Searching for " + str(name) + " " + str(state))
    os.chdir(r"C:\Users\Sam\Documents\django_2\blog")
    dat = open("pol_data.csv", "r")
    dat = csv.reader(dat, delimiter=",", quotechar="|")
    os.chdir(r"C:\Users\Sam\Documents\django_2")
    good_ids = set({})
    name = name.lower()
    state = state.lower()

    for i, row in enumerate(dat):
        if i > 0:
            if state!="":
                for nam in re.sub("[\.,;]", " ", name).split():
                    if (nam in row[1].lower() and str.startswith(state_codes[row[3]].lower(), state)):
                        good_ids.add(row[0])
                    else:
                        good_ids = good_ids.difference(set([row[0], ]))
            else:
                for nam in re.sub("[\.,;]", " ", name).split():
                    if nam in row[1].lower():
                        good_ids.add(row[0])
                    else:
                        good_ids = good_ids.difference(set([row[0], ]))
    return good_ids
