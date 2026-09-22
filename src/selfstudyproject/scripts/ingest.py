from selfstudyproject.nodes.retrieve import retrieve_documents
from selfstudyproject.nodes.generate_answer import generate_answer
from selfstudyproject.nodes.evaluate_answer import evaluate_answer


def main():
    state = {
        "question": "What is C#?"
    }

    # -------------------------
    # 1. Retrieve from Chroma
    # -------------------------

    state = retrieve_documents(state)

    print("\n==============================")
    print("RETRIEVED DOCUMENTS")
    print("==============================")

    print(f"Documents retrieved: {len(state['documents'])}")

    for index, document in enumerate(state["documents"], start=1):
        print(f"\n--- Document {index} ---")
        print(f"Metadata: {document.metadata}")
        print(document.page_content[:500])


    # -------------------------
    # 2. Generate answer
    # -------------------------

    state = generate_answer(state)

    print("\n==============================")
    print("GENERATED ANSWER")
    print("==============================")

    print(state["answer"])


    # -------------------------
    # 3. Evaluate answer
    # -------------------------

    state = evaluate_answer(state)

    print("\n==============================")
    print("EVALUATION")
    print("==============================")

    print(
        f"Evaluation reason: "
        f"{state['evaluation_reason']}"
    )

    print(
        f"Needs research: "
        f"{state['needs_research']}"
    )

    print(
        f"Research query: "
        f"{state['research_query']}"
    )




if __name__ == "__main__":
    main()