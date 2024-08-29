
import runner
import script

TOTAL_ROOMS = 5


def main():
    script.before_intro()
    name = script.intro()
    game = runner.Game(name)

    # Main game loop
    while game.rooms_cleared < TOTAL_ROOMS:
        # Show room info
        script.show_room_info(
            name=game.get_current_room(),
            message=game.get_current_room_message()
        )
        # Check for monster in room, if so, fight it
        # This does not require any player interaction for now.
        # It runs automatically and the result of the fight will be displayed
        # in the console immediately.
        monster = game.get_current_room_monster()
        if monster is None:
            script.no_monsters()
        else:
            script.show_monster_info(
                name=monster.name,
                type=monster.type
            )
            script.run_battle_loop(game.player, monster)
            if game.player.is_dead():
                script.game_over()
                exit(0)  # Exit the program (with return code 0)
            elif monster.is_dead():
                script.battle_won(game)
                game.clear_room()

        # Choose and enter next room
        choice = script.choose_next_room(game)
        script.pause()
        if choice == "back":
            game.dungeon.enter_previous_room()
            print("You have entered the previous room...")
            script.pause()
            continue
        game.dungeon.enter_room(int(choice))

    # Boss battle
    script.boss_fight(game.player)


if __name__ == "__main__":
    main()
