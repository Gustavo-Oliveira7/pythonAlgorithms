import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(0, 0)
    assert encrypt_message('word', 2) == 'dr_ow'
    assert encrypt_message('word', 3) == 'row_d'
    assert encrypt_message('word', 8) == 'drow'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('word', 'word')
