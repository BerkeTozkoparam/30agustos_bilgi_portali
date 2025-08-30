# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# --------------------------
# Sayfa Ayarları
# --------------------------
st.set_page_config(page_title="30 Ağustos Bilgi Portalı", layout="wide")
st.title("🇹🇷 30 Ağustos Zafer Bayramı Bilgi Portalı 🇹🇷")
st.write("Bu portal, 30 Ağustos Zafer Bayramı hakkında bilgi sunar, olayları kronolojik-haritada ve grafiklerle gösterir.")

# --------------------------
# Bilgi ve Grafik Modülü
# --------------------------
st.header("📊 30 Ağustos Olayları ve Şehit Sayısı")

# Olaylar ve şehit sayısı veri seti
events = pd.DataFrame({
    "Olay": ["Büyük Taarruz Başladı", "Afyonkarahisar Zaferi", "30 Ağustos Zafer Bayramı"],
    "Tarih": ["26-08-1922","30-08-1922","30-08-1923"],
    "Sehir": ["Afyonkarahisar","Afyonkarahisar","Ankara"],
    "Sehit_Sayisi": [15000, 20000, 0],
    "Lat": [38.419, 38.759, 39.933],
    "Lon": [30.547, 30.538, 32.859]
})

st.markdown("Aşağıdaki grafik, 30 Ağustos Zaferi sırasında yaşanan olaylar ve şehit sayılarını göstermektedir:")

# Bar grafiği
fig = px.bar(events, x="Olay", y="Sehit_Sayisi", color="Sehir",
             labels={"Sehit_Sayisi":"Şehit Sayısı", "Olay":"Olay"},
             title="30 Ağustos Zaferi Olayları ve Şehit Sayısı")
st.plotly_chart(fig)

# Kısa bilgi listesi
st.markdown("### Olay Bilgileri")
for idx, row in events.iterrows():
    st.markdown(f"**{row['Olay']}** ({row['Tarih']} - {row['Sehir']}): {row['Sehit_Sayisi']} şehit")

# --------------------------
# Kronolojik Harita
# --------------------------
st.header("🗺️ Kronolojik Harita")

map_container = st.container()

with map_container:
    m = folium.Map(location=[39.0, 31.0], zoom_start=6)
    for idx, row in events.iterrows():
        popup_html = f"""
        <b>{row['Olay']}</b><br>
        Tarih: {row['Tarih']}<br>
        Şehir: {row['Sehir']}<br>
        Şehit Sayısı: {row['Sehit_Sayisi']}
        """
        folium.Marker([row["Lat"], row["Lon"]], popup=popup_html).add_to(m)

    st_folium(m, width=700, height=500)

# --------------------------
# Atatürk Resmi ve Anma Mesajı
# --------------------------
st.header("🇹🇷 Mustafa Kemal Atatürk 🇹🇷")
st.image("https://upload.wikimedia.org/wikipedia/commons/1/1b/Atatürk_1925.jpg", width=400)

st.markdown("""
**Rahmet ve Minnetle Anıyoruz.**  
30 Ağustos Zaferi'nde hayatını kaybeden tüm şehitlerimizi saygıyla yad ediyoruz. 🇹🇷
""")
