import floresta
import bip39
import electrum
import time
import random
import threading
import bitcoin

def load_wallet(create=True):
    try:
        wallet = open("./wallet", "rb")
        wallet = wallet.read()
        if len(wallet) == 32:
            print("loaded existing wallet")
            return  wallet 
    except:
        pass

    seed = random.randbytes(32)
    file =  open("./wallet", "wb+")
    file.write(seed)

    mnemonic = bip39.encode_bytes(seed)
    print(f"wallet created with seed: {mnemonic}")
    return seed 

def check_balance(address: str) -> int:
    pass

def run_fl():
    floresta.Florestad().run()

def main():
    wallet = load_wallet()
    threading.Thread(target=run_fl).start()
    print(wallet)
    for i in range(100):
        try:
            e = electrum.ElectrumClient(addr="127.0.0.1", port=50001)
            e.connect()
            print("connected with the electrum server!")
            break
        except Exception as e:
            print(f"waiting... {e}")
            time.sleep(1)
   
main()
