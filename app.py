import streamlit as st

# 1. Configuration de la page
st.set_page_config(
    page_title="CV - Sokhna Mame Diarra Thiam", 
    page_icon="📄", 
    layout="wide"
)

# 2. STYLE CSS PERSONNALISÉ
st.markdown("""
    <style>
    /* Fond de la zone principale en gris clair */
    .stApp {
        background-color: #E0E0E0;
    }
    
    /* Sidebar en noir avec texte blanc */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
        color: white;
    }
    
    /* Forcer la couleur blanche pour tous les éléments de la sidebar */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* Style des titres dans la zone grise */
    h1, h2, h3 {
        color: #2E4053;
    }
    
    /* Séparateur horizontal */
    hr {
        border: 1px solid #2E4053;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (SECTION NOIRE - 30%)
with st.sidebar:
    st.title("Sokhna Mame Diarra Thiam")
    st.write("---")
    
    st.subheader("Contact")
    st.write("📧 [soxnajaarah490@gmail.com](mailto:soxnajaarah490@gmail.com)")
    st.write("📍 Parcelles Assainies Unité 21, Dakar")
    
    st.write("---")
    st.subheader("Langues")
    st.write("• Français")
    st.write("• Anglais")

    st.write("---")
    st.subheader("Centres d'intérêt")
    st.write("🏀 Basket")
    st.write("🍳 Cuisine")
    st.write("🎶 Musique")
    st.write("📚 Lecture")

# 4. ZONE PRINCIPALE (SECTION GRISE - 70%)

# En-tête
st.title("Étudiante en Géomatique")
st.write("---")

# Profil
st.header("Profil")
st.write("""
Professionnelle polyvalente et motivée, ayant une forte capacité d'adaptation 
et un excellent sens de l'organisation, prête à relever de nouveaux défis 
et à contribuer activement au succès de l'équipe.
""")

# Formation
st.header("Formation")
col_f1, col_f2 = st.columns([3, 1])
with col_f1:
    st.markdown("**Deuxième Année Géomatique**") 
    st.write("Centre d'Entreprenariat et de Développement Technique (G15), Dakar")
with col_f2:
    st.write("2024 - Présent")

col_f3, col_f4 = st.columns([3, 1])
with col_f3:
    st.markdown("**Baccalauréat Scientifique S2**")
    st.write("Lycée des Parcelles Assainies (Ex Djinda Thiam)")
with col_f4:
    st.write("2022 - 2023")

# Expérience
st.header("Expérience Professionnelle")
exp_col1, exp_col2 = st.columns([3, 1])
with exp_col1:
    st.markdown("**Gérante Multiservice**")
    st.write("Thiam et FRERES, Dakar")
with exp_col2:
    st.write("Juin 2024 - Présent")

# Compétences techniques
st.header("Compétences & Outils")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Soft Skills")
    st.write("• Gestion des opérations")
    st.write("• Sens de l'organisation")
    st.write("• Capacité d'adaptation")

with c2:
    st.subheader("Logiciels")
    st.write("• SIG: QGIS, ArcGIS")
    st.write("• CAO: AutoCAD")
    st.write("• Bureautique: Word, Excel")
