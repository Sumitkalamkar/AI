import requests

API_URL = "https://api-inference.huggingface.co/models/avichr/heBERT_sentiment_analysis"
headers = {"Authorization": "Bearer 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"}



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	print(response.json())
	
output = query({
	"inputs": " ",
})