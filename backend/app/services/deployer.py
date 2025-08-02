import os
import httpx
from fastapi import HTTPException

class Deployer:
    def __init__(self):
        self.vercel_token = os.getenv("VERCEL_TOKEN")
        self.render_token = os.getenv("RENDER_TOKEN")
        self.project_name = os.getenv("VERCEL_PROJECT")  # e.g. "domination-core"

    async def start_workflow(self, agent_name: str, data: str) -> str:
        """
        Trigger a build/deploy based on agent_name.
        Currently wired to Vercel Deploy Hook;
        you can swap in Render if you prefer.
        """
        hook_url = os.getenv(f"{agent_name.upper()}_HOOK_URL")  # set in .env
        if not hook_url:
            raise HTTPException(status_code=500, detail="Deploy hook URL not configured")

        async with httpx.AsyncClient() as client:
            resp = await client.post(hook_url, json={"payload": data})
            if resp.status_code not in (200, 201):
                raise HTTPException(status_code=500, detail=f"Deploy failed: {resp.text}")
            return resp.json().get("deploymentId", "unknown")
