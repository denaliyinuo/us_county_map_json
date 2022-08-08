# us_county_map_json

![image](/images/county_map_example.jpeg)

This project's aim is to provide Power BI users with a US county map json file, along with every US counties' corresponding id number, which can be used to properly map US county data in Power BI.

# Suumary of Repo Files

* geoid_fips.csv

This csv file includes all 3143 US counties, and their corresponding FIPS, state abbreviation, and Power BI id number. The id number is specific to the json file in this repo, and is useful for generating a US county shape map.

github_albersusa.json

This json file is a US county map of all 50 US states and DC. The geoid_fips.csv file includes every US counties' id number, which is useful for mapping US county data in Power BI.

main.py

This python file was used to generate the information in the geoid_fips.csv file.

json_txt.csv

This csv file was used to upload the json file contents into the main.py file to extract the useful information for this project.
