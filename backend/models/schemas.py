from pydantic import BaseModel
from typing import List, Optional

class TaskRequest(BaseModel):
    """
    Modèle pour une tâche individuelle dans un plan de projet
    """
    name: str
    duration_days: int
    resources: List[str] = []
    predecessors: List[int] = []

class ProjectPlanRequest(BaseModel):
    """
    Modèle pour la requête de génération de plan de projet
    Reçu par POST /api/project/generate-xml
    """
    project_name: str
    project_start_date: str
    tasks: List[TaskRequest]
    resources: List[str] = []