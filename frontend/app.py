import streamlit as st
import requests
import json

st.set_page_config(page_title="PreSalesAI", layout="wide")

st.title("🤖 PreSalesAI - Assistant Pré-ventes")

# Configuration
API_URL = "http://localhost:8000"

# Sidebar navigation (sans Estimation)
page = st.sidebar.radio("Navigation", ["🏠 Accueil", "📋 Plan de Projet", "📤 Upload Documents"])

if page == "🏠 Accueil":
    st.markdown("""
    ## Bienvenue sur PreSalesAI !
    
    Ce système vous aide à :
    - ✅ Créer des plans de projet MS Project
    - ✅ Indexer vos documents historiques
    
    ### Comment ça marche ?
    1. Uploadez vos documents historiques
    2. Ajoutez vos tâches avec durées et dépendances
    3. Téléchargez votre fichier XML MS Project
    """)

elif page == "📋 Plan de Projet":
    st.header("Générer un Plan de Projet MS Project")
    
    with st.form("project_form"):
        project_name = st.text_input("Nom du projet", "Mon Projet")
        start_date = st.date_input("Date de début")
        
        st.subheader("Tâches")
        task_count = st.number_input("Nombre de tâches", min_value=1, max_value=20, value=3)
        
        tasks = []
        for i in range(task_count):
            with st.expander(f"Tâche {i+1}"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input(f"Nom", key=f"name_{i}")
                    duration = st.number_input(f"Durée (jours)", min_value=1, value=5, key=f"dur_{i}")
                with col2:
                    resources = st.text_input(f"Ressources", key=f"res_{i}")
                    predecessors = st.multiselect(
                        f"Dépendances",
                        [t["name"] for t in tasks if t.get("name")],
                        key=f"pred_{i}"
                    )
                
                tasks.append({
                    "name": name,
                    "duration_days": duration,
                    "resources": [r.strip() for r in resources.split(",") if r.strip()],
                    "predecessors": [j+1 for j, t in enumerate(tasks) if t.get("name") in predecessors]
                })
        
        resources_list = st.text_input("Ressources disponibles (séparées par des virgules)", "Chef de projet, Développeur, Testeur")
        
        submitted = st.form_submit_button("📥 Générer XML MS Project")
        
        if submitted:
            with st.spinner("Génération du XML..."):
                data = {
                    "project_name": project_name,
                    "project_start_date": start_date.strftime("%Y-%m-%d"),
                    "tasks": tasks,
                    "resources": [r.strip() for r in resources_list.split(",") if r.strip()]
                }
                response = requests.post(f"{API_URL}/api/project/generate-xml", json=data)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ XML généré ! {result['task_count']} tâches")
                    
                    st.subheader("XML généré")
                    st.code(result["xml"], language="xml")
                    
                    st.download_button(
                        "📥 Télécharger le fichier MS Project",
                        result["xml"],
                        f"{project_name.replace(' ', '_')}.xml",
                        "application/xml"
                    )
                else:
                    st.error(f"Erreur: {response.text}")

elif page == "📤 Upload Documents":
    st.header("Uploader des documents historiques")
    
    uploaded_file = st.file_uploader("Choisir un document", type=["txt", "pdf", "docx"])
    
    if uploaded_file:
        files = {"file": uploaded_file}
        if st.button("📤 Indexer le document"):
            with st.spinner("Indexation en cours..."):
                response = requests.post(f"{API_URL}/api/documents/upload", files=files)
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ Document indexé ! {result['chars']} caractères")
                    st.write(f"ID: {result['doc_id']}")
                else:
                    st.error(f"Erreur: {response.text}")
    
    if st.button("📊 Voir le nombre de documents"):
        response = requests.get(f"{API_URL}/api/documents/list")
        if response.status_code == 200:
            st.info(f"📚 {response.json()['count']} documents dans la base")