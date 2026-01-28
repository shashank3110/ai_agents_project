from os import error
from google.adk.agents.llm_agent import Agent, LlmAgent



eda_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='eda_agent',
    description='You are an EDA agent. And you are responsible for performing data analysis',
    instruction='perform EDA on the given dataset and and help user understand the data better, using statistical and visual methods.',
)

feature_engineering_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='feature_engineering_agent',
    description='You are a feature engineering agent. And you are responsible for performing feature engineering',
    instruction='identify important features and also perform feature engineering.',
)

model_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='model_agent',
    description='You are a model agent. And you are responsible for performing model training',
    instruction='train a model on the given dataset which does not overfit the data',
)


evaluation_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='evaluation_agent',
    description='You are an evaluation agent. And you are responsible for performing model evaluation and validation and test set.',
    instruction='evaluate the given model',
)

# how to solve root_agent not defined error?

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    sub_agents=[eda_agent, feature_engineering_agent, model_agent, evaluation_agent],
    description='You are a data scientist. And you are responsible for performing data analysis, feature engineering, model training and model evaluation',
    instruction='Answer user questions to the best of your knowledge',
)
