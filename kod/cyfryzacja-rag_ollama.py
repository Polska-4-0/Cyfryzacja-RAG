import os
import logging
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

WORKING_DIR = "./dokumenty"

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="llama3.2:1b",
    llm_model_max_async=4,
    llm_model_max_token_size=32768,
    llm_model_kwargs={"host": "http://localhost:11434", "options": {"num_ctx": 32768}},
    tiktoken_model_name="gpt2", #cl100k_base",
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(
            texts, embed_model="nomic-embed-text", host="http://localhost:11434"
        ),
    ),
)

with open("./dokumenty/Strategia_Cyfryzacji_Państwa_Projekt_do_konsultacji_społecznych.tks", "r", encoding="utf-8") as f:
    rag.insert(f.read())

# Wykonaj naiwne szukanie
print(
    rag.query("Jakie są najważniejsze założenia cyfryzacji?", param=QueryParam(mode="naive"))
)

# Wykonaj lokalne szukanie
print(
    rag.query("Jakie są najważniejsze założenia cyfryzacji?", param=QueryParam(mode="local"))
)

# Wykonaj globalne szukanie
print(
    rag.query("Jakie są najważniejsze założenia cyfryzacji?", param=QueryParam(mode="global"))
)

# Wykonaj hybrydowe szukanie
print(
    rag.query("Jakie są najważniejsze założenia cyfryzacji?", param=QueryParam(mode="hybrid"))
)
