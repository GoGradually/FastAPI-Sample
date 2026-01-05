docs = ["../docs/resume/feedhanjum.md", "../docs/resume/pinit.md", "../docs/resume/Superboard.md"]

documents = []
for fname in docs:
    with open(fname, 'r', encoding='utf-8') as f:
        documents.append(f.read())

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

embeddings = model.encode(documents)
print(f"임베딩 벡터 shape: {embeddings.shape}")

import faiss
import numpy as np

embedding_dim = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)

index.add(np.array(embeddings, dtype='float32'))
print(f"현재 저장된 벡터 개수: {index.ntotal}")


question = "pinit은 어떤 서비스인가요?"
q_vec = model.encode([question])

D, I = index.search(np.array(q_vec, dtype='float32'), k=1)
nearest_idx = I[0][0]
print(f"질문에 가장 관련 있는 문서 인덱스: {nearest_idx}")
print(f"해당 문서 내용 (일부분):\n{documents[nearest_idx][:300]}...")

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
context = documents[nearest_idx]
prompt = f"다음 문서를 참고하여 질문에 답하세요:\n'''{context}'''\n질문: {question}\n답변:"

response = client.responses.create(
    model="gpt-4o",
    input=prompt,
    max_output_tokens=100,
    temperature=0.2,
    top_p=1.0,
)


answer = response.output[0].content[0].text
print("답변:", answer)