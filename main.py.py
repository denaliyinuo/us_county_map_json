import pandas as pd

def to_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path = 'json_txt.csv'
df = to_csv(path)

txt = ''

for i in range(len(df)):
    txt_single = df.loc[i,'1']
    txt = txt + txt_single

new_txt_id = txt.split('"id":')
new_txt_fips = txt.split('"fips":"')
new_txt_county = txt.split('"CoState":"')
new_txt_state = txt.split('iso_3166_2')

geoid = []
fips = []
county = []
state = []

for i in range(1,len(new_txt_id)):
    k = new_txt_id[i].split(',"fips":')
    local_geoid = k[0]
    geoid.append(local_geoid)

for i in range(1,len(new_txt_fips)):
    k = new_txt_fips[i]
    local_fips = k[:5]
    fips.append(local_fips)

for i in range(1,len(new_txt_county)):
    k = new_txt_county[i].split(',  ')
    local_county = k[0]
    county.append(local_county)


for i in range(1,len(new_txt_state)):
    local_state = new_txt_state[i][3:5]
    state.append(local_state)

df_new = pd.DataFrame({'fips':fips,'id':geoid,'county':county,'state':state})
df_new = df_new.sort_values('fips')

path = 'us_county_map_id_fips.csv'

df_new.to_csv(path, index = False)
