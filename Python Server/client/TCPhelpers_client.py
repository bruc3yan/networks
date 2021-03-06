import os
import hashlib

# string = 'yousonofabitch,networks is getting so hard. -_-;;; and bruce is just watching me code in python.'
# print 'Testing md5 with string: ', string
# k = hashlib.md5()
# k.update(string)
# print 'Digest is: ', k.hexdigest()

def generateMetaData(inputfile, blockSize):
	results = []
	size = os.path.getsize(inputfile)
	numBlocks = size / blockSize 
	if size % blockSize != 0:
		numBlocks += 1
	totalCheckSum = md5_for_file(inputfile, blockSize)

	results.append('name:'+inputfile)
	results.append('file size:'+str(size))
	results.append('number of blocks:'+str(numBlocks))
	results.append('block size:'+str(blockSize))
	results.append('checksum:'+totalCheckSum)
	return results


def md5_for_file(filename, block_size):
	f = open(filename, 'r')
	md5 = hashlib.md5()
	data = f.read(block_size)
	while data:
		md5.update(data)
		data = f.read(block_size)
	f.close()
	return md5.hexdigest()

# filename = raw_input("file name: ")
# result = generateMetaData(filename, 512)
# print result
# print result[1][0], result[1][1]