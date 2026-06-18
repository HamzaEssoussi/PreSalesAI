from lxml import etree
from typing import List, Dict
from datetime import datetime, timedelta

class MSProjectXMLGenerator:
    def generate(self, project_name: str, tasks: List[Dict], resources: List[str]) -> str:
        """Génère un fichier XML compatible MS Project"""
        
        # Racine
        root = etree.Element('Project',
            xmlns='http://schemas.microsoft.com/project')
        
        # Nom du projet
        name = etree.SubElement(root, 'Name')
        name.text = project_name
        
        # Date de début
        start = etree.SubElement(root, 'Start')
        start.text = datetime.now().strftime('%Y-%m-%d')
        
        # Tâches
        tasks_elem = etree.SubElement(root, 'Tasks')
        
        for idx, task in enumerate(tasks, 1):
            task_elem = etree.SubElement(tasks_elem, 'Task')
            
            # ID
            etree.SubElement(task_elem, 'UID').text = str(idx)
            etree.SubElement(task_elem, 'ID').text = str(idx)
            
            # Nom
            etree.SubElement(task_elem, 'Name').text = task.get('name', f'Tâche {idx}')
            
            # Durée
            duration = task.get('duration_days', 5)
            etree.SubElement(task_elem, 'Duration').text = f"PT{duration}D"
            
            # Pourcentage d'avancement
            etree.SubElement(task_elem, 'PercentComplete').text = "0"
            
            # Type de tâche
            etree.SubElement(task_elem, 'TaskType').text = "1"
            
            # Statut
            etree.SubElement(task_elem, 'Status').text = "0"
            
            # Actif
            etree.SubElement(task_elem, 'Active').text = "1"
            
            # Dépendances
            predecessors = task.get('predecessors', [])
            if predecessors:
                links = etree.SubElement(task_elem, 'PredecessorLinks')
                for pred in predecessors:
                    link = etree.SubElement(links, 'PredecessorLink')
                    etree.SubElement(link, 'PredecessorUID').text = str(pred)
                    etree.SubElement(link, 'Type').text = "0"
        
        # Ressources
        if resources:
            resources_elem = etree.SubElement(root, 'Resources')
            for idx, resource in enumerate(resources, 1):
                res = etree.SubElement(resources_elem, 'Resource')
                etree.SubElement(res, 'UID').text = str(idx)
                etree.SubElement(res, 'Name').text = resource
                etree.SubElement(res, 'Type').text = "1"
        
        return etree.tostring(root, pretty_print=True, encoding='unicode', xml_declaration=True)