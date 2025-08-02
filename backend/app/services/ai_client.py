import os
import openai
from fastapi import HTTPException

openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTClient:
    async def generate_text(self, prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 512) -> str:
        try:
            resp = await openai.ChatCompletion.acreate(
                model=model,
                messages=[{"role": "system", "content": "You are AgentZero, the master planner."},
                          {"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"OpenAI error: {e}")Placeholder for ai_client.py
