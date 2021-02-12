import random
from time import time
from hashlib import sha256
from datetime import datetime

# Data
NAME = 'Bassel Shurbaji'
EMAIL = 'bms23@mail.aub.edu'
ID = 201801284
PREVIOUS_HASH = 0x00000000000000000001f37f994d809554741b50276b32fe7e8cf3fd45db9980
TIME_STAMP = int(time())
nonce = 0

# Formatting Data
NAME_HEX = NAME.encode(encoding='ascii', errors='ignore').hex()
EMAIL_HEX = EMAIL.encode(encoding='ascii', errors='ignore').hex()
ID_HEX = '{:08x}'.format(ID)
PREVIOUS_HASH_HEX = '{:064x}'.format(PREVIOUS_HASH)
TIME_STAMP_HEX = '{:08x}'.format(TIME_STAMP)

csv_str = 'Required Leading Zeros, Nonce, Hash, Time'

leading_zeros = 10
while leading_zeros < 30:
    MAX_NONCE = pow(2, 32) - 1
    block_hash = pow(2, 256)
    block_hash_hex = ''
    start_time = time()
    while block_hash > pow(2, 256 - leading_zeros):
        nonce = random.randint(0, MAX_NONCE)
        block_data = PREVIOUS_HASH_HEX + '{:08x}'.format(nonce) + TIME_STAMP_HEX + ID_HEX + EMAIL_HEX + NAME_HEX
        block_hash_hex = sha256(block_data.encode()).hexdigest()
        block_hash = int(block_hash_hex, 16)
    end_time = time()
    seconds = end_time - start_time
    csv_row = str(leading_zeros) + ', 0x' + '{:08x}'.format(nonce) + ", 0x" + block_hash_hex + ", " + str(seconds)
    csv_str += '\n' + csv_row
    print(csv_row)
    leading_zeros = leading_zeros + 1

current_time = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
file = open('mining_output' + current_time + '.csv', 'w+')
file.write(csv_str)
file.close()
