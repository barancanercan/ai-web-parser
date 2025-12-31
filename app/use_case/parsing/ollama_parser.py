from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


from config.settings import OLLAMA_MODEL

template = (
    "Aşağıdaki metinlerden şu bilgiyi çıkartman gerekiyor: {parse_instructions}\n\n"
    "Metin:\n{chunk}\n\n"
    "Sadece doğrudan eşleşen bilgileri çıkart. Başka hiç bir ek açıklama yapma."
    "Eğer bilgi yoksa boş string (' ') döndür."
)

model = OllamaLLM(model= OLLAMA_MODEL)

def parse_with_ollama(chunks: list[str], parse_instructions: str) -> str:
    prompt = ChatPromptTemplate.from_template(template=template)
    chain = prompt | model

    results = []

    for i, chunk in enumerate(chunks,1):
        print(f"[OllamaParser] Parsing chunk {i}  of {len(chunks)}") # Kaçıncı chunktayım?
        response = chain.invoke({
            "chunk": chunk,
            "parse_instructions": parse_instructions
        })
        results.append(response.strip())

    return "\n".join(results)