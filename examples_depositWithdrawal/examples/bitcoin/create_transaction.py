# -*- coding: utf-8 -*-
#
#    BitcoinLib - Python Cryptocurrency Library
#
#    EXAMPLES - Wallets and Transactions
#
#    © 2018 February - 1200 Web Development <http://1200wd.com/>
#
# source from : https://github.com/1200wd/bitcoinlib/blob/master/examples/wallets_transactions.py

import os
from pprint import pprint
from bitcoinlib.wallets import Wallet, BCL_DATABASE_DIR

# First recreate database to avoid already exist errors
test_databasefile = os.path.join(BCL_DATABASE_DIR, 'bitcoinlib.test.sqlite')
test_database = 'sqlite:///' + test_databasefile

# If database file already exists, remove it to avoid conflicts
if os.path.isfile(test_databasefile):
    os.remove(test_databasefile)

# === Create a wallet and a simple transaction ===
print("\n=== Create a wallet and a simple transaction ===")
# Create a wallet called 'wlttest1' using the test network and specify a custom database URI
wlt = Wallet.create('wlttest1', network='bitcoinlib_test', db_uri=test_database)

# Get the key for this wallet
wlt.get_key()

# Update UTXOs (this creates some test unspent outputs for the wallet)
wlt.utxos_update()

# Print wallet information
wlt.info()

# Get the destination key (to send funds to the same wallet)
to_key = wlt.get_key()

# Create a transaction to send 50,000,000 satoshis (0.5 BTC) to the destination key
print("\n- Create transaction (send to own wallet)")
t = wlt.send_to(to_key.address, 50000000)

# Print transaction information
t.info()

# Print updated wallet info after the transaction
print("\n- Successfully send, updated wallet info:")
wlt.info()

# === Create a wallet, generate 6 UTXOs and create a sweep transaction ===
print("\n=== Create a wallet, generate 6 UTXOs and create a sweep transaction ===")
# Create another wallet called 'wlttest2' using the test network and custom database URI
wlt = Wallet.create('wlttest2', network='bitcoinlib_test', db_uri=test_database)

# Generate 3 new keys for this wallet
wlt.get_keys(number_of_keys=3)

# Update UTXOs (this generates some test UTXOs for the wallet)
wlt.utxos_update()

# Print wallet information
wlt.info()

# Get the destination key (to sweep funds to this address)
to_key = wlt.get_key()

# Create a sweep transaction that sends all the funds to another address
print("\n- Create transaction to sweep wallet")
t = wlt.sweep('21Cr5enTHDejL7rQfyzMHQK3i7oAN3TZWDb')

# Print transaction information
t.info()

# Print updated wallet info after the sweep transaction
print("\n- Successfully send, updated wallet info:")
wlt.info()

