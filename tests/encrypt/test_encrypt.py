import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(0,0)
    assert encrypt_message('word', 2) == 'wo_rd'
    assert encrypt_message('word', 3) == 'wor_d'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('word','word')

    pass
