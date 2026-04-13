# Advanced RAG Techniques

15 notebooks covering every major RAG retrieval and reranking technique,
implemented with LangChain, FAISS, LlamaIndex, and Qdrant.

## Notebooks
| # | File | Technique |
|---|---|---|
| 1 | 1_hybrid_search | Ensemble retrieval — FAISS + BM25 keyword search |
| 2 | 2_reranking_cosine | Cosine similarity reranking |
| 3 | 3_reranking_cross_encoder | Cross-encoder reranking (sentence-transformers) |
| 4 | 4_lost_in_middle | LongContextReorder — lost-in-middle fix |
| 5 | 5_rank_fusion | Reciprocal Rank Fusion (RRF) |
| 6 | 6_flash_rerank | FlashRank cross-encoder — ms-marco-MiniLM-L-12-v2 |
| 7 | 7_contextual_compression | Contextual compression retriever |
| 8 | 8_self_query | Self-querying retriever with metadata filters |
| 9 | 9_child_parent | Child-parent (small-to-big) retriever |
| 10 | 10_sentence_window | Sentence window retrieval (LlamaIndex) |
| 11 | 11_HYDE | Hypothetical Document Embeddings |
| 12 | 12_auto_merge | Auto-merge hierarchical retriever |
| 13 | 13_Corrective_RAG | Corrective RAG — grades retrieval quality |
| 14 | 14_Agentic_RAG | Agentic RAG — LangGraph routing |
| 15 | 15_self_RAG | Self-RAG — reflection + grounding |
| 16 | Neo4j notebook | Knowledge graph RAG with Neo4j |

## Production implementation
All techniques in notebooks 1–7 are combined into a 4-stage production
pipeline in [rohanta-rag-chatbot](https://github.com/rohantabhamar/rohanta-rag-chatbot):
FAISS MMR + BM25 → custom RRF → FlashRank → LongContextReorder

## Tech stack
LangChain · LlamaIndex · FAISS · Qdrant · BM25 · FlashRank ·
sentence-transformers · Neo4j · Groq · HuggingFace
