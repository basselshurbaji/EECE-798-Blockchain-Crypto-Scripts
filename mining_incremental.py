from time import time
from hashlib import sha256
from datetime import datetime

# Data
NAME = 'Bassel Shurbaji'
EMAIL = 'bms23@mail.aub.edu'
ID = 201801284
PREVIOUS_HASH = 0x00000000000000000001f37f994d809554741b50276b32fe7e8cf3fd45db9980
TIME_STAMP = int(time())

# NONCE
MAX_NONCE = pow(2, 32) - 1
nonce = 0

# LEADING ZEROS
MIN_LEADING_ZEROS = 23
MAX_LEADING_ZEROS = 27

# Formatting Data
NAME_HEX = NAME.encode(encoding='ascii', errors='ignore').hex()
print("Name: 0x" + NAME_HEX)
EMAIL_HEX = EMAIL.encode(encoding='ascii', errors='ignore').hex()
print("Email: 0x" + EMAIL_HEX)
ID_HEX = '{:08x}'.format(ID)
print("ID: 0x" + ID_HEX)
PREVIOUS_HASH_HEX = '{:064x}'.format(PREVIOUS_HASH)
print("Previous Hash: 0x" + PREVIOUS_HASH_HEX)
TIME_STAMP_HEX = '{:08x}'.format(TIME_STAMP)
print("TimeStamp: 0x" + TIME_STAMP_HEX)

# Mining Loop
csv_str = 'Name, ' + NAME + ', 0x' + NAME_HEX
csv_str += '\n' + 'Email, ' + EMAIL + ', 0x' + EMAIL_HEX
csv_str += '\n' + 'ID, ' + str(ID) + ', 0x' + ID_HEX
csv_str += '\n' + 'Previous Hash, ' + ', 0x' + PREVIOUS_HASH_HEX
csv_str += '\n' + 'Time Stamp, ' + str(TIME_STAMP) + ', 0x' + TIME_STAMP_HEX
csv_str += '\n' + 'Required Leading Zeros, Nonce, Hash, Time (seconds)'
leading_zeros = MIN_LEADING_ZEROS
print("# Incremental Mining Loop #")
while leading_zeros <= MAX_LEADING_ZEROS:
    block_hash = pow(2, 256)
    block_hash_hex = ''
    nonce = -1
    start_time = time()
    block_hash_upper_limit = pow(2, 256 - leading_zeros)
    while block_hash > block_hash_upper_limit:
        nonce += 1
        block_data_hex = PREVIOUS_HASH_HEX + '{:08x}'.format(nonce) + TIME_STAMP_HEX + ID_HEX + EMAIL_HEX + NAME_HEX
        block_data = bytes.fromhex(block_data_hex)
        block_hash_hex = sha256(block_data).hexdigest()
        block_hash = int(block_hash_hex, 16)
    end_time = time()
    seconds_elapsed = '{:.2f}'.format(end_time - start_time)
    csv_row = str(leading_zeros) + ', 0x' + '{:08x}'.format(nonce) + ", 0x" + block_hash_hex + ", " + seconds_elapsed
    csv_str += '\n' + csv_row
    print(csv_row)
    leading_zeros = leading_zeros + 1

# Publish Results to CSV File
current_time = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
file = open('mining_incremental_output ' + current_time + '.csv', 'w+')
file.write(csv_str)
file.close()
