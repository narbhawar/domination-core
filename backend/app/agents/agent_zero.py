from fastapi import APIRouter
from app.services.ai_client import GPTClient
from app.services.deployer import Deployer

router = APIRouter(prefix="/agent_zero", tags=["AgentZero"])

client = GPTClient()
deployer = Deployer()

@router.post("/plan")
async def generate_plan():
    """
    1) Ask GPT for a new micro-SaaS idea based on past performance.
    2) Trigger CodeForge workflow with the idea spec.
    """
    # 1) Generate a new SaaS concept
    prompt = (
        "You are AgentZero. Based on our current portfolio revenue and trends, "
        "suggest one new micro-SaaS tool we should build next. "
        "Output as a short spec."
    )
    spec = await client.generate_text(prompt)

    # 2) Kick off CodeForge to build it
    workflow_id = await deployer.start_workflow("code_forge", spec)

    return {
        "spec": spec,
        "workflow_id": workflow_id
    }Placeholder for agent_zero.py
