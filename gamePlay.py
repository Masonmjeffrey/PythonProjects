import gameFunctions as gF
import gameState as gS
import professions as prof


def game_play():
    gF.game_intro()
    userProf = prof.GetProfession()
    prof.SetProfession(userProf)
    while gS.playState:
        gF.get_action()
    gF.win_state()
    gF.reset_game_state()


