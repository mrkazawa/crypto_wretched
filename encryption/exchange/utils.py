# partial key = pub ** priv % pub receiver
def generate_partial_key(private_key, public_key, public_key_receiver):
    exp = public_key ** private_key
    return exp % public_key_receiver

# full key = partial key ** priv % pub reciver
def generate_full_key(partial_key, private_key, public_key_receiver):
    exp = partial_key ** private_key
    return exp % public_key_receiver