import argparse

import func
import CONST


tinkoff_credit_mastercard_bins = CONST.TINKOFF_CREDIT_MASTERCARD_BINS
last_4_digits = CONST.LAST_4_DIGITS
card_num_hash = CONST.CARD_NUM_HASH
path_to_result = CONST.PATH_TO_RESULT
path_to_png = CONST.PATH_TO_PNG


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", help="collizions_found OR luna_check OR search_time_visualization"
    )
    parser.add_argument("card_number", nargs="?", const=None, help="номер карты")
    args = parser.parse_args()

    def opt_1() -> None:
        """switch case replacement for COLLIZION_FOUND"""
        print(
            "Card num --> ",
            func.card_num_bruteforce(
                last_4_digits,
                card_num_hash,
                tinkoff_credit_mastercard_bins,
                path_to_result,
            )[1],
        )

    def opt_2() -> None:
        """switch case replacement for LUNA_CHECK"""
        if args.card_number:
            print("result of luna check --> ", func.luna_check(args.card_number))
        else:
            print("no card number")

    def opt_3() -> None:
        """switch case replacement for SEARCH_TIME_VISUALIZATION"""
        func.search_time_visualization(
            last_4_digits,
            card_num_hash,
            tinkoff_credit_mastercard_bins,
            path_to_result,
            path_to_png,
        )

    task = {
        "collizions_found": opt_1,
        "luna_check": opt_2,
        "search_time_visualization": opt_3,
    }
    task[args.mode]()


if __name__ == "__main__":
    main()
