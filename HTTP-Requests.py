import browser.aio as aio

async def request(url1: str, method1: str):
	req = await aio.ajax(method=method1,url=url1)
	return req.data

async def main():
	# Put your code here. This is the only place you can get the data from requests.
	# Proper format; (RequestVariable = await request(url, method)
	req = await request("https://catfact.ninja/fact", "GET") # example request
	print(req) # will print response of request
    
aio.run(main())
