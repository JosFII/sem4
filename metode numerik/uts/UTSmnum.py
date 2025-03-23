import streamlit as st
import base64
import pandas as pd
st.markdown(
'''
<style>
    .stApp {
   background-color: white;
    }
 
       .stWrite,.stMarkdown,.stTextInput,h1, h2, h3, h4, h5, h6 {
            color: purple !important;
        }
</style>
''',
unsafe_allow_html=True
)
st.title("Teknik Iterasi pada Matriks Aljabar: Fast Fourier Transform")
st.write("""dibuat oleh  
         nama: Joseph FIlius H  
         NIM: 20234920002""")
st.header("Flowchart")
st.image("fftfchart.jpg")

st.header("Data: data listrik oleh AECI di amerika dari juli sampai desember")
st.write("data berisi data data yang berhubungan dengan listrik dibagian amerika dimana provider listriknya AECI"
" data diambil dari https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48")
df=pd.read_csv("aeci_BALANCE_2024_Jul_Dec.csv")
df
st.write("""penjelasan variabel  
         - balancing authority: sumber dari listriknya  
         - Data Date : hari data di record  
         - Hour Number: jam data di record  
         - Local Time at End of Hour: hari dan jam data di record  
         - UTC Time at End of Hour: hari dan jam data di record pada waktu utc  
         - Demand Forecast (MW): forecast dari demand listrik  
         - Demand: demand listrik  
         - Net Generation (MW): generasi listrik  
         - Total Interchange (MW): interchange total  
         - Net Generation (MW) from x: listrik yang digenrasi dari sumber x  
         """)

st.subheader("Data Exploration")
df
st.markdown("""berikut kode R untuk line chart demand dan hasilnya \n
         df=read.csv("aeci_BALANCE_2024_Jul_Dec.csv")
        df[,4]=as.POSIXct(df[,4],format = "%m/%d/%Y %H")
        ggplot(df, aes(Local.Time.at.End.of.Hour ,Demand..MW.)) +
        geom_line(color = "green")
""")
st.image("linep.png")
st.write("berikut jumlah data null di setiap kolum")
st.write(df.isnull().sum())
st.write("berikut statistik deskriptif")
st.write(df.describe())


st.subheader("Feature Engineering")
st.write("untuk analisa hanya akan digunakan data demand")
st.markdown(""" berikut menormalisasikan data demand \n 
         df[,7]=scale(df[,7])
""")
st.write("""data demand digunakan karena demand merupakan berapa banyak listrik yang diperlukan, dan hal tersebut biasanya 
         bergantung pada jam hari karena demand biasanya naik pada waktu dimana orang banyak menggunakan listrik. 
         normalisasi dilakukan supaya hasil analisa tidak dipengaruhi dengan angka yang terlalu besar/kecil dari data """)

st.subheader("Fast Fourier Transform")
st.markdown(""" berikut kode untuk melakukan FFT di R\n 
                ffft=fft(df[,7])
            """ )
st.markdown(""" sekarang akan dibuat grafik untuk hasil dari FFT \n 
            magnamon=Mod(ffft)
            N = length(ffft)
            half_N= round(N / 2)
            freq =seq(0, 0.5, length.out = half_N)  
            magnamon = magnamon [1:half_N]

            dfft =data.frame(freq,magnamon)

            ggplot(dfft, aes(x = freq, y = magnamon)) +
            geom_line(color = "blue") +
            labs(x = "Frequency",
                y = "Amplitude")

""")
st.image("gafft.png")
st.write("""Dari grafik ini bisa di lihat bahwa dari data, terdapat tiga frequency yang dominan didalam data.
Jadi dapat dibilang terdapat tiga factor yang dominan dalam mempengaruhi nilai dan varians demand Listrik.
""")

st.subheader("Evaluation and Discussion")
st.write("""hasil analisa: jadi didapatakan bahwa terdapat 3 frequensi yang distinct dari data demand listrik, jadi dapat 
         diartikan sebagai terdapat tiga faktor yang mempengaruhi nilai dan varians dari data demand.""")
st.write("""kelebihan:   
         1. FFT jauh lebih cepat dari DFT  
         2. melihat suatu data time series di dimesni frekuensi dapat memberi pengertian yang lebih dalam tentang data   
         3. FFT memiliki banyak aplikasi dalam bidang audio dan telekomunikasi   """)
st.write("""keterbatasan:  
         1. FFT hanya dapat menganalisa signal secara diskrit  
         2. FFT kurang akurat jika digunakan pada data yang tidak stationer   
         3. Jika data terlalu sedikit atau singal terlalu pendek maka hasil FFT akan kurang akurat  """)


st.write("""Kesimpulan: jadi fft berguna untuk melihat frequensi apa saja yang terdapat pada data time series, hal tersebut sangat berguna
         untuk analisa di berbagai bidang akan tetapi karena keterbatasan kurang berguna pada bidang yang lain.""")