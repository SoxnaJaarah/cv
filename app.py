import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Sokhna Mame Diarra Thiam", page_icon="📄")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stHeader {
        color: #2e4053;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (INFOS DE CONTACT) ---
with st.sidebar:
    st.title("Contact")
    st.write("📧 [soxnajaarab490@gmail.com](mailto:soxnajaarab490@gmail.com)")
    st.write("📍 Parcelles Assainies Unité 21, Dakar")
    
    st.write("---")
    st.subheader("Langues")
    st.write("- Français")
    st.write("- Anglais")

    st.subheader("Centres d'intérêt")
    st.write("🏀 Basket | 🍳 Cuisine | 🎶 Musique | 📚 Lecture")

# --- EN-TÊTE ---
st.title("Sokhna Mame Diarra Thiam")
st.subheader("Étudiante en Géomatique & Professionnelle Polyvalente")
st.write("---")

# --- PROFIL ---
st.header("Profil")
st.info("""
Professionnelle polyvalente et motivée, ayant une forte capacité d'adaptation 
et un excellent sens de l'organisation, prête à relever de nouveaux défis 
et à contribuer activement au succès de l'équipe.
""")

# --- FORMATION ---
st.header("Formation")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Deuxième Année Géomatique**")
    st.write("Centre d'Entreprenariat et de Développement Technique (G15), Dakar")
with col2:
    st.write("Oct. 2024 - Présent")

col3, col4 = st.columns([3, 1])
with col3:
    st.markdown("**Baccalauréat Scientifique S2**")
    st.write("Lycée des Parcelles Assainies (Ex Djinda Thiam)")
with col4:
    st.write("2022 - 2023")

# --- EXPÉRIENCE PROFESSIONNELLE ---
st.header("Expérience Professionnelle")
exp_col1, exp_col2 = st.columns([3, 1])
with exp_col1:
    st.markdown("**Gérante Multiservice**")
    st.write("Thiam et FRERES, Dakar")
with exp_col2:
    st.write("Juin 2025 - Présent")

# --- COMPÉTENCES ---
st.header("Compétences & Outils")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Soft Skills")
    st.write("- Gestion des opérations")
    st.write("- Sens de l'organisation")
    st.write("- Capacité d'adaptation")

with c2:
    st.subheader("Logiciels")
    st.write("- SIG: QGIS, ARCGIS")
    st.write("- CAO: AUTOCAD")
    st.write("- Bureautique: Word, Excel")
