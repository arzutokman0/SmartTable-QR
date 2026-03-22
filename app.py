import streamlit as st
import time

# Sayfa Yapılandırması
st.set_page_config(page_title="SmartTable - Gurme Deneyimi", page_icon="🍴", layout="wide")

# 1. DİNAMİK MASA NUMARASI (URL'den okur: ?masa=12)
query_params = st.query_params
masa_no = query_params.get("masa", "Bilinmiyor")

# Başlık Kısmı
st.title(f"🍽️ SmartTable Gurme - Masa {masa_no}")
st.markdown("*Şehrin en iyi lezzet durağında dijital asistanınız devrede.*")

# 2. ZENGİNLEŞTİRİLMİŞ MENÜ VERİSİ
menu = {
    "🥗 Başlangıçlar & Salatalar": [
        {"ad": "🥣 Günün Sıcacık Çorbası", "fiyat": "85 TL"},
        {"ad": "🥙 Pastırmalı Sıcak Humus", "fiyat": "145 TL"},
        {"ad": "🥗 Çıtır Tavuklu Sezar Salata", "fiyat": "190 TL"},
        {"ad": "🧀 İtalyan Peynir Tabağı", "fiyat": "240 TL"},
        {"ad": "🥑 Avokadolu Karides Kokteyl", "fiyat": "210 TL"}
    ],
    "🥩 Gurme Ana Yemekler": [
        {"ad": "🍔 Trüflü Mantarlı Burger", "fiyat": "310 TL"},
        {"ad": "🍕 Odun Ateşinde Pizza Mix", "fiyat": "285 TL"},
        {"ad": "🍝 Deniz Mahsullü Linguine", "fiyat": "260 TL"},
        {"ad": "🥩 Lokum Bonfile (250g)", "fiyat": "520 TL"},
        {"ad": "🍣 Özel Sushi Set (12 Parça)", "fiyat": "450 TL"},
        {"ad": "🍗 Köri Soslu Tavuk Dünyası", "fiyat": "225 TL"}
    ],
    "🍰 Tatlılar & İçecekler": [
        {"ad": "🍰 Orman Meyveli Cheesecake", "fiyat": "155 TL"},
        {"ad": "🍮 Akışkan Belçika Çikolatalı Sufle", "fiyat": "145 TL"},
        {"ad": "🥤 Taze Sıkılmış Portakal Suyu", "fiyat": "75 TL"},
        {"ad": "☕ Caramel Macchiato", "fiyat": "95 TL"},
        {"ad": "🍵 Yaseminli Yeşil Çay", "fiyat": "70 TL"}
    ]
}

# Menü Görselleştirme (3 Kolonlu Yapı)
st.divider()
cols = st.columns(3)

for i, (kategori, urunler) in enumerate(menu.items()):
    with cols[i]:
        st.subheader(kategori)
        for urun in urunler:
            st.write(f"**{urun['ad']}**")
            st.caption(f"Fiyat: {urun['fiyat']}")
            st.write("---")

# 3. YAN MENÜ - HIZLI SERVİS (Sidebar)
st.sidebar.header("🛎️ Müşteri Hizmetleri")
if st.sidebar.button("🙋‍♂️ Garson Çağır"):
    st.toast("Garsonumuza haber verildi!", icon="🔔")
    with open("talepler.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} | Masa: {masa_no} | İşlem: Garson Çağırdı\n")

if st.sidebar.button("🧾 Hesap İste"):
    st.toast("Hesabınız hazırlanıyor...", icon="💰")
    with open("talepler.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} | Masa: {masa_no} | İşlem: Hesap İstedi\n")

# 4. PUANLAMA VE YORUM SİSTEMİ
st.divider()
st.subheader("⭐ Deneyiminizi Paylaşın")
c1, c2 = st.columns([1, 2])

with c1:
    puan = st.select_slider("Bizi Puanlayın", 
                            options=["Çok Kötü", "Zayıf", "Orta", "İyi", "Mükemmel"], 
                            value="Mükemmel")

with c2:
    yorum = st.text_area("Görüş ve Önerileriniz", placeholder="Yemekler nasıldı? Servisten memnun kaldınız mı?")

if st.button("Değerlendirmeyi Kaydet"):
    if yorum: # Boş yorum gönderilmesin diye kontrol
        with open("talepler.txt", "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%H:%M:%S')} | Masa: {masa_no} | Puan: {puan} | Yorum: {yorum}\n")
        st.balloons()
        st.success("Harika! Geri bildiriminiz başarıyla şefimize iletildi.")
    else:
        st.warning("Lütfen bir yorum yazın.")

# 5. YÖNETİCİ PANELİ (GİZLİ)
st.write("## ") # Boşluk
with st.expander("⚙️ İşletme Paneli (Yalnızca Personel)"):
    st.write("### 📢 Gelen Son Talepler ve Yorumlar")
    try:
        with open("talepler.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in reversed(lines[-15:]): # Son 15 hareketi listeler
                st.text(line.strip())
    except FileNotFoundError:
        st.write("Henüz bir işlem kaydı bulunmuyor.")
