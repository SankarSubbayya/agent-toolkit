import os
from pathlib import Path
from contextual import ContextualAI


def get_client() -> ContextualAI:
    return ContextualAI(api_key=os.environ["CONTEXTUAL_API_KEY"])


def create_agent_with_datastore(name: str) -> tuple[str, str]:
    """Create a Contextual AI agent with an auto-created datastore.
    Returns (agent_id, datastore_id).
    """
    client = get_client()

    ds = client.datastores.create(name=f"ds-{name[:40]}")
    datastore_id = ds.id

    result = client.agents.create(
        name=name,
        datastore_ids=[datastore_id],
        system_prompt=(
            "You are a research assistant. Answer questions based on the documents "
            "provided. Always cite your sources. If you don't know the answer from "
            "the provided documents, say so clearly."
        ),
    )
    agent_id = result.id
    return agent_id, datastore_id


def upload_documents(datastore_id: str, file_paths: list[str]) -> None:
    """Upload scraped documents to a Contextual AI datastore."""
    client = get_client()
    for path in file_paths:
        client.datastores.documents.ingest(
            datastore_id=datastore_id,
            file=Path(path),
        )


def query_agent(agent_id: str, question: str, conversation_id: str | None = None) -> dict:
    """Query the Contextual AI agent and return the response."""
    client = get_client()

    messages = [{"role": "user", "content": question}]

    kwargs = {"messages": messages}
    if conversation_id:
        kwargs["conversation_id"] = conversation_id

    response = client.agents.query.create(
        agent_id=agent_id,
        **kwargs,
    )

    return {
        "answer": response.message.content,
        "conversation_id": str(response.conversation_id),
        "attributions": [
            {"source": a.source_title if hasattr(a, "source_title") else "", "text": a.attributed_text if hasattr(a, "attributed_text") else ""}
            for a in (response.attributions or [])
        ],
    }
