from fastapi import APIRouter, HTTPException
from models.schemas import ProjectPlanRequest
from services.xml_generator import MSProjectXMLGenerator

router = APIRouter()

@router.post("/generate-xml")
async def generate_xml(request: ProjectPlanRequest):
    try:
        # Convertir les tâches
        tasks = []
        for task in request.tasks:
            tasks.append({
                "name": task.name,
                "duration_days": task.duration_days,
                "resources": task.resources,
                "predecessors": task.predecessors
            })
        
        # Générer le XML
        generator = MSProjectXMLGenerator()
        xml = generator.generate(
            project_name=request.project_name,
            tasks=tasks,
            resources=request.resources
        )
        
        return {
            "status": "success",
            "xml": xml,
            "task_count": len(tasks),
            "resource_count": len(request.resources)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))