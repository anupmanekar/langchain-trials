import langsmith

from langchain import chat_models, prompts, smith
from langchain.schema import output_parser


# Define your runnable or chain below.
prompt = prompts.ChatPromptTemplate.from_messages(
  [
    ("system", "You are an AI assistant with knowledge of Indian stock exchange. Given are the closing points of Nifty PSU Bank Index of Indian Stock Exchange"),
    ("human", "Give me close points of Nifty PSU Bank Index on {Date}")
  ]
)
llm = chat_models.ChatOllama(model="llama2", temperature=0)
chain = prompt | llm | output_parser.StrOutputParser()

# Define the evaluators to apply
eval_config = smith.RunEvalConfig(
    evaluators=[
        "cot_qa"
    ],
    custom_evaluators=[],
    eval_llm=chat_models.ChatOllama(model="llama2", temperature=0)
)

client = langsmith.Client()
chain_results = client.run_on_dataset(
    dataset_name="ds-weary-interconnection-72",
    llm_or_chain_factory=chain,
    evaluation=eval_config,
    project_name="test-nifty-psu-bank-01",
    concurrency_level=5,
    verbose=True,
)