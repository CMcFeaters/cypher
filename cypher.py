#python class that can perform basic cyphers

import string
import random
import os
import sys
import cypher_constant as const

class CypherClass:
	'''
		A class that will encode and ecode basic substituion cyphers
		stores teh original, the cypher and the key in separate text files
	'''
	def __init__(self,name,original=False):
		'''initializes the class'''
		self.name=name
		#name_encode=encoded message
		#name_decode=decoded_message
		#name_cypher=cypher/key
		self.original=original	#file location for the original message
		self.encoder_dict={}	#the cypher is used to encode a message{real:fake}
		self.decoder_dict={}	#the cypher is used to decode a message{fake:real}

		
	def encode(self):
		'''
			encodes the message with the encoder dict
		'''
		#print("Origin file: ",self.original)
		if(not self.original):
			return "No Origin File, can't decode"
				
		encode_dest=open(self.name+"_encoded","w")
		encode_orig=open(os.path.join(sys.path[0],self.original),"r")
		
		orig=encode_orig.read()
		for thing in orig:
			if thing.lower() in self.encoder_dict:
				encode_dest.write(self.encoder_dict[thing.lower()])
			else:
				encode_dest.write(thing)
		encode_dest.close()
		encode_orig.close()
		
		
		return ("File encoded at: ",self.name,"_encode")
		
	def decode(self):
	
		'''
			decodes an encoded message utilizing the decoder_dict
		'''
		#print("Origin file: ",self.original)
		
		decode_dest=open(self.name+"_decoded","w")
		decode_orig=open(self.name+"_encoded","r")
		
		orig=decode_orig.read()
		for thing in orig:
			if thing.lower() in self.decoder_dict:
				decode_dest.write(self.decoder_dict[thing.lower()])
			else:
				decode_dest.write(thing)
			
		decode_dest.close()
		decode_orig.close()
		
		return ("File decoded at: ",self.name,"_encode")
	
	

	def create_cypher_dicts(self):
		'''
		creates the cypher dicts from the encode/decode files
		'''
		enc=open(self.name+"_encoder",'r')
		dec=open(self.name+"_decoder",'r')
		letters=string.ascii_lowercase
		enc_read=enc.read()
		dec_read=dec.read()
		i=0
		
		for thing in letters:
			self.encoder_dict[thing]=enc_read[i]
			self.decoder_dict[thing]=dec_read[i]
			i=i+1
		
		enc.close()
		dec.close()
		
	
	def create_cypher_pair(self):
		'''
		creates a new cypher pair for encdoing/deconding
		stores in a file
		'''
		self.encoder=self.name+"_encoder"
		self.decoder=self.name+"_decoder"
		encoder=open(self.encoder,"w")
		letters=[x for x in string.ascii_lowercase]
		letters_copy=[x for x in string.ascii_lowercase]
		
		decode_dict={}
		i=0
		while(len(letters)>0):
			index=random.randrange(0,len(letters))
			letter=letters.pop(index)
			decode_dict[letters_copy.index(letter)]=letters_copy[i]
			encoder.write(letter)
			i=i+1
			
		encoder.close()
		
		sorted_keys=sorted(decode_dict)
		decoder=open(self.decoder,"w")
		[decoder.write(decode_dict[ind]) for ind in sorted_keys]
		decoder.close()
	
	def print_files(self):
		'''
			prints the contents of all teh files
		'''
		decoded=open(self.name+"_decoded","r")
		encoded=open(self.name+"_encoded","r")
		origin=open(os.path.join(sys.path[0],self.original),"r")
		
		orig=origin.read()
		dec=decoded.read()
		enc=encoded.read()
		origin.close()
		encoded.close()
		decoded.close()
		
		print("---------Original------------")
		print(orig)
		print("*********")
		print("Encoded: ")
		print(enc)
		print("*********")
		print("decoded: ")
		print(dec)
		
		if orig.lower()==dec:
			print("Decode Success")
		else:
			print("Decode Fail")
	
	def test_decoder(self):
		'''
			compares the decoder to the encoder and turns percent correct
		'''
		x=0
		wrong=[]
		right=[]
		for key in self.encoder_dict.keys():
			if self.decoder_dict[self.encoder_dict[key]]==key:
				x+=1
				right.append(self.decoder_dict[self.encoder_dict[key]]+" is "+key)
			else:
				wrong.append(self.decoder_dict[self.encoder_dict[key]]+" is not "+key)
		print(x, " out of 26 correct")
		for thing in wrong:
			print (thing)
		for thing in right:
			print(thing)
			
	def print_cyphers(self):
		encoder=open(self.encoder,'r')
		decoder=open(self.decoder,'r')
		
		print(encoder.read())
		print(decoder.read())
		encoder.close()
		decoder.close()
		print(self.encoder_dict)
		print(self.decoder_dict)
		
	'''
test=CypherClass("Galladum","Galladum_text.txt")
test.create_cypher_pair()
test.create_cypher_dicts()
test.print_cyphers()
test.encode()
test.decode()
test.print_files()
test.test_decoder()

		'''