import pytest
import os
import sys
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../src')))
import dash_utils

# def wif_to_privkey(string):
# def generate_privkey():
# def num_to_varint(a):
# def privkey_valid(privkey):
# def from_string_to_bytes(a):
# def electrum_sig_hash(message):
# def ecdsa_sign(msg, priv):
# def serialize_input_str(tx, prevout_n, sequence, script_sig):
# def bip32_path_n_to_string(path_n):
# def encrypt(input_str, key):
# def decrypt(input_str, key):
# def seconds_to_human(number_of_seconds, out_seconds=True, out_minutes=True, out_hours=True):


# @pytest.fixture
# def compressed_wif():
#     return 'XGzrjz3x336SswmFUKtkXNCkECmYTHJroYreBwFwiEstAVFUnxFv'
#
#
# @pytest.fixture
# def uncompressed_wif():
#     return '7rquWDvgf56mNxucuQmMHPvs852UyFa3g6QUumvEJVyPU89TbjT'


def test_wif_to_privkey():
    compressed_wif = 'XGzrjz3x336SswmFUKtkXNCkECmYTHJroYreBwFwiEstAVFUnxFv'
    uncompressed_wif = '7rquWDvgf56mNxucuQmMHPvs852UyFa3g6QUumvEJVyPU89TbjT'

    actual_privkey = 'aa6529b54e49a0e1a143e9481b48d84cd8d135bd1c351d89645fd0fef39a267a'

    assert dash_utils.wif_to_privkey(compressed_wif) == actual_privkey
    assert dash_utils.wif_to_privkey(uncompressed_wif) == actual_privkey
