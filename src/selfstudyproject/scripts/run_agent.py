from selfstudyproject.graph import create_graph


def main():
    graph = create_graph()

    question = input("Enter a question: ")

    result = graph.invoke(
        {
            "question": question
        }
    )

    print("\n==============================")
    print("FINAL ANSWER")
    print("==============================")
    print(result["answer"])

    print("\n==============================")
    print("EVALUATION")
    print("==============================")
    print(f"Needs research: {result['needs_research']}")
    print(f"Reason: {result['evaluation_reason']}")

    if result["needs_research"]:
        print(f"Research query: {result['research_query']}")
        print(f"Answer after research: {result['answer']}")


if __name__ == "__main__":
    main()