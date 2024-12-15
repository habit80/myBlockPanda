To run bitcoin-qt on Linux without downloading the entire blockchain, you can use a feature called pruned mode. This allows you to store only a portion of the blockchain, significantly reducing disk space usage. Here’s how you can do it:

Steps to Run Bitcoin-Qt in Pruned Mode:
Close Bitcoin-Qt if it's running: Make sure the application is not running before making configuration changes.

Edit the Bitcoin configuration file: Locate the configuration file named bitcoin.conf. If it doesn't exist, you can create it.

Default location: ~/.bitcoin/bitcoin.conf
Open it in a text editor:

bash
Copy code
nano ~/.bitcoin/bitcoin.conf
Enable Pruned Mode: Add the following line to the configuration file:

plaintext
Copy code
prune=550
The prune value specifies the target disk space in MB for storing blockchain data. The minimum allowed is 550 MB, but you can increase this if you have more space available.
Save and Exit: Save the file (Ctrl+O and Ctrl+X if using nano).

Restart Bitcoin-Qt: Start bitcoin-qt again, and it will run in pruned mode. It will download only the most recent blocks needed for normal operation, discarding older data.

If you prefer to run it from the terminal with pruning enabled, use:

bash
Copy code
bitcoin-qt -prune=550
