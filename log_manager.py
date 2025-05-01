from colorama import init, Fore, Style

init()


def print_blocking_state(blocking):
    if blocking:
        print(f'{Fore.RED}❌ DROPPING PACKETS{Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}✅ ALLOWING PACKETS{Style.RESET_ALL}')
