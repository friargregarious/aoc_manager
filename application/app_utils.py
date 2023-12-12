


def path(*args) -> str:
    """cleans up escaped characters and will put 2"""
    for item in args:
        item.replace("\\", "/").strip("/")

    return "/".join(args)

    # if isinstance(args, dict):
    #     # if isinstance(args, list):
    #     temp = [clean_up(y) for y in args.values()]
    #     return "/".join(temp)






class Account(dict):
    """ """
