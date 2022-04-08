import base64
import json 
from django.http import HttpResponse
from django.shortcuts import render
from Crypto.Hash import SHA512, SHA384

def homePageView(request):
	return render(request, 'home.html')

def getBatchID(request):
	body = json.loads(request.body)
	print(body)
	return HttpResponse(request.body)

def verifyBatches(r):
	b = json.loads(r.body)
	p = b['payments']
	t = b''
	for pt in p: 
		c = SHA384.new(data=bytes(pt['Name'] + pt['CC'] + pt['CVV'] + pt['Amount'], 'utf-8')).hexdigest()
		print(c)
		d = base64.b64decode(pt['transactionID']).hex()
		print(d)
		t += bytearray.fromhex(d) if c == d else '\x00\x00'
	if SHA512.new(data=t).digest() != bytearray.fromhex(b['batchSignature']):
		r = "Signature Mismatch: %s != %s" % (SHA512.new(data=t).hexdigest(), b['batchSignature'])
	else:
		r = "Success: %s successful transactions" % len(p)
	m = {}
	m['message'] = r
	return HttpResponse(json.dumps(m))