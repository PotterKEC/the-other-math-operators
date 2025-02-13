import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from assignment import (
    create_player_tag,
    calculate_points_needed,
    create_team_roster,
    distribute_powerups
)

def test_create_player_tag():
    assert create_player_tag("Mario", 123) == "Mario#123"
    assert create_player_tag("Luigi", 456) == "Luigi#456"
    assert create_player_tag("Yoshi", 789) == "Yoshi#789"
    assert create_player_tag("", 999) == "#999"  # Edge case: empty name

def test_calculate_points_needed():
    assert calculate_points_needed(100, 150) == 50
    assert calculate_points_needed(0, 100) == 100
    assert calculate_points_needed(50, 50) == 0
    assert calculate_points_needed(200, 100) == -100  # Edge case: current > target

def test_create_team_roster():
    assert create_team_roster(3, "🏃") == "🏃🏃🏃"
    assert create_team_roster(2, "⭐") == "⭐⭐"
    assert create_team_roster(1, "🎮") == "🎮"
    assert create_team_roster(0, "🎲") == ""  # Edge case: team size 0

def test_distribute_powerups():
    assert distribute_powerups(10, 3) == 1  # 10 ÷ 3 = 3 each, 1 remainder
    assert distribute_powerups(100, 20) == 0  # Divides evenly
    assert distribute_powerups(7, 2) == 1  # 7 ÷ 2 = 3 each, 1 remainder
    assert distribute_powerups(5, 6) == 5  # Edge case: more players than powerups