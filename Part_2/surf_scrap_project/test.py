import surf_scrap

# Test 1 : Lacanau
print("=" * 50)
print("Test 1 : Lacanau")
print("=" * 50)
df1 = surf_scrap.extract_surf_data(
    'https://www.surf-report.com/meteo-surf/lacanau-s1043.html',
    'output/lacanau.csv'
)
print(df1.head())

# Test 2 : Carcans
print("\n" + "=" * 50)
print("Test 2 : Carcans")
print("=" * 50)
df2 = surf_scrap.extract_surf_data(
    'https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html',
    'output/carcans.csv'
)
print(df2.head())

# Test 3 : Moliets
print("\n" + "=" * 50)
print("Test 3 : Moliets")
print("=" * 50)
df3 = surf_scrap.extract_surf_data(
    'https://www.surf-report.com/meteo-surf/moliets-plage-centrale-s102799.html',
    'output/moliets.csv'
)
print(df3.head())