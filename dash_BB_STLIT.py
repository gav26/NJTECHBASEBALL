#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:15:31 2022

@author: grantvurpillat
"""
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime
import pandas as pd

master_csv = pd.read_csv(r'/Users/grantvurpillat/Desktop/bellarmine_csv.csv')

st.title('BB Stat Dashboard')

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)


# FPS
unused_columnsFPS = master_csv.columns.difference(set(['count']).union(set(['Strike?'])).union(set({'result'})))
FPS = master_csv.drop(unused_columnsFPS, axis=1)
pivot_tableFPS = FPS.pivot_table(
    index=['count'],
    columns=['Strike?'],
    values=['result'],
    aggfunc={'result': ['count']}
)

FPS_pivot = pivot_tableFPS.reset_index()

# Filtered count in fallworldv2_csv_pivot
FPS_pivot = FPS_pivot[FPS_pivot['count'].str.contains('0-0', na=False)]
FPS_pivot["sum"] = FPS_pivot.sum(axis=1)

      
col1.metric('FPS%',value = round((FPS_pivot.iloc[0,2]/FPS_pivot['sum']),2)*100)


# Pivoted fallworldv2_csv into df2
unused_columnsMD = master_csv.columns.difference(set([]).union(set(['pitch_type'])).union(set({'miss__dist'})))
MD = master_csv.drop(unused_columnsMD, axis=1)
pivot_tableMD = MD.pivot_table(
    columns=['pitch_type'],
    values=['miss__dist'],
    aggfunc={'miss__dist': ['median']}
)

#MD_pivot = pivot_tableMD.reset_index()



col2.metric('MD FB',value = round(pivot_tableMD.FB,3))
col3.metric('MD CB',value = round(pivot_tableMD.CB,3)) #inches)


# Pivoted fallworldv2_csv into df2
unused_columnsBB = master_csv.columns.difference(set(['result_of_ab']).union(set([])).union(set({'result_of_ab'})))
BB = master_csv.drop(unused_columnsBB, axis=1)
pivot_tableBB = BB.pivot_table(
    index=['result_of_ab'],
    values=['result_of_ab'],
    aggfunc={'result_of_ab': ['count']}
)

col4.metric('BB%',value = round(pivot_tableBB.loc['walk']/pivot_tableBB.sum(),3)*100)


col5.metric('K%',value = round(pivot_tableBB.loc['strikeout']/pivot_tableBB.sum(),3)*100)

# Filtered Pitch_type in fallworldv2_csv
col4.metric('k/9', value =(pivot_tableBB.loc['strikeout']*9)/((pivot_tableBB.loc['strikeout']+pivot_tableBB.loc['BIP_out'])/3))
            
          

# pitch mix
unused_columnsPM = master_csv.columns.difference(set(['pitch_type']).union(set([])).union(set({'result'})))
PM = master_csv.drop(unused_columnsPM, axis=1)
pivot_tablePM = PM.pivot_table(
    index=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)

#fallworldv2_csv_pivot = pivot_table.reset_index()


col6.metric('FB%',(pivot_tablePM.loc['FB']/pivot_tablePM.sum())*100)



# Pivoted fallworldv2_csv into df2
unused_columns2k = master_csv.columns.difference(set(['count']).union(set(['result_of_ab'])).union(set({'result_of_ab'})))
strikes2 = master_csv.drop(unused_columns2k, axis=1)
pivot_table2k = strikes2.pivot_table(
    index=['count'],
    columns=['result_of_ab'],
    values=['result_of_ab'],
    aggfunc={'result_of_ab': ['count']}
)
twok_csv_pivot = pivot_table2k.reset_index()
twok_csv_pivot = twok_csv_pivot[(twok_csv_pivot['count'].str.contains('-2', na=False))]

# Pivoted fallworldv2_csv into df2
unused_columns = master_csv.columns.difference(set(['count']).union(set([])).union(set({'result_of_ab'})))
tmp_df = master_csv.drop(unused_columns, axis=1)
pivot_table = tmp_df.pivot_table(
    index=['count'],
    values=['result_of_ab'],
    aggfunc={'result_of_ab': ['count']}
)


# Pivoted fallworldv2_csv into df2
csv_csw = master_csv[master_csv['pitch_type'] == 'FB']

unused_columnCSW = csv_csw.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
CSW = csv_csw.drop(unused_columnCSW, axis=1)
pivot_tableCSW = CSW.pivot_table(
    index=['result'],
    columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)

# Pivoted fallworldv2_csv into df2


#col7.metric('FB CSW%',value = round((pivot_tableCSW.loc['called_strike']+pivot_tableCSW.loc['swing_miss']
                                #     )/pivot_tableCSW.sum(),3)*100)


#round((pivot_tableCSW.loc['called_strike']+pivot_tableCSW.loc['swing_miss']
#                                     )/pivot_tableCSW.sum(),3)*100

#col7.metric('punchem w/ 2',
        
#twok_csv_pivot.loc['strikeout']/


csv_cswCB = master_csv[master_csv['pitch_type'] == 'CB']

unused_columnCSW = csv_cswCB.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
CSW = csv_cswCB.drop(unused_columnCSW, axis=1)
pivot_tableCSW = CSW.pivot_table(
    index=['result'],
    columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)


col7.metric('CB CSW%',value = round((pivot_tableCSW.loc['called_strike']+pivot_tableCSW.loc['swing_miss'])/pivot_tableCSW.sum(),3)*100)



z_zone_csv = master_csv[((master_csv['actual_x'] >= -10) & (master_csv['actual_x'] <= 10))&((master_csv['actual_y'] >= 13) & (master_csv['actual_y'] <= 37))]

csv_z_zone_FB = z_zone_csv[z_zone_csv['pitch_type'] == 'FB']
# Filtered actual_y3 in fallworldv2_csv
#z_zone_csv = master_csv[((master_csv['actual_y'] >= 13) & (master_csv['actual_y'] <= 37))]

# Pivoted fallworldv2_csv into df5
unused_columns_zzone = csv_z_zone_FB.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
z_zone = csv_z_zone_FB.drop(unused_columns_zzone, axis=1)
pivot_table_z_zoneFB = z_zone.pivot_table(
    index=['result'],
    columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)


#z swing %
#col8.metric('FB Z swing%',value =round(((pivot_table_z_zoneFB.sum()-pivot_table_z_zoneFB.loc['called_strike'])/pivot_table_z_zoneFB.sum()),3)*100)



# z contact %
#col8.metric('FB Z contact%',value=round((((pivot_table_z_zoneFB.sum()-pivot_table_z_zoneFB.loc['called_strike'])-pivot_table_z_zoneFB.loc['swing_miss']
                                         # )/(pivot_table_z_zoneFB.sum()-pivot_table_z_zoneFB.loc['called_strike'])),3)*100)



#FB z zone 
csv_z_zone_CB = z_zone_csv[z_zone_csv['pitch_type'] == 'CB']
# Filtered actual_y3 in fallworldv2_csv
#z_zone_csv = master_csv[((master_csv['actual_y'] >= 13) & (master_csv['actual_y'] <= 37))]

# Pivoted fallworldv2_csv into df5
unused_columns_zzone = csv_z_zone_CB.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
z_zone = csv_z_zone_CB.drop(unused_columns_zzone, axis=1)
pivot_table_z_zone = z_zone.pivot_table(
    index=['result'],
    columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)


#z swing %
#col8.metric('CB Z swing%',value =round(((pivot_table_z_zone.sum()-pivot_table_z_zone.loc['called_strike'])/pivot_table_z_zone.sum()),3)*100)

#z contact CB
#col8.metric('CB Z contact%',value=round((((pivot_table_z_zone.sum()-pivot_table_z_zone.loc['called_strike'])-pivot_table_z_zone.loc['swing_miss'])/(pivot_table_z_zone.sum()-pivot_table_z_zone.loc['called_strike'])),3)*100)


csv_veloFB = master_csv[master_csv['pitch_type'] == 'FB']

unused_columns_velo = csv_veloFB.columns.difference(set([]).union(set(['pitch_type'])).union(set({'velo'})))
velo = csv_veloFB.drop(unused_columns_velo, axis=1)
pivot_table_velo = velo.pivot_table(
    columns=['pitch_type'],
    values=['velo'],
    aggfunc={'velo': ['mean']}
)

#col2.metric('avgFB velo',pivot_table_velo)

csv_veloCB = master_csv[master_csv['pitch_type'] == 'CB']

unused_columns_velo = csv_veloCB.columns.difference(set([]).union(set(['pitch_type'])).union(set({'velo'})))
velo = csv_veloCB.drop(unused_columns_velo, axis=1)
pivot_table_velo = velo.pivot_table(
    columns=['pitch_type'],
    values=['velo'],
    aggfunc={'velo': ['mean']}
)

#col3.metric('avgCB velo',pivot_table_velo)









o_zone_csv = master_csv[((master_csv['actual_x'] >= 10) | (master_csv['actual_x'] <= -10) | (master_csv['actual_y'] >= 37) | (master_csv['actual_y'] <= 13))]

csv_o_zone_FB = o_zone_csv[o_zone_csv['pitch_type'] == 'FB']
# Pivoted fallworldv2 into df2
#result by pitch type
unused_columns_oz = csv_o_zone_FB.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
o_zone = csv_o_zone_FB.drop(unused_columns_oz, axis=1)
pivot_table_oz = o_zone.pivot_table(
    index=['result'],
    #columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
    
)

#o swing %
#col9.metric('FB O-Swing%',value = round(((pivot_table_oz.sum()-pivot_table_oz.loc['ball'])/pivot_table_oz.sum()),2)*100)


# O contact %
#col9.metric('FB O-Contact%',value =((pivot_table_oz.sum()-pivot_table_oz.loc['ball']-pivot_table_oz.loc['swing_miss']
#                                     )/(pivot_table_oz.sum()-pivot_table_oz.loc['ball'])*100))





csv_o_zone_CB = o_zone_csv[o_zone_csv['pitch_type'] == 'CB']
# Pivoted fallworldv2 into df2
#result by pitch type
unused_columns_oz = csv_o_zone_CB.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
o_zone = csv_o_zone_CB.drop(unused_columns_oz, axis=1)
pivot_table_oz = o_zone.pivot_table(
    index=['result'],
    #columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
    
)

#o swing %
#col9.metric('CB O-Swing%',value = round(((pivot_table_oz.sum()-pivot_table_oz.loc['ball'])/pivot_table_oz.sum()),2)*100)


# O contact %
#col9.metric('CB O-Contact%',value =round(((pivot_table_oz.sum()-pivot_table_oz.loc['ball']-pivot_table_oz.loc['swing_miss'])/(pivot_table_oz.sum()-pivot_table_oz.loc['ball'])),2)*100)




zone = z_zone_csv.drop(unused_columns_zzone, axis=1)

pivot_table_zz = zone.pivot_table(
    index=['result'],
    #columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)
unused_columns_results = master_csv.columns.difference(set(['result']).union(set([])).union(set({'count'})))
results = master_csv.drop(unused_columns_results, axis=1)
pivot_table_R = results.pivot_table(
    index=['result'],
    values=['count'],
    aggfunc={'count': ['count']}
)


#fallworldv2_csv_pivot = pivot_table.reset_index()

#col1.metric('Zone%',value = round((pivot_table_zz.sum()/master_csv['PC'].count()),2)*100)


# Pivoted fallworldv2_csv into df2
#csv_results = master_csv[master_csv['pitch_type'] == 'FB']

unused_columnswstr = master_csv.columns.difference(set(['result']).union(set(['pitch_type'])).union(set({'result'})))
swstr = master_csv.drop(unused_columnswstr, axis=1)
pivot_tableswstr = swstr.pivot_table(
    index=['result'],
   # columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)


col5.metric('swstr%',value = round(pivot_tableswstr.loc['swing_miss']/pivot_tableswstr.sum(),3)*100)

col6.metric('whiff%',value = round((pivot_tableswstr.loc['swing_miss'])/(pivot_tableswstr.sum()-pivot_tableswstr.loc['called_strike']-pivot_tableswstr.loc['ball']),3)*100)

master_FB = master_csv[master_csv['pitch_type'] == 'FB']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-24, 24])
ax.set_ylim([0, 80])
ax.scatter(master_FB.actual_x,master_FB.actual_y)
fig.set_figheight(15)
fig.set_figwidth(9)
ax.vlines(10, 14, 37) 
ax.vlines(-10, 14, 37)
ax.hlines(14, -10, 10) 
ax.hlines(37, 10, -10)
ax.vlines(-14.5, 0, 37)
ax.vlines(14.5, 0, 37) 
ax.hlines(65, -14.5, -24) 
ax.hlines(65, 14.5, 24)
ax.hlines(2, -8.5, 8.5)  
plt.gca().set_aspect('equal', adjustable='box')          

#plt.show()
with st.expander("FB"):
    st.pyplot(fig)





master_CB = master_csv[master_csv['pitch_type'] == 'CB']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-24, 24])
ax.set_ylim([0, 80])
ax.scatter(master_CB.actual_x,master_CB.actual_y)
fig.set_figheight(15)
fig.set_figwidth(9)
ax.vlines(10, 14, 37) 
ax.vlines(-10, 14, 37)
ax.hlines(14, -10, 10) 
ax.hlines(37, 10, -10)
ax.vlines(-14.5, 0, 37)
ax.vlines(14.5, 0, 37) 
ax.hlines(65, -14.5, -24) 
ax.hlines(65, 14.5, 24)
ax.hlines(2, -8.5, 8.5)  
plt.gca().set_aspect('equal', adjustable='box')  

with st.expander("CB"):
    st.pyplot(fig)


col1, col2, col3, col4 = st.columns(4)

col1.dataframe(pivot_table_R)

unused_columnsBIPS = master_csv.columns.difference(set(['BIP_speed']).union(set([])).union(set({'BIP_type'})))
BIPS = master_csv.drop(unused_columnsBIPS, axis=1)
pivot_tableBIPS = BIPS.pivot_table(
    index=['BIP_speed'],
    values=['BIP_type'],
    aggfunc={'BIP_type': ['count']}
)
col2.dataframe(pivot_tableBIPS)

st.dataframe(master_csv)


unused_columnsPPCM = master_csv.columns.difference(set(['pitch_type']).union(set(['prev_pitch'])).union(set({'pitch_type'})))
PPCM = master_csv.drop(unused_columnsPPCM, axis=1)
pivot_tablePPCM = PPCM.pivot_table(
    index=['pitch_type'],
    columns=['prev_pitch'],
    values=['pitch_type'],
    aggfunc={'pitch_type': ['count']}
)


col3.dataframe(pivot_tablePPCM)
#/FPS_pivot.sum()

unused_columnsLR = master_csv.columns.difference(set(['L_R']).union(set(['result'])).union(set({'result'})))
LR = master_csv.drop(unused_columnsLR, axis=1)
pivot_tableLR = LR.pivot_table(
    index=['result'],
    columns=['L_R'],
    values=['result'],
    aggfunc={'result': ['count']}
)
st.table(pivot_tableLR/pivot_tableLR.sum())
st.dataframe(pivot_tableLR)
#FPS_pivot.sum()
col1, col2 =st.columns(2)

unused_columnsPT = master_csv.columns.difference(set(['pitch_type']).union(set(['result'])).union(set({'result'})))
PT = master_csv.drop(unused_columnsPT, axis=1)
pivot_tablePT = PT.pivot_table(
    index=['result'],
    columns=['pitch_type'],
    values=['result'],
    aggfunc={'result': ['count']}
)
st.table(pivot_tableLR/pivot_tableLR.sum())
st.dataframe(pivot_tableLR)




st.dataframe(pivot_tablePT)

import plotly.graph_objects as go
fig = go.Figure()

# Add the histogram traces to the figure
for column_header in ['miss__dist']:
    fig.add_trace(go.Histogram(x=master_CB[column_header], name=str(column_header)))
# Update the layout
# See Plotly documentation for customizations: https://plotly.com/python/reference/histogram/
fig.update_layout(
	xaxis_title=str(0),
    title="miss__dist CB frequencies",
    barmode='group'
)
fig.show(renderer="iframe")

col1.plotly_chart(fig)



fig = go.Figure()

# Add the histogram traces to the figure
for column_header in ['miss__dist']:
    fig.add_trace(go.Histogram(x=master_FB[column_header],nbinsx=6, name=str(column_header)))
# Update the layout
# See Plotly documentation for customizations: https://plotly.com/python/reference/histogram/
fig.update_layout(
	xaxis_title=str(0),
    title="miss__dist FB frequencies",
    barmode='group',
    bargap=0.2
)
fig.show(renderer="iframe")

col2.plotly_chart(fig)



fig = go.Figure()

# Add the histogram traces to the figure
for column_header in ['miss__dist']:
    fig.add_trace(go.Histogram(x=master_CB[column_header],bingroup ='pitch_type',opacity =.7, name='CB'))
    fig.add_trace(go.Histogram(x=master_FB[column_header],bingroup ='pitch_type', opacity =.4,name='FB'))
# Update the layout
# See Plotly documentation for customizations: https://plotly.com/python/reference/histogram/
fig.update_layout(
	xaxis_title=str(0),
    title="miss__dist frequencies",
    barmode='overlay',
    bargap=0.2
)
fig.show(renderer="iframe")

st.plotly_chart(fig)


#df_1_22_22command_data_csv = pd.read_csv(r'/Users/grantvurpillat/Desktop/baseball /1-22-22command_data.csv')
# Import plotly and create a figure
#import plotly.graph_objects as go
#fig = go.Figure()



# Add the scatter traces to the figure
#for column_header in ['x_abs']:
 ##      x=df_1_22_22command_data_csv[column_header], 
   #     mode='markers',
  #    name=str(column_header)
  # ))

# Update the layout
# See Plotly documentation for cutomizations: https://plotly.com/python/reference/scatter/
#fig.update_layout(
 #   xaxis_title="x_abs",
  #  yaxis_title="index",
   # title="x_abs scatter plot",
#)
#fig.show(renderer="iframe")


#st.plotly_chart(fig)


