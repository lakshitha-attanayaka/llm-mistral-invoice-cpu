# Note: Precise formatting of spacing and indentation of the prompt template is important,
# as it is highly sensitive to whitespace changes. For example, it could have problems generating
# a summary from the pieces of context if the spacing is not done correctly
#
# qa_template = """Use the following pieces of information to answer the user's question.
# If you don't know the answer, just say that you don't know, don't try to make up an answer.
#
# Context: {context}
# Question: {question}
#
# Only return the helpful answer below and nothing else.
# Helpful answer:
# """

qa_template = """Use the following conversation between customer support agent and customer. And analyse the sentiment
 of the conversation. User will ask questions mentioning the member name or member Id or both and agent name or agent Id
  or both to give the sentiment of the conversation.
Use that analysis to build up json formatted result as follows.
memberId = member id of the member. If not available - "N/A"
agentId = agent id of the agent. - "N/A"
timeOfFirstEngagement = date and time of first engagement. - "N/A"
timeOfLastEngagement = date and time of last engagement. - "N/A"
sentimentScore = sentiment score of the conversation. This must be between -1 and 1.


Context: {context}
Question: {question}

Only return the answer as matching to above json. Nothing else.
Answer:
"""
