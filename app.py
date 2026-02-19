import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Sokhna Mame Diarra Thiam", page_icon="📄", layout="wide")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    /* Fond de la zone principale (70%) en gris */
    .stApp {
        background-color: #E0E0E0;
    }
    
    /* Sidebar (30%) en noir avec texte blanc */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
        color: white;
    }
    
    /* Ajustement des textes dans la sidebar pour qu'ils soient lisibles */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
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

# --- SIDEBAR (SECTION NOIRE - 30%) ---
with st.sidebar:
    [span_1](start_span)st.title("Sokhna Mame Diarra Thiam")[span_1](end_span)
    st.write("---")
    
    st.subheader("Contact")
    [span_2](start_span)st.write("📧 [soxnajaarah490@gmail.com](mailto:soxnajaarah490@gmail.com)")[span_2](end_span)
    [span_3](start_span)st.write("📍 Parcelles Assainies Unité 21, Dakar")[span_3](end_span)
    
    st.write("---")
    st.subheader("Langues")
    [span_4](start_span)st.write("• Français")[span_4](end_span)
    [span_5](start_span)st.write("• Anglais")[span_5](end_span)

    st.write("---")
    st.subheader("Centres d'intérêt")
    [span_6](start_span)st.write("🏀 Basket")[span_6](end_span)
    [span_7](start_span)st.write("🍳 Cuisine")[span_7](end_span)
    [span_8](start_span)st.write("🎶 Musique")[span_8](end_span)
    [span_9](start_span)st.write("📚 Lecture")[span_9](end_span)

# --- ZONE PRINCIPALE (SECTION GRISE - 70%) ---

# En-tête
[span_10](start_span)st.title("Étudiante en Géomatique")[span_10](end_span)
st.write("---")

# Profil
st.header("Profil")
st.write("""
Professionnelle polyvalente et motivée, ayant une forte capacité d'adaptation 
et un excellent sens de l'organisation, prête à relever de nouveaux défis 
et à contribuer activement au succès de l'équipe.
[span_11](start_span)""")[span_11](end_span)

# Formation
st.header("Formation")
col_f1, col_f2 = st.columns([3, 1])
with col_f1:
    st.markdown("**Deuxième Année Géomatique**") 
    [span_12](start_span)st.write("Centre d'Entreprenariat et de Développement Technique (G15), Dakar")[span_12](end_span)
with col_f2:
    st.write("2024 - Présent")

col_f3, col_f4 = st.columns([3, 1])
with col_f3:
    [span_13](start_span)st.markdown("**Baccalauréat Scientifique S2**")[span_13](end_span)
    [span_14](start_span)st.write("Lycée des Parcelles Assainies (Ex Djinda Thiam)")[span_14](end_span)
with col_f4:
    [span_15](start_span)st.write("2022 - 2023")[span_15](end_span)

# Expérience
st.header("Expérience Professionnelle")
exp_col1, exp_col2 = st.columns([3, 1])
with exp_col1:
    [span_16](start_span)st.markdown("**Gérante Multiservice**")[span_16](end_span)
    [span_17](start_span)st.write("Thiam et FRERES, Dakar")[span_17](end_span)
with exp_col2:
    [span_18](start_span)st.write("Juin 2025 - Présent")[span_18](end_span)

# Compétences techniques
st.header("Compétences & Outils")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Soft Skills")
    [span_19](start_span)st.write("• Gestion des opérations")[span_19](end_span)
    [span_20](start_span)st.write("• Sens de l'organisation")[span_20](end_span)
    [span_21](start_span)st.write("• Capacité d'adaptation")[span_21](end_span)

with c2:
    st.subheader("Logiciels")
    [span_22](start_span)st.write("• SIG: QGIS, ARCGIS")[span_22](end_span)
    [span_23](start_span)st.write("• CAO: AUTOCAD")[span_23](end_span)
    [span_24](start_span)st.write("• Bureautique: Word, Excel")[span_24](end_span)
