import pytest
from main import Game
from player import Player

@pytest.fixture
def player1():
    return Player("Knight", attack=20, defense=10, health=100)

@pytest.fixture
def player2():
    return Player("Orc", attack=25, defense=5, health=100)

def test_player_initialization(player1):
    assert player1.name == "Knight"
    assert player1.attack == 20
    assert player1.defense == 10
    assert player1.health == 100

def test_player_attack(player1, player2):
    # Assume the move reduces health based on attack and defense difference
    player1.attack("slash", player2)  # Assuming "slash" is a move with the same attack power
    assert player2.health < 100

def test_display_stats(player1, capsys):
    player1.display_stats()
    captured = capsys.readouterr()
    assert "Knight" in captured.out
    assert "Health: 100" in captured.out




@pytest.fixture
def game(player1, player2):
    return Game(player1, player2)

def test_game_initialization(game):
    assert len(game.players) == 2

def test_game_turn(game, capsys):
    # Simulate player turn
    game.turn(1)  # Assume player 1 attacks player 2
    captured = capsys.readouterr()
    assert "Player 1 attacks" in captured.out

def test_game_winner(game):
    game.player1.health = 0  # Simulate player 1 defeat
    assert game.check_winner() == "Player 2 wins"

def test_game_restart(game):
    game.restart()
    assert game.player1.health == 100  # Assuming 100 is full health

def test_game_exit(game, capsys):
    game.exit()
    captured = capsys.readouterr()
    assert "Exiting game" in captured.out
