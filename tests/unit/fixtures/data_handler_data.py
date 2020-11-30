#!/usr/bin/env python

from pathlib import Path

import pandas as pd

_PACKAGE_DIR = Path(__file__).absolute().parent  # .../unit
_FIXTURES = Path.joinpath(_PACKAGE_DIR, 'fixtures')  # .../unit/fixtures
_HTML = Path.joinpath(_FIXTURES, 'html')  # .../unit/fixtures/html

sample_file = Path('03-30-2020.csv')

raw_cols = ['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key']
lowercased_cols = ['fips', 'admin2', 'province_state', 'country_region', 'last_update', 'lat', 'long_', 'confirmed', 'deaths', 'recovered', 'active', 'combined_key']
necessary_cols = ['fips', 'confirmed', 'deaths']
bins_cols = ['fips', 'confirmed', 'deaths', 'confirmed_bins', 'deaths_bins']
date_cols = ['fips', 'confirmed', 'deaths', 'date']

raw_data = [
    [2282, 'Yakutat', 'Alaska', 'US', '3/30/20 22:52', 59.8909808, -140.3601451, 0, 0, 0, 0, 'Yakutat, Alaska, US'],
    [4025, 'Yavapai', 'Arizona', 'US', '3/30/20 22:52', 34.59933926, -112.5538588, 15, 0, 0, 0, 'Yavapai, Arizona, US'],
    [5149, 'Yell', 'Arkansas', 'US', '3/30/20 22:52', 35.00292371, -93.41171338, 0, 0, 0, 0, 'Yell, Arkansas, US'],
    [2290, 'Yukon-Koyukuk', 'Alaska', 'US', '3/30/20 22:52', 65.50815459, -151.3907387, 0, 0, 0, 0, 'Yukon-Koyukuk, Alaska, US'],
    [4027, 'Yuma', 'Arizona', 'US', '3/30/20 22:52', 32.76895712, -113.9066674, 6, 0, 0, 0, 'Yuma, Arizona, US'],
    [None, None, 'Alberta', 'Canada', '3/30/20 22:58', 53.9333, -116.5765, 661, 3, 0, 0, 'Alberta, Canada'],
    [60000, None, 'American Samoa', 'US', '3/30/20 22:52', -14.271, -170.132, 0, 0, 0, 0, 'American Samoa, US'],
    [None, None, 'Anguilla', 'United Kingdom', '3/30/20 22:52', 18.2206, -63.0686, 2, 0, 0, 2, 'Anguilla, United Kingdom'],
    [None, None, None, 'United Kingdom', '3/30/20 22:52', 55.3781, -3.436, 22141, 1408, 135, 20598, 'United Kingdom'],
    [88888, 'Big Boat', 'Diamond Princess', 'US', '3/30/20 22:52', 0, 0, 49, 0, 0, 0, 'Diamond Princess, US']
]

# Precursor: raw_data
dropna_data = [
    [2282, 'Yakutat', 'Alaska', 'US', '3/30/20 22:52', 59.8909808, -140.3601451, 0, 0, 0, 0, 'Yakutat, Alaska, US'],
    [4025, 'Yavapai', 'Arizona', 'US', '3/30/20 22:52', 34.59933926, -112.5538588, 15, 0, 0, 0, 'Yavapai, Arizona, US'],
    [5149, 'Yell', 'Arkansas', 'US', '3/30/20 22:52', 35.00292371, -93.41171338, 0, 0, 0, 0, 'Yell, Arkansas, US'],
    [2290, 'Yukon-Koyukuk', 'Alaska', 'US', '3/30/20 22:52', 65.50815459, -151.3907387, 0, 0, 0, 0, 'Yukon-Koyukuk, Alaska, US'],
    [4027, 'Yuma', 'Arizona', 'US', '3/30/20 22:52', 32.76895712, -113.9066674, 6, 0, 0, 0, 'Yuma, Arizona, US'],
    [88888, 'Big Boat', 'Diamond Princess', 'US', '3/30/20 22:52', 0, 0, 49, 0, 0, 0, 'Diamond Princess, US']
]

# Precursor: raw_data
us_data = [
    [2282.0, 'Yakutat', 'Alaska', 'US', '3/30/20 22:52', 59.8909808, -140.3601451, 0, 0, 0, 0, 'Yakutat, Alaska, US'],
    [4025.0, 'Yavapai', 'Arizona', 'US', '3/30/20 22:52', 34.59933926, -112.5538588, 15, 0, 0, 0, 'Yavapai, Arizona, US'],
    [5149.0, 'Yell', 'Arkansas', 'US', '3/30/20 22:52', 35.00292371, -93.41171338, 0, 0, 0, 0, 'Yell, Arkansas, US'],
    [2290.0, 'Yukon-Koyukuk', 'Alaska', 'US', '3/30/20 22:52', 65.50815459, -151.3907387, 0, 0, 0, 0, 'Yukon-Koyukuk, Alaska, US'],
    [4027.0, 'Yuma', 'Arizona', 'US', '3/30/20 22:52', 32.76895712, -113.9066674, 6, 0, 0, 0, 'Yuma, Arizona, US'],
    [60000.0, None, 'American Samoa', 'US', '3/30/20 22:52', -14.271, -170.132, 0, 0, 0, 0, 'American Samoa, US'],
    [88888.0, 'Big Boat', 'Diamond Princess', 'US', '3/30/20 22:52', 0, 0, 49, 0, 0, 0, 'Diamond Princess, US']
]

# Precursor: raw_data
neccessarycol_data = [
    [2282, 0, 0],
    [4025, 15, 0],
    [5149, 0, 0],
    [2290, 0, 0],
    [4027, 6, 0],
    [None, 661, 3],
    [60000, 0, 0],
    [None, 2, 0],
    [None, 22141, 1408],
    [88888, 49, 0]
]

# Precursor: raw_data
recognizedfips_data = [
    [2282, 'Yakutat', 'Alaska', 'US', '3/30/20 22:52', 59.8909808, -140.3601451, 0, 0, 0, 0, 'Yakutat, Alaska, US'],
    [4025, 'Yavapai', 'Arizona', 'US', '3/30/20 22:52', 34.59933926, -112.5538588, 15, 0, 0, 0, 'Yavapai, Arizona, US'],
    [5149, 'Yell', 'Arkansas', 'US', '3/30/20 22:52', 35.00292371, -93.41171338, 0, 0, 0, 0, 'Yell, Arkansas, US'],
    [2290, 'Yukon-Koyukuk', 'Alaska', 'US', '3/30/20 22:52', 65.50815459, -151.3907387, 0, 0, 0, 0, 'Yukon-Koyukuk, Alaska, US'],
    [4027, 'Yuma', 'Arizona', 'US', '3/30/20 22:52', 32.76895712, -113.9066674, 6, 0, 0, 0, 'Yuma, Arizona, US'],
    [None, None, 'Alberta', 'Canada', '3/30/20 22:58', 53.9333, -116.5765, 661, 3, 0, 0, 'Alberta, Canada'],
    [None, None, 'Anguilla', 'United Kingdom', '3/30/20 22:52', 18.2206, -63.0686, 2, 0, 0, 2, 'Anguilla, United Kingdom'],
    [None, None, None, 'United Kingdom', '3/30/20 22:52', 55.3781, -3.436, 22141, 1408, 135, 20598, 'United Kingdom']
]

# Precursor: raw_data
leftpaddedfips_data = [
    ['02282', 'Yakutat', 'Alaska', 'US', '3/30/20 22:52', 59.8909808, -140.3601451, 0, 0, 0, 0, 'Yakutat, Alaska, US'],
    ['04025', 'Yavapai', 'Arizona', 'US', '3/30/20 22:52', 34.59933926, -112.5538588, 15, 0, 0, 0, 'Yavapai, Arizona, US'],
    ['05149', 'Yell', 'Arkansas', 'US', '3/30/20 22:52', 35.00292371, -93.41171338, 0, 0, 0, 0, 'Yell, Arkansas, US'],
    ['02290', 'Yukon-Koyukuk', 'Alaska', 'US', '3/30/20 22:52', 65.50815459, -151.3907387, 0, 0, 0, 0, 'Yukon-Koyukuk, Alaska, US'],
    ['04027', 'Yuma', 'Arizona', 'US', '3/30/20 22:52', 32.76895712, -113.9066674, 6, 0, 0, 0, 'Yuma, Arizona, US'],
    ['88888', 'Big Boat', 'Diamond Princess', 'US', '3/30/20 22:52', 0, 0, 49, 0, 0, 0, 'Diamond Princess, US']
]

# Precursor: neccessarycol_data
logbins_data = [
    [2282, 0, 0, '0', '0'],
    [4025, 15, 0, '2', '0'],
    [5149, 0, 0, '0', '0'],
    [2290, 0, 0, '0', '0'],
    [4027, 6, 0, '1', '0'],
    [None, 661, 3, '3', '1'],
    [60000, 0, 0, '0', '0'],
    [None, 2, 0, '1', '0'],
    [None, 22141, 1408, '5', '4'],
    [88888, 49, 0, '2', '0']
]

# Precursor: neccessarycol_data
datecol_data = [
    [2282, 0, 0, '03-30-2020'],
    [4025, 15, 0, '03-30-2020'],
    [5149, 0, 0, '03-30-2020'],
    [2290, 0, 0, '03-30-2020'],
    [4027, 6, 0, '03-30-2020'],
    [None, 661, 3, '03-30-2020'],
    [60000, 0, 0, '03-30-2020'],
    [None, 2, 0, '03-30-2020'],
    [None, 22141, 1408, '03-30-2020'],
    [88888, 49, 0, '03-30-2020']
]

# Expected output DataFrames
raw_df = pd.DataFrame(raw_data, columns=raw_cols)
dropna_df = pd.DataFrame(dropna_data, columns=raw_cols)
lowercasedcols_df = pd.DataFrame(dropna_data, columns=lowercased_cols)
us_df = pd.DataFrame(us_data, columns=lowercased_cols)
neccessarycol_df = pd.DataFrame(neccessarycol_data, columns=necessary_cols)
recognizedfips_df = pd.DataFrame(recognizedfips_data, columns=lowercased_cols)
leftpaddedfips_df = pd.DataFrame(leftpaddedfips_data, columns=lowercased_cols)
logbins_df = pd.DataFrame(logbins_data, columns=bins_cols)
datecol_df = pd.DataFrame(datecol_data, columns=date_cols)

print(neccessarycol_df)
