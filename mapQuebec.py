import folium
import pandas as pd

df = pd.read_excel("popQuebec.xlsx")
#print(df.head(17))

m = folium.Map(location=[53.9073, -68.8623], tiles= "Cartodb Positron", zoom_start=5)
regions = r"quebec_regions.json"

folium.Choropleth(geo_data=regions,
                  data=df,
                  columns=["ID", "Population"],
                  key_on="feature.properties.cartodb_id",
                  fill_color="plasma",
                  fill_opacity=0.5,
                  line_opacity=0.2,
                  legend_name="Population régionale du Québec (2024)",
                  ).add_to(m)

m.save("index.html")