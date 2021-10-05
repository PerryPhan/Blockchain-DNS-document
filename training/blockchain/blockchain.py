from block import Block
import datetime

num_of_block_adding = 10

block_chain = [Block.create_genesis_block()]

print("Block đầu tiên đã được tạo ")
print("Có hash là : %s" % block_chain[0].hash )
 

for i in range(1,num_of_block_adding ):
    block_chain.append(Block(block_chain[i-1].hash,
                            "Block number %d" % i,
                            datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)